#coding: utf-8
__author__ = 'Дмитрий'
from hashlib import md5


class HashTree():
    class __TreeNode:
        def __init__(self, value):
            self.value = value
            self.left_child = None
            self.right_child = None

    def __init__(self, file_path=None, block_size=None):
        """
        :param block_size: int
        :param file_path: str or unicode
        """
        if file_path is not None:
            self.make_tree(file_path, block_size)
        else:
            self.__root = None
            self.__levels = 0
            self.__block_size = 0

    def make_tree(self, file_path, block_size=None):
        """
        :type file_path: str or unicode
        :type block_size: int
        """
        self.__block_size = 8192 if block_size is None else block_size

        hash_list = [[self.__TreeNode(value) for value in self.__get_hash_list(file_path, self.__block_size)]]
        self.__root, self.__levels = self.__list_to_tree(hash_list)

    def __list_to_tree(self, hash_list):
        """
        :type hash_list: list
        :rtype: self.__TreeNode and int
        """
        for node_level in hash_list:
            if len(node_level) == 1:
                break

            new_level = []
            for index in range(0, len(node_level), 2):
                if index + 1 < len(node_level):
                    node_value = int(md5(str(node_level[index].value) + str(node_level[index+1].value)).hexdigest(), 16)
                    new_level.append(self.__TreeNode(node_value))
                    new_level[-1].left_child = node_level[index]
                    new_level[-1].right_child = node_level[index + 1]
                else:
                    new_level.append(node_level[index])

            hash_list.append(new_level)
        return hash_list[-1][0], len(hash_list)

    def __get_hash_list(self, file_path, block_size):
        """
        :rtype: list
        :type block_size: int
        :type file_path: str or unicode
        """
        hash_list = []
        with open(file_path, 'rb') as fh:
            while True:
                data = fh.read(block_size)
                if not data:
                    break
                hash_list += [int(md5(data).hexdigest(), 16)]
        return hash_list

    def get_final_hash(self):
        return self.__root.value

    def find_hash(self, input_hash):
        """
        :type input_hash: int or long
        :rtype: self.__TreeNode
        """
        for hash_node in self.iterator_tree_node_pre_order():
            if hash_node.value == input_hash:
                return hash_node
        else:
            return None

    def find_similar_part(self, input_hash):
        """
        :type input_hash:  int or long
        :rtype: cortege (int, int)
        """
        hash_left_leaf = hash_right_leaf = hash_node = self.find_hash(input_hash)
        if hash_node is None:
            return None

        while hash_left_leaf.left_child is not None:
            hash_left_leaf = hash_left_leaf.left_child

        while hash_right_leaf.right_child is not None:
            hash_right_leaf = hash_right_leaf.right_child

        list_number = -1
        left_list_number = 0
        for node in self.iterator_tree_node_pre_order():
            if node.left_child is None:
                list_number += 1
                if node == hash_left_leaf:
                    left_list_number = list_number
                if node == hash_right_leaf:
                    return self.__block_size * left_list_number, self.__block_size * (list_number + 1)

    def iterator_tree_node_pre_order(self):
        if self.__root is None:
            return

        node = self.__root
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