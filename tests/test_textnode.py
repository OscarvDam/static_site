import unittest

from src.textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a link node", TextType.LINK, "https://www.boot.dev/")
        node2 = TextNode("This is a link node", TextType.LINK, "https://www.boot.dev/")
        self.assertEqual(node, node2)

    def test_not_eq_text(self):
        node = TextNode("This is not same text node", TextType.PLAIN)
        node2 = TextNode("This is different text node", TextType.PLAIN)
        self.assertNotEqual(node, node2)

    def test_not_eq_url(self):
        node = TextNode("This is not same url node", TextType.LINK, "https://www.boot.dev/")
        node2 = TextNode("This is not same url node", TextType.LINK, "http://www.boot.dev/")
        self.assertNotEqual(node, node2)


    def test_not_eq_type(self):
        node = TextNode("This is not same type node", TextType.PLAIN)
        node2 = TextNode("This is not same type node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("Test", TextType.ITALIC, "http://example.com")
        self.assertEqual(repr(node), "TextNode('Test', italic, 'http://example.com')")

    def test_invalid_text_type(self):
        with self.assertRaises(ValueError):
            TextNode("Test", "invalid")


if __name__ == "__main__":
    unittest.main()
