import streamlit as st
from langchain.agents import create_sql_agent
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain.agents.agent_types import AgentType
from langchain_community.utilities import SQLDatabase
from sqlalchemy import create_engine
from langchain_openai import AzureChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate
from langchain.agents import AgentExecutor


def main():
    st.title("NLP with MSSQLServer DB")
    llm_model = st.sidebar.selectbox("Chat Model", ("GPT 3.5 Turbo", ""))
    azure_chat_deployment_name = st.sidebar.text_input("Azure LLM Deployment Name")
    azure_api_version = st.sidebar.selectbox("API Version", ("2023-12-01-preview", ""))
    azure_endpoint = st.sidebar.text_input("Azure LLM Endpoint")
    azure_api_key = st.sidebar.text_input("Azure LLM API Key", type='password')
    query = st.chat_input('Ask questions to DB')
    
    if query and azure_api_key and azure_endpoint and azure_chat_deployment_name:
        st.spinner("Thinking..")
        llm = AzureChatOpenAI(
                temperature=0,
                openai_api_key=azure_api_key,
                openai_api_version=azure_api_version,
                azure_deployment=azure_chat_deployment_name,
                azure_endpoint=azure_endpoint
                )
    
        connection_string = f"mssql+pymssql://sa_user:<DB_password>@localhost:1433/testdb"
        db = SQLDatabase.from_uri(connection_string)
        db_engine=create_engine(connection_string)
        db=SQLDatabase(db_engine)
        sql_toolkit=SQLDatabaseToolkit(db=db,llm=llm)
        # args={"return_intermediate_steps": True}
        sql_toolkit.get_tools()

        prompt=ChatPromptTemplate.from_messages(
            [
                ("system",
                """
                This script queries testdb database with 5 tables. 
                """
                ),
                ("user","{question}\ ai: ")
            ]
        )         
        
        agent=create_sql_agent(llm=llm,toolkit=sql_toolkit,agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,verbose=True)
        agent_handle_parsing_errors=True

        response = agent.run(prompt.format_prompt(question=query))
        st.write(response)

      

if __name__ == "__main__":
  main()
