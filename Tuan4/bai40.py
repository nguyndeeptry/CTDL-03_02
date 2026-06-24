class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def build(lst):
    head = None
    for v in reversed(lst):
        node = Node(v)
        node.next = head
        head = node
    return head

def to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def insertion_sort_ll(head):
    sorted_head = None
    curr = head
    while curr:
        next_node = curr.next
        if sorted_head is None or sorted_head.val >= curr.val:
            curr.next = sorted_head
            sorted_head = curr
        else:
            tmp = sorted_head
            while tmp.next and tmp.next.val < curr.val:
                tmp = tmp.next
            curr.next = tmp.next
            tmp.next = curr
        curr = next_node
    return sorted_head

head = build([3, 1, 2])
head = insertion_sort_ll(head)
print(to_list(head))
