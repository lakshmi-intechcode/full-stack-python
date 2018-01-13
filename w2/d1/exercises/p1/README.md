Single Linked List
===========

Wikipedia on [Linked Lists](http://en.wikipedia.org/wiki/Linked_list).
CS50 on [Linked Lists](https://www.youtube.com/watch?v=5nsKtQuT6E8)

A linked list is a common data structure, where nodes are grouped to form a sequence. Each node holds data and a pointer to another node.

### Visualization

    |42|-> |55|-> |4|-> |39|-> None

A linked last can be advantageous over an array because it is dynamic - to insert or delete a node in the middle of the list, we don't need to re-index the entire list, like an array. We only need to alter a pointer.

For example, to insert `|79|` after `|4|` in the list above, pseudocode would look this:

    79 = new node
    79.next should point to 4.next (i.e. 4.next points to 39)
    # after insertion:
        - 4.next should point to 79
        - 79.next should point to 39
        - 39.next should still point to None
        
    

### Implementation

Do not use lists or dictionaries. That's cheating. Create this using classes only. You will want a Node class and a LinkedList class.

Create your data structures and the following methods that allow your linked list to:
- insert
- search (First iteratively then recursively)
- delete
- print backwards
