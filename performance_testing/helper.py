import timeit
from random import randint


def test_performance(trials, func=None, args="", stmt=None, prnt=False):
    """Main testing function"""

    setup = ""
    statement = ""

    if func is not None:
        setup = "from __main__ import " + func
        statement = func + "(" + str(args) + ")"

    elif stmt is not None:
        statement = stmt

    t = timeit.Timer(statement, setup)

    if trials is None:
        time = t.timeit(10)
        print("time: " + str(time))
        trials = int((time ** -1))
        print("num trials: " + str(trials))


    val = min(t.repeat(10, trials))

    if prnt:
        print(val)
        return
    else:
        return str(val)
    
def test_performance_2(trials, func, args=None, setup=None, print_out=False):

    statement = func + "(" + str(args) + ")"
    #print("statement: " + statement)

    if setup is None:
        setup = "from __main__ import " + func
    else:
        setup = "from __main__ import " + func + "\n" + "\n".join(setup)

    #print(setup)

    t = timeit.Timer(statement, setup)

    val = min(t.repeat(10, trials))

    if print_out:
        print(val)
        return
    else:
        return str(val)

""" Set creation vs clearing functions """

def createNewSets():
    for i in range(100):
        newSet = set()
        for index in range(100):
            newSet.add(index)

def clearOldSets():
    newSet = set()
    for i in range(100):
        newSet.clear()
        for index in range(100):
            newSet.add(index)

"""Ant Cube Testing"""

def ant_cube_first_attempt():
    """runs an ant_cube simulation, returns true on collision, false otherwise"""
    cube = []
    for x in range(0, 8):
        x = ("000" + bin(x)[2:])[-3:] #this is disgusting
        cube.append(x)
    for index in range(0, 8):
        path = randint(0, 2)
        ant = cube[index]
        ant = ant[0:path] + str(int(ant[path]) ^ 1) + ant[path+1:]
        cube[index] = ant
    testSet = set()
    for ant in cube:
        testSet.add(ant)
    if len(testSet) == 8:
        return False
    else:
        return True

def ant_cube_second_attempt():
    cube = [0b000, 0b001, 0b010, 0b011, 0b100, 0b101, 0b110, 0b111]
    masks = [0b001, 0b010, 0b100]
    for index in range(0, 8):
        rand = randint(0, 2)
        cube[index] ^= masks[rand]
    test_set = set()
    for ant in cube:
        test_set.add(ant)
    if len(test_set) == 8:
        return False
    else:
        return True

def ant_cube_third_attempt():
    masks = [0b001, 0b010, 0b100]
    newSet = set()
    for index in range(0, 8):
        ant = index ^ masks[randint(0, 2)]
        newSet.add(ant)
    if len(newSet) == 8:
        return False
    return True

def ant_cube_fourth_attempt(trials):
    masks = [0b001, 0b010, 0b100]
    newSet = set()
    collisions = 0

    for trial in range(0, trials):

        newSet.clear()

        for index in range(0, 8):
            ant = index ^ masks[randint(0, 2)]
            newSet.add(ant)

        if len(newSet) != 8:
            collisions += 1

    return collisions / trials

""" Binary Search Tree testing """ 

def get_setup(type):

    base = ["from __main__ import BinarySearchTree", "from __main__ import TreeNode", "tree = BinarySearchTree()"]
    import_randint = ["from random import randint"]
    random_set = ["vals = set()", "for i in range(2**12): \n \t vals.add(randint(-99999999, 99999999))"]

    if type == "insert":
        return  base + import_randint + random_set

class BinarySearchTree:
    """Implements an unblanced binary search tree"""

    def __init__(self):
        self.root = None
        self.isEmpty = True
        self.num_items = 0

    def insert(self, newkey):
        """inserts a key into the tree"""

        #case: Tree is empty
        if self.is_empty():
            self.root = TreeNode(newkey)

        #case: Tree is not empty
        else:

            #call insert on root
            self.root.insert(newkey)

        self.isEmpty = False
        self.num_items += 1

    def find(self, key):
        """returns True if key is in the tree, False otherwise"""

        #case: Tree is empty
        if self.is_empty():
            return False

        if self.root.find(key) is not None:
            return True

        return False

    def delete(self, key):
        """deletes the node containing key from the tree"""

        #case: Tree is empty
        if self.is_empty():
            return None

        #quick verification key is in tree
        if not self.find(key):
            return None

        #case: trying to delete root node
        if self.root.key == key:

            #case: no children
            if self.root.has_no_children():

                #delete it
                self.root = None

            #case: 1 child:
            elif self.root.has_one_child():

                #get the child
                child = self.root.get_only_child()

                #set it as the new root
                self.root = child

            #case: 2 children
            else:

                #node delete method can handle this properly
                self.root.delete(key)

        #otherwise, proceed as normal
        else:

            #run the node delete function
            self.root.delete(key)

        #decrement the number of items
        self.num_items -= 1

        #update isEmpty property
        if self.size() == 0:
            self.isEmpty = True

        #return the key
        return key

    def print_tree(self):
        """print inorder the entire tree"""

        #if empty, do nothing
        if self.is_empty():
            return

        #otherwise get the lowest node and start from there
        self.root.find_min_node().inorder_print_tree()

    def is_empty(self):
        """returns True if tree is empty, else False"""

        return self.isEmpty

    def size(self):
        """returns number of elements in the tree"""

        return self.num_items

class TreeNode:

    def __init__(self, key, data=None, left=None, right=None, parent=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def insert(self, key):
        """  Insert new node with key, assumes data not present """

        
        if self.key is None:
            self.key = key
        elif key < self.key and self.left is None:
            self.left = TreeNode(key, parent=self)
        elif key < self.key:
            self.left.insert(key)
        elif key >= self.key and self.right is None:
            self.right = TreeNode(key, parent=self)
        elif key >= self.key:
            self.right.insert(key)

        '''
        if key < self.key:
            if self.left is None:
                self.left = TreeNode(key, parent=self)
                return
            self.left.insert(key)
            return
        
        if self.right is None:
            self.right = TreeNode(key, parent=self)
            return
        
        self.right.insert(key)
        '''

        '''
        if self.key is not None:
            if key < self.key:
                if self.left is None:
                    self.left = TreeNode(key, parent=self)
                else:
                   self.left.insert(key)
            elif key > self.key:
                if self.right is None:
                    self.right = TreeNode(key, parent=self)
                else:
                    self.right.insert(key)
        else:
            self.key = key
        '''

    def delete(self, key):
        """deletes a node, assume it exists, assume it is not the root (has parent)"""

        #get the node
        node_to_remove = self.find(key)

        #get its parent
        parent = node_to_remove.parent

        #case: No children
        if node_to_remove.has_no_children():

            #remove its parents link
            if node_to_remove.is_left_child_of(parent):
                parent.left = None
            else:
                parent.right = None

        #case: node_to_remove has one child 
        elif node_to_remove.has_one_child():
            
            #get the child
            child = node_to_remove.get_only_child()

            #adjust the parent pointer
            if node_to_remove.is_left_child_of(parent):
                parent.left = child
            else:
                parent.right = child

            #adjust the child pointer
            child.parent = parent

        #case: node_to_remove has 2 children
        else:

            #get smallest node in right branch
            smallKey = node_to_remove.right.find_min()

            #replace the key in current node with that one
            node_to_remove.key = smallKey

            #delete that node from the subtree
            node_to_remove.right.delete(smallKey)

    def find(self, key):

        if self.key == key:
            return self

        if self.left is not None and self.left.find(key) is not None:
            return self.left.find(key)

        if self.right is not None and self.right.find(key) is not None:
            return self.right.find(key)

        return None

    def find_min(self):
        
        if self.left is None:
            return self.key

        return self.left.find_min()

    def find_min_node(self):
        
        if self.left is None:
            return self

        return self.left.find_min_node()

    def find_max(self):
        
        if self.right is None:
            return self.key

        return self.right.find_max()

    def find_max_node(self):
        
        if self.right is None:
            return self

        return self.right.find_max_node()

    def find_successor(self):
        """returns the inorder successor node, or None if there is no successor""" 

        #case: There are right nodes available
        if self.right is not None:

            #successor is smallest node in the right branch
            return self.right.find_min_node()

        #case: We are at root with no right nodes
        elif self.parent is None:

            #This is the highest node -> no successor -> return None
            return None

        #case: No right nodes and not the root
        else:

            #start at self node
            child = self
            parent = self.parent

            #cycle through unless we reach the root
            while parent is not None:

                #this is the true condition
                if child.is_left_child_of(parent):
                    return parent

                #otherwise move up a level
                else:

                    child = parent
                    parent = parent.parent

            #There was no successor
            return None

    def inorder_print_tree(self):
        """print inorder the subtree of self"""

        #create output list
        output = []

        #start at smallest node
        current_node = self.find_min_node()

        #cycle through nodes in order and append the key to output
        while current_node is not None:
            output.append(str(current_node.key))
            current_node = current_node.find_successor()

        #print with a little formatting -> "[1, 2, 3]"
        print("[" + ", ".join(output) + "]")

    def print_levels(self, level=0):
        """inorder traversal prints list of pairs, [key, level of the node] where root is level 0"""

        #print left
        if self.left is not None:
            self.left.print_levels(level + 1)

        #print [key, level] of the current node
        print("[" + str(self.key) + ", " + str(level) + "]")

        #print right
        if self.right is not None:
            self.right.print_levels(level + 1)

    def has_no_children(self):
        """returns true if node has no children, false otherwise"""

        if self.left is None and self.right is None:
            return True

        return False

    def has_two_children(self):
        """returns true if node has two children, false otherwise"""

        if self.left is not None and self.right is not None:
            return True

        return False

    def has_one_child(self):
        """returns true if node has exactly 1 child"""

        if self.has_no_children() or self.has_two_children():
            return False

        return True

    def get_only_child(self):
        """assumes node has only 1 child, returns it"""

        if self.left is not None:
            return self.left
        else:
            return self.right

    def is_left_child_of(self, node):
        """returns true if self is left child of node, false otherwise"""

        if self is node.left:
            return True

        return False

def test_insert(tree, vals):
    for index in range(20):
        tree.insert(vals.pop())
