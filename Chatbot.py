# Set up and run this Streamlit App
import streamlit as st
from logics.crew import generate_answer
from utility import check_password

# newly added
import sqlite3
import pysqlite3
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="wide",
    page_title="💬 HDB resale Intelligent Bot"
)

# Do not continue if check_password is not True.  
if not check_password():  
    st.stop()

# endregion <--------- Streamlit App Configuration --------->

st.title("💬 HDB resale Intelligent Bot")
st.write("Ask me anything about HDB resale transaction")


# Store LLM generated responses
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

# Display or clear chat messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Generate a new response if last message is not from assistant
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    if st.session_state.messages[-1]["role"] != "assistant":
        # with st.chat_message("assistant"):
        with st.spinner("Thinking..."):        
            response = generate_answer(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)
##
###