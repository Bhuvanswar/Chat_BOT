from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import os

load_dotenv()

chat = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)
def chat_with_groq(question):
    response = chat.invoke([HumanMessage(content=question)])
    return response.content

# while True:
#     question = input("You: ")

#     if question.lower() in ["exit", "quit"]:
#         break

#     response = chat_with_groq(question)

#     print("AI:", response)