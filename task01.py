class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("The previous node does not exist.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next 
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # Merge sort for the linked list
    def merge_sort(self, h):
        if not h or not h.next:
            return h

        middle = self.get_middle(h) 
        next_to_middle = middle.next
        middle.next = None

        left = self.merge_sort(h) 
        right = self.merge_sort(next_to_middle) 

        sorted_list = self.sorted_merge(left, right)
        return sorted_list

    # Helper function to merge two sorted lists
    def sorted_merge(self, a, b):
        if not a:
            return b
        if not b:
            return a

        if a.data <= b.data:
            result = a
            result.next = self.sorted_merge(a.next, b)
        else:
            result = b
            result.next = self.sorted_merge(a, b.next)
        return result

    # Find the middle of the list
    def get_middle(self, head):
        if not head:
            return head

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    # Merge two sorted linked lists into one sorted list
    def merge_two_sorted_lists(self, l1, l2):
        dummy = Node(0)
        tail = dummy

        while l1 and l2:
            if l1.data < l2.data:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        return dummy.next


if __name__ == "__main__":

    llist = LinkedList()
    llist.insert_at_beginning(9)
    llist.insert_at_beginning(3)
    llist.insert_at_beginning(7)
    llist.insert_at_end(1)
    llist.insert_at_end(5)

    print("Initial list:")
    llist.print_list()

    llist.reverse()
    print("\nReversed list:")
    llist.print_list()

    llist.head = llist.merge_sort(llist.head)
    print("\nSorted list:")
    llist.print_list()

    llist1 = LinkedList()
    llist1.insert_at_end(1)
    llist1.insert_at_end(2)
    llist1.insert_at_end(4)

    llist2 = LinkedList()
    llist2.insert_at_end(3)
    llist2.insert_at_end(5)
    llist2.insert_at_end(6)

    merged_list = LinkedList()
    merged_list.head = llist.merge_two_sorted_lists(llist1.head, llist2.head)
    print("\nMerged sorted list:")
    merged_list.print_list()