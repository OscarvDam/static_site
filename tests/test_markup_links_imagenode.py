import unittest

from src.markupnode import extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link
from src.textnode import TextNode, TextType

class TestMarkUpNode(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with an [link](https://www.boot.dev/)"
        )
        self.assertListEqual([("link", "https://www.boot.dev/")], matches)

    def test_extract_markdown_links_not_image(self):
        matches = extract_markdown_links(
            "This is a [link](https://www.boot.dev/) and this is an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("link", "https://www.boot.dev/")], matches)

    def test_extract_markdown_image_not_links(self):
        matches = extract_markdown_images(
            "This is a [link](https://www.boot.dev/) and this is an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAIN),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )

    def test_split_the_same_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another same ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another same ", TextType.PLAIN),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_without_an_image(self):
        node = TextNode(
            "This is text without an image",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text without an image", TextType.PLAIN),
            ],
            new_nodes,
        )

    def test_split_only_image(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAIN),
                TextNode("second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )

    def test_split_the_same_link(self):
        node = TextNode(
            text="This is text with an [link](https://i.imgur.com/zjjcJKZ.png) and another same [link](https://i.imgur.com/zjjcJKZ.png)",
            text_type=TextType.PLAIN,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode(text="This is text with an ", text_type=TextType.PLAIN),
                TextNode(text="link", text_type=TextType.LINK, url="https://i.imgur.com/zjjcJKZ.png"),
                TextNode(text=" and another same ", text_type=TextType.PLAIN),
                TextNode(text="link", text_type=TextType.LINK, url="https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_without_an_link(self):
        node = TextNode(
            text="This is text without an image",
            text_type=TextType.PLAIN,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode(text="This is text without an image", text_type=TextType.PLAIN),
            ],
            new_nodes,
        )

    def test_split_link_and_image(self):
        node = TextNode(text="This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://www.boot.dev/)", text_type=TextType.PLAIN)
        split_nodes = split_nodes_link([node])
        new_nodes = split_nodes_image(split_nodes)
        self.assertListEqual(
            [
                TextNode(text="This is text with an ", text_type=TextType.PLAIN),
                TextNode(text="image", text_type=TextType.IMAGE, url="https://i.imgur.com/zjjcJKZ.png"),
                TextNode(text=" and a ", text_type=TextType.PLAIN),
                TextNode(text="link", text_type=TextType.LINK, url="https://www.boot.dev/"),
            ],
            new_nodes,
        )

    def test_split_image_and_link(self):
        node = TextNode(text="This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://www.boot.dev/)", text_type=TextType.PLAIN)
        split_nodes = split_nodes_image([node])
        new_nodes = split_nodes_link(split_nodes)
        self.assertListEqual(
            [
                TextNode(text="This is text with an ", text_type=TextType.PLAIN),
                TextNode(text="image", text_type=TextType.IMAGE, url="https://i.imgur.com/zjjcJKZ.png"),
                TextNode(text=" and a ", text_type=TextType.PLAIN),
                TextNode(text="link", text_type=TextType.LINK, url="https://www.boot.dev/"),
            ],
            new_nodes,
        )

    def test_split_only_link(self):
        node = TextNode(
            text="[link](https://www.boot.dev/)",
            text_type=TextType.PLAIN,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode(text="link", text_type=TextType.LINK, url="https://www.boot.dev/")
            ],
            new_nodes,
        )


