#coding: utf-8
__author__ = 'Дмитрий'


def print_tree_pre_order(root):
    if root is not None:
        print root.value
        print_tree_pre_order(root.left_child)
        print_tree_pre_order(root.right_child)


def print_tree_post_order(root):
    if root is not None:
        print_tree_post_order(root.left_child)
        print_tree_post_order(root.right_child)
        print root.value


def print_tree_in_order(root):
    if root is not None:
        print_tree_in_order(root.left_child)
        print root.value
        print_tree_in_order(root.right_child)


class Tree:
    class __TreeNode:
        def __init__(self, value):
            self.value = value
            self.left_child = None
            self.right_child = None

        def has_child(self):
            if self.left_child is None and self.right_child is None:
                return False
            else:
                return True

    def __init__(self, value=None):
        self.root = self.__TreeNode(value) if value is not None else None

    def search(self, value):
        current_node = self.root
        while current_node is not None:
            if value == current_node.value:
                return current_node
            elif value < current_node.value:
                current_node = current_node.left_child
            elif value > current_node.value:
                current_node = current_node.right_child
        return None

    def add_tree_node(self, value):
        if self.root is None:
            self.root = self.__TreeNode(value)
        else:
            current_node = self.root

            while True:
                if value == current_node.value:
                    break
                elif value < current_node.value:
                    if current_node.left_child is not None:
                        current_node = current_node.left_child
                    else:
                        current_node.left_child = self.__TreeNode(value)
                        break
                elif value > current_node.value:
                    if current_node.right_child is not None:
                        current_node = current_node.right_child
                    else:
                        current_node.right_child = self.__TreeNode(value)
                        break

    def print_tree_pre_order(self):
        for node in self.iterator_tree_node_pre_order():
            print node.value

    def print_tree_post_order(self):
        for node in self.iterator_tree_node_post_order():
            print node.value

    def print_tree_in_order(self):
        for node in self.iterator_tree_node_in_order():
            print node.value

    def iterator_tree_node_pre_order(self):
        if self.root is not None:
            node = self.root
            parents = []
            while True:
                parents.append(node)
                yield node
                if node.left_child is not None:
                    node = node.left_child
                elif node.right_child is not None:
                    node = node.right_child
                else:
                    for parent in parents[-2::-1]:
                        if parent.right_child is not None and not parent.right_child in parents:
                            parents = parents[:parents.index(parent) + 1]
                            node = parent.right_child
                            break
                    else:
                        break

    def iterator_tree_node_in_order(self):
        if self.root is not None:
            node = self.root
            parents = []
            while True:
                parents.append(node)
                if node.left_child is not None:
                    node = node.left_child
                elif node.right_child is not None:
                    yield node
                    node = node.right_child
                else:
                    yield node
                    for parent in parents[-2::-1]:
                        if parent.right_child is not None:
                            if not parent.right_child in parents:
                                parents = parents[:parents.index(parent) + 1]
                                node = parent.right_child
                                yield parent
                                break
                        else:
                            parents = parents[:parents.index(parent) + 1]
                            yield parent
                    else:
                        break

    def iterator_tree_node_post_order(self):
        if self.root is not None:
            node = self.root
            parents = []
            while True:
                parents.append(node)
                if node.left_child is not None:
                    node = node.left_child
                elif node.right_child is not None:
                    node = node.right_child
                else:
                    yield node
                    for parent in parents[-2::-1]:
                        if parent.right_child is not None:
                            if not parent.right_child in parents:
                                parents = parents[:parents.index(parent) + 1]
                                node = parent.right_child
                                break
                            else:
                                parents = parents[:parents.index(parent) + 1]
                                yield parent
                        else:
                            parents = parents[:parents.index(parent) + 1]
                            yield parent
                    else:
                        break

    def delete_tree_node(self, value):
        if self.root is not None:
            current_root = self.root
            parent_node = current_root
            while True:
                if value == current_root.value:
                    break
                elif value > current_root.value:
                    if current_root.right_child is not None:
                        parent_node = current_root
                        current_root = current_root.right_child
                elif value < current_root.value:
                    if current_root.left_child is not None:
                        parent_node = current_root
                        current_root = current_root.left_child
                else:
                    return
            current_node = current_root.left_child or current_root.right_child
            if current_node is None:
                if parent_node.left_child == current_root:
                    parent_node.left_child = None
                else:
                    parent_node.right_child = None
                del current_root
            elif current_node == current_root.left_child:
                while True:
                    if current_node.right_child is None:
                        if current_node.left_child is None:
                            current_root.value = current_node.value
                            if parent_node.right_child.value == current_node.value:
                                parent_node.right_child = None
                            else:
                                parent_node.left_child = None
                            del current_node
                            break
                        else:
                            parent_node = current_node
                            current_node = current_node.left_child
                    else:
                        parent_node = current_node
                        current_node = current_node.right_child
            else:
                while True:
                    if current_node.left_child is None:
                        if current_node.right_child is None:
                            current_root.value = current_node.value
                            if parent_node.left_child.value == current_node.value:
                                parent_node.left_child = None
                            else:
                                parent_node.right_child = None
                            del current_node
                            break
                        else:
                            parent_node = current_node
                            current_node = current_node.right_child
                    else:
                        parent_node = current_node
                        current_node = current_node.left_child