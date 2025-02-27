import streamlit as st
import pandas as pd
import plotly.express as px
import PyPDF2
from PIL import Image
import numpy as np

def analyze_tabular_data(df):
    st.subheader("Data Overview")
    st.write(df.head())
    st.write("Summary Statistics")
    st.write(df.describe())
    
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    if numeric_cols:
        selected_col = st.selectbox("Select a column to visualize", numeric_cols)
        fig = px.histogram(df, x=selected_col, marginal="box")
        st.plotly_chart(fig, use_container_width=True)

def analyze_text(text):
    st.subheader("Text Analysis")
    word_count = len(text.split())
    st.write(f"Word Count: {word_count}")
    st.text_area("Text Preview", text[:1000])

def analyze_pdf(uploaded_file):
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = "\n".join([page.extract_text() for page in pdf_reader.pages if page.extract_text()])
    analyze_text(text)

def analyze_image(uploaded_file):
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    st.write(f"Image Size: {image.size}")
    if image.mode == 'RGB':
        r, g, b = image.split()
        fig, ax = plt.subplots()
        ax.hist(np.array(r).flatten(), bins=256, color='red', alpha=0.5, label='Red')
        ax.hist(np.array(g).flatten(), bins=256, color='green', alpha=0.5, label='Green')
        ax.hist(np.array(b).flatten(), bins=256, color='blue', alpha=0.5, label='Blue')
        ax.legend()
        st.pyplot(fig)
