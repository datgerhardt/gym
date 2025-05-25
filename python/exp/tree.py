from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p.val != q.val:
            return False
        if p.left != q.left:
            return False
        if p.right != q.right:
            return False

        return True



if __name__ == "__main__":
    print(Solution().isSameTree(TreeNode(1,2,3), TreeNode(1,2,3)))
