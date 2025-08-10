import unittest

from src.markupnode import split_node_delimiter
from src.textnode import TextNode, TextType


class TestMarkUpInlineNode(unittest.TestCase):
    def test_plain_to_bold(self):
        node = TextNode("**This text is bold**", TextType.PLAIN)
        new_nodes = split_node_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            repr(new_nodes), repr([TextNode("This text is bold", TextType.BOLD)])
        )

    def test_plain_to_italic(self):
        node = TextNode("_This text is italic_", TextType.PLAIN)
        new_nodes = split_node_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(
            repr(new_nodes), repr([TextNode("This text is italic", TextType.ITALIC)])
        )

    def test_plain_to_code(self):
        node = TextNode("`This text is code`", TextType.PLAIN)
        new_nodes = split_node_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            repr(new_nodes), repr([TextNode("This text is code", TextType.CODE)])
        )

    def test_text_multiple_same_formatting(self):
        node = TextNode("This text is **bold** and **this** is", TextType.PLAIN)
        new_nodes = split_node_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            repr(new_nodes),
            repr(
                [
                    TextNode("This text is ", TextType.PLAIN),
                    TextNode("bold", TextType.BOLD),
                    TextNode(" and ", TextType.PLAIN),
                    TextNode("this", TextType.BOLD),
                    TextNode(" is", TextType.PLAIN),
                ]
            ),
        )

    def test_text_does_not_contain_delimiter(self):
        node = TextNode("Text does not contain delimiter", TextType.PLAIN)
        new_nodes = split_node_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(repr(new_nodes), repr([node]))

    def test_text_not_complete_inside(self):
        node = TextNode("This text is not **bold", TextType.PLAIN)
        new_nodes = split_node_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(repr(new_nodes), repr([node]))

    def test_text_not_complete_inside_and_some_bold(self):
        node = TextNode("This text is **bold** and this is not **bold", TextType.PLAIN)
        new_nodes = split_node_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            repr(new_nodes),
            repr(
                [
                    TextNode("This text is ", TextType.PLAIN),
                    TextNode("bold", TextType.BOLD),
                    TextNode(" and this is not **bold", TextType.PLAIN),
                ]
            ),
        )

    def test_text_multiple_nodes(self):
        node = TextNode(
            "This text is **bold** this is _italic_ this is `code` for all types",
            TextType.PLAIN,
        )
        bold_nodes = split_node_delimiter([node], "**", TextType.BOLD)
        italic_nodes = split_node_delimiter(bold_nodes, "_", TextType.ITALIC)
        new_nodes = split_node_delimiter(italic_nodes, "`", TextType.CODE)
        self.assertEqual(
            repr(new_nodes),
            repr(
                [
                    TextNode("This text is ", TextType.PLAIN),
                    TextNode("bold", TextType.BOLD),
                    TextNode(" this is ", TextType.PLAIN),
                    TextNode("italic", TextType.ITALIC),
                    TextNode(" this is ", TextType.PLAIN),
                    TextNode("code", TextType.CODE),
                    TextNode(" for all types", TextType.PLAIN),
                ]
            ),
        )
