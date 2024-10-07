# Realtime-insights-from-database or NLP with MSSQLServer DB using LangChain and Streamlit

This project is a web application built using Streamlit, LangChain, and SQLAlchemy that allows users to interact with an MSSQLServer database using natural language processing (NLP). By integrating Azure OpenAI's GPT-3.5, it enables users to ask questions in natural language, which are then processed and translated into SQL queries to retrieve data from the database.

Features
Natural Language Queries: Users can ask questions in plain English, which the application translates into SQL queries to interact with an MSSQLServer database.
Azure OpenAI GPT-3.5 Integration: Leverages Azure’s GPT-3.5 Turbo model to generate responses.
Streamlit UI: A simple, user-friendly interface for selecting models, providing API keys, and querying the database.
SQLAlchemy and LangChain: Utilizes LangChain to manage the process of converting user inputs into SQL queries using SQLAlchemy as the database engine.

How It Works

User Input: Users provide a question or query in the chat input box (e.g., "What is the average salary from the employees table?").
LLM Processing: The question is sent to the Azure OpenAI service, where it is processed by a selected LLM model (GPT-3.5 Turbo).
SQL Query Generation: LangChain agents use the user's input to generate a corresponding SQL query for the connected MSSQLServer database.
Database Interaction: The SQL query is executed on the database, and the results are fetched.
Response Display: The results are displayed back to the user in the Streamlit interface.

Requirements

Python 3.9+
Streamlit
LangChain
SQLAlchemy
Azure OpenAI API Access
MSSQLServer Database

Installation
Clone the repository:

<img width="339" alt="image" src="https://github.com/user-attachments/assets/72b1f505-d174-40fa-879b-ea294e396ae2">

Navigate to the project directory:

bash
Copy code
cd nlp-mssql-langchain
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt

Set up an MSSQLServer database and note down the connection string (e.g., mssql+pymssql://username:password@localhost:1433/database).

Obtain Azure OpenAI API access and note down your:

Deployment Name
API Version
API Key
API Endpoint
Running the Application
Run the Streamlit application:

bash
Copy code
streamlit run app.py

In the sidebar, provide the necessary details:

Chat Model: Choose GPT 3.5 Turbo.
Azure LLM Deployment Name: Enter your deployment name from Azure OpenAI.
API Version: Select the API version, e.g., 2023-12-01-preview.
Azure LLM Endpoint: Enter your Azure OpenAI endpoint URL.
Azure LLM API Key: Provide your API key (this will be kept secure).
In the chat box, ask your natural language query related to the database, and the system will return the results.

Example Usage
The user inputs a question: "What are the top 5 employees with the highest salary?"
The application:
Processes the input with the selected Azure LLM.
Converts the question into an SQL query.
Executes the query on the MSSQLServer database.
Displays the result in the chat.
Project Structure
app.py: Main application script.
requirements.txt: List of required dependencies.
License
This project is licensed under the MIT License. See the LICENSE file for more details.


Acknowledgments
Streamlit for building intuitive web applications.
LangChain for the robust NLP and agent tools.
Azure OpenAI for providing the language models.
