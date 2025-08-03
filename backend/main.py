from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import json
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.agents import tool, AgentExecutor, create_react_agent
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_community.utilities import WikipediaAPIWrapper

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

app = FastAPI()
app.mount("/data", StaticFiles(directory="data"), name="data")

# --- Add CORS Middleware ---
origins = [
    "http://localhost:3000",
    "http://localhost:5173", # Vite/React port
    "http://localhost:8501", # Streamlit port
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATA_FILE = os.path.join(os.path.dirname(__file__), "data/mountains.json")

with open(DATA_FILE, "r", encoding="utf-8") as f:
  mountains = json.load(f)

# --- Base and Mountain-specific Endpoints ---
@app.get("/")
def read_root():
  return {"message": "Welcome to Mountain Explorer API."}

@app.get("/api/mountains")
def get_all_mountains():
  return mountains

@app.get("/api/mountains/{mountain_id}")
def filter_mountain(mountain_id: int):
  for mountain in mountains:
    if mountain["id"] == mountain_id:
      return mountain
  return {"error": "Mountain not found"}

# --- AI Agent Configuration ---
@tool
def wikipedia_search(query: str) -> str:
  """Search Wikipedia for information about a topic"""
  try: 
    wikipedia = WikipediaAPIWrapper()
    result = wikipedia.run(query)
    return result
  except Exception as e:
    return f"Error searching Wikipedia: {str(e)}"
  
tavily_tool = TavilySearchResults(max_results=2)
  
prompt = PromptTemplate.from_template(
    """
    You are a helpful mountain research assistant.
    Answer the following questions as best you can. You have access to the following tools:

    {tools}

    Use the following format:

    Question: the input question you must answer
    Thought: you should always think about what to do
    Action: the action to take, should be one of [{tool_names}]
    Action Input: the input to the action
    Observation: the result of the action
    ... (this Thought/Action/Action Input/Observation can repeat N times)
    Thought: I now know the final answer
    Final Answer: the final answer to the original input question

    Begin!

    Question: {input}
    Thought:{agent_scratchpad}
    """
)

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", 
                             api_key=GEMINI_API_KEY, 
                             temperature=0.3)
tools = [tavily_tool, wikipedia_search]
agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(
  agent=agent, 
  tools=tools, 
  verbose=True,
  handle_parsing_errors=True,
)

@app.get("/api/mountains/{mountain_id}/ai-facts")
def get_ai_facts(mountain_id: int):
  mountain = next((m for m in mountains if m["id"] == mountain_id), None)

  if not mountain: 
    return {"error": "Mountain not found"}
  
  mountain_name = mountain["name"]
  prompt_input = f"Generate 1 fascinating and little-known facts about {mountain_name}, focusing on its history, cultural significance, or unique geological features. Also, mention one recent event or discovery related to it if available."

  try: 
    response = agent_executor.invoke({
      "input": prompt_input,
    })
    return {"facts" : response["output"]}
  except Exception as e:
    print(f"AI Agent Error: {e}")
    return {"error": "Failed to generate AI facts."}