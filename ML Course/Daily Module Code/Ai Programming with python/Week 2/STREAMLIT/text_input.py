import streamlit as st
#to run this
#streamlit run text_input.py

st.title(" :world_map: My web apps",anchor=False) #anchor for link removal

st.header("Content 1",divider=True)

st.subheader("Content 1 SubHeader")

#to get any output
st.write("Hello World")

st.text("Hello World")

#markdown
st.markdown(":red-background[:red[**Hello**] :orange[*world*]] :world_map:") #** for bold * for italic

#variable show
a=10
b=20

st.write(a,b)





