import unittest

from src.htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def setUp(self):
        self.node = HTMLNode(
            tag="a",
            value="Click here",
            children=[],
            props={"href": "http://example.com", "target": "_blank"}
        )

    def test_init(self):
        self.assertEqual(self.node.tag, "a")
        self.assertEqual(self.node.value, "Click here")
        self.assertEqual(self.node.children, [])
        self.assertEqual(self.node.props, {"href": "http://example.com", "target": "_blank"})

    def test_props_to_html(self):
        expected = 'href="http://example.com" target="_blank"'
        self.assertEqual(self.node.props_to_html(), expected)

    def test_props_to_html_none(self):
        node = HTMLNode()
        self.assertIsNone(node.props_to_html())

    def test_repr(self):
        repr_output = repr(self.node)
        self.assertIn("tag=a", repr_output)
        self.assertIn("value=Click here", repr_output)
        self.assertIn("children=[]", repr_output)
        self.assertIn('href="http://example.com"', repr_output)

    def test_repr_none_props(self):
        node = HTMLNode(tag="div", value="Test")
        repr_output = repr(node)
        self.assertIn("tag=div", repr_output)
        self.assertIn("value=Test", repr_output)
        self.assertIn("props=", repr_output)

    def test_to_html_raises(self):
        with self.assertRaises(NotImplementedError):
            self.node.to_html()


if __name__ == "__main__":
    unittest.main()
