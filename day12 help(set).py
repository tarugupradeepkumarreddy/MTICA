Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: C:/Users/User/Desktop/pythonpractice43/day12/day12 set(difference_update)4.py
{50, 20, 40, 10, 30}

= RESTART: C:/Users/User/Desktop/pythonpractice43/day12/day12 set(difference_update)4.py
{50, 20, 40, 10, 30}

= RESTART: C:/Users/User/Desktop/pythonpractice43/day12/day12 set(difference_update)4.py
{50, 40}

= RESTART: C:/Users/User/Desktop/pythonpractice43/day12/day12 set(difference_symmetric)5.py
Traceback (most recent call last):
  File "C:/Users/User/Desktop/pythonpractice43/day12/day12 set(difference_symmetric)5.py", line 3, in <module>
    set1.difference_symmetric(set2)
AttributeError: 'set' object has no attribute 'difference_symmetric'

= RESTART: C:/Users/User/Desktop/pythonpractice43/day12/day12 set(difference_symmetric)5.py
{50, 20, 40, 10, 30}
{50, 20, 40, 10, 30}
{50, 20, 40, 10, 30}
set1={10,20,30,40,50};
set2={30,40,50,60,70}
SyntaxError: multiple statements found while compiling a single statement
set1={10,20,30,40,50};set2={30,40,50,60,70}
set1
{50, 20, 40, 10, 30}
set2
{50, 70, 40, 60, 30}
set1-set2
{10, 20}
set2-set1
{60, 70}

= RESTART: C:/Users/User/Desktop/pythonpractice43/day12/day12 set(difference_symmetric)5.py
{50, 20, 40, 10, 30}

= RESTART: C:/Users/User/Desktop/pythonpractice43/day12/day12 set(display two items)5.py
two sets have no items in common
{40, 50, 30}

= RESTART: C:/Users/User/Desktop/pythonpractice43/day12/day12 set(display two items)5.py
two sets have no items in common
{40, 50, 30}

= RESTART: C:/Users/User/Desktop/pythonpractice43/day12/day12 set(display two items)5.py
two sets have no items in common
{40, 50, 30}

= RESTART: C:/Users/User/Desktop/pythonpractice43/day12/day12 set(display two items)5.py
two sets have no items in common
{40, 50, 30}

= RESTART: C:/Users/User/Desktop/pythonpractice43/day12/day12 set(add two set1)7.py
{20, 70, 10, 60}

= RESTART: C:/Users/User/Desktop/pythonpractice43/day12/day12 set(remove items)7.py
{40, 50, 30}

= RESTART: C:/Users/User/Desktop/pythonpractice43/day12/day12 set(remove items)7.py
{40, 50, 30}
help(set)
Help on class set in module builtins:

class set(object)
 |  set() -> new empty set object
 |  set(iterable) -> new set object
 |  
 |  Build an unordered collection of unique elements.
 |  
 |  Methods defined here:
 |  
 |  __and__(self, value, /)
 |      Return self&value.
 |  
 |  __contains__(...)
 |      x.__contains__(y) <==> y in x.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iand__(self, value, /)
 |      Return self&=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __ior__(self, value, /)
 |      Return self|=value.
 |  
 |  __isub__(self, value, /)
 |      Return self-=value.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __ixor__(self, value, /)
 |      Return self^=value.
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __or__(self, value, /)
 |      Return self|value.
 |  
 |  __rand__(self, value, /)
 |      Return value&self.
 |  
 |  __reduce__(...)
 |      Return state information for pickling.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __ror__(self, value, /)
 |      Return value|self.
 |  
 |  __rsub__(self, value, /)
 |      Return value-self.
 |  
 |  __rxor__(self, value, /)
 |      Return value^self.
 |  
 |  __sizeof__(...)
 |      S.__sizeof__() -> size of S in memory, in bytes
 |  
 |  __sub__(self, value, /)
 |      Return self-value.
 |  
 |  __xor__(self, value, /)
 |      Return self^value.
 |  
 |  add(...)
 |      Add an element to a set.
 |      
 |      This has no effect if the element is already present.
 |  
 |  clear(...)
 |      Remove all elements from this set.
 |  
 |  copy(...)
 |      Return a shallow copy of a set.
 |  
 |  difference(...)
 |      Return the difference of two or more sets as a new set.
 |      
 |      (i.e. all elements that are in this set but not the others.)
 |  
 |  difference_update(...)
 |      Remove all elements of another set from this set.
 |  
 |  discard(...)
 |      Remove an element from a set if it is a member.
 |      
 |      Unlike set.remove(), the discard() method does not raise
 |      an exception when an element is missing from the set.
 |  
 |  intersection(...)
 |      Return the intersection of two sets as a new set.
 |      
 |      (i.e. all elements that are in both sets.)
 |  
 |  intersection_update(...)
 |      Update a set with the intersection of itself and another.
 |  
 |  isdisjoint(...)
 |      Return True if two sets have a null intersection.
 |  
 |  issubset(...)
 |      Report whether another set contains this set.
 |  
 |  issuperset(...)
 |      Report whether this set contains another set.
 |  
 |  pop(...)
 |      Remove and return an arbitrary set element.
 |      Raises KeyError if the set is empty.
 |  
 |  remove(...)
 |      Remove an element from a set; it must be a member.
 |      
 |      If the element is not a member, raise a KeyError.
 |  
 |  symmetric_difference(...)
 |      Return the symmetric difference of two sets as a new set.
 |      
 |      (i.e. all elements that are in exactly one of the sets.)
 |  
 |  symmetric_difference_update(...)
 |      Update a set with the symmetric difference of itself and another.
 |  
 |  union(...)
 |      Return the union of sets as a new set.
 |      
 |      (i.e. all elements that are in either set.)
 |  
 |  update(...)
 |      Update a set with the union of itself and others.
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  __class_getitem__(...) from builtins.type
 |      See PEP 585
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

