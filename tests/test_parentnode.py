import unittest

from src.htmlnode import LeafNode, ParentNode

class TestParentNode(unittest.TestCase):
    def setUp(self):
        self.node = ParentNode(
            tag="p",
            children=[
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
            props={"href": "http://example.com", "target": "_blank"}
        )

    def test_init(self):
        self.assertEqual(self.node.tag, "p")
        self.assertEqual(self.node.value, None)
        self.assertEqual(repr(self.node.children), repr([
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ]))
        self.assertEqual(self.node.props, {"href": "http://example.com", "target": "_blank"})

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_multiple_children(self):
        self.assertEqual(self.node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_no_tag(self):
        parent_node = ParentNode(None, self.node.children)
        with self.assertRaises(ValueError) as cm:
            parent_node.to_html()
        self.assertIn("non-empty string", str(cm.exception))

    def test_to_html_empty_children(self):
        parent_node = ParentNode(tag="a", children=[])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_children_not_list_raises_value_error(self):
        child = LeafNode(tag="span", value="Test")
        parent = ParentNode(tag="div", children=child)  # Not a list!
        with self.assertRaises(ValueError) as cm:
            parent.to_html()
        self.assertIn("non-empty list", str(cm.exception))

    def test_empty_children_list_raises_value_error(self):
        parent = ParentNode(tag="div", children=[])
        with self.assertRaises(ValueError) as cm:
            parent.to_html()
        self.assertIn("non-empty list", str(cm.exception))

    def test_invalid_child_type_raises_type_error(self):
        parent = ParentNode(tag="ul", children=["not a node"])
        with self.assertRaises(TypeError):
            parent.to_html()

    def test_mixed_valid_and_invalid_children(self):
        valid_child = LeafNode(tag="li", value="Item")
        invalid_child = 123
        parent = ParentNode(tag="ul", children=[valid_child, invalid_child])
        with self.assertRaises(TypeError):
            parent.to_html()

if __name__ == "__main__":
    unittest.main()
