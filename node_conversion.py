from leafnode import LeafNode
from htmlnode import HTMLNode
from textnode import TextNode, TextType

def text_node_to_html_node(text_node):
    if not isinstance(text_node, TextNode):
        raise TypeError("Expected a TextNode instance.")

    if text_node.text_type == TextType.TEXT:
        # Plain text with no tag
        return LeafNode(None, text_node.text)
    
    elif text_node.text_type == TextType.BOLD:
        # Bold text with <b> tag
        return LeafNode("b", text_node.text)
    
    elif text_node.text_type == TextType.ITALIC:
        # Italic text with <i> tag
        return LeafNode("i", text_node.text)
    
    elif text_node.text_type == TextType.CODE:
        # Code text with <code> tag
        return LeafNode("code", text_node.text)
    
    elif text_node.text_type == TextType.LINK:
        # Hyperlink with <a> tag and href attribute
        if not text_node.url:
            raise ValueError("TextNode of type LINK requires a URL.")
        return LeafNode("a", text_node.text, {"href": text_node.url})
    
    elif text_node.text_type == TextType.IMAGE:
        # Image with <img> tag, src and alt attributes
        if not text_node.url:
            raise ValueError("TextNode of type IMAGE requires a URL.")
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})

    else:
        raise ValueError(f"Unhandled TextType: {text_node.text_type}")
