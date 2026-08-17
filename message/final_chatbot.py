import streamlit as st


st.header("Chatbot")

if "count" not in st.session_state:
    st.session_state.count = 0

st.write(f"Count: {st.session_state.count}")

if st.button("Increment"):
    st.session_state.count += 1
    
if st.button("Decrement"):
    st.session_state.count -= 1
if st.button("Reset"):
    st.session_state.count = 0

st.write(f"Updated Count: {st.session_state.count}")