# Set up and run this Streamlit App
import streamlit as st
from logics.crew import generate_answer
from utility import check_password
import replicate

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


### Create form <------------------------------------------
# form = st.form(key="form")
# form.subheader("Prompt")

# user_prompt = form.text_area("Enter your prompt here", height=200)

# if form.form_submit_button("Submit"):
#     st.toast("User Input Submitted - {user_prompt}")
#     response = generate_answer(user_prompt) #<--- This calls the `process_user_message` function that we have created 🆕
#     # st.write(response[0])
#     st.write(response)
#     # response[1]
#     # print(f"User Input is {user_prompt}")

### End of Create form < -----------------------------------












# import streamlit as st
# from streamlit_chat import message


# def on_input_change():
#     user_input = st.session_state.user_input
#     st.session_state.past.append(user_input)
#     st.session_state.generated.append("The messages from Bot\nWith new line")

# def on_btn_click():
#     del st.session_state.past[:]
#     del st.session_state.generated[:]

# audio_path = "https://docs.google.com/uc?export=open&id=16QSvoLWNxeqco_Wb2JvzaReSAw5ow6Cl"
# img_path = "https://www.groundzeroweb.com/wp-content/uploads/2017/05/Funny-Cat-Memes-11.jpg"
# youtube_embed = '''
# <iframe width="400" height="215" src="https://www.youtube.com/embed/LMQ5Gauy17k" title="YouTube video player" frameborder="0" allow="accelerometer; encrypted-media;"></iframe>
# '''

# st.session_state.setdefault(
#     'past', 
#     ["aaa"]
# )
# st.session_state.setdefault(
#     'generated', 
#     ["bbb"]
# )

# chat_placeholder = st.empty()

# with chat_placeholder.container():    
#     for i in range(len(st.session_state['generated'])):                
#         message(st.session_state['past'][i], is_user=True, key=f"{i}_user")
#         message(
#             st.session_state['generated'][i]['data'], 
#             key=f"{i}", 
#             allow_html=True,
#             is_table=True if st.session_state['generated'][i]['type']=='table' else False
#         )
    
#     st.button("Clear message", on_click=on_btn_click)

# with st.container():
#     st.text_input("User Input:", on_change=on_input_change, key="user_input")

# Store LLM generated responses
# if "messages" not in st.session_state.keys():
#     st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

# Display or clear chat messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.write(message["content"])

# def clear_chat_history():
#     st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]
# st.sidebar.button('Clear Chat History', on_click=clear_chat_history)


# User-provided prompt
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = generate_answer(prompt)
            placeholder = st.empty()
            full_response = ''
            for item in response:
                full_response += item
                placeholder.markdown(full_response)
            placeholder.markdown(full_response)
    message = {"role": "assistant", "content": full_response}
    st.session_state.messages.append(message)
    
# Load the environment variables
# If the .env file is not found, the function will return `False
    

# from dotenv import load_dotenv
# from openai import OpenAI

# if load_dotenv('.env'):
#    # for local development
#    OPENAI_KEY = os.getenv('OPENAI_API_KEY')
# else:
#    OPENAI_KEY = st.secrets['OPENAI_API_KEY']


# if prompt := st.chat_input():
#     client = OpenAI(api_key=OPENAI_KEY)
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     st.chat_message("user").write(prompt)
#     response = generate_answer(prompt)
#     # response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
#     # msg = response.choices[0].message.content
#     # st.session_state.messages.append({"role": "assistant", "content": msg})
#     # st.chat_message("assistant").write(msg)
#     st.session_state.messages.append({"role": "assistant", "content": response})
#     st.chat_message("assistant").write(response)
###
###