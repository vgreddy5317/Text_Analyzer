import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from wordcloud import WordCloud

def analyze_tabular_data(df):
    """Analyzes tabular data (CSV, Excel) with multiple visualizations."""
    print("Data Overview:")
    print(df.head())
    print("Summary Statistics:")
    print(df.describe())

    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    categorical_cols = df.select_dtypes(include=['object']).columns.tolist()

    if numeric_cols:
        selected_num_col = numeric_cols[0]

        # Histogram
        plt.figure(figsize=(8, 5))
        sns.histplot(df[selected_num_col], kde=True)
        plt.title("Histogram & Density Plot")
        plt.show()

        # Box Plot
        plt.figure(figsize=(5, 5))
        sns.boxplot(y=df[selected_num_col])
        plt.title("Box Plot for Outliers")
        plt.show()

        # Scatter Plot
        if len(numeric_cols) > 1:
            plt.figure(figsize=(8, 5))
            sns.scatterplot(x=df[numeric_cols[0]], y=df[numeric_cols[1]])
            plt.title("Scatter Plot")
            plt.show()

        # Heatmap for correlation
        plt.figure(figsize=(8, 5))
        sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
        plt.title("Correlation Heatmap")
        plt.show()

    if categorical_cols:
        selected_cat_col = categorical_cols[0]

        # Pie Chart
        plt.figure(figsize=(6, 6))
        df[selected_cat_col].value_counts().plot.pie(autopct="%.1f%%")
        plt.title("Pie Chart Distribution")
        plt.ylabel("")
        plt.show()

        # Bar Chart
        plt.figure(figsize=(8, 5))
        sns.countplot(x=df[selected_cat_col])
        plt.title("Categorical Data Distribution")
        plt.xticks(rotation=45)
        plt.show()

        # Stacked Bar Chart
        if numeric_cols:
            plt.figure(figsize=(8, 5))
            sns.barplot(x=df[selected_cat_col], y=df[numeric_cols[0]], ci=None)
            plt.title("Stacked Bar Chart")
            plt.xticks(rotation=45)
            plt.show()

def analyze_text(text):
    """Performs text analysis with visualizations."""
    word_count = len(text.split())
    print(f"Word Count: {word_count}")
    print("Text Preview:", text[:1000])

    # Generate Word Cloud
    generate_wordcloud(text)

    # Word Frequency Bar Chart
    generate_word_frequency_chart(text)

def generate_wordcloud(text):
    """Generates and displays a word cloud if text is available."""
    if not text.strip():
        print("No words found in the text. Cannot generate a Word Cloud.")
        return

    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
    plt.figure(figsize=(8, 4))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title("Word Cloud")
    plt.show()

def generate_word_frequency_chart(text):
    """Generates a bar chart of the most frequent words in the text."""
    words = text.split()
    if not words:
        return

    word_freq = pd.Series(words).value_counts().head(10)
    plt.figure(figsize=(8, 5))
    sns.barplot(x=word_freq.values, y=word_freq.index, palette="coolwarm")
    plt.title("Most Frequent Words")
    plt.xlabel("Frequency")
    plt.ylabel("Words")
    plt.show()
