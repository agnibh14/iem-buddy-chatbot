import streamlit as st
from chatbot import get_answer

st.set_page_config(page_title="IEM BUDDY", layout="centered")

# Title and header
st.markdown("""
    <h1 style='text-align: center; color: #2E8B57;'>🤖 IEM BUDDY</h1>
    <h4 style='text-align: center;'>INSTITUTE OF ENGINEERING AND MANAGEMENT, SALT LAKE</h4>
    <p style='text-align: center;'>💬 Ask your question about IEM Kolkata below</p>
    <hr>
""", unsafe_allow_html=True)

# Initialize chat history only once
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input field (DO NOT use key="user_input" to avoid modify-after-instantiated error)
query = st.text_input("Type your question:")

# On submit
if st.button("Ask"):
    if query.strip():
        response = get_answer(query.strip())
        st.session_state.chat_history.append((query.strip(), response))

# Display chat history
for user_input, bot_response in st.session_state.chat_history:
    st.markdown(f"<div style='color: black;'><b>🧑 You:</b> {user_input}</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='color: darkblue; background-color: #f0f8ff; padding: 8px; border-radius: 6px;'><b>🤖 IEM BUDDY:</b> {bot_response}</div>", unsafe_allow_html=True)
    st.markdown("---")
