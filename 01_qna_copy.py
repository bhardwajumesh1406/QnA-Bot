from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

llm = ChatGroq(model="openai/gpt-oss-120b") 


st.title("AskBuddy - AI QnA Bot")
st.markdown("My QnA Bot with Langchain and GroqAI !")
query = st.chat_input("Ask Anything...")



if "messages" not in st.session_state:
    st.session_state.messages = []
    
    
if query:
    st.session_state.messages.append({
        "role":"user", "content": query
    })
  
    st.chat_message("user").markdown(query)
    res = llm.invoke(query)

    st.spinner("Wait for answer...")
    st.chat_message("ai").markdown(res.content)
    st.session_state.messages.append({
            "role":"ai", "content": res.content
        })
    
for message in st.session_state.messages:
    print("message -------------------------- ",message)
    role = message['role']
    content = message['content']
    st.chat_message(role).markdown(content)

