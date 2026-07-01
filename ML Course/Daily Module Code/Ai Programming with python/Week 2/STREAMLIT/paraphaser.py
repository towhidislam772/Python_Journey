from google import genai
import os
from dotenv import load_dotenv

import streamlit as st

load_dotenv()

st.title("Paraphase Your Thought",anchor=False)

api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

inp=st.text_input("Enter your sentence : ", value=None,placeholder="Type your sentence")

selected=st.selectbox("Choose your tone : ",
             ("Professional","Fancy","Academic","Informal","Creative"),
             index=None,
             accept_new_options = False)

st.write("You selected :",selected)

pressed=st.button("Press to paraphase",type="primary")

if pressed:
    if inp:
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=f"Improve this sentence - {inp} - in {selected} tone.The ans should just give the exact part that paraphased nothing elese not a single word"
        )
        if response.text:
            st.markdown(response.text)
        else:
            st.write("No response received:", response)
    else:
        st.write("Please enter something first")