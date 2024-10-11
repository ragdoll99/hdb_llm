# Set up and run this Streamlit App
import streamlit as st
from logics.test import generate_answer
from utility import check_password
from streamlit_chat import message

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="wide",
    page_title="HDB resale Intelligent Bot"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("HDB resale Intelligent Bot")
st.write("Ask me anything about HDB resale transaction")

def on_input_change():
    user_input = st.session_state.user_input
    st.session_state.past.append(user_input)
    st.session_state.generated.append("The messages from Bot\nWith new line")

def on_btn_click():
    del st.session_state.past[:]
    del st.session_state.generated[:]

message1 = """
The area of Yishun stands out as the cheapest for HDB resale prices in Singapore, with an average resale price of approximately $375,347. This indicates that Yishun is a favorable option for prospective buyers seeking affordable housing solutions. Compared to other regions such as Bukit Merah, Queenstown, and Toa Payoh, which report higher average resale prices, Yishun offers competitive and appealing pricing for budget-conscious homebuyers. Therefore, for those looking to invest in HDB resale flats, considering Yishun would be advantageous due to its lower cost and the potential for future urban development enhancing property values.
"""

st.session_state.setdefault(
    'past', 
    ['Which area of hdb resale is cheaper',
     'play the song "Dancing Vegetables"', 
     'show me image of cat', 
     'and video of it']
)
st.session_state.setdefault(
    'generated', 
    [{'type': 'normal', 'data': message1},
     {'type': 'normal', 'data': f'a'}, 
     {'type': 'normal', 'data': f'<img width="100%" height="200" src=/>'}, 
     {'type': 'normal', 'data': f'c'}]
)

chat_placeholder = st.empty()

with chat_placeholder.container():    
    for i in range(len(st.session_state['generated'])):                
        message(st.session_state['past'][i], is_user=True, key=f"{i}_user")
        message(
            st.session_state['generated'][i]['data'], 
            key=f"{i}", 
            allow_html=True,
            is_table=True if st.session_state['generated'][i]['type']=='table' else False
        )
    
    st.button("Clear message", on_click=on_btn_click)

with st.container():
    st.text_input("User Input:", on_change=on_input_change, key="user_input")