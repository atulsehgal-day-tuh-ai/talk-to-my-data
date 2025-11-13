from utils.config_loader import load_env
load_env()

# --- LangChain imports ---
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def test_langchain():
    print("🚀 Starting LangChain test...")

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, timeout=20)

    prompt = ChatPromptTemplate.from_template("Translate this sentence into Spanish: {sentence}")
    chain = prompt | llm | StrOutputParser()

    response = chain.invoke({"sentence": "Hello, how are you today?"})
    print("✅ LangChain test succeeded!")
    print("Response:", response)


if __name__ == "__main__":
    test_langchain()
