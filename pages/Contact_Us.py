import streamlit as st
from send_email import sent_email
import pandas as pd

st.header("Contact me")
df = pd.read_csv("topics.csv")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    subject_line = st.selectbox('What is your topic?',
                                (df['topic']))
    raw_message = st.text_area("Your message")
    message = f"""\
Subject: {subject_line}

From: {user_email}
{raw_message}
"""
    button = st.form_submit_button("Sumit")
    if button:
        sent_email(message)
        st.info("your message was successfully sent")