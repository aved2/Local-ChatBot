import streamlit as st
from openai import OpenAI

st.title("Local ChatGPT Clone")
st.caption("Chat with Meta's LLama3 locally hosted by LM studio. No internet required!")

client = OpenAI(base_url="http://localhost:8000", api_key="lm-studio")

if "messages" not in st.session_state:
    st.session_state.messages = []

#Displaying chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#User input
if prompt:= st.chat_input("What is up?"):
    #Add to chat history and display user input
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    #Generate response
    response = client.chat.completions.create(
        model= "lmstudio-community/Meta-LLama3-8B-Instruct-GGUF",
        messages= st.session_state.messages,
        temperature= 0.7,
    )
    #Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content})

    with st.chat_message("assistant"):
        st.markdown(response.choices[0].message.content)