#coding: utf-8
__author__ = 'Дмитрий'

import Tree
from hashlib import md5


class HashTree(Tree.Tree):
    def make_tree(self, file_path, block_size=None):
        """
        :type file_path: str or unicode
        :type block_size: int
        """
        if block_size is None:
            block_size = 32

        node_levels = [self.__get_hash_list(file_path, block_size)]

        for node_level in node_levels:
            if len(node_level) == 1:
                break
            elif len(node_level) % 2:
                node_level += [0]
            node_levels.append([int(md5(str(node_level[index]) + str(node_level[index + 1])).hexdigest(), 16)
                                for index in range(0, len(node_level) - 1, 2)])

        for node_level in node_levels[::-1]:
            for node in node_level:
                if node != 0:
                    self.add_tree_node(node)

    def __get_hash_list(self, file_path, block_size):
        """
        :param block_size: int
        :type file_path: str
        :return: list
        """
        hash_list = []
        with open(file_path, 'rb') as fh:
            while True:
                data = fh.read(block_size)
                if not data:
                    break
                hash_list += [int(md5(data).hexdigest(), 16)]
        return hash_list

if __name__ == '__main__':
    root = HashTree()
    root.make_tree(u"E:\\Торрент\\ubuntu-13.04-desktop-amd64.iso", 16384)

    root2 = HashTree()
    root2.make_tree(u"E:\\Торрент\\ubuntu-13.04-desktop-amd642.iso", 16384)
    #root.print_tree_pre_order()

    for node in root.iterator_tree_node_pre_order():
        print hex(node.value)
        break

    for node in root2.iterator_tree_node_pre_order():
        print hex(node.value)
        break
