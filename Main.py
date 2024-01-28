from langchain_experimental.llm_symbolic_math.base import LLMSymbolicMathChain
from langchain_openai import OpenAI
import streamlit as st

st.title("Symbolic Math Chain")

question=st.text_input("Enter your question here")
