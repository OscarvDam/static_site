from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)
        
    def to_html(self):
        if not isinstance(self.tag, str) or not self.tag.strip():
            raise ValueError("Tag must be a non-empty string")

        if not isinstance(self.children, list) or not self.children:
            raise ValueError("Children must be a non-empty list")

        child_html = ""
        for child in self.children:
            if not hasattr(child, "to_html") or not callable(child.to_html):
                raise TypeError(f"Child {child!r} does not implement a to_html() method")
            child_html += child.to_html()

        return f"<{self.tag}>{child_html}</{self.tag}>"