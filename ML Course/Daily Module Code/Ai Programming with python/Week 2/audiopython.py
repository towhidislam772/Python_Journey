from gtts import gTTS
import streamlit as st
import io

text = "Hello, Welcome meem"

speech=gTTS(text,lang='en',slow=False)

speech.save("Welcome.mp3")

#without locally saving
audio_buffer=io.BytesIO()
speech.write_to_fp(audio_buffer)


st.audio("Welcome.mp3")

st.audio(audio_buffer)