from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from travel_agent_api.config import Config


def get_historical_info(destination: str) -> str:
    print("[CHAIN] historical_expert chiamato")

    prompt = ChatPromptTemplate.from_template(
        "Sei una guida storico-culturale. "
        "Descrivi in italiano 3 elementi storici o culturali importanti "
        "per questa richiesta di viaggio: {destination}. "
        "Rispondi in modo breve e utile per un turista."
    )

    model = ChatOpenAI(
        model=Config.OPENAI_MODEL,
        api_key=Config.OPENAI_API_KEY,
        temperature=0.2,
    )

    chain = prompt | model | StrOutputParser()

    return chain.invoke({"destination": destination})
