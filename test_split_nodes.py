import unittest
from textnode import TextNode, TextType
from split_nodes import split_nodes_image, split_nodes_link

class TestSplitNodes(unittest.TestCase):

    def test_split_nodes_image_single(self):
        node = TextNode("This is text with an ![alt](https://example.com/image.jpg) image", TextType.TEXT)
        expected = [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("alt", TextType.IMAGE, "https://example.com/image.jpg"),
            TextNode(" image", TextType.TEXT)
        ]
        self.assertEqual(split_nodes_image([node]), expected)

    def test_split_nodes_link_single(self):
        node = TextNode("This is a link [example](https://example.com)", TextType.TEXT)
        expected = [
            TextNode("This is a link ", TextType.TEXT),
            TextNode("example", TextType.LINK, "https://example.com")
        ]
        self.assertEqual(split_nodes_link([node]), expected)

    def test_split_nodes_image_multiple(self):
        node = TextNode("Image one ![img1](https://example.com/1.jpg) and two ![img2](https://example.com/2.jpg)", TextType.TEXT)
        expected = [
            TextNode("Image one ", TextType.TEXT),
            TextNode("img1", TextType.IMAGE, "https://example.com/1.jpg"),
            TextNode(" and two ", TextType.TEXT),
            TextNode("img2", TextType.IMAGE, "https://example.com/2.jpg")
        ]
        self.assertEqual(split_nodes_image([node]), expected)

    def test_split_nodes_link_multiple(self):
        node = TextNode("Visit [BootDev](https://boot.dev) and [YouTube](https://youtube.com)", TextType.TEXT)
        expected = [
            TextNode("Visit ", TextType.TEXT),
            TextNode("BootDev", TextType.LINK, "https://boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("YouTube", TextType.LINK, "https://youtube.com")
        ]
        self.assertEqual(split_nodes_link([node]), expected)

if __name__ == "__main__":
    unittest.main()