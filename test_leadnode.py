import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html_with_tag_and_props(self):
        # LeafNode with tag and props
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_to_html_with_tag_no_props(self):
        # LeafNode with tag and no props
        node = LeafNode("p", "This is a paragraph.")
        self.assertEqual(node.to_html(), '<p>This is a paragraph.</p>')

    def test_to_html_no_tag(self):
        # LeafNode with no tag, should return value as raw text
        node = LeafNode(None, "This is raw text.")
        self.assertEqual(node.to_html(), "This is raw text.")

    def test_to_html_no_value(self):
        # LeafNode with None value, should raise ValueError
        with self.assertRaises(ValueError):
            LeafNode("p", None)

    def test_to_html_missing_value_raises_error(self):
        # Test to_html raises ValueError if value is missing
        node = LeafNode("p", "Text here")
        node.value = None
        with self.assertRaises(ValueError):
            node.to_html()

if __name__ == "__main__":
    unittest.main()
