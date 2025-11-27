import unittest
from src.markdown_inline import extract_markdown_images, extract_markdown_links
from src.textnode import TextNode, TextType

class TestExtractMarkdown(unittest.TestCase):

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://www.google.com)"
        )
        self.assertListEqual(matches, [("link", "https://www.google.com")])
    
    def test_multiple_links(self):
        matches = extract_markdown_links(
            "In here [number one](https://www.smth.com) and in here [number two](https://www.smthdft.com) is smth."
        )
        self.assertListEqual(matches, [("number one", "https://www.smth.com"), ("number two", "https://www.smthdft.com")])
    
if __name__ == "__main__":
    unittest.main()

