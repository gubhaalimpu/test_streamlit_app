import streamlit as st

st.title('My first streamlit app')
st.write('Welcome to my Streamlit app!')

user_input = st.text_input('Enter a custome message:', 'Hello, Streamlit!')
st.write('Customized Message:', user_input)
