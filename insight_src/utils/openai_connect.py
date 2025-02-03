import os


def llm_connect(openai_key=None, model="gpt-4o"):
    from langchain_openai import ChatOpenAI
    OPENAI_API_KEY = openai_key or os.environ['OPENAI_API_KEY']
    model = model or os.environ['OPENAI_MODEL_NAME']
    llm = ChatOpenAI(model=model,
                     api_key=OPENAI_API_KEY)
    return llm
