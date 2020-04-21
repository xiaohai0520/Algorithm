# 二叉树详解

二叉树可以算是数据结构中经常用的，而且也是算法中容易考到的一个点。但二叉树无非是增删查改四个方面。这次我们用一个统一的模板，一次性高清二叉树的几种操作。

## 标准模板

```
def BST(root):
    # 处理root
    BST(root.left)
    BST(root.right)
```


## 查
```
def BST_search(root，target):
    if not root:
        return False
    if root.val == target:
        return True
        
    return BST_search(root.left) or BST_search(root.right)
```

## 改
```
def BST_change(root，target,changed):
    if not root:
        return
    if root.val == target:
        root.val = changed
        return
    BST_change(root.left)
    BST_change(root.right)
```

## 增
```
def BST_insert(root,val):
    if not root:
        return TreeNode(val)
    if root.val < val:
        root.right = BST_insert(root.right,val)
    if root.val > val:
        root.left = BST_insert(root.left,val)
    return root
```

## 删
```
def BST_delete(root,key):
    if not root:
        return
    if root.val == key:
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        minNode = getMin(root.right)
        root.val = minNode.val
        root.right = BST_delete(root.right,minNode.val)
    elif root.val > key:
        root.left = BST_delete(root.left,key)
    else:
        root.right = BST_delete(root.right,key)
    return root
```
