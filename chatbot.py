import os
import openai
import streamlit as st

# Load API key from environment variables (more secure for Streamlit Cloud)
openai.api_key = os.getenv("OPENAI_API_KEY")

# Streamlit app title
st.title("AI Customer Support Chatbot")

# User input
user_input = st.text_input("Ask me anything:")

if st.button("Get Answer"):
    if user_input:
        client = openai.OpenAI()  # Initialize OpenAI client

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )

        st.write("🤖 AI:", response.choices[0].message.content)
    else:
        st.write("Please enter a question.")
