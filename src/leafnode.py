from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=[], props=props or {})

    def to_html(self) -> str:
        if self.value == None:
            raise ValueError("Value of a leaf node can't be none")
        if self.tag == None:
            return self.value
        props_html = self.props_to_html()
        if props_html != None:
            if self.value == "":
                return f"<{self.tag} {props_html} />"
            return f"<{self.tag} {props_html}>{self.value}</{self.tag}>"
        if self.value == "":
            return f"<{self.tag}>"
        return f"<{self.tag}>{self.value}</{self.tag}>"

    def props_to_html(self):
        return super().props_to_html()

