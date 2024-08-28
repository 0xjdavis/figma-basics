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

# Setting page layout
st.set_page_config(
    page_title="Figma basics",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Sidebar for API Key and User Info
st.sidebar.header("About App")
st.sidebar.markdown('This is an app that retreives data from files using the Figma API created by <a href="https://ai.jdavis.xyz" target="_blank">0xjdavis</a>.', unsafe_allow_html=True)

# Calendly
st.sidebar.markdown("""
    <hr />
    <center>
    <div style="border-radius:8px;padding:8px;background:#fff";width:100%;">
    <img src="https://avatars.githubusercontent.com/u/98430977" alt="Oxjdavis" height="100" width="100" border="0" style="border-radius:50%"/>
    <br />
    <span style="height:12px;width:12px;background-color:#77e0b5;border-radius:50%;display:inline-block;"></span> <b style="color:#000000">I'm available for new projects!</b><br />
    <a href="https://calendly.com/0xjdavis" target="_blank"><button style="background:#126ff3;color:#fff;border: 1px #126ff3 solid;border-radius:8px;padding:8px 16px;margin:10px 0">Schedule a call</button></a><br />
    </div>
    </center>
    <br />
""", unsafe_allow_html=True)

# Copyright
st.sidebar.caption("©️ Copyright 2024 J. Davis")

# Main Page
st.title("Figma basics")
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
        thumbnail_url = figma_data.get('thumbnailUrl', '')
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
            thumbnail_url = figma_data.get('thumbnailUrl', '')
            
            st.subheader(name)
            st.write("Last Modified: " + lastModified)
            st.write("Version: " + version)
            st.write("Role: " + role)
            st.write("Editor Type: " + editorType)
            st.write("Link Access: " + linkAccess)
            
            # st.write("""<p>Live View</p><figure><embed type="image/svg+xml" src="./figma.svg" /></figure>""", unsafe_allow_html=True)
            st.markdown('<a href="' + file_url + '" target="_blank"><button style="background-color:#000;color:#fff;border-radius:3px;"><img src="https://static.figma.com/app/icon/1/favicon.svg" height="14" /> Open File in Figma</button></a>', unsafe_allow_html=True)
        else:
            st.warning('Thumbnail URL not found in the Figma data.')
        
        # Display other Figma data
        st.write(figma_data)

    except KeyError as e:
        st.warning(f'Error in accessing thumbnail URL: {e}')

else:
    st.warning(f'Failed to retrieve the file. Status code: {response.status_code}')
