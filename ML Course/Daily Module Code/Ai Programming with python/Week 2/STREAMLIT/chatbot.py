from google import genai
import os
from dotenv import load_dotenv

import streamlit as st

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

inp=st.text_input("Enter your query : ", value=None,placeholder="Type your query")

pressed=st.button("Press to generate",type="primary")

if pressed:
    if inp:
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=inp
        )
        if response.text:
            st.markdown(response.text)
        else:
            st.write("No response received:", response)
    else:
        st.write("Please enter something first")