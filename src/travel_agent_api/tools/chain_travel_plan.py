from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from travel_agent_api.config import Config


def create_travel_plan(destination: str) -> str:
    print("[CHAIN] travel_plan chiamato")

    prompt = ChatPromptTemplate.from_template(
        "Crea un breve piano di viaggio per questa richiesta: {destination}. "
        "Rispondi in italiano, con massimo 5 punti."
    )

    model = ChatOpenAI(
        model=Config.OPENAI_MODEL,
        api_key=Config.OPENAI_API_KEY,
        temperature=0.3,
    )

    chain = prompt | model | StrOutputParser()

    return chain.invoke({"destination": destination})
