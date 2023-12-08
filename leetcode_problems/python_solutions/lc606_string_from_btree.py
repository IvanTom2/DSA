"""
Given the root of a binary tree, construct a string consisting of parenthesis and integers from a binary tree with the preorder traversal way, and return it.
Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship between the string and the original binary tree.

Input: root = [1,2,3,4]
Output: "1(2(4))(3)"
Explanation: Originally, it needs to be "1(2(4)())(3()())", but you need to omit all the unnecessary empty parenthesis pairs. And it will be "1(2(4))(3)"
"""
from time_measure import repeater


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1(object):
    """
    43 ms, 18.8 MB

    Mean time = 0.01800 ms
    Min time  = 0.01663 ms
    """

    def run_rec(self, node: TreeNode, container: str) -> str:
        container = f"{node.val}"

        if node.left is not None:
            out = self.run_rec(node.left, container)
            container += "(" + out + ")"

        if node.right is not None:
            out = self.run_rec(node.right, container)
            if node.left is None:
                container += "()"
            container += "(" + out + ")"

        return container

    @repeater()
    def run(self, root: TreeNode) -> str:
        container = ""
        container = self.run_rec(root, container)
        return container


def setup_btree1():
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node8 = TreeNode(8)
    node9 = TreeNode(9)
    node10 = TreeNode(10)

    root = node1
    root.left = node2
    root.right = node3

    node2.left = node4
    node2.right = node5

    node4.left = node8
    node5.right = node9

    node3.left = node6
    node3.right = node7

    node7.right = node10
    return root


def setup_btree2():
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)

    root = node1
    root.left = node2
    root.right = node3

    node2.right = node4
    return root


if __name__ == "__main__":
    btree = setup_btree1()

    sol1 = Solution1()

    print(sol1.run(btree))
