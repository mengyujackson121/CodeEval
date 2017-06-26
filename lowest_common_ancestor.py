import sys


class BST_Node(object):
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left_node = left
        self.right_node = right

    def lowest_common_ancestor(self,first,second):
        if first < self.value and second < self.value:
            temp = self.left_node.lowest_common_ancestor(first,second)
            return temp
        elif first > self.value and second > self.value:
            temp =  self.right_node.lowest_common_ancestor(first, second)
            return temp
        else:
            return self.value


def main():
    root = BST_Node(30,
                    BST_Node(8,
                             BST_Node(3),
                             BST_Node(20,
                                      BST_Node(10),
                                      BST_Node(29))),
                    BST_Node(52))
    lines = open(sys.argv[-1], 'r').readlines()
    for line in lines:
        a,b = map(int,line.strip().split(' '))
        answer = root.lowest_common_ancestor(a,b)
        print answer
main()

