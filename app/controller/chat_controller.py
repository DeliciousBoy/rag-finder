import time
import streamlit as st

class ChatController:
    def __init__(self):
        if "messages" not in st.session_state:
            st.session_state.messages = []

    def response_generator(self, prompt):
        response = f"{prompt} is a great choice! I love it! "
        for word in response.split():
            yield word + " "
            time.sleep(0.02)

    def display_conversation(self):
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    def handle_user_input(self, prompt):
        with st.chat_message("user"):
            # Display any files uploaded by the user
            if prompt.files:
                for file in prompt.files:
                    if file.type.startswith("image/"):
                        st.image(file, width=300)
                        st.session_state.messages.append({"role": "user", "content": f"![{file.name}]({file.name})"})
                    elif file.type == "text/plain":
                        content = file.read().decode("utf-8")
                        st.text(content)
                        st.session_state.messages.append({"role": "user", "content": f"```\n{content}\n```"})
                    elif file.type == "application/pdf":
                        st.write(f"PDF file: {file.name}")
                        st.session_state.messages.append({"role": "user", "content": f"PDF file: {file.name}"})

            # Display the user's message
            if prompt.text:
                st.markdown(prompt.text)
                st.session_state.messages.append({"role": "user", "content": prompt.text})

        # Generate a response
        with st.chat_message("assistant"):
            response = st.write_stream(self.response_generator(prompt.text))

        st.session_state.messages.append({"role": "assistant", "content": response})
