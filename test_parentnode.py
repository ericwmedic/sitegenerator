import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        # ParentNode with multiple children, including LeafNodes with tags and raw text
        node = ParentNode("p", [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "Italic text"),
            LeafNode(None, "More normal text"),
        ])
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>Italic text</i>More normal text</p>")

    def test_to_html_nested_parentnode(self):
        # Nested ParentNode structures
        node = ParentNode("div", [
            LeafNode("h1", "Header"),
            ParentNode("p", [
                LeafNode(None, "Paragraph with "),
                LeafNode("b", "bold text")
            ]),
            LeafNode("p", "Another paragraph")
        ])
        self.assertEqual(node.to_html(), "<div><h1>Header</h1><p>Paragraph with <b>bold text</b></p><p>Another paragraph</p></div>")

    def test_to_html_no_tag_raises_error(self):
        # ParentNode with no tag should raise ValueError
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("b", "Bold text")]).to_html()

    def test_to_html_no_children_raises_error(self):
        # ParentNode with no children should raise ValueError
        with self.assertRaises(ValueError):
            ParentNode("div", []).to_html()

    def test_to_html_with_props(self):
        # ParentNode with props
        node = ParentNode("div", [
            LeafNode("span", "Text inside span")
        ], props={"class": "container"})
        self.assertEqual(node.to_html(), '<div class="container"><span>Text inside span</span></div>')


if __name__ == "__main__":
    unittest.main()
