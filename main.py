import streamlit as st
import pandas as pd
import PyPDF2
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Function to analyze tabular data
def analyze_tabular_data(df):
    """Analyzes tabular data (CSV, Excel) with multiple visualizations."""
    st.subheader("📊 Data Overview")

    col1, col2 = st.columns([1.5, 1])  # Adjusted column width
    with col1:
        st.write(df.head())  # Displaying first few rows  
    with col2:
        st.write("📌 Summary Statistics")
        st.write(df.describe())

    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    categorical_cols = df.select_dtypes(include=['object']).columns.tolist()

    if numeric_cols:
        selected_num_col = st.selectbox("📌 Select a numeric column", numeric_cols)

        # Histogram
        fig, ax = plt.subplots(figsize=(5, 3))
        sns.histplot(df[selected_num_col], kde=True, bins=20, ax=ax, color='blue')
        ax.set_title("Histogram & Density Plot")
        st.pyplot(fig)

        # Box Plot
        fig, ax = plt.subplots(figsize=(5, 3))
        sns.boxplot(y=df[selected_num_col], ax=ax, color='red')
        ax.set_title("Box Plot for Outliers")
        st.pyplot(fig)

        # Scatter Plot
        scatter_x = st.selectbox("📌 Select X-axis for Scatter Plot", numeric_cols)
        scatter_y = st.selectbox("📌 Select Y-axis for Scatter Plot", numeric_cols, index=1)

        fig, ax = plt.subplots(figsize=(5, 3))
        sns.scatterplot(x=df[scatter_x], y=df[scatter_y], ax=ax, color='green')
        ax.set_title("Scatter Plot")
        st.pyplot(fig)

        # Heatmap
        st.subheader("🔥 Correlation Heatmap")
        fig, ax = plt.subplots(figsize=(5, 3))
        sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5, ax=ax)
        st.pyplot(fig)

    if categorical_cols:
        selected_cat_col = st.selectbox("📌 Select a categorical column", categorical_cols)

        # Pie Chart
        pie_data = df[selected_cat_col].value_counts()
        fig, ax = plt.subplots(figsize=(5, 3))
        ax.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%', colors=sns.color_palette("pastel"))
        ax.set_title("Pie Chart Distribution")
        st.pyplot(fig)

        # Bar Chart
        fig, ax = plt.subplots(figsize=(5, 3))
        sns.barplot(x=pie_data.index, y=pie_data.values, ax=ax, palette="coolwarm")
        ax.set_title("Categorical Data Distribution")
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
        st.pyplot(fig)

# Function to analyze text data
def analyze_text(text):
    """Performs text analysis with visualizations."""
    st.subheader("📚 Text Analysis")
    word_count = len(text.split())
    st.write(f"📝 Word Count: {word_count}")
    st.text_area("📜 Text Preview", text[:1000], height=150)

    generate_wordcloud(text)
    generate_word_frequency_chart(text)
    plot_text_length_distribution(text)

# Word cloud visualization
def generate_wordcloud(text):
    """Generates and displays a word cloud if text is available."""
    if not text.strip():
        st.warning("⚠ No words found in the text. Cannot generate a Word Cloud.")
        return

    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    st.subheader("🌥️ Word Cloud")
    st.pyplot(fig)

# Word frequency bar chart
def generate_word_frequency_chart(text):
    """Generates a bar chart of the most frequent words in the text."""
    words = text.split()
    if not words:
        return

    word_freq = pd.Series(words).value_counts().head(10)
    fig, ax = plt.subplots(figsize=(5, 3))
    sns.barplot(x=word_freq.values, y=word_freq.index, palette="coolwarm", ax=ax)
    ax.set_title("👥 Most Frequent Words")
    st.pyplot(fig)

# Text length distribution
def plot_text_length_distribution(text):
    """Plots the distribution of text lengths."""
    text_lengths = [len(word) for word in text.split()]
    if not text_lengths:
        return

    fig, ax = plt.subplots(figsize=(5, 3))
    sns.histplot(text_lengths, bins=20, kde=True, ax=ax)
    ax.set_title("📑 Text Length Distribution")
    st.pyplot(fig)

# File upload and processing
def analyze_file(uploaded_file):
    """Determines file type and processes the uploaded file."""
    if uploaded_file is not None:
        file_extension = uploaded_file.name.split(".")[-1].lower()

        if file_extension in ["csv", "xlsx"]:
            df = pd.read_csv(uploaded_file) if file_extension == "csv" else pd.read_excel(uploaded_file)
            analyze_tabular_data(df)

        elif file_extension == "txt":
            text = uploaded_file.read().decode("utf-8", errors="ignore")  # Ignore decoding errors
            analyze_text(text)

        elif file_extension == "pdf":
            reader = PyPDF2.PdfReader(uploaded_file)
            text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
            analyze_text(text)

        else:
            st.error("❌ Unsupported file format. Please upload a CSV, Excel, TXT, or PDF file.")

# Streamlit App Layout
st.set_page_config(page_title="File Analyzer", page_icon="📂", layout="wide")

st.title("📂 File Analyzer")

uploaded_file = st.file_uploader("📤 Upload a file (CSV, Excel, TXT, PDF)", type=["csv", "xlsx", "txt", "pdf"])

if uploaded_file:
    analyze_file(uploaded_file)
else:
    st.info("Please upload a file to start analysis.")
