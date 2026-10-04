class TreeNode:
  def __init__(self , val = 0 , left= None , right = None):
    self.val = val
    self.left = left
    self.right = right
class Solutiion:
  def inordertraversal(self , root: TreeNode | None) -> list[int]:
    curr = root
    stack = []
    res = []
    while stack or curr:
      while curr:
        stack.append(curr)
        curr = curr.left
      curr = stack.pop()
      res.append(curr.val)
      curr = curr.right
    return res

  
