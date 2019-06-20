#!/usr/bin/python2.7
"""
    rather than re-invent the wheel, Laurent Luce has a concrete example
    of a binary search tree node object in python
    http://www.laurentluce.com/posts/binary-search-tree-library-in-python/
    This has been extended for additional use-cases
"""

class Node:
    """
    Tree node: left and right child + data which can be any object
    """
    def __init__(self, data):
        """
        Node constructor

        @param data node data object
        """
        self.left = None
        self.right = None
        self.data = int(data)

    def insert(self, data):
        """
        Insert new node with data

        @param data node data object to insert
        """
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
        else:
            print "'%d' already exists in tree" % data

    def lookup(self, data, parent=None):
        """
        Lookup node containing data

        @param data node data object to look up
        @param parent node's parent
        @returns node and node's parent if found or None, None
        """
        if data < self.data:
            if self.left is None:
                return None, None
            return self.left.lookup(data, self)
        elif data > self.data:
            if self.right is None:
                return None, None
            return self.right.lookup(data, self)
        else:
            return self, parent

    def get_range(self, left, right):
        """
        Find the range of inclusive values between left and right

        @param left data
        @param right data
        """
        count = 0
        start = left
        end = right
        if right > left:
          start = right
          end = left
        print "start %d, end %d" % (start, end)
        return count

    def delete(self, data):
        """
        Delete node containing data

        @param data node's content to delete
        """
        # get node containing data
        node, parent = self.lookup(data)

        if node is not None:
            children_count = node.children_count()

        if children_count == 0:
            # if node has no children, just remove it
            if parent.left is node:
                parent.left = None
            else:
                parent.right = None
        elif children_count == 1:
            # if node has 1 child
            # replace node by its child
            if node.left:
                node.data = node.left.data
                node.left = None
            else:
                node.data = node.right.data
                node.right = None
        else:
            # if node has 2 children
            # find its successor
            parent = node
            successor = node.right
            while successor.left:
                parent = successor
                successor = successor.left
            # replace node data by its successor data
            node.data = successor.data
            # fix successor's parent node child
            if parent.left == successor:
                parent.left = successor.right
            else:
                parent.right = successor.right

    def compare_trees(self, node):
        """
        Compare 2 trees

        @param node tree to compare
        @returns True if the tree passed is identical to this tree
        """
        if node is None:
            return False
        if self.data != node.data:
            return False
        res = True
        if self.left is None:
            if node.left:
                return False
        else:
            res = self.left.compare_trees(node.left)
        if self.right is None:
            if node.right:
                return False
        else:
            res = self.right.compare_trees(node.right)
        return res

    def inorder_traversal(self, node):
        """
        Print tree content inorder. left -> root -> right

        @param node tree to compare
        """
        values = []
        if node:
            values = self.inorder_traversal(node.left)
            values.append(node.data)
            values += self.inorder_traversal(node.right)
        return values

    def tree_data(self):
        """
        Generator to get the tree nodes data
        """
        # we use a stack to traverse the tree in a non-recursive way
        stack = []
        node = self
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else: # we are returning so we pop the node and we yield it
                node = stack.pop()
                yield node.data
                node = node.right

    def children_count(self):
        """
        Return the number of children

        @returns number of children: 0, 1, 2
        """
        cnt = 0
        if self.left:
            cnt += 1
        if self.right:
            cnt += 1
        return cnt

def get_range(values, left=None, right=None):
  """ get the range of values between left, right """
  tree = None
  for val in values:
    try:
      if not tree:
        tree = Node(val)
      else:
        tree.insert(val)
    except TypeError as error:
      print error
  #node, parent = tree.lookup(6)
  #print "node: %d, parent: %d" % (node.data, parent.data)
  print tree.inorder_traversal(tree)
  if left and right:
    count = 0
    for val in tree.inorder_traversal(tree):
        if val >= left and val <= right:
          count += val
        if val > right:
          break
    print "left: %d, right %d" % (left, right)
    print "count: %d" % count


if __name__ == '__main__':
    print '-'*80
    tree = None
    values = [10,5,15,3,7,13,18,1,None,6]
    get_range(values)
    get_range(values, 5, 14)
