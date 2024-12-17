# Q2: Sum Nums

def sum_nums(s):
    """
    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_nums(a)
    14
    """
    if s.rest is Link.empty:
        return s.first
    return s.first + sum_nums(s.rest)
    
# Q5: (Tutorial) Multiply Lnks

def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest is Link.empty
    True
    """
    total = 1
    for i in range(len(lst_of_lnks)):
        if lst_of_lnks[i] is Link.empty:
            return Link.empty
        total *= lst_of_lnks[i].first
        lst_of_lnks[i] = lst_of_lnks[i].rest

    return Link(total, multiply_lnks(lst_of_lnks))

# Q6: (Tutorial) Flip Two

def flip_two(s):
    """
    >>> one_lnk = Link(1)
    >>> flip_two(one_lnk)
    >>> one_lnk
    Link(1)
    >>> lnk = Link(1, Link(2, Link(3, Link(4, Link(5)))))
    >>> flip_two(lnk)
    >>> lnk
    Link(2, Link(1, Link(4, Link(3, Link(5)))))
    """
    if s.rest is Link.empty:
        return None
    
    s.first, s.rest.first = s.rest.first, s.first
    flip_two(s.rest.rest)

# Q7: Make Even

def make_even(t):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
    >>> make_even(t)
    >>> t.label
    2
    >>> t.branches[0].branches[0].label
    4
    """
    if t.label % 2 == 1:
        t.label += 1
    for branch in t.branches:
        make_even(branch)    


# Q8. Has Cycle


def has_cycle(link):
    """
    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    """

    current = link.rest

    while current is not Link.empty:
        if current is link:
            return True
        current = current.rest
    return False 



# Q9. Seq in link

def seq_in_link(link, sub_link):
    """
    >>> lnk1 = Link(1, Link(2, Link(3, Link(4))))
    >>> lnk2 = Link(1, Link(3))
    >>> lnk3 = Link(4, Link(3, Link(2, Link(1))))
    >>> seq_in_link(lnk1, lnk2)
    True
    >>> seq_in_link(lnk1, lnk3)
    False
    """
    if sub_link is Link.empty:
        return True

    while link is not Link.empty:
        if link.first == sub_link.first:
            sub_link = sub_link.rest
            if sub_link is Link.empty:
                return True
        link = link.rest
    return False


# Q10. Remove duplicates

def remove_duplicates(lnk):
    """
    >>> lnk = Link(1, Link(1, Link(1, Link(1, Link(5)))))
    >>> remove_duplicates(lnk)
    >>> lnk
    Link(1, Link(5))
    """

    current = lnk.rest
    while current is not Link.empty:
        if lnk.first == current.first:
            current = current.rest
        else:
            lnk.rest = current
            lnk = lnk.rest
            current = current.rest
    lnk.rest = current
            
# Q11. Remove duplicates

def reverse(lnk):
    """
    >>> a = Link(1, Link(2, Link(3)))
    >>> r = reverse(a)
    >>> r.first
    3
    >>> r.rest.first
    2
    """    
    prev = lnk
    succ = lnk.rest

    while succ is not Link.empty:
        temp = succ.rest 
        succ.rest = prev
        prev = succ
        succ = temp 
    
    lnk.rest = Link.empty
    return prev



class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'
    
class Tree:
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = branches

    def is_leaf(self):
        return not self.branches