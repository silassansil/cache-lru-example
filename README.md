# Cache LRU Example
Example how to implements cache LRU using python.

LRU cache stand for **Least Recently Used** Cache. which evict least recently used entry. As Cache purpose is to provide fast and efficient way of retrieving data. It need to meet certain requirement.
### Some of the Requirement are
* Fixed Size: Cache needs to have some bounds to limit memory usages.
* Fast Access: Cache Insert and lookup operation should be fast , preferably O(1) time.
* Replacement of Entry in case , Memory Limit is reached: A cache should have efficient algorithm to evict the entry when memory is full.
