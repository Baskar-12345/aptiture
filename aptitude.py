import streamlit as st
import pandas as pd

# Sample questions and answers
questions = [
    {"question": "What is 5 + 3?", "options": ["6", "7", "8", "9"], "answer": "8"},
    {"question": "What is 12 - 4?", "options": ["6", "8", "10", "12"], "answer": "8"},
    {"question": "What is 7 * 2?", "options": ["12", "14", "16", "18"], "answer": "14"},
    {"question": "What is 16 / 4?", "options": ["2", "3", "4", "5"], "answer": "4"}
]

# Function to start the test
def start_test(email):
    st.session_state.email = email
    st.session_state.responses = []
    st.session_state.current_question = 0

def submit_answers():
    correct_answers = 0
    for i, q in enumerate(questions):
        if st.session_state.responses[i] == q['answer']:
            correct_answers += 1
    return correct_answers

def main():
    st.title("Aptitude Test App")

    if 'email' not in st.session_state:
        st.subheader("Enter your email to start the test")
        email = st.text_input("Email")
        if st.button("Start Test"):
            if email:
                start_test(email)
            else:
                st.warning("Please enter your email.")
    else:
        question = questions[st.session_state.current_question]

        st.subheader(f"Question {st.session_state.current_question + 1}: {question['question']}")
        selected_option = st.radio("", question['options'], key=st.session_state.current_question)
        if st.button("Next"):
            st.session_state.responses.append(selected_option)
            if st.session_state.current_question + 1 < len(questions):
                st.session_state.current_question += 1
            else:
                score = submit_answers()
                st.subheader(f"Test Completed! Your score: {score}/{len(questions)}")
                st.session_state.email = None
                st.session_state.responses = []
                st.session_state.current_question = 0

if __name__ == "__main__":
    main()
