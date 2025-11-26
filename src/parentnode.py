from src.htmlnode import HTMLNode

class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Missing tag!")
        if self.children is None:
            raise ValueError("Missing children!")
        res = f"<{self.tag}>"
        for child in self.children:
            res = res + child.to_html()
        res = res + f"</{self.tag}>"
        return res
        
            
        