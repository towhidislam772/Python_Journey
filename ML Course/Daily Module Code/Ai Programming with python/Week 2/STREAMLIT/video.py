import streamlit as st
#to run this
#streamlit run text_input.py

st.title(" :world_map: Input your video",anchor=False) 
st.divider()

video=st.file_uploader("Enter your video : ",
                 type=['mp4','mkv'])

button = st.button("Click to upload")

if button:
    if video:
        st.video(video)
        st.success("Uploaded successfully")

    else:
        st.error("you must upload")