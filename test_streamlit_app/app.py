import streamlit as st
import streamlit.components.v1 as com 

com.iframe("https://lottie.host/embed/b3141772-dead-41f9-935e-b5e4b2cfe704/PFverSAzrS.json")

st.title('My first streamlit app')
st.write('Welcome to my Streamlit app!')

user_input = st.text_input('Enter a custome message:', 'Hello, Streamlit!')
st.write('Customized Message:', user_input)
