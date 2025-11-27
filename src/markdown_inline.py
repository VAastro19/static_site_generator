from src.textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            parts = node.text.split(sep=delimiter)
            if len(parts) % 2 == 0:
                raise Exception("Invalid markdown syntax")
            checked_parts = []
            for i, part in enumerate(parts):
                if part == "":
                    continue
                if i % 2 == 0:
                    checked_parts.append(TextNode(part, TextType.TEXT))
                else:
                    checked_parts.append(TextNode(part, text_type))
            new_nodes.extend(checked_parts)
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            curr_text = node.text
            image_matches = extract_markdown_images(curr_text)
            for match in image_matches:
                before, after = curr_text.split(f"![{match[0]}]({match[1]})", 1)
                curr_text = after
                if before != "":
                    new_nodes.append(TextNode(before, TextType.TEXT))
                new_nodes.append(TextNode(match[0], TextType.IMAGE, match[1]))
            if curr_text != "":
                new_nodes.append(TextNode(curr_text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            curr_text = node.text
            link_matches = extract_markdown_links(curr_text)
            for match in link_matches:
                before, after = curr_text.split(f"[{match[0]}]({match[1]})", 1)
                curr_text = after
                if before != "":
                    new_nodes.append(TextNode(before, TextType.TEXT))
                new_nodes.append(TextNode(match[0], TextType.LINK, match[1]))
            if curr_text != "":
                new_nodes.append(TextNode(curr_text, TextType.TEXT))
    return new_nodes

def text_to_textnode(text):
    textnode = TextNode(text, TextType.TEXT)
    curr = split_nodes_delimiter([textnode], "**", TextType.BOLD)
    curr = split_nodes_delimiter(curr, "_", TextType.ITALIC)
    curr = split_nodes_delimiter(curr, "`", TextType.CODE)
    curr = split_nodes_image(curr)
    curr = split_nodes_link(curr)
    return curr

