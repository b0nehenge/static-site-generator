from textnode import TextNode, TextType


def main():
    node = TextNode("i am text", TextType.PLAIN, 'https://google.com')
    print(node)


main()

