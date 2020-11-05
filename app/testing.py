import unittest2

from caching import LRUCache


class TestLRUCache(unittest2.TestCase):

    """Unit tests for shared LRU cache library."""

    def test_lru_remember_everything(self):
        cache = LRUCache(5)
        cache[1] = '1'
        cache[2] = '2'
        cache[3] = '3'
        self.assertEqual("[(1, '1'), (2, '2'), (3, '3')]", str(cache))
        self.assertEqual(3, len(cache))

    def test_lru_keep_fresh(self):
        cache = LRUCache(3)
        cache[1] = '1'
        cache[2] = '2'
        cache[3] = '3'
        cache[4] = '4'
        self.assertEqual("[(2, '2'), (3, '3'), (4, '4')]", str(cache))
        self.assertEqual(3, len(cache))

    def test_lru_fresh_on_access(self):
        cache = LRUCache(3)
        cache[1] = '1'
        cache[2] = '2'
        cache[3] = '3'

        # Just access to first element.
        _ = cache[1]
        self.assertEqual("[(2, '2'), (3, '3'), (1, '1')]", str(cache))
        self.assertEqual(3, len(cache))

    def test_lru_get_unexisting(self):
        cache = LRUCache(3)
        try:
            _ = cache[1]
        except KeyError:
            pass

    def test_get_make_copy_and_keys(self):
        cache = LRUCache(3)
        cache[1] = '1'
        cache[2] = '2'
        cache[3] = '3'
        self.assertEqual({1: '1', 2: '2', 3: '3'}, cache.make_copy())
        keys = cache.keys()
        # Sort keys to make sure they are in the same order on all platforms.
        keys.sort()
        self.assertEqual([1, 2, 3], keys)
        self.assertEqual(3, len(cache))

    def test_reset(self):
        cache = LRUCache(3)
        cache[1] = '1'
        cache[2] = '2'
        cache[3] = '3'
        self.assertEqual(3, len(cache))
        cache.reset()
        self.assertEqual(0, len(cache))

    def test_del_element(self):
        cache = LRUCache(4)
        cache[1] = '1'
        cache[2] = '2'
        cache[3] = '3'
        cache[4] = '4'
        del cache[3]
        self.assertEqual("[(1, '1'), (2, '2'), (4, '4')]", str(cache))
        self.assertEqual(3, len(cache))

    def test_get_element(self):
        cache = LRUCache(3)
        cache[1] = '1'
        cache[2] = '2'
        cache[3] = '3'
        self.assertEqual('test', cache.get(11, 'test'))
        self.assertEqual("[(1, '1'), (2, '2'), (3, '3')]", str(cache))
        self.assertEqual('1', cache.get(1, 'test'))
        self.assertEqual("[(2, '2'), (3, '3'), (1, '1')]", str(cache))
        self.assertEqual(3, len(cache))

    def test_pop_element(self):
        cache = LRUCache(3)
        cache[1] = '1'
        cache[2] = '2'
        cache[3] = '3'
        self.assertEqual("[(1, '1'), (2, '2'), (3, '3')]", str(cache))
        self.assertEqual('1', cache.pop(1))
        self.assertEqual("[(2, '2'), (3, '3')]", str(cache))
        self.assertEqual(2, len(cache))
        self.assertRaises(KeyError, cache.pop, 1)


if __name__ == '__main__':
    unittest2.main()