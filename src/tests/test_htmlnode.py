import unittest
from src.htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_raise(self):
        node = HTMLNode("p", "ribbit")
        with self.assertRaises(NotImplementedError):
            node.to_html()
    
    def test_empty_props(self):
        node = HTMLNode("p", "valalala", None, None)
        self.assertEqual(node.props_to_html(), "")
    
    def test_props(self):
        node = HTMLNode("p", "valalala", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), " href=\"https://www.google.com\" target=\"_blank\"")
    
    def test_repr(self):
        node = HTMLNode("p", "ola boga", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.__repr__(),
        f"Tag: {'p'}\n"
        f"Value: {'ola boga'}\n"
        f"Children: {None}\n"
        f"Props: {{'href': 'https://www.google.com', 'target': '_blank'}}"
        )

if __name__ == "__main__":
    unittest.main()