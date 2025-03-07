import streamlit as st


st.write(":rainbow[Hello, world!]")

with st.sidebar:
    st.title("RAG Finder")
    st.write("This is a sidebar")
    st.write("You can use this to add widgets")

with st.container(height=500, border=True):
    st.code("print('Hello, world!')", language="python", line_numbers=True)
    test = st.checkbox("Check me out")
    if test:
        st.write("Great!")

    test = st.text_input("Enter some text")
    if test:
        st.write(test)
