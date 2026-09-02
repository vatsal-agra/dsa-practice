class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def serialize(node, result):
            if node is None:
                result.append("null")
                return
            result.append(node.val)
            serialize(node.left, result)
            serialize(node.right, result)
        
        a = []
        b = []
        serialize(p, a)
        serialize(q, b)
        return a == b