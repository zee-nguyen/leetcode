""" Breadth-first Search """

def bfs(root):
    if not root:
	    return

    q = [(root, 1)]
    min_depth = 10^8
    while q:
        new_q = []
        for (node, depth) in q:
            if not node.left and not node.right: # leaf
                min_depth = min(min_depth, depth)
            for n in (node.left, node.right):
                if n:
                    new_q.append(n)
