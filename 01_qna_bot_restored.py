from dotenv import load_dotenv
load_dotenv()


from langchain_groq import ChatGroq

llm = ChatGroq(model="openai/gpt-oss-120b") 
que = "Who is PM of India?"

res = llm.invoke(que)
print(res.content)