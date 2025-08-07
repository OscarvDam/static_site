class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def to_html(self):
        raise NotImplementedError("This method has not been implemented use children classes")

    def props_to_html(self):
        if self.props=={}:
            return
        prop_text = ""
        for prop in self.props:
            prop_text += f'{prop}="{self.props[prop]}" '
        return prop_text[:-1]

    def __repr__(self):
        return f"tag={self.tag}\nvalue={self.value}\nchildren={self.children}\nprops={self.props_to_html()}"

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
