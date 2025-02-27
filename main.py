import streamlit as st
import pandas as pd
import os
from datetime import datetime
from analyzer import analyze_file
from styles import custom_css

# Page configuration
st.set_page_config(
    page_title="File Analyzer",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("File Analyzer")
    st.markdown("---")
    st.write("Analyze various file types with ease.")
    st.markdown("## Features")
    st.write("✅ CSV/Excel data analysis")
    st.write("✅ Text file analysis")
    st.write("✅ Image metadata")
    st.write("✅ Basic PDF text extraction")
    st.markdown("---")
    st.info("Upload a file to get started!")
    st.markdown("### About")
    st.write("Version 1.0.0")
    st.write("Built with Streamlit & Python")

# Main content
st.title("📊 File Analyzer")
st.write("Upload a file and get instant analysis based on its type and content.")

# File upload section
st.subheader("Upload File")
uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx", "txt", "pdf", "jpg", "jpeg", "png"])

if uploaded_file is not None:
    file_extension = os.path.splitext(uploaded_file.name)[1].lower()
    analyze_file(uploaded_file, file_extension)
else:
    st.info("👆 Upload a file to get started with the analysis.")