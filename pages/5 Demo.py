# Set up and run this Streamlit App
import streamlit as st
from logics.crew import generate_answer
from utility import check_password
from streamlit_chat import message

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


message1 = """
The area of Yishun stands out as the cheapest for HDB resale prices in Singapore, with an average resale price of approximately $375,347. 

This indicates that Yishun is a favorable option for prospective buyers seeking affordable housing solutions. Compared to other regions such as Bukit Merah, Queenstown, and Toa Payoh, which report higher average resale prices, Yishun offers competitive and appealing pricing for budget-conscious homebuyers. 

Therefore, for those looking to invest in HDB resale flats, considering Yishun would be advantageous due to its lower cost and the potential for future urban development enhancing property values.
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
The resale HDB that is closest to a hawker centre is located at 32 New Market Road, in the Central Area. This property is a 3-room flat with a resale price of $392,000. 

Remarkably, it is situated merely 1.87 meters away from the nearest hawker centre, offering unparalleled convenience for residents who prioritize access to dining and local amenities. 

With a floor area of 66 sqm, this flat represents an attractive option for potential buyers seeking affordability in a bustling urban environment. 

Its prime location not only enhances livability but also ensures easy access to public transportation and grocery stores. Given these factors, the resale HDB at 32 New Market Road stands out as the optimal choice for those looking to live close to hawker centres.
"""

message4="""
When applying for Housing and Development Board (HDB) Flat Eligibility (HFE) in Singapore, the following documents and information are required to ensure a successful application:

Identity Documents:

National Registration Identity Card (NRIC) for all applicants and essential family members.
Income Documents:

Recent payslips from the last three months.
Income tax statements or Notice of Assessment for self-employed individuals.
Documentation for any other income sources, such as rental income or dividends.
Family Nucleus:

Details about family members who will reside in the flat, including their NRICs and relationships to the applicant.
Relationship Documents:

Marriage Certificate if applying with a spouse.
Divorce Certificate if applicable.
Eligibility Criteria:

Ensure compliance with citizenship, age, and family nucleus requirements outlined by HDB.
Application Form:

A completed HDB application form, usually available online.
Additional Documentation:

Any relevant supplementary documents based on individual circumstances, such as adoption papers or a death certificate of a spouse.
To enhance the chances of securing eligibility, it’s advised to systematically gather these documents. Additionally, applicants should regularly check HDB's official website for any updates to ensure compliance with evolving application requirements. By being well-prepared, applicants can facilitate a smoother application process.
"""

query1 = "Which area of hdb resale is cheaper"
query2 = "What is the process of buying resale hdb"
query3 = "Which resale hdb has the nearest distance to hawker centre"
query4 = "What is needed when applying for HFE"

# Store LLM generated responses
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

# st.session_state.messages.append({"role": "assistant", "content": "How can I help you?"})
st.session_state.messages.append({"role": "user", "content": query1})
st.session_state.messages.append({"role": "assistant", "content": message1})
st.session_state.messages.append({"role": "user", "content": query2})
st.session_state.messages.append({"role": "assistant", "content": message2})
st.session_state.messages.append({"role": "user", "content": query3})
st.session_state.messages.append({"role": "assistant", "content": message3})
st.session_state.messages.append({"role": "user", "content": query4})
st.session_state.messages.append({"role": "assistant", "content": message4})

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

st.write("hello")