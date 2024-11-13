import re

def extract_markdown_images(text):
    # Pattern to capture image markdown with balanced parentheses in URLs
    image_pattern = r"!\[([^\[\]]*)\]\((https?://[^\s\(\)]+(?:\([^\)]+\))*[^\s]*)\)"
    matches = re.findall(image_pattern, text)
    return matches  # Returns list of tuples (alt text, URL)

def extract_markdown_links(text):
    # Pattern for capturing links with balanced parentheses in URLs
    link_pattern = r"(?<!!)\[([^\[\]]*)\]\((https?://[^\s\(\)]+(?:\([^\)]+\))*[^\s]*)\)"
    matches = re.findall(link_pattern, text)
    return matches  # Returns list of tuples (anchor text, URL)