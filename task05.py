import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, title):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(10, 7))
    plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def heap_to_tree(heap, index=0):
    if index >= len(heap):
        return None

    node = Node(heap[index])

    node.left = heap_to_tree(heap, 2 * index + 1)
    node.right = heap_to_tree(heap, 2 * index + 2)

    return node


def generate_color_gradient(n):
    colors = []
    for i in range(n):
        intensity = int(255 * (i + 1) / n)
        colors.append(f'#{intensity:02X}{intensity:02X}{255 - intensity:02X}')
    return colors


def bfs(root):
    if root is None:
        return []

    queue = deque([root])
    visited = []
    while queue:
        node = queue.popleft()
        visited.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return visited


def dfs(root):
    if root is None:
        return []

    stack = [root]
    visited = []
    while stack:
        node = stack.pop()
        visited.append(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return visited


def visualize_traversal(root, traversal_fn, title):
    traversal_order = traversal_fn(root)
    colors = generate_color_gradient(len(traversal_order))

    for i, node in enumerate(traversal_order):
        node.color = colors[i]
    
    draw_tree(root, title)


def main():
    heap = [15, 5, 2, 9, 3, 2, 9, 17, 4, 11, 24, 22, 3, 2, 7]
    root = heap_to_tree(heap)

    # Visualize BFS traversal
    visualize_traversal(root, bfs, title="BFS Traversal")

    # Visualize DFS traversal
    visualize_traversal(root, dfs, title="DFS Traversal")


if __name__ == "__main__":
    main()