import argparse


def read_word(in_str: str):
    in_str = in_str.strip()
    pointer = 0
    c = in_str[pointer]
    while c != ' ' and c != ')':
        pointer += 1
        c = in_str[pointer]
    # Point to next word starting position
    pointer += 1
    return in_str[:pointer], in_str[pointer:]


def print_node(text: str, depth: int):
    text = text.strip(')( ')
    if not text:
        return
    if not depth:
        print(text)
        return

    # Each node needs to be prefixed with the following seq:
    node_prefix = '+-- '
    # depth_prefix is indentation needs to be applied to match the start of the node of the next line:
    # (depth - 1) * len(node_prefix)
    depth_prefix = ' ' * ((depth - 1) * len(node_prefix))
    # each line except first has indent of one on start
    line_prefix = ' ' + depth_prefix + node_prefix
    # If first two symbols are not starting with ' +', we need to indicate a line with ' |'
    # Equivalent to depth > 1
    if line_prefix[1] != '+':
        line_prefix = ' |' + line_prefix[2:]
    print(line_prefix+text)


def print_tree(line: str, depth: int = 0):
    if not line:
        return
    word, line = read_word(line)
    print_node(word, depth)
    if word[-1] == ')':
        depth -= 1
    elif word[0] == '(':
        depth += 1
    print_tree(line, depth)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Print tree')
    parser.add_argument('--text', type=str, help='String-serialized tree')

    args = parser.parse_args()

