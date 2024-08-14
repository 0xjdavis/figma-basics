import streamlit as st
import requests

# Your Figma API access token
access_token = st.secrets["FIGMA_API_KEY"]

# The file key from the Figma file URL
file_key = 'pagv93kJSWZUwhmr6BIyVG'  # Replace with your Figma file key

# Figma API endpoint for getting file data
url = f'https://api.figma.com/v1/files/{file_key}'
file_url = f'https://www.figma.com/design/{file_key}'

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
    # Please adjust this path based on your actual JSON structure
    try:
        # Assuming that 'thumbnailUrl' is a key present at the top level for simplicity
        # The actual key path may vary based on your Figma file structure
        thumbnail_url = figma_data.get('thumbnailUrl', '')  # Adjust this path as needed
        # and...    
        name = figma_data.get('name', '')
        lastModified = figma_data.get('lastModified', '')
        version = figma_data.get('version', '')
        role = figma_data.get('role', '')
        editorType = figma_data.get('editorType', '')
        linkAccess = figma_data.get('linkAccess', '')

        
        # Display the thumbnail image if URL is found
        if thumbnail_url:
            st.image(thumbnail_url, width=300)
            thumbnail_url = figma_data.get('thumbnailUrl', '')  # Adjust this path as needed
            
            st.subheader(name)
            st.write("Last Modified: " + lastModified)
            st.write("Version: " + version)
            st.write("Role: " + role)
            st.write("Editor Type: " + editorType)
            st.write("Link Access: " + linkAccess)
            st.markdown('<a href="' + file_url + '" target="_blank"><button style="background-color:#000;color:#fff;border-radius:3px;">Open File in Figma</button></a>', unsafe_allow_html=True)
        else:
            st.warning('Thumbnail URL not found in the Figma data.')
        
        # Display other Figma data
        st.write(figma_data)

    except KeyError as e:
        st.warning(f'Error in accessing thumbnail URL: {e}')

else:
    st.warning(f'Failed to retrieve the file. Status code: {response.status_code}')
