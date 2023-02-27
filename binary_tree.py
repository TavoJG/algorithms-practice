from random import shuffle


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value) -> None:
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return

        temp = self.root

        while True:
            if new_node.value == temp.value:
                raise Exception(
                    f'{new_node.value} already exists into Binary Tree')

            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return
                temp = temp.right

    def contains(self, value) -> bool:
        temp = self.root

        while temp is not None:
            if temp.value > value:
                temp = temp.left
            elif temp.value < value:
                temp = temp.right
            elif temp.value == value:
                return True

        return False

    def contains_recursive(self, value):
        def recursive_search(node, value):
            if not node:
                return False
            if node.value == value:
                return True
            elif node.value > value:
                return recursive_search(node.left, value)
            else:
                return recursive_search(node.right, value)

        result = recursive_search(self.root, value)
        return result

    def dfs_preorder(self):
        results = []

        def transverse(current_node: Node):
            results.append(current_node.value)

            if current_node.left:
                transverse(current_node.left)
            if current_node.right:
                transverse(current_node.right)

        transverse(self.root)
        return results

    def dfs_postorder(self):
        results = []

        def transverse(current_node: Node):

            if current_node.left:
                transverse(current_node.left)
            if current_node.right:
                transverse(current_node.right)

            results.append(current_node.value)

        transverse(self.root)
        return results

    def dfs_inorder(self):
        results = []

        def transverse(current_node: Node):

            if current_node.left:
                transverse(current_node.left)
            results.append(current_node.value)
            if current_node.right:
                transverse(current_node.right)

        transverse(self.root)
        return results

    def bfs(self):
        current_node = self.root
        queue = [current_node]
        results = []
        levels = 0

        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            levels += 1
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        return results, levels

    def print_tree(self):
        results, levels = self.bfs()

        for i in range(levels):
            print(results[i:i*2-1])


if __name__ == '__main__':

    value_list = list(range(1, 21))
    shuffle(value_list)

    my_tree = BinarySearchTree()

    for value in value_list:
        my_tree.insert(value)

    print(my_tree.contains(20))
    print(my_tree.contains_recursive(55))
    print(my_tree.dfs_preorder())
    print(my_tree.dfs_postorder())
    print(my_tree.dfs_inorder())
    print(my_tree.bfs()[0])
    my_tree.print_tree()
