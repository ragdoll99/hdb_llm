import os
from dotenv import load_dotenv
import json
from openai import OpenAI
from langchain.agents import Tool
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI
import pandas as pd
import streamlit as st

# Import the key CrewAI classes
from crewai import Agent, Task, Crew

# Load the environment variables
# If the .env file is not found, the function will return `False
if load_dotenv('.env'):
   # for local development
   OPENAI_KEY = os.getenv('OPENAI_API_KEY')
else:
   OPENAI_KEY = st.secrets['OPENAI_API_KEY']

# Pass the API Key to the OpenAI Client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

os.environ['OPENAI_MODEL_NAME'] = "gpt-4o-mini"

# read csv
url = 'https://drive.google.com/file/d/19P2q3RyermaGJuD88vq1ZxcMjotpq18h/view?usp=sharing'
url='https://drive.google.com/uc?id=' + url.split('/')[-2]
df = pd.read_csv(url)

# Create Pandas Agent
pandas_tool_agent = create_pandas_dataframe_agent(
    llm=ChatOpenAI(temperature=0, model='gpt-4o-mini'),
    df=df,
    agent_type=AgentType.OPENAI_FUNCTIONS,
    allow_dangerous_code=True # <-- This is an "acknowledgement" that this can run potentially dangerous code
)

# Create the tool
pandas_tool = Tool(
    name="Manipulate and Analyze tabular data with Code",
    func=pandas_tool_agent.invoke, # <-- This is the function that will be called when the tool is run. Note that there is no `()` at the end
    description="Useful for search-based queries",
)

from crewai_tools import WebsiteSearchTool

# Create a new instance of the WebsiteSearchTool
tool_websearch = WebsiteSearchTool("https://www.hdb.gov.sg/")


# Creating Agents
agent_data_analyst = Agent(
    role="Data Analyzer",
    goal="Analyze the data based on user query: {topic}",
    backstory="""You're the best data analyst.
    You are answering user queries related to Housing Development Board (HDB) Singapore resale transactions and procedures.
    You have access to historical HDB resale transaction and web search tools to gather the necessary information to respond to user and you will use the information to answer user query""",
    allow_delegation=False,
	verbose=True,
    tools=[pandas_tool, tool_websearch],
)

task_analyze = Task(
    description="""\
    1. Understand the user query: {topic}.
    2. Decide which tool to analyze user query. 
    2. Use the tool to research or analyze the user query.
    3. Develop a factually correct analysis based on user query.""",

    expected_output="""\
    A factually correct response to answer user query""",

    agent=agent_data_analyst
)

crew = Crew(
    agents=[agent_data_analyst],
    tasks=[task_analyze],
    verbose=True
)

def generate_answer(topic):
    result = crew.kickoff(inputs={"topic": topic})
    return result.raw