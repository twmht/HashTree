#coding: utf-8
__author__ = 'Дмитрий'
import sys
import os
from HashTree import HashTree


def argumentsCountError(count):
    print "Script takes exactly two arguments (" + str(count) + " given)"
    exit()


def pathFileError():
    print "Can't find file in current path"
    exit()


def hashValueError():
    print "Something wrong with hash value. May be it's not hex number."
    exit()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        argumentsCountError(len(sys.argv) - 1)

    file_path = sys.argv[1]

    if not os.path.exists(file_path):
        if not os.path.isfile(file_path):
            pathFileError()

    try:
        input_hash = int(sys.argv[2], 16)
    except ValueError:
        input_hash = None
        hashValueError()

    root = HashTree(file_path)

    file_hash = root.get_final_hash()

    print "Hash of file is " + str(hex(file_hash))[:-1] if str(hex(file_hash))[-1] == 'L' else str(hex(file_hash))

    if file_hash == input_hash:
        print "File's hash is equivalent to input hash"
    else:
        diapason = root.find_similar_part(input_hash)
        if diapason is not None:
            print "Hash of file's part from " + str(diapason[0]) + "b to " + \
                  str(diapason[1]) + "b equivalent to input hash"
        else:
            print "File's hash hasn't equivalent part to input hash"