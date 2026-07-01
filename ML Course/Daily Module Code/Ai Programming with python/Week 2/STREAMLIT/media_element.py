import streamlit as st
#to run this
#streamlit run text_input.py

st.title(" :world_map: Input your Media",anchor=False) 
st.divider()

#from file
st.image("images/photo.png")

#url
st.image("https://miro.medium.com/v2/resize:fit:1100/format:webp/1*eUFeLY6n-hB7N_h1P9irNg.jpeg")

st.divider()

image=st.file_uploader("Enter your image (at max 2) : ",
                 type=['jpg','jpeg','png'],
                 accept_multiple_files=True)

print(type(image))

if image:
    if(len(image)>2):
        st.warning("you uploaded 3 or more")
    col = st.columns(len(image))
    for i,img in enumerate(image):
        with col[i]:
            st.image(img)

    
st.divider()

