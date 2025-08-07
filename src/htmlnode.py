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

