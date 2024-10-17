# draw a line chart
""" Draw a line chart"""
import streamlit as st
import numpy as np
import pandas as pd

st.title(":blue[Methodology]")
st.markdown("The **HDB Resale Transactions Intelligent Bots and Data Explorer** application was built with the goal of providing users with fast, accurate, and comprehensive insights into the Singapore HDB resale market.")

st.image("image/hdb_llm_flowchat.jpeg", caption="Methodology flow chart")

container = st.container(border=True)

container.write(
    """
    ### **Methodology**

    #### **1. Platform & Data Sources**
    The application leverages the **OpenAI platform** to deliver intelligent chatbot interactions and advanced data exploration capabilities. **Data** was sourced from **data.gov.sg**, specifically focusing on HDB resale transactions to ensure accuracy and relevance.

    #### **2. Data Pre-processing**
    To ensure smooth performance and minimize query latency, the data was **pre-processed**. This involved:
    - Cleaning and standardizing the dataset.
    - Optimizing data structures for faster retrieval.
    - Aggregating key data points such as historical prices, locations, and flat types for efficient querying.

    #### **3. Intelligent Query Handling**
    User queries are managed through an integrated AI system based on **Crew AI**, enhanced with:
    - **Pandas tools** for dataset-specific questions: These allow for rapid analysis and response to user inquiries about HDB transactions, such as historical statistics, trends, and prices.
    - **Web search tools** for general enquiries: For procedural questions (e.g., buying or selling processes), the chatbot can access and provide real-time, accurate information based on official guidelines and resources.

    #### **4. User Interaction & Experience**
    The system is designed to provide users with two key features:
    - **HDB Resale Intelligent Chatbots**: Capable of answering a wide variety of questions, from transactional data to procedural advice.
    - **HDB Resale Transaction Explorer**: A powerful, intuitive platform that allows users to explore data visually, using advanced slicers and dropdowns to filter according to their needs.

    By combining **AI-driven intelligence** with structured data from trusted sources, the application provides users with a seamless, insightful experience in navigating the HDB resale market.

    """)

