import langchain
import os
import json

from getpass import getpass

from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

#from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

from termcolor import colored

#os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY") or getpass("Enter OpenAI API Key: ")
os.environ["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY") or getpass("Enter Google GEMINI API Key: ")

def main():

    #model = "gpt-4.1"
    #llm = ChatOpenAI(temperature=0.0, model=model)
    #creative_llm = ChatOpenAI(temperature=0.9, model=model)

    api_key = os.environ["GEMINI_API_KEY"]
    model = 'gemini-2.0-flash'
    llm = ChatGoogleGenerativeAI(temperature=0.0, model=model, google_api_key=api_key)
    creative_llm = ChatGoogleGenerativeAI(temperature=0.9, model=model, google_api_key=api_key)

    print(f"\nInitializing langchain model '{colored(model,'yellow')}'..")

    article = "Our client leverages AI to analyze customer feedback from various sources in real-time, helping companies quickly identify product issues and opportunities, ultimately improving customer satisfaction. It transforms raw feedback into actionable insights, enabling businesses to enhance their offerings and optimize the customer experience."

    # Defining the system prompt (how the AI should act)
    system_prompt = SystemMessagePromptTemplate.from_template(
        "Be an AI assistant called {name} that helps generate article titles.",
        input_variables=["name"]
    )

    # Define the desired structure of the output
    response_schemas = [
        ResponseSchema(name="article_titles", description="A valid JSON list of 10 items", type="list")
    ]

    # Create the parser
    output_parser = StructuredOutputParser(response_schemas=response_schemas)

    # Get the format instructions from the parser
    format_instructions = output_parser.get_format_instructions()

    # Defining the user prompt
    user_prompt = HumanMessagePromptTemplate.from_template(
        """
        The article you will examine is the following:
        
        ---

        {article}
        
        ---

        You are tasked with creating names for an article.
        The names should be based on the context of the article.
        Be creative, but make sure the names are clear, catchy, and relavant to the theme of the article.
        Response should be in a valid JSON dictionary format.
        """,
            input_variables= ["article"]
    )

    #user_prompt.format(article="TEST STRING")
    first_prompt = ChatPromptTemplate.from_messages([system_prompt, user_prompt])

    chain_one = (
        {
            "article": lambda x: x["article"],
            "name": lambda x: x["name"]
        }
        | first_prompt
        | creative_llm
        | output_parser
        #| {"article_title": lambda x: x.content}
    )

    agent_response = chain_one.invoke({
        "article": article,
        "name": "Joe",
        "format_instructions": format_instructions
    })

    print(f"\nAI Agent RAW response: \n\n{agent_response}\n")

    output_json_str = json.dumps(agent_response, indent=4)
    print(f"\nAI Agent JSON response: \n\n{output_json_str}\n")

main()
