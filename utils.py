import os
from datetime import datetime

def get_file_details(uploaded_file):
    """Returns basic file details."""
    return {
        "Filename": uploaded_file.name,
        "File Type": uploaded_file.type,
        "File Size": f"{uploaded_file.size / 1024:.2f} KB",
        "Upload Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

def get_file_extension(filename):
    """Extracts and returns the file extension."""
    return os.path.splitext(filename)[1].lower()

def save_uploaded_file(uploaded_file, save_path):
    """Saves uploaded file to a specified path."""
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return save_path