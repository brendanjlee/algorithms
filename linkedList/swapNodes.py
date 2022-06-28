def swapPairs(head):
    dummy = ListNode(0, head)
    prev = dummy
    curr = head

    # a - b - c
    while curr is not None and curr.next is not None:
        # save pointers
        c = curr.next.next
        b = curr.next

        # reverse the a,b pair
        a.next = c
        b.next = a
        prev.next = b

        # update pointer
        prev = curr
        curr = c

    return dummy.next

