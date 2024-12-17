def has_cycle(link):
    """
    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    """
    lnk_ptr = link.rest
    while not lnk_ptr is Link.empty:
        if lnk_ptr is link:
            return True
        lnk_ptr = lnk_ptr.rest
    return False 

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

    while not link is Link.empty:
        if link.first == sub_link.first:
            sub_link = sub_link.rest
            if sub_link is Link.empty:
                return True
        link = link.rest
    return False

def remove_duplicates(lnk):
    """
    >>> lnk = Link(1, Link(1, Link(1, Link(1, Link(5)))))
    >>> remove_duplicates(lnk)
    >>> lnk
    Link(1, Link(5))
    """

    lnk_ptr = lnk.rest
    while lnk_ptr is not Link.empty:
        if lnk.first == lnk_ptr.first:
            lnk_ptr = lnk_ptr.rest
        else:
            lnk.rest = lnk_ptr
            lnk = lnk.rest
            lnk_ptr = lnk_ptr.rest
    lnk.rest = lnk_ptr

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
    next_lnk = lnk.rest

    while next_lnk is not Link.empty:
        temp = next_lnk.rest
        next_lnk.rest = prev
        prev = next_lnk
        next_lnk = temp 
    
    lnk.rest = Link.empty
    return prev

# Link 

class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(repr(self.first), rest_str)

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'