from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load variables from .env
load_dotenv()

# Create LangChain OpenAI model
llm = ChatOpenAI(model="gpt-4.1-mini")

prompt = "Tell me a fun fact about Tamil Nadu."

response = llm.invoke(prompt)

print(f"Input: {prompt}")
print(f"Output: {response.content}")