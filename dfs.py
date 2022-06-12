def dfs(root, target):
    if root is None:
        return None
    if root.val == target:
        return root
    
    # left
    left = dfs(root.left, target)
    