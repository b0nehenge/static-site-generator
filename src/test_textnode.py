import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_ne(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT, "http://www.google.com")
        self.assertNotEqual(node, node2)

    def test_ne2(self):
        node = TextNode("This is an italic text node", TextType.ITALIC)
        node2 = TextNode("This is an italic text node", TextType.ITALIC, "http://www.google.com")


if __name__ == "__main__":
    unittest.main()
