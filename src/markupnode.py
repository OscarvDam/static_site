from src.textnode import TextNode, TextType
import re


def split_node_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        # new_nodes_text = [u for x in node.text.split(delimiter) for u in (x, delimiter)]  This splits with delimiter intact, maybe for later
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
            continue
        new_nodes_text = node.text.split(delimiter)
        for i in range(len(new_nodes_text)):
            if new_nodes_text[i] == "":
                continue
            if len(new_nodes_text) % 2 == 0 and len(new_nodes_text[i:]) == 2:
                new_nodes.append(
                    TextNode(
                        new_nodes_text[i] + delimiter + new_nodes_text[i + 1],
                        TextType.PLAIN,
                    )
                )
                break
            if i % 2 == 0:
                new_nodes.append(TextNode(new_nodes_text[i], TextType.PLAIN))
            if i % 2 == 1:
                new_nodes.append(TextNode(new_nodes_text[i], text_type))
    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text == "":
            continue
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
            continue
        altText_urls = extract_markdown_images(node.text)
        if altText_urls == []:
            new_nodes.append(node)
            continue
        altUrlString = "![" + altText_urls[0][0] + "](" + altText_urls[0][1] + ")"
        new_lists_text = node.text.split(altUrlString)
        for i in range(len(new_lists_text) - 1):
            if new_lists_text[i] != "":
                new_nodes.append(TextNode(new_lists_text[i], TextType.PLAIN))
            new_nodes.append(
                TextNode(altText_urls[0][0], TextType.IMAGE, altText_urls[0][1])
            )
        if new_lists_text[-1] != "":
            new_nodes.append(TextNode(new_lists_text[-1], TextType.PLAIN))
    if len(new_nodes) == len(old_nodes):
        return new_nodes
    elif len(new_nodes) > len(old_nodes):
        return split_nodes_image(new_nodes)
    else:
        print(new_nodes)
        print(old_nodes)
        raise Exception("this should not be possible")


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if not isinstance(node, TextNode):
            print(node)
            raise Exception("old nodes list is not good")
        if node.text == "":
            continue
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
            continue
        altText_urls = extract_markdown_links(node.text)
        if altText_urls == []:
            new_nodes.append(node)
            continue
        altUrlString = "[" + altText_urls[0][0] + "](" + altText_urls[0][1] + ")"
        new_lists_text = node.text.split(altUrlString)
        for i in range(len(new_lists_text) - 1):
            if new_lists_text[i] != "":
                new_nodes.append(TextNode(new_lists_text[i], TextType.PLAIN))
            new_nodes.append(
                TextNode(altText_urls[0][0], TextType.LINK, altText_urls[0][1])
            )
        if new_lists_text[-1] != "":
            new_nodes.append(TextNode(new_lists_text[-1], TextType.PLAIN))
    if len(new_nodes) == len(old_nodes):
        return new_nodes
    elif len(new_nodes) > len(old_nodes):
        return split_nodes_link(new_nodes)
    else:
        print(new_nodes)
        print(old_nodes)
        raise Exception("this should not be possible")
