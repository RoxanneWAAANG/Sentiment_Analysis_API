import streamlit as st
import requests

st.title('Sentiment Analysis Demo')

input_text = st.text_area('Enter text for sentiment analysis:')
if st.button('Analyze Sentiment'):
    if input_text:
        with st.spinner('Analyzing...'):
            try:
                response = requests.post('http://0.0.0.0:8000/predict', json={'text': input_text})
                if response.status_code == 200:
                    sentiment = response.json().get('sentiment', 'Unknown')
                    st.success(f'Sentiment: {sentiment}')
                else:
                    st.error('Error: Unable to get sentiment')
            except Exception as e:
                st.error(f'Error: {e}')
    else:
        st.warning('Please enter some text to analyze.')