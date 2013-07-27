import unittest
import hw2

class HW2Test(unittest.TestCase):
    def test_vec_select(self):
        D = {'a', 'b', 'c'}
        v1 = hw2.Vec(D, {'a': 1})
        v2 = hw2.Vec(D, {'a': 0, 'b': 1})
        v3 = hw2.Vec(D, {        'b': 2})
        v4 = hw2.Vec(D, {'a': 10, 'b': 10})
        assert hw2.vec_select([v1, v2, v3, v4], 'a') == [hw2.Vec(D, {'b': 1}), hw2.Vec(D, {'b': 2})]

    def test_vec_sum(self):
        D = {'a','b','c'}
        v1 = hw2.Vec(D, {'a': 1})
        v2 = hw2.Vec(D, {'a': 0, 'b': 1})
        v3 = hw2.Vec(D, {        'b': 2})
        v4 = hw2.Vec(D, {'a': 10, 'b': 10})
        assert hw2.vec_sum([v1, v2, v3, v4], D) == hw2.Vec(D, {'b': 13, 'a': 11})

    def test_vec_select_sum(self):
        D = {'a','b','c'}
        v1 = hw2.Vec(D, {'a': 1})
        v2 = hw2.Vec(D, {'a': 0, 'b': 1})
        v3 = hw2.Vec(D, {        'b': 2})
        v4 = hw2.Vec(D, {'a': 10, 'b': 10})
        assert hw2.vec_select_sum([v1, v2, v3, v4], 'a', D) == hw2.Vec(D, {'b': 3})

    def test_scale_vecs(self):
        v1 = hw2.Vec({1,2,3}, {2: 9})
        v2 = hw2.Vec({1,2,4}, {1: 1, 2: 2, 4: 8})
        assert hw2.scale_vecs({3: v1, 5: v2}) == [hw2.Vec({1,2,3},{2: 3.0}), hw2.Vec({1,2,4},{1: 0.2, 2: 0.4, 4: 1.6})]
