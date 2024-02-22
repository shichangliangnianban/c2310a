# 1.判断队列是否为空
def is_empty(self):
    """判断队列是个否为空"""
    return self.items == []
# 2.进队列代码实现
def enqueue(self, item):
    """进队列"""
    self.items.insert(0, item)
# 3.出队列代码实现
def dequeue(self):
    """出队列"""
    return self.items.pop()
# 4.返回队列的大小，代码实现
def size(self):
    """返回大小"""
    return len(self.items)
# 5.树的种类有哪些
# 无序树:树中任意节点之间没有顺序关系,这种树称为无序树,也称为自由树;
# 有序树:树中任意节点的子节点之间有顺序关系,这种树成为有序树;
# 二叉树:每个节点最多含有两个子树;
# 完全二叉树:对于一颗二叉树,比如深度为d(d>1),除了第d层之外,其他各层的节点数目已经达到最大值
# d层节点从左到右紧密排列,这样的二叉树称为完全二叉树.
# 平衡二叉树:当且仅当任何节点的两颗子树的高度差不大于1的二叉树;
# 排序二叉树:也称二叉搜索树,(BST),二叉查找树,有序二叉树;
# 霍夫曼树:又称最优树
# B树:一种对读写操作进行优化的自平衡的二叉查找树,能够保持数据有序,拥有多于两颗子树;

# 6.树的存储有几种方式
#将数据结构存储在固定的数组中，在遍历速度上有一定的优势，但是占用空间比较大,是非主流的二叉树,
# 二叉树通常以链式存储
# 顺序存储:将数据结构存储在固定的数组中，然在遍历速度上有一定的优势，但因所占空间比较大，是非主流二叉树。二叉树通常以链式存储。

# 7.二叉树的节点的代码
class Node(object):
    """节点类"""
    def __init__(self,elem=-1,lchild=None,rchild=None):
        self.elem=elem
        self.lchild=lchild
        self.rchild=rchild
# 8.代码创建树，为树添加节点
class Tree(object):
    """树类"""
    def __init(self,root=None):
        self.root=root
    def add(self,elem):
        """为树添加节点"""
        node=Node(elem)
#         如果树是空的,需要对根节点赋值
        if self.root==None:
            self.root=node
        else:
            queue=[]
            queue.append(self.root)
            while queue:
#                 弹出队列的第一个元素
                cur = queue.pop(0)
                if cur.lchild==None:
                    cur.lchild=node
                elif cur.rchild==None:
                    cur.rchild=node
                else:
#                     如果左右子树都不为空,加入队列继续判断
                    queue.append(cur.lchild)
                    queue.append(cur.rchild)
# 9.代码实现二叉树的深度优先遍历
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def dfs(root):
        if root is None:
            return

        # 先访问根节点
        print(root.val)
        # 递归遍历左子树
        dfs(root.left)
        # 递归遍历右子树
        dfs(root.right)


# 10.代码实现二叉树的广度优先遍历
def breadth_travel(self,root):
    """利用队列实现树的层次遍历"""
    if root==None:
        return
    queue=[]
    queue.append(root)
    while queue:
        node=queue.pop(0)
        print(node.elem)
        if node.lchild!=None:
            queue.append(node.lchild)
        if node.rchild!=None:
            queue.append(node.rchild)