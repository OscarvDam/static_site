from src.textnode import TextNode, TextType

def split_node_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        # new_nodes_text = [u for x in node.text.split(delimiter) for u in (x, delimiter)]
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
            continue
        new_nodes_text = node.text.split(delimiter)
        for i in range(len(new_nodes_text)):
            if i % 2 == 0:
                if new_nodes_text[i] == "":
                    continue
                new_nodes.append(TextNode(new_nodes_text[i], TextType.PLAIN))
            if i % 2 == 1:
                new_nodes.append(TextNode(new_nodes_text[i], text_type))
    return new_nodes
