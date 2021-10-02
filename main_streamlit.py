from logging import NullHandler
from flask import Flask, render_template , request  
import streamlit as st


def praxis():
    st.title("Learning streamlit")
    name = st.text_input("Student_name", "Type here")
    roll = st.text_input("Roll_no", "Type here")
    
    result = ""

    if st.button("Print_result"):
        st.success(f"{name} with {roll} is in praxis")


if __name__ == "__main__":
    praxis()