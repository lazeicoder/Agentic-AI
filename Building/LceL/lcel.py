from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes
import os 
from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.getenv("GROK_API_KEY")
model = ChatGroq(model="llama-3.1-8b-instant", groq_api_key=groq_api_key) 


system_template = "You are an expert AI Engineer with over 30+ years of experience in the Software and AI Research domain, with large scale understanding of how AI (different machine learning, deep learning, reinforcement learning techniques, transformers, agentic ai) systems work, perform, architecture, and how to scale them for larger client and user base. Based on your experience in the field, provide me with answers mathematically."

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", system_template),
        ("user", "{text}"),
    ]
)

# Create output parser
parser = StrOutputParser()

# Create chain
chain = prompt_template | model | parser 

# App Defination
app = FastAPI(
    title="Langchain Server", 
    version="1.0",
    description="A simple API server using Langchain"
)

# Adding chain Routes
add_routes(
    app, 
    chain,
    path="/chain"
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8080)