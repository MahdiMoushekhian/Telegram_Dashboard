import streamlit as st
import os
import json

# Set the title and header image
st.title(':rocket: Telegram Dashboard')
st.image('./data/Telegram-Banner.jpg', use_column_width=True)

# Create an expander for file upload
with st.expander("Upload JSON File"):
    uploaded_file = st.file_uploader("Choose a JSON file", type="json")

    if uploaded_file is not None:
        # Save the uploaded file to the data directory
        data_dir = 'data'
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        
        file_path = os.path.join(data_dir, uploaded_file.name)
        with open(file_path, 'wb') as f:
            f.write(uploaded_file.getbuffer())
        
        st.success(f"File saved to {file_path}")

        # Optionally, display the content of the JSON file
        with open(file_path, 'r') as f:
            data = json.load(f)
            st.json(data)