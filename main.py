import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

company_name = "NexTech Solutions"
mission_statement = ("At NexTech Solutions, our mission is to revolutionize the digital "
                     "landscape by delivering cutting-edge technology solutions that empower "
                     "businesses to thrive in the modern world. We are committed to innovation, "
                     "excellence, and customer satisfaction, providing tailor-made IT services "
                     "that enhance operational efficiency, drive growth, and foster a sustainable "
                     "future. Our goal is to be the trusted partner for businesses of all sizes, "
                     "enabling them to achieve their fullest potential through advanced technology "
                     "and unparalleled support.")
st.title(company_name)
st.write(mission_statement)
st.subheader("Our Team")

col1, empty_col1, col2, empty_col2, col3 = st.columns([1, 0.5, 1, 0.5, 1])

df = pd.read_csv("data.csv", sep=",")


with col1:
    for index, row in df[:3].iterrows():
        st.title(f"{row["first name"].title()} {row["last name"].title()}")
        st.write(row["role"])
        st.image("images/" + row["image"])

with col2:
    for index, row in df[4:7].iterrows():
        st.title(f"{row["first name"].title()} {row["last name"].title()}")
        st.write(row["role"])
        st.image("images/" + row["image"])

with col3:
    for index, row in df[8:11].iterrows():
        st.title(f"{row["first name"].title()} {row["last name"].title()}")
        st.write(row["role"])
        st.image("images/" + row["image"])
