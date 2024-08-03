from collections import deque

class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, id):
        # Use a queue for breadth-first traversal
        queue = deque([self.root])
        
        while queue:
            node = queue.popleft()
            if node is None:
                continue
            if node.get('id') == id:
                return node
            queue.extend(node.get('children', []))
        
        return None
