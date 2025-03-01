import os
import openai
import streamlit as st

# Load API key securely from environment variables
api_key = os.getenv("OPENAI_API_KEY")

# Ensure API key exists before proceeding
if not api_key:
    st.error("❌ OpenAI API key is missing. Please set it in Streamlit Secrets.")
else:
    openai.api_key = api_key  # Correctly set API key

# Streamlit app title
st.title("💬 AI Customer Support Chatbot")

# Store conversation history in Streamlit session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
if user_input := st.chat_input("Ask me anything:"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Display user message in chat interface
    with st.chat_message("user"):
        st.write(user_input)

    # AI response
    with st.spinner("Thinking..."):  # Show loading spinner
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=st.session_state.messages
        )

        ai_response = response["choices"][0]["message"]["content"]

        # Display AI response in chat
        with st.chat_message("assistant"):
            st.write(ai_response)

        # Add AI response to chat history
        st.session_state.messages.append({"role": "assistant", "content": ai_response})
