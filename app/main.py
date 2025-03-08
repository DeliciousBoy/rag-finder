import streamlit as st
from app.controller.chat_controller import ChatController

st.header(":rainbow[RAG Finder]", help="This is a chatbot that helps you find the perfect color for your project.")

# Initialize the chat controller
chat_controller = ChatController()

# Display the conversation
chat_controller.display_conversation()

# Get user input
if prompt := st.chat_input(placeholder="Type a message...", accept_file=True):
    chat_controller.handle_user_input(prompt)


