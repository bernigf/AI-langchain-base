import langchain
import os

from getpass import getpass
from langchain_openai import ChatOpenAI

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY") or getpass("Enter OpenAI API Key: ")

def main():

    model = "gpt-5-mini"
    print(f"Init langchain model '{model}..")

    llm = ChatOpenAI(temperature=0.0, model=model)
    
main()
