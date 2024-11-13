from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if not children:
            raise ValueError("ParentNode must have children.")
        # Initialize the parent class with the given tag, children, and props; no value
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        # Raise ValueError if there's no tag
        if not self.tag:
            raise ValueError("ParentNode must have a tag.")

        # Generate HTML for each child
        children_html = ''.join(child.to_html() for child in self.children)

        # Return the HTML for the ParentNode, wrapping children HTML between tags
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode(tag={self.tag}, children={self.children}, props={self.props})"
