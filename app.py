from io import StringIO
import streamlit as st

from djwid import getSummary


st.header("Paper Summarizer")
uploaded_file = st.file_uploader("Upload PDF")
if uploaded_file is not None:
    # To read file as bytes:
    s = getSummary(uploaded_file.name)
    st.write("Summary: \n" + s)
