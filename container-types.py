'''
Container Types

Ordered sequences, fast index access, repeatable values

list -> [1,5,9], ["x", 11, 8.9], ["mot"] -> []
tuple -> (1,5,9), ("mot",) -> Non modifiable values (immutable) -> ()
expression with only comas

str, bytes -> ordered sequences of chars/bytes -> "", b""

tuple1 = 11, "y", 7.4
print(tuple1)

tuple1 = ("mot",)
print(tuple1)

The reason why you need a comma , for a single tuple is that "tuple is an object delimited by comma , ", not "an object enclosed in parentheses () ". Note that it is actually the comma which makes a tuple, not the parentheses.
'''
'''
key containers -> {}
no a priori order, fast key access, each key is unique

dict -> key/value associations {"key" : "value"}
print(dict(a=3, b=4, k="v"))
empty dict -> {}, dict()

set (collection) -> {"key1", "key2"}
{1,9,3,0}
keys = hashable values (base types, immutables)
frozenset -> immutable set
empty set -> set()
'''
print({
    1: "one",
    3: "three",
    2: "two",
    3.14: "π"
})
print({1, 9.0, "three", False, (1, 2, 3), frozenset({1, 2, 3})})
