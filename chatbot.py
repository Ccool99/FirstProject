import openai
import os
import streamlit as st

# Load API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

# Ensure API key exists
if not api_key:
    st.error("❌ OpenAI API key is missing. Please set it in Streamlit Secrets.")
else:
    client = openai.OpenAI(api_key=api_key)  # Correct OpenAI client initialization

# Streamlit app title
st.title("💬 AI Customer Support Chatbot")

# Store conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
if user_input := st.chat_input("Ask me anything:"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Display user message
    with st.chat_message("user"):
        st.write(user_input)

    # AI response
    with st.spinner("Thinking..."):  # Show loading spinner
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=st.session_state.messages
        )

        ai_response = response.choices[0].message.content

        # Display AI response
        with st.chat_message("assistant"):
            st.write(ai_response)

        # Add AI response to chat history
        st.session_state.messages.append({"role": "assistant", "content": ai_response})

