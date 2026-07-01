import streamlit as st
#to run this
#streamlit run text_input.py

st.title(" :world_map: Input your Audio & Video",anchor=False) 
st.divider()

#frm directory
st.audio("audio/test.mp3",loop=True)

st.divider()

audio=st.file_uploader("Enter your audio : ",
                 type=['mp3','ogg','flac'])

if audio:
    st.audio(audio)

st.divider()