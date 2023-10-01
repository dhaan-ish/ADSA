class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def preOrder(self, rootNode):
        if rootNode is not None:
            print(rootNode.data)
            self.preOrder(rootNode.left)
            self.preOrder(rootNode.right)

    def inOrder(self, rootNode):
        if rootNode is not None:
            self.inOrder(rootNode.left)
            print(rootNode.data)
            self.inOrder(rootNode.right)

    def postOrder(self, rootNode):
        if rootNode is not None:
            self.postOrder(rootNode.left)
            self.postOrder(rootNode.right)
            print(rootNode.data)

a = TreeNode(10)
b = TreeNode(20)
c = TreeNode(30)
d = TreeNode(40)
e = TreeNode(50)
f = TreeNode(60)
g = TreeNode(70)

d.left = b
d.right = f
b.left = a
b.right = c
f.left = e
f.right = g

print("Pre-order Traversal:")
d.preOrder(d)

print("In-order Traversal:")
d.inOrder(d)

print("Post-order Traversal:")
d.postOrder(d)
