import unittest
from src.markdown_inline import split_nodes_delimiter
from src.textnode import TextNode, TextType

class TestSplitNode(unittest.TestCase):

    def test_raises(self):
        node = TextNode("Incorrect **syntax", TextType.TEXT)
        with self.assertRaises(Exception):
            new_node = split_nodes_delimiter([node], "**", TextType.BOLD)
    
    def test_bold(self):
        node = TextNode("**Hello there**", TextType.TEXT)
        self.assertEqual(split_nodes_delimiter([node], "**", TextType.BOLD), [TextNode("Hello there", TextType.BOLD)])
    
    def test_bold_italic(self):
        node = TextNode("And then _he_ said **Hello there**", TextType.TEXT)
        self.assertEqual(split_nodes_delimiter([node], "_", TextType.ITALIC), [
            TextNode("And then ", TextType.TEXT),
            TextNode("he", TextType.ITALIC), 
            TextNode(" said **Hello there**", TextType.TEXT)
        ])
    
    def test_two_nodes(self):
        node1 = TextNode("And then _he_ said **Hello there**", TextType.TEXT)
        node2 = TextNode("What a **day**", TextType.TEXT)
        self.assertEqual(split_nodes_delimiter([node1, node2], "**", TextType.BOLD), [
            TextNode("And then _he_ said ", TextType.TEXT),
            TextNode("Hello there", TextType.BOLD),
            TextNode("What a ", TextType.TEXT),
            TextNode("day", TextType.BOLD)
        ])
    
    def test_not_text_type(self):
        node = TextNode("Lacrosse", TextType.CODE)
        self.assertEqual(split_nodes_delimiter([node], "`", TextType.CODE), [TextNode("Lacrosse", TextType.CODE)])
    
if __name__ == "__main__":
    unittest.main()