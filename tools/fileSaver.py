# tools/file_saver.py
import os

def file_saver(content: str, filename: str) -> str:
    """
    Saves content to a file inside the 'html/' folder.

    Args:
        content (str): Content to write
        filename (str): Filename, e.g., 'car_comparison.html'

    Returns:
        str: Full path where the file was saved
    """
    html_folder = "html"
    os.makedirs(html_folder, exist_ok=True)
    file_path = os.path.join(html_folder, filename)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    return file_path

