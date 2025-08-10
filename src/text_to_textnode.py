from src.textnode import TextNode, TextType
from src.markupnode import split_node_delimiter, split_nodes_image, split_nodes_link


def text_to_textnodes(text):
    node = [TextNode(text, TextType.PLAIN)]
    return split_italic(
        split_bold(
            split_nodes_link(
                split_nodes_image(
                    split_code(node)
                )
            )
        )
    )


def split_bold(nodes):
    return split_node_delimiter(nodes, "**", TextType.BOLD)


def split_italic(nodes):
    return split_node_delimiter(nodes, "_", TextType.ITALIC)


def split_code(nodes):
    return split_node_delimiter(nodes, "`", TextType.CODE)
