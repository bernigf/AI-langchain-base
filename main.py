import langchain
import os

from getpass import getpass
from langchain_openai import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)

from termcolor import colored

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY") or getpass("Enter OpenAI API Key: ")

def main():

    model = "gpt-5-mini"
    print(f"Init langchain model '{colored(model,'yellow')}'..")

    llm = ChatOpenAI(temperature=0.0, model=model)
    creative_llm = ChatOpenAI(temperature=0.9, model=model)
    
    article = "Our client leverages AI to analyze customer feedback from various sources in real-time, helping companies quickly identify product issues and opportunities, ultimately improving customer satisfaction. It transforms raw feedback into actionable insights, enabling businesses to enhance their offerings and optimize the customer experience."

    # Defining the system prompt (how the AI should act)
    system_prompt = SystemMessagePromptTemplate.from_template(
        "Be an AI assistant called {name} that helps generate article titles.",
        input_variables=["name"]
    )

    # Defining the user prompt
    user_prompt = HumanMessagePromptTemplate.from_template(
        """
        The article you will examine is the following:
        ```
        {article}
        ```
        You are tasked with creating a name for a article.
        The name should be based on the context of the article.
        Be creative, but make sure the names are clear, catchy, and relavant to the theme of the article.

        Only output the article name, no other explanation or text will be provided.
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
        | {"article_title": lambda x: x.content}
    )

    article_title_msg = chain_one.invoke({
        "article": article,
        "name": "Joe"
    })

main()
