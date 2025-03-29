import streamlit as st
import random
import time

# Set the title of the application
st.title("Quiz Application with Usernames")

# Initialize session state for username
if "username" not in st.session_state:
    st.session_state.username = ""

# User input for the username
if not st.session_state.username:
    st.session_state.username = st.text_input("Enter your username:")
    if not st.session_state.username:
        st.stop()  # Stop execution until username is entered

st.write(f"Welcome, {st.session_state.username}!")

# List of quiz questions
questions = [
    {
        "question": "What is the capital of Pakistan?",
        "options": ["Karachi", "Lahore", "Islamabad", "Peshawar"],
        "answer": "Islamabad"
    },
    {
        "question": "Which is the national language of Pakistan?",
        "options": ["Punjabi", "Urdu", "Sindhi", "Pashto"],
        "answer": "Urdu"
    },
    {
        "question": "What is the currency of Pakistan?",
        "options": ["Rupee", "Dollar", "Euro", "Dinar"],
        "answer": "Rupee"
    },
    {
        "question": "Who is the founder of Pakistan?",
        "options": ["Allama Iqbal", "Liaquat Ali Khan", "Quaid-e-Azam", "Benazir Bhutto"],
        "answer": "Quaid-e-Azam"
    },
    {
        "question": "Which is the largest province of Pakistan by area?",
        "options": ["Punjab", "Sindh", "Balochistan", "KPK"],
        "answer": "Balochistan"
    }
]

# Initialize session state for the current question
if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)

question = st.session_state.current_question

# Display the question
st.subheader(question["question"])

# Create radio buttons for options
selected_option = st.radio("Choose your answer:", question["options"], key="answer")

# Submit Answer Button
if st.button("Submit Answer"):
    if selected_option == question["answer"]:
        st.success(f"Correct, {st.session_state.username}!")
        st.balloons()
    else:
        st.error(f"Incorrect, {st.session_state.username}! The correct answer is {question['answer']}.")
    
    time.sleep(3)  # Pause before the next question
    st.session_state.current_question = random.choice(questions)
    st.rerun()
