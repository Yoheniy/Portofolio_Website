import streamlit as st
import google.generativeai as genai
api_key=st.secrets['GOOGLE_API_KEY']
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')
col1,col2=st.columns(2)

with col1:
    st.subheader("Mr.Y")
    st.title("I am Yohannes Welel")
with col2:
    st.image("images/about.png")

st.title(" ")
persona="""You are Yohannes Welel AI bot. You help people answer questions about your self (i.e Yohannes)
        Answer as if you are responding . dont answer in second or third person.
        If you don't know they answer you simply say "That's a secret"
        Here is more info about Yohannes: 

        Yohannes Welel is a student at Adama Science and Technology University in the field of Software Engineering.
       """
st.title("JOHN's AI Bot")
user_question=st.text_input('Ask anything about me')
if st.button('ASK',use_container_width=True):
    prompt=persona + "Here is the question that the user asked: " + user_question
    response=model.generate_content(prompt)
    st.write(response.text)

