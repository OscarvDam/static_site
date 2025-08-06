from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag can't be empty, it needs a value")
        if self.children is []:
            raise ValueError("Children can't be empty, parent needs children")
        
        childHTML = ""
        for child in self.children:
            childHTML += child.to_html()
        return f"<{self.tag}>{childHTML}</{self.tag}>"
        
