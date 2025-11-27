import unittest
from src.markdown_inline import split_nodes_image, split_nodes_link
from src.textnode import TextNode, TextType

class TestSplitImagesLinks(unittest.TestCase):

    def split_nodes_image(self):
        matches = split_nodes_image([
            TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT)
        ])
        self.assertListEqual([
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")
        ], matches)
    
    def split_nodes_link(self):
        matches = split_nodes_link([
            TextNode("This is text with a [link](https://www.google.com)", TextType.TEXT)
        ])
        self.assertListEqual(matches, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://www.google.com")
        ])
    
    def test_multiple_links(self):
        matches = split_nodes_link([
            TextNode("In here [number one](https://www.smth.com) and in here [number two](https://www.smthdft.com) is smth.", TextType.TEXT)
        ])
        self.assertListEqual(matches, [
            TextNode("In here ", TextType.TEXT),
            TextNode("number one", TextType.LINK, "https://www.smth.com"),
            TextNode(" and in here ", TextType.TEXT),
            TextNode("number two", TextType.LINK, "https://www.smthdft.com"),
            TextNode(" is smth.", TextType.TEXT)
        ])
    
    def test_multiple_nodes(self):
        node1 = (
            TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT)
        )
        node2 = (
            TextNode("This is text with another ![image](https://i.imgur.com/azjjcJKZ.png)", TextType.TEXT)
        )
        matches = split_nodes_image([node1, node2])
        self.assertListEqual(matches, 
            [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode("This is text with another ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/azjjcJKZ.png")
            ]
        )
    
if __name__ == "__main__":
    unittest.main()

