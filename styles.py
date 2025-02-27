def get_custom_css():
    """Returns custom CSS for styling the Streamlit app."""
    return """
    <style>
        .main {
            background-color: #f5f7f9;
        }
        .stApp {
            max-width: 1200px;
            margin: 0 auto;
        }
        .css-18e3th9 {
            padding-top: 2rem;
        }
        .css-1d391kg {
            padding: 3.5rem 1rem 1rem;
        }
        .st-bv {
            padding-top: 3rem;
        }
        .css-hxt7ib {
            padding-top: 2rem;
        }
        .stButton > button {
            background-color: #4CAF50;
            color: white;
            border-radius: 5px;
            border: none;
            padding: 10px 24px;
            font-size: 16px;
        }
        .stButton > button:hover {
            background-color: #45a049;
        }
        .upload-container {
            background-color: white;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .results-container {
            background-color: white;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-top: 20px;
        }
        h1, h2, h3 {
            color: #2c3e50;
        }
    </style>
    """
