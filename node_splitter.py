from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            # If node is not plain text, add it as is
            new_nodes.append(node)
            continue

        # Split the text based on the delimiter
        parts = node.text.split(delimiter)
        
        if len(parts) % 2 == 0:
            raise ValueError(f"Unmatched delimiter '{delimiter}' in text: {node.text}")

        # Iterate over parts, alternating between TEXT and specified text_type
        for i, part in enumerate(parts):
            if part:  # Only add non-empty parts
                new_type = text_type if i % 2 == 1 else TextType.TEXT
                new_nodes.append(TextNode(part, new_type))

    return new_nodes