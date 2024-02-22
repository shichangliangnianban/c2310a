# 1
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = ListNode(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = ListNode(value)

    def count(self, x):
        count = 0
        current = self.head
        while current:
            if current.value == x:
                count += 1
            current = current.next
        return count

# 示例使用
HL = LinkedList()
HL.append(1)
HL.append(2)
HL.append(3)
HL.append(2)
HL.append(6)

# 统计值为 2 的节点数
print(HL.count(6))  # 应该输出 2

# 2.
def classe(arr, k):
    left, right = 0, len(arr) - 1

    while left <= right:
        while arr[left] < k:
            left += 1
        while arr[right] >= k:
            right -= 1

        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return left


# 示例数据
data = [3, 1, 4, 2, 88, 9, 10, 42, 63, 56, 3, 5]
k_value = 10

# 执行划分
p = classe(data, k_value)

# 输出划分结果
left_class = data[:p]
right_class = data[p:]

print("左半部分:", left_class)
print("右半部分:", right_class)

# 3
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def intersection(self, head1: ListNode, head2: ListNode) -> ListNode:
        # 用于保存交集节点的头结点
        dummy = ListNode(-1, None)
        curr = dummy

        while head1 and head2:
            # 如果两个链表当前节点的值相等，将该节点插入到交集链表中
            if head1.val == head2.val:
                curr.next = ListNode(head1.val)
                curr = curr.next
                head1 = head1.next
                head2 = head2.next

        return dummy.next


# 5.
# def quicksort(data):
#     # 如果只有一个数据则不用排序
#     if len(data) <= 1:
#         return data
#     a = data[0]
#     list1 = [i for i in data[1:] if i <= a]
#     print(list1)
#     list2 = [j for j in data[1:] if j > a]
#     print(list2)
#     b = quicksort(list1) + [a] + quicksort(list2)
#     print(b)
#     return b
# data =(10,18,4,3,6,12,1,9,18,8)
# sorted_data = quicksort(data)
