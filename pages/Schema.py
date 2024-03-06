import streamlit as st
import requests

st.set_page_config(
    page_title="Schema",
    page_icon="🗄️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

def fetch_data_from_api():
    # Make a request to the API and fetch the data
    response = requests.get("http://194.68.245.145:22197/metadata")
    data = response.json()
    return data["metadata"]

data = fetch_data_from_api()


def update_data_to_api(new_data):
    # Make a request to the API and update the data
    print("inside update_data_to_api")
    print(new_data)
    response = requests.put("http://194.68.245.145:22197/metadata", json=new_data)
    if response.status_code == 200:
        st.success("Data updated successfully!")
    else:
        st.error("Failed to update data.")



# Display the data in a text element
text_input = st.text_area(label="SQL Schema",value=data ,height=200,label_visibility="hidden",key="sql_schema")
#st.text(data)
# Example usage:
if st.button("Update"):
    data ={"metadata":text_input}   
    update_data_to_api(data)
