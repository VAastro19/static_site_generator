from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "order_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    res = []
    for block in blocks:
        block = block.strip()
        if block == "":
            continue
        res.append(block)
    return res

def block_to_block_type(block):
    # Headings
    count = 0
    while count <= 6:
        if block[count] == "#":
            count += 1
        else:
            break
    if count > 0 and block[:(count + 1)] == "#" * count + " " and len(block) > count + 1:
        return BlockType.HEADING

    # Code blocks
    if block[:3] == block[(len(block) - 3):] == "```":
        return BlockType.CODE

    # Quote block
    lines = block.split("\n")
    is_quote = True
    for line in lines:
        if not line.startswith(">"): is_quote = False
    if is_quote is True:
        return BlockType.QUOTE

    # Unordered list
    is_list = True
    for line in lines:
        if not line.startswith("- "): is_list = False
    if is_list is True:
        return BlockType.UNORDERED_LIST
    
    # Ordered list
    is_list = True
    index = 1
    for line in lines:
        if not line.startswith(f"{index}. "): is_list = False
        index += 1
    if is_list is True:
        return BlockType.ORDERED_LIST
    
    # Paragraphs
    return BlockType.PARAGRAPH
