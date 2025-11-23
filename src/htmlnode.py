class HTMLNode():

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
        res = ""
        for key in self.props:
            res += f" {str(key)}=\"{str(self.props[key])}\""
        return res
    
    def __repr__(self):
        res = (
        f"Tag: {self.tag}\n"
        f"Value: {self.value}\n"
        f"Children: {self.children}\n"
        f"Props: {self.props}"
        )
        return res