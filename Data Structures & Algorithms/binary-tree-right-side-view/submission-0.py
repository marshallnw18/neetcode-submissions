# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        # initialize the queue
        queue = collections.deque()
        if root:
            queue.append(root)
        
        # level counter
        level = 0

        returnList = []
        # traverse the tree
        while len(queue) > 0:
            subList = []
            print("level: ", level)
            for i in range(len(queue)):
                curr = queue.popleft()
                subList.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            level += 1
            returnList.append(subList[len(subList) - 1])
        
        return returnList