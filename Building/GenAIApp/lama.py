import os 
import streamlit as st

from dotenv import load_dotenv
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

os.environ["LANGCHAIN_GEMINI_API_KEY"] = os.getenv("LANGCHAIN_GEMINI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")


# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an expert AI Engineer with over 20+ years of experience in the Software and AI Research domain, with large scale understanding of how AI (different machine learning, deep learning, reinforcement learning techniques, transformers, agentic ai) systems work, perform, architecture, and how to scale them for larger client and user base. So based on your experience in the field, provide me with answers."),
        ("user", "Question: {question}")
    ]
)

# Streamlit Framework
st.title("AIGpt - Your personal AI mentor")
input_text = st.text_input("What question do you have in mind?")


# Calling the LLM Model
llm = Ollama(model="gemma:2b") 
output_parser = StrOutputParser()

# Chaining the Agent
chain = prompt | llm | output_parser

# Starting the question-response cycle
if input_text:
    st.write(
        chain.invoke({
            "question": input_text,
        })
    )