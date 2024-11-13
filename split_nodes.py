from textnode import TextNode, TextType
from markdown_extractor import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        images = extract_markdown_images(node.text)
        text = node.text

        if not images:
            new_nodes.append(node)
            continue

        for alt_text, url in images:
            sections = text.split(f"![{alt_text}]({url})", 1)
            # Append text before the image, if it exists
            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            # Append the image as a new node
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
            # Move to the remaining text after the image
            text = sections[1]

        # Append any remaining text after the last image
        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        links = extract_markdown_links(node.text)
        text = node.text

        if not links:
            new_nodes.append(node)
            continue

        for anchor_text, url in links:
            sections = text.split(f"[{anchor_text}]({url})", 1)
            # Append text before the link, if it exists
            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            # Append the link as a new node
            new_nodes.append(TextNode(anchor_text, TextType.LINK, url))
            # Move to the remaining text after the link
            text = sections[1]

        # Append any remaining text after the last link
        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes