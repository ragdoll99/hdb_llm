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

message2 = """
The process of buying a resale Housing and Development Board (HDB) flat in Singapore is structured and involves several critical steps:

Eligibility Check: Confirm that you meet the criteria established by HDB, including citizenship, age, and family nucleus requirements.

Obtaining HDB Loan Eligibility (HLE) Letter: If you need financing, apply for the HLE letter, which indicates your borrowing capacity and is valid for six months.

Searching for a Resale Flat: Use online platforms and real estate agents to find a flat that matches your preferences and budget.

Verification of Flat Details: Check the flat’s lease duration, condition, and any financial encumbrances to ensure everything is in order.

Making an Offer: Submit your offer to the seller and negotiate the price and terms of sale.

Signing the Option to Purchase (OTP): Once an agreement is reached, sign the OTP and pay an option fee, usually 1% of the purchase price.

Exercising the OTP: Complete the OTP within 21 days by signing the sale and purchase agreement and paying a deposit of around 4%.

Loan Application: If financing, submit your application along with the necessary documents to the bank or HDB.

Finalizing the Sale: Go to the HDB office to complete the sale, sign documents, and pay the remaining amount for the property.

Transfer of Ownership: HDB will facilitate the ownership transfer, and you will receive the keys to your flat.

Renovation and Moving In: After receiving the keys, you can renovate your flat as desired before moving in.

Post-Purchase Obligations: Be aware of ongoing commitments like the Minimum Occupation Period (MOP) which may impact your ownership.

By following these steps, you can navigate the process efficiently and secure your new home, ensuring compliance with all necessary legal and financial requirements. Engaging with professionals can also aid in a smoother transition into homeownership.
"""
message3="""
The resale HDB that is closest to a hawker centre is located at 32 New Market Road, in the Central Area. This property is a 3-room flat with a resale price of $392,000. Remarkably, it is situated merely 1.87 meters away from the nearest hawker centre, offering unparalleled convenience for residents who prioritize access to dining and local amenities. With a floor area of 66 sqm, this flat represents an attractive option for potential buyers seeking affordability in a bustling urban environment. Its prime location not only enhances livability but also ensures easy access to public transportation and grocery stores. Given these factors, the resale HDB at 32 New Market Road stands out as the optimal choice for those looking to live close to hawker centres.
"""

st.session_state.setdefault(
    'past', 
    ['Which area of hdb resale is cheaper',
     'What is the process of buying resale hdb', 
     'which resale hdb has the nearest distance to hawker centre', 
     'and video of it']
)
st.session_state.setdefault(
    'generated', 
    [{'type': 'normal', 'data': message1},
     {'type': 'normal', 'data': message2}, 
     {'type': 'normal', 'data': message3}, 
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