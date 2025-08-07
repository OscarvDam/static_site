import unittest

from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def setUp(self):
        self.node = LeafNode(
            tag="a",
            value="Click here",
            props={"href": "http://example.com", "target": "_blank"}
        )

    def test_leaf_to_html_a(self):
        html = self.node.to_html()
        self.assertEqual(html, '<a href="http://example.com" target="_blank">Click here</a>')

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_children_raise(self):
        with self.assertRaises(TypeError):
            LeafNode("p", "Hello, world!", children=[])

    def test_value_none(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None).to_html()

    def test_leaf_no_tag(self):
        node = LeafNode(tag=None, value="Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_leaf_img(self):
        node = LeafNode(tag="img", value="", props={"src": "url/of/image.jpg", "alt": "This is an image"})
        self.assertEqual(node.to_html(), '<img src="url/of/image.jpg" alt="This is an image" />')

if __name__ == "__main__":
    unittest.main()
