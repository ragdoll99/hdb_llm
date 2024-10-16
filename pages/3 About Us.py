# draw a line chart
""" Draw a line chart"""
import streamlit as st
import numpy as np
import pandas as pd

st.title(":blue[About this page]")
st.markdown("This is a Streamlit App that demonstrates how to use the OpenAI API to generate text completions.")

container = st.container(border=True)

container.write(
    """
    Welcome to HDB Resale Transactions Intelligent Bots and Data Explorer, your go-to platform for navigating the Singapore HDB resale market with ease and confidence.\n

    Our mission is simple: to provide buyers and sellers with the data-driven tools and insights needed to make well-informed decisions.\n

    Our application is built around two core features:\n

    1. HDB Resale Intelligent Chatbots - Whether you're curious about past transactions or need guidance on resale procedures, our smart chatbots are here to assist. They can answer a wide range of queries, making your experience smoother and more informed.\n
    2. HDB Resale Transaction Explorer - This powerful, user-friendly tool allows you to visualize and filter resale flat data through advanced slicers and dropdowns. From location and price to flat types, finding the perfect option has never been easier.\n
    Explore the HDB resale market with confidence, backed by intelligent insights and seamless tools.\n
                
    """)
