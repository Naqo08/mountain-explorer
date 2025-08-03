# import os
# from dotenv import load_dotenv
# from langchain_google_genai import ChatGoogleGenerativeAI

# load_dotenv()
# GEMIMI_API_KEY = os.getenv("GEMINI_API_KEY")
# llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", api_key=GEMIMI_API_KEY)

# message = [
#   {
#     "system", 
#     "You are a help"
#   }
# ]

import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", api_key=GEMINI_API_KEY)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
                You are a helpful assistant that translates {input_language} to {output_language}. 
                If the text cannot be translated or is unclear, respond with: 'Unable to translate text'
            """
        ),
        (
            "human",
            "{text_input}",
        ),
    ]
)

chain = prompt | llm

class TranslationRequest(BaseModel):
    input_language: str
    output_language: str
    text_input: str

class TranslationResponse(BaseModel):
    translated_text: str

@app.post("/translate", response_model=TranslationResponse)
async def translate_text(request: TranslationRequest):
    try:
        ai_msg = chain.invoke(
            {
                "input_language": request.input_language,
                "output_language": request.output_language,
                "text_input": request.text_input,
            }
        )
        
        return TranslationResponse(translated_text=ai_msg.content)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"message": "Welcome to the Translation API"}
