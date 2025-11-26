from src.textnode import TextNode, TextType

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
    