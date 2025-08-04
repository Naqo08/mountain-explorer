# **🏔️ mountain-explorer**

### **Mountain Explorer Web App**

This app enables the user to view and get interesting facts about mountains. The user also able to generate unique facts about the mountains just by pressing the "Generate AI Facts".

## **📁 Project Structure**

This repository contains both the fronend and backend system built with: 

- **React** for frontend framework
- **Bootstrap** for styling
- **FastAPI** for the web API
- **LangChain & Gemini** for AI-powered fact generation

## **🚀 Getting Started**
#### Follow these steps to set up the project.

## **🔗 I. Clone the Repository**

```bash
git clone https://github.com/Naqo08/mountain-explorer.git
cd mountain-explorer
```

## **II. 🐍 Backend Setup (FastAPI)**

### **A. Set Up Virtual Environment**

1. **Navigate to the backend folder**
  - Open your preferred terminal and from the project's root directory, run: 
  `cd backend`
  - Now your current directory will look like:  

    `./mountain-explorer/backend`

2. **Create the virtual environment**
  - Run the following command. This creates a .venv folder in your backend directory

    ```bash
    # For Windows
    python -m venv .venv
    
    # For macOS/Linux
    python3 -m venv .venv
    ```

3. **Activate the Virtual Environment**
  - *Windows*
    ```bash
    # For Git Bash
    source .venv/Scripts/activate`

    # For Command Prompt
    .\venv\Scripts\activate
    ```

  - *macOS/Linux*
    ```bash
    source .venv/bin/activate
    ```

### **B. Install Dependencies & Run**

1. **Install Dependencies**
  - With your virtual environment active, install all required packages from the requirements.txt file.

    ```bash
    pip install -r requirements.txt
    ```
2. **Set Up Environment Variables**
  - In the `backend` directory, create a new file named `.env`.
  - Add your API keys to this file. This is crucial for the AI features to work. 

    ```bash
    GEMINI_API_KEY="your_google_api_key_here"
    TAVILY_API_KEY="your_tavily_api_key_here"
    ```

3. **Run the FastAPI Server**
  - From the `backend` directory, run the development server with: 

    ```bash
    uvicorn main:app --reload
    ```
  - Once the server is running, you can access it at: 
    - API Root: `http://127.0.0.1:8000`
    - API Docs (Swagger UI) `http://127.0.0.1:8000/docs`


## **III. 💻 Frontend Setup (React)**

### **A. Install Node.js**

1. **Download Node.js**
  - If you don't have Node.js installed, download the LTS (Long-Term Support) version from the official Node.js website.
2. **Verify Installation**
  - Open a new terminal and run the following commands to ensure Node.js and npm are installed correctly.: 

    ```bash
    node --version
    npm --version
    ```

### **B. Install Dependencies & Run**

1. **Navigate to the frontend folder**
  - From the project's root directory, run: 

    ```bash
    cd frontend
    ```

2. **Install Dependencies**
  - This command will download all the necessary React packages defined in `package.json`.

    ```bash
    npm install
    ```
3. **Run the React Development Server**
  - Start the frontend application with: 

    ```bash
    npm run dev
    ```
  - Your browser should automatically open to `http://localhost:5173` (or a similar port), where you can see the Mountain Explorer app running.


