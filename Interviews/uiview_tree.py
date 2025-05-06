# Amplitude 2025

from __future__ import annotations
from itertools import zip_longest

# For mobile apps, views are the fundamental building blocks of your app's user interface.
# You are given a UIView class, please implement following APIs.
class UIView:

    # Constructor
    # Tag is how you want name this View. It could be a string, 'A' or 'B' or even 'XYZ'
    def __init__(self, tag = ""):
        self.tag = tag
        self.index = -1
        self.sub_views = []
        self.parent = None
        self.lineage = None
        
    # Each view will contains multiple views. This function will keep the relations between
    # views and it subviews.
    # def addSubview(self, view: 'UIView'):
    def addSubview(self, view: UIView):
        self.sub_views.append(view)
        # minus one to get zero index from length of arary
        view.setIndex(len(self.sub_views) - 1)
        view.setParent(self)
    
    # Will return the tag (String)
    def description(self):
        return self.tag
    
    # Will return its index (Integer)
    def getIndex(self):
        return self.index

    def setIndex(self, index):
        self.index = index
    
    # Get its parent view (UIView)
    def getParent(self):
        return self.parent
        
    def setParent(self, parent: UIView):
        self.parent = parent

    def getLineage(self):

        if self.lineage:
            # If lineage is already calculated, return it
            # print("Lineage already calculated")
            return self.lineage

        lineage = [self.getIndex()]

        curr = self

        while curr.getParent():
            lineage.append(self.getParent().getIndex())
            curr = curr.getParent()
        
        self.lineage = lineage

        return lineage
    
    def getDepth(self):
        if self.lineage:
            return len(self.lineage) - 1
        else:
            # If lineage is not calculated, calculate it
            self.lineage = self.getLineage()
            return len(self.lineage) - 1


# def compare_views(a: UIView, b: UIView) -> bool:

#     # Add parent comparison

#     depth_a = 0
#     index_a = a.getIndex()
#     a_parent_indexes = []
#     depth_b = 0
#     index_b = b.getIndex()
#     b_parent_indexes = []

#     while a.getParent():
#         depth_a += 1
#         a = a.getParent()
#         a_parent_indexes.append(a.getIndex())
    
#     while b.getParent():
#         depth_b += 1
#         b = b.getParent()
#         b_parent_indexes.append(b.getIndex())

#     while a_parent_indexes and b_parent_indexes:
#         if a_parent_indexes[-1] != b_parent_indexes[-1]:
#             return False
#         a_parent_indexes.pop()
#         b_parent_indexes.pop()

#     if a_parent_indexes or b_parent_indexes:
#         return False

#     if index_a != index_b:
#         return False

#     return True

def compare_views(a: UIView, b: UIView) -> bool:
 
        a_lineage = a.getLineage()
        b_lineage = b.getLineage()

        if len(a_lineage) != len(b_lineage):
            return False
        
        for i in range(len(a_lineage)):
            if a_lineage[i] != b_lineage[i]:
                return False

        # common = [(i,j) for i, j in zip_longest(a_lineage, b_lineage) if i == j]

        # if len(common) != len(a_lineage) or len(common) != len(b_lineage):
        #     return False

        return True

def find_clone_target(target: UIView, clone_root: UIView) -> UIView:

    q = [clone_root]

    while q:
        clone = q.pop()

        # if clone.description() == target.description():
        # if compare_views(target, clone):
        if compare_views(target, clone):
            return clone
        else:
            q.extend(clone.sub_views)
    
    return None

view_a = UIView('a')
view_b = UIView('b')
view_c = UIView('c')
view_d = UIView('d')
view_e = UIView('e')
view_f = UIView('f')
view_g = UIView('g')
view_h = UIView('h')

view_a.addSubview(view_b)
view_a.addSubview(view_c)

view_b.addSubview(view_d)
view_b.addSubview(view_e)

view_d.addSubview(view_f)
view_d.addSubview(view_g)
view_d.addSubview(view_h)


# Get a views parent (not set)
assert view_a.getParent() is None
# Get a views parent (set)
assert view_b.getParent() == view_a

# Get a views description
assert view_a.description() == 'a'

# Get a views index (not sub_view)
assert view_a.getIndex() == -1

# Get a views index (sub_view) 1
assert view_b.getIndex() == 0
# Get a views index (sub_view) 2
assert view_c.getIndex() == 1


clone_a = UIView("a")
clone_b = UIView("b")
clone_c = UIView("c")
clone_d = UIView("d")
clone_e = UIView("e")
clone_f = UIView("f")
clone_g = UIView("g")
clone_h = UIView("h")

clone_a.addSubview(clone_b)
clone_a.addSubview(clone_c)

clone_b.addSubview(clone_d)
clone_b.addSubview(clone_e)

clone_d.addSubview(clone_f)
clone_d.addSubview(clone_g)
clone_d.addSubview(clone_h)

# return1 = find_clone_target(target = view_a, clone_root = clone_a)
# print(return1.description())
assert find_clone_target(target = view_a, clone_root = clone_a) == clone_a
assert find_clone_target(target = view_g, clone_root = clone_a) == clone_g
assert find_clone_target(target = view_g, clone_root = clone_a) == clone_g
assert find_clone_target(target = view_g, clone_root = clone_a) == clone_g
assert find_clone_target(target = view_g, clone_root = clone_a) == clone_g
assert find_clone_target(target = view_g, clone_root = clone_a) == clone_g


