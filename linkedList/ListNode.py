class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

# inserts into list
def insert(head, item):
  temp = ListNode(item)
  if (head == None):
    head = temp
  else:
    ptr = head
    while ptr.next is not None:
      ptr = ptr.next
    ptr.next = temp
  return head

# turns array into a list 
def createList(arr):
  head = None
  for i in arr:
    head = insert(head, i)
  return head

# print list
def printList(head):
  while head is not None:
    print(head.val)
    head = head.next

