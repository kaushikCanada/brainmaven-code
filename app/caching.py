"""LRUCache.

A correctly constructed
LRU Cache will have its maximum capacity set at the time of the construction, and when adding
new keys that cause the capacity to be exceeded, the “least recently used” item needs to be
identified and discarded.

Key Requirements:
1. You must initialize a cache with a maximum size.
2. You must be able to put the value of a key.
3. You must be able to get the value of a key.
4. You must be able to delete a key. Attempting to delete a key that doesn’t exist is a no-op.
5. You must be able to reset the cache, which will remove all items from the cache.
6. When adding new keys that cause the capacity to be exceeded, the “least recently used” key needs to be identified and discarded.
a. Both reading and writing the value of a key are considered the use of that key.

"""

import time


class ANCHOR:

    """DUMMY Used as an identifier of the end and beginning of linked lists."""

    pass


class _LRUCacheLink(object):

    """Doubly Linked list object for the LRU cache."""

    __slots__ = ('left', 'right', 'key', 'obj')


class LRUCache(object):

    """LRU(Least Recently Used) Cache. Main class
    """

    __slots__ = ('_size', '_anchor', '_ldict')

    def __init__(self, size):
        """Constructor.

        :param size: Static size of LRU cache.
        """
        if size < 2:
            raise ValueError('Cache size minimum 2')

        self._size = size

        # Anchor is the beginning of the cache list.
        self._anchor = _LRUCacheLink()
        self._anchor.key = ANCHOR
        self._anchor.left = self._anchor
        self._anchor.right = self._anchor

        # Map of all cache elements for fast access.
        self._ldict = {}

    def reset(self):
        """Reset all cache data."""
        self._ldict.clear()
        self._anchor.left = self._anchor
        self._anchor.right = self._anchor

    def __len__(self):
        return len(self._ldict)

    def __getitem__(self, key):
        return self._move_to_top(key).obj

    def __setitem__(self, key, obj):
        """Add new item into cache."""

        if key in self._ldict:
            # Unlink item and put it as fresh element.
            item = self._move_to_top(key)
            item.obj = obj
        else:
            if len(self._ldict) >= self._size:
                # Reuse item that is going to be removed.
                new_item = self._remove_item(self._anchor.left.key)
            else:
                new_item = _LRUCacheLink()
            new_item.obj = obj
            new_item.key = key
            self._link_item_as_top(new_item)
            self._ldict[key] = new_item

    def _move_to_top(self, key):
        """Moves element to the top of the list and returns associated item."""
        item = self._ldict[key]
        l_item = item.left
        r_item = item.right
        l_item.right = r_item
        r_item.left = l_item
        self._link_item_as_top(item)
        return item

    def _link_item_as_top(self, item):
        """Set linked list item to the top of the list."""
        anchor = self._anchor
        anchor_r = anchor.right
        item.left = anchor
        item.right = anchor_r
        anchor_r.left = item
        anchor.right = item

    def _remove_item(self, key):
        """Removes item from the linked list and returns associated item."""
        item = self._ldict.pop(key)
        l_item = item.left
        r_item = item.right
        l_item.right = r_item
        r_item.left = l_item
        return item

    __delitem__ = _remove_item

    def __repr__(self):
        all_items = list()
        curr = self._anchor.left
        while curr.key != ANCHOR:
            all_items.append((curr.key, curr.obj))
            curr = curr.left
        return repr(all_items)

    def has_key(self, key):
        """Check if cache has the specified element in the storage.

        :param key: Object key.
        :return: True if object exists, otherwise False.
        """
        return key in self._ldict

    def keys(self):
        """Return cached object keys."""
        return self._ldict.keys()

    def make_copy(self):
        """Make a copy of cache storage.

        :return: Dictionary of cached data.
        """
        res = {}
        for item in self._ldict.itervalues():
            res[item.key] = item.obj
        return res

    def pop(self, key):
        """Remove specified key and return the corresponding value."""
        return self._remove_item(key).obj

    def get(self, key, default=None):
        """Get data from cache.

        :param key: Object key.
        :param default: Default value if object not found.
        :return: Object associated with key.
        """

        if key in self._ldict:
            return self._move_to_top(key).obj
        else:
            return default

