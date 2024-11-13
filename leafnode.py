from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("LeafNode must have a value.")
        super().__init__(tag=tag, value=value, props=props, children=None)

    def to_html(self):
        if not self.value and self.tag != "img":
            raise ValueError("LeafNode must have a value.")
        
        # Special handling for self-closing tags like <img>
        if self.tag == "img":
            return f"<img{self.props_to_html()}>"
        
        # If there's no tag, return value as raw text
        if not self.tag:
            return self.value
        
        # Otherwise, render as a standard tag with value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
