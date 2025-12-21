import unittest

from htmlnode import HtmlNode, LeafNode, ParentNode, text_node_to_html_node
from test_textnode import TextNode, TextType


class TestHtmlNode(unittest.TestCase):
    def test_eq(self):
        node = HtmlNode('div', 'hello')
        node2 = HtmlNode('div', 'hello')
        self.assertEqual(node, node2)

    def test_ne(self):
        node = HtmlNode('div', 'hello')
        node2 = HtmlNode('span', 'hello')
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = HtmlNode(tag='div', children=[HtmlNode('a', 'google', None, {'href': 'https://google.com'})])
        self.assertEqual(repr(node), "HtmlNode(div, None, [HtmlNode(a, google, None, {'href': 'https://google.com'})], None)")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_plain(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_leaf_no_value(self):
        node = LeafNode("p", None)
        self.assertRaises(ValueError, node.to_html)

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_url(self):
        node = TextNode("google.com", TextType.LINK, "https://google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'a')
        self.assertEqual(html_node.value, "google.com")
        self.assertEqual(html_node.props['href'], "https://google.com")


if __name__ == '__main__':
    unittest.main()
