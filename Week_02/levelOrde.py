# 给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。
#
#  例如，给定一个 3叉树 :
#
#
#
#
#
#
#
#  返回其层序遍历:
#
#  [
#      [1],
#      [3,2,4],
#      [5,6]
# ]
#
#
#
#
#  说明:
#
#
#  树的深度不会超过 1000。
#  树的节点总数不会超过 5000。
#  Related Topics 树 广度优先搜索
#  👍 98 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """

# leetcode submit region end(Prohibit modification and deletion)
        if not root:
            return []
        res, quene = [], [root]
        while quene:
            n = len(quene)
            level = []
            for i in range(n):
                node = quene.pop(0)
                level.append(node.val)
                for no in node.children:
                    quene.append(no)
            res.append(level)
        return res