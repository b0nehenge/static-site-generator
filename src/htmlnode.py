from src.textnode import TextNode, TextType


class HtmlNode:

    def __init__(self, tag: str = None, value: str = None, children: list['HtmlNode'] = None, props: dict = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __eq__(self, other: 'HtmlNode') -> bool:
        return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props

    def __repr__(self) -> str:
        return f"HtmlNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        props = ""

        if self.props is None:
            return props

        for key, value in self.props.items():
            props += f" {key}=\"{value}\""

        return props


class LeafNode(HtmlNode):
    def __init__(self, tag: str | None, value: str, props: dict = None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError

        if self.tag is None:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HtmlNode):
    def __init__(self, tag: str, children: list[HtmlNode], props: dict = None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.children is None:
            raise ValueError("Parent node must have children")
        if self.tag is None:
            raise ValueError("Parent node must have a tag")

        return f"<{self.tag}{self.props_to_html()}>{"".join(list(map(lambda x: x.to_html(), self.children)))}</{self.tag}>"


def text_node_to_html_node(text_node: TextNode) -> HtmlNode:
    props = None
    if text_node.text_type.value == TextType.LINK.value:
        props = {'href': text_node.url}
    elif text_node.text_type.value == TextType.IMAGE.value:
        props = {'src': text_node.url, 'alt': text_node.text}

    return LeafNode(text_node.text_type.value, text_node.text, props)
