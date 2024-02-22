class SingleNode(object):
    """单链表的结点"""

    def __init__(self, item):
        # item 存放数据元素
        self.item = item
        self.next = None

    # 单链接的实现


class SingleLinkList(object):
    """单链表"""

    def __init__(self):
        self._head = None

    def is_empty(self):
        """判断链表是否为空"""
        return self._head == None

    def length(self):
        """链表长度"""
        cur = self._head
        count = 0
        # 尾节点指向None，当未到达尾部时
        while cur != None:
            count += 1
            # 将cur后移一个节点
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        cur = self._head
        while cur != None:
            print(cur.item)
            cur = cur.next

            # 在头部添加元素

    def add_data(self, item):
        # 在头部添加元素
        # 先创建一个保存item值的节点
        node = SingleNode(item)
        # 讲新的节点的链接域next指向头节点，即_head指向的位置
        node.next = self._head
        # 将链表的头_head 指向新节点
        self._head = node

    # 尾部添加元素
    def append_data(self, item):
        """尾部添加元素"""
        node = SingleNode(item)
        # 先判断链表是否为空，若是空链表，则将_head指向新节点
        if self.is_empty():
            self._head = node
        # 若不为空，则找到尾部，讲尾节点的next指向新的节点
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    # 指定位置添加元素
    def insert_data(self, pos, item):
        # 若指定位置pos为第一个元素之前，则执行头部插入
        if pos <= 0:
            self.add_data(item)
        # 若指定位置超过链表尾部，则执行尾部插入
        elif pos > self.length() - 1:
            self.append_data(item)
        # 找到指定的位置
        else:
            node = SingleNode(item)
            count = 0
            # pre用来指向指定位置pos的前一个位置pos-1，初始的指针从头节点开始移动到指定位置
            pre = self._head
            while count < (pos - 1):
                count += 1
                pre = pre.next
            # 先将新节点node的next执行插入位置的节点
            node.next = pre.next
            # 将插入位置的前一个节点的next指向新节点
            pre.next = node

        # 删除节点

    def remove_data(self, item):
        cur = self._head
        pre = None
        while cur != None:
            # 找到了指定的元素
            if cur.item == item:
                if not pre:
                    self._head = cur.next
                else:
                    # 将删除位置前一个节点的next指向删除位置的后一个节点
                    pre.next = cur.next
                break
            else:
                # 继续按链表后移节点
                pre = cur
                cur = cur.next

        # 查找节点是否存在

    def search_data(self, item):
        cur = self._head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False


if __name__ == "__main__":
    ll = SingleLinkList()
    ll.add_data(1)
    ll.add_data(2)
    ll.append_data(3)
    ll.insert_data(2, 4)
    print("length", ll.length())
    ll.travel()
    print(ll.search_data(3))
    print(ll.search_data(5))
    ll.remove_data(1)
    print("length:", ll.length())
    ll.travel()
