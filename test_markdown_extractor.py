import unittest
from markdown_extractor import extract_markdown_images, extract_markdown_links

class TestMarkdownExtractor(unittest.TestCase):
    def test_extract_images_single(self):
        text = "This is an image ![alt text](https://example.com/image.jpg)"
        expected = [("alt text", "https://example.com/image.jpg")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_images_multiple(self):
        text = "![image1](https://example.com/1.jpg) and ![image2](https://example.com/2.jpg)"
        expected = [("image1", "https://example.com/1.jpg"), ("image2", "https://example.com/2.jpg")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_images_no_images(self):
        text = "This text has no images."
        expected = []
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_links_single(self):
        text = "This is a link [link text](https://example.com)"
        expected = [("link text", "https://example.com")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_extract_links_multiple(self):
        text = "[Google](https://google.com) and [GitHub](https://github.com)"
        expected = [("Google", "https://google.com"), ("GitHub", "https://github.com")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_extract_links_no_links(self):
        text = "This text has no links."
        expected = []
        self.assertEqual(extract_markdown_links(text), expected)

    def test_mixed_text_with_images_and_links(self):
        text = "Here is an ![image](https://img.com) and a [link](https://link.com)"
        expected_images = [("image", "https://img.com")]
        expected_links = [("link", "https://link.com")]
        self.assertEqual(extract_markdown_images(text), expected_images)
        self.assertEqual(extract_markdown_links(text), expected_links)

    def test_images_with_special_characters(self):
        text = "![alt (special) chars](https://example.com/image(1).jpg)"
        expected = [("alt (special) chars", "https://example.com/image(1).jpg")]
        self.assertEqual(extract_markdown_images(text), expected)

if __name__ == "__main__":
    unittest.main()