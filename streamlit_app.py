import streamlit as st
import requests

# Your Figma API access token
access_token = st.secrets["FIGMA_API_KEY"] # 'your_access_token_here'

# The file key from the Figma file URL
# LINK: https://www.figma.com/design/pagv93kJSWZUwhmr6BIyVG/Figma-basics?m=auto&t=U8vfwSQqWWQO9rBO-6

placeholder = 'pagv93kJSWZUwhmr6BIyVG' # 'your_file_key_here'
file_key = placeholder # 'your_file_key_here'
# Figma API endpoint for getting file data
url = f'https://api.figma.com/v1/files/{file_key}'

headers = {
    'X-Figma-Token': access_token
}

response = requests.get(url, headers=headers)

st.title("Figgy Putting")
st.write("Get Figma data using the API.")
st.text_input("Figma File ID", file_key, placeholder=file_key)

# Check if the request was successful
if response.status_code == 200:
    figma_data = response.json()
    # Now you can process the figma_data JSON as needed
    st.write(figma_data)
else:
    st.warning('Failed to retrieve the file:', response.status_code)
