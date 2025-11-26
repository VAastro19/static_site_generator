import unittest
from src.parentnode import ParentNode
from src.leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
        
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
    )

    def test_to_html_without_children(self):
        parent_node = ParentNode("p", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()
    
    def test_parent_without_tag(self):
        parent_node = ParentNode(None, LeafNode("b", "text"))
        with self.assertRaises(ValueError):
            parent_node.to_html()
    
    def test_with_multiple_children(self):
        grandchild1 = LeafNode("b", "grandchild1")
        grandchild2 = LeafNode("div", "grandchild2")
        child1 = LeafNode("span", "child1")
        child2 = LeafNode("div", "child2")
        child3 = ParentNode("p", [grandchild1, grandchild2])
        parent_node = ParentNode("p", [child1, child2, child3])
        self.assertEqual(
            parent_node.to_html(),
            f"<p><span>child1</span><div>child2</div><p><b>grandchild1</b><div>grandchild2</div></p></p>",
        )

if __name__ == "__main__":
    unittest.main()