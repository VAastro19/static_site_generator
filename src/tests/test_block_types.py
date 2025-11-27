import unittest
from src.markdown_block import block_to_block_type, markdown_to_blocks, BlockType

class TestBlockToBlockTypes(unittest.TestCase):

    def test_paragraph(self):
        md = "This is a paragraph"
        self.assertEqual(block_to_block_type(markdown_to_blocks(md)[0]), BlockType.PARAGRAPH)
    
    def test_heading(self):
        md = "### This is a heading"
        self.assertEqual(block_to_block_type(markdown_to_blocks(md)[0]), BlockType.HEADING)
    
    def test_code(self):
        md = """
```
This is some code
```
"""
        self.assertEqual(block_to_block_type(markdown_to_blocks(md)[0]), BlockType.CODE)
    
    def test_quote(self):
        md = """
>This is
>a
>quote.
"""
        self.assertEqual(block_to_block_type(markdown_to_blocks(md)[0]), BlockType.QUOTE)
    
    def test_unordered_list(self):
        md = """
- This is an
- unordered
- list
"""
        self.assertEqual(block_to_block_type(markdown_to_blocks(md)[0]), BlockType.UNORDERED_LIST)
    
    def test_ordered_list(self):
        md = """
1. This is
2. an ordered
3. list
"""
        self.assertEqual(block_to_block_type(markdown_to_blocks(md)[0]), BlockType.ORDERED_LIST)

if __name__ == "__main__":
    unittest.main()

