import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def setUp(self):
        self.node = LeafNode(
            tag="a",
            value="Click here",
            props={"href": "http://example.com", "target": "_blank"}
        )

    def test_leaf_to_html_a(self):
        html = self.node.to_html()
        print(html)
        print(self.node.props_to_html())
        self.assertEqual(html, '<a href="http://example.com" target="_blank">Click here</a>')

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_children_raise(self):
        with self.assertRaises(ValueError):
            LeafNode("p", "Hello, world!", [])

    def test_value_none(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None).to_html()
