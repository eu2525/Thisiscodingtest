n = int(input())

tree = [[0] * 2 for _ in range(n + 1)] 

for _ in range(n):
    root, left, right = input().split()
    tree[ord(root) - 65][0] = ord(left) - 65
    tree[ord(root) - 65][1] = ord(right) - 65

def preorder(idx):
    if idx == -19:
        return
    
    print(chr(idx + 65), end = '')
    preorder(tree[idx][0])
    preorder(tree[idx][1])

def inorder(idx):
    if idx == -19:
        return
    
    inorder(tree[idx][0])
    print(chr(idx + 65), end = '')
    inorder(tree[idx][1])

def postorder(idx):
    if idx == -19:
        return
    
    postorder(tree[idx][0])
    postorder(tree[idx][1])
    print(chr(idx + 65), end = '')

preorder(0)
print()
inorder(0)
print()
postorder(0)