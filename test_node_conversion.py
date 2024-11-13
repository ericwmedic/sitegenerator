import unittest
from node_conversion import text_node_to_html_node
from textnode import TextNode, TextType
from leafnode import LeafNode

class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_text_type_text(self):
        text_node = TextNode("Simple text", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "Simple text")

    def test_text_type_bold(self):
        text_node = TextNode("Bold text", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<b>Bold text</b>")

    def test_text_type_italic(self):
        text_node = TextNode("Italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<i>Italic text</i>")

    def test_text_type_code(self):
        text_node = TextNode("Code snippet", TextType.CODE)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<code>Code snippet</code>")

    def test_text_type_link(self):
        text_node = TextNode("Google", TextType.LINK, url="https://www.google.com")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<a href="https://www.google.com">Google</a>')

    def test_text_type_image(self):
        text_node = TextNode("Image description", TextType.IMAGE, url="https://example.com/image.jpg")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<img src="https://example.com/image.jpg" alt="Image description">')

    def test_text_type_link_missing_url(self):
        text_node = TextNode("Missing URL", TextType.LINK)
        with self.assertRaises(ValueError):
            text_node_to_html_node(text_node)

    def test_text_type_image_missing_url(self):
        text_node = TextNode("Missing URL for image", TextType.IMAGE)
        with self.assertRaises(ValueError):
            text_node_to_html_node(text_node)

    def test_unhandled_text_type(self):
        text_node = TextNode("Unhandled type", None)  # Invalid TextType
        with self.assertRaises(ValueError):
            text_node_to_html_node(text_node)

if __name__ == "__main__":
    unittest.main()