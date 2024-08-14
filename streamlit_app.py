import streamlit as st
import requests

# Your Figma API access token
access_token = st.secrets["FIGMA_API_KEY"]

# The file key from the Figma file URL
file_key = 'pagv93kJSWZUwhmr6BIyVG' # your_file_key_here

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
    
    # Example extraction of the thumbnail URL from the JSON data
    # You need to adjust the key paths based on the actual structure of your JSON
    try:
        thumbnail_url = figma_data['document']['children'][0]['children'][0]['thumbnailUrl']  # Modify this path as needed
        st.image(thumbnail_url, width=300)  # Display the thumbnail image
    except KeyError:
        st.warning('Thumbnail URL not found in the Figma data.')

    st.write(figma_data)
else:
    st.warning('Failed to retrieve the file:', response.status_code)
