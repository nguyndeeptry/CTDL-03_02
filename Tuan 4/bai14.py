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

def selection_sort_ll(head):
    result = None
    result_tail = None
    while head:
        prev_min = None
        prev = None
        curr = head
        min_node = head
        while curr:
            if curr.val < min_node.val:
                min_node = curr
                prev_min = prev
            prev = curr
            curr = curr.next
        if prev_min:
            prev_min.next = min_node.next
        else:
            head = min_node.next
        min_node.next = None
        if result is None:
            result = min_node
            result_tail = min_node
        else:
            result_tail.next = min_node
            result_tail = min_node
    return result

head = build([3, 1, 2])
head = selection_sort_ll(head)
print(to_list(head))
