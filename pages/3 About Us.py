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
    How to use this App \n
    1. Enter your prompt in the text area. \n
    2. Click the 'Submit' button. \n
    3. The app will generate a text completion based on your prompt.
    Instruction \n
    A detailed page outlining the project scope, objectives, data sources, and features.
                
    """)

container2 = st.container(border=True)
container2.write(
    """
    Instruction \n
    A detailed page outlining the project scope, objectives, data sources, and features.

    """)

container3 = st.container(border=True)
container3.write(
    """
    Methodology Page:
    A comprehensive explanation of the data flows and implementation details.
    A flowchart illustrating the process flow for each of the use cases in the application. For example, if the application has two main use cases: a) chat with information and b) intelligent search, each of these use cases should have its own flowchart.
    """)