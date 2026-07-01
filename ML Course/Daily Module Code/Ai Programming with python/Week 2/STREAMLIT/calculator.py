import streamlit as st

st.title(" My First Streamlit Project ",anchor=False) 
st.divider()
st.subheader("Calculator")
st.divider()

#input 
n1=st.number_input("Enter the first number: ",value=None,placeholder="Enter the 1st number")

n2=st.number_input("Enter the second number: ",value=None,placeholder="Enter the 2nd number")

st.divider()

#select box
selected=st.selectbox("Choose your operation",
             ("+","-","*","/"),
             index=None,
             accept_new_options = False)

st.write("You selected :",selected)

st.divider()

#putting a button
pressed=st.button("Press to calculate",type="primary")

result=0

if n1 is not None:
    if n2 is not None:
        if pressed:
            if selected=="+":
                result=n1+n2
            elif selected=="-":
                result=n1-n2
            elif selected=="*":
                result=n1*n2
            elif selected=="/":
                if n2 !=0:
                    result=n1/n2
                else:
                    st.write("Cant Divide by 0")
            else:
                st.write("Select an option first")

    else:
        st.write("Enter 2nd number")
else:
    st.write("enter 1st number")

st.divider()

if pressed and n1 is not None and n2 is not None and selected:
    st.write(f"Your calculation of **({selected})** is : {result}")
