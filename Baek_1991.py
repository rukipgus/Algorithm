import sys

class node:
    def __init__(self, item, lchild, rchild):
        self.item = item
        self.lchild = lchild
        self. rchild = rchild

def preorder(node):
    print(node.item, end = "")
    if node.lchild != ".":
        preorder(tree[node.lchild])
    if node.rchild != ".":
        preorder(tree[node.rchild])
    
def inorder(node):
    if node.lchild != ".":
        inorder(tree[node.lchild])
    print(node.item, end = "")
    if node.rchild != ".":
        inorder(tree[node.rchild])
    
def postorder(node):
    if node.lchild != ".":
        postorder(tree[node.lchild])
    if node.rchild != ".":
        postorder(tree[node.rchild])
    print(node.item, end = "")

n = int(sys.stdin.readline())

tree = {}

for i in range(n):
    x, y, z = sys.stdin.readline().split()
    tree[x] = node(item = x, lchild = y, rchild = z)

preorder(tree["A"])
print()
inorder(tree["A"])
print()
postorder(tree["A"])