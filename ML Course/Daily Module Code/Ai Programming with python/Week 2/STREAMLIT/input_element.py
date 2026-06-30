import streamlit as st
#to run this
#streamlit run text_input.py

st.title(" :world_map: Input your info",anchor=False) 
st.divider()

#input 
name=st.text_input("Enter your name :")

print(type(name))

st.write("Your name is ",name)

st.divider()

age=st.number_input("Enter your age : ", value=None,placeholder="Type your age")


print(type(age))

st.write("Your age is ",age)

st.divider()

#putting a button
pressed=st.button("Enter to confirm",type="primary")


if pressed:
    st.write("Your name is ",name)
    st.write("Your age is ",age)

st.divider()

password=st.text_input("Enter your password :",type="password")

print(type(password))

st.write("Your password is ",password)

st.divider()

#select box
selected=st.selectbox("Choose your profession",
             ("Student","Employee","Businessman"),
             index=None,
             accept_new_options = True)

print(type(selected))

st.write("You selected :",selected)