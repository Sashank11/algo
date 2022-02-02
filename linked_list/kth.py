from LinkedList import LinkedList

def kthToLast(ll, k):
    pointer1 = ll.head
    pointer2 =ll.head

    for i in range(k):
        if pointer2 is None:
            return None
        else:
            pointer2 = pointer2.next

    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    
    return pointer1.value

customLL = LinkedList()
customLL.generate(10, 0 ,99)
print(customLL)
print(kthToLast(customLL, 3))