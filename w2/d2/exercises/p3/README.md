## Binary Search Tree

Wikipedia on [Binary Search Tree](http://en.wikipedia.org/wiki/Binary_search_tree)

A binary search tree is a node based binary tree data structure. It is ordered in a particular way, where all values to the left of a node must be lower and all values to the right of a node must be higher relative to the root node aka the top node

#### Visualization

![binary search tree](http://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Binary_search_tree.svg/200px-Binary_search_tree.svg.png)

Like the linked list, each node holds pointer to other nodes. In this case, each node has two pointers - a left and a right.

#### Implementation
You will create two classes:
  - `TreeNode`
    - instantiate it with a value, as well as properties named left and right to hold other nodes.
  - `Tree`
    - instantiate it with a root node.

#### Methods

You will create the following methods for your Tree class:
  - `preorder`: this will traverse the tree and print every node's value
  - `search`: a recursive function that searches the tree for the value. Returns True if node exists, else returns False
  - `insert`: this should correctly insert a TreeNode in proper place (i.e.)
  - `inorder`: function that prints every node's value **in order** from lowest to highest