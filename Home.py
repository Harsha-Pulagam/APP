import streamlit as st
import pandas as pd
import sqlite3
import requests
import json

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Connect to the database
conn = sqlite3.connect('movie.sqlite')
cursor = conn.cursor()

# Define a function to execute SQL queries
def run_query(query):
    #st.write("Query:", query)
    cursor.execute(query)
    data = cursor.fetchall()
    return data

    
def api_call(query):
    j_obj = {"text": query}
    # Execute the query and fetch the data
    response = requests.post('http://194.68.245.145:22197/sqlcoder', json=j_obj)
    data = run_query(response.json())
    
    # Display the data in a table
    df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description])
    return df
        
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])       


# Run the app
if prompt := st.chat_input("Ask your question here..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = api_call(prompt)
        st.write(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    
