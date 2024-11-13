import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq_same_content(self):
        # Test two nodes with the same text and text_type
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)

    def test_eq_different_text(self):
        # Test two nodes with different text content
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("Different text", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_eq_different_text_type(self):
        # Test two nodes with the same text but different text_type
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_eq_with_url_none(self):
        # Test nodes where one has a URL of None and the other has a URL specified
        node1 = TextNode("This is a text node", TextType.BOLD, url=None)
        node2 = TextNode("This is a text node", TextType.BOLD, url="http://example.com")
        self.assertNotEqual(node1, node2)

    def test_eq_both_urls_none(self):
        # Test nodes with None URLs and verify they are still equal if other properties match
        node1 = TextNode("This is a text node", TextType.BOLD, url=None)
        node2 = TextNode("This is a text node", TextType.BOLD, url=None)
        self.assertEqual(node1, node2)


if __name__ == "__main__":
    unittest.main()