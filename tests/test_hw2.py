import unittest

from hw2 import *

from GF2 import one

class HW2TestCase(unittest.TestCase):


    def test_vec_select(self):
        D = {'a', 'b', 'c'}
        v1 = Vec(D, {'a': 1})
        v2 = Vec(D, {'a': 0, 'b': 1})
        v3 = Vec(D, {        'b': 2})
        v4 = Vec(D, {'a': 10, 'b': 10})
        assert vec_select([v1, v2, v3, v4], 'a') == [Vec(D, {'b': 1}), Vec(D, {'b': 2})]

    def test_vec_sum(self):
        D = {'a','b','c'}
        v1 = Vec(D, {'a': 1})
        v2 = Vec(D, {'a': 0, 'b': 1})
        v3 = Vec(D, {        'b': 2})
        v4 = Vec(D, {'a': 10, 'b': 10})
        assert vec_sum([v1, v2, v3, v4], D) == Vec(D, {'b': 13, 'a': 11})

    def test_vec_select_sum(self):
        D = {'a','b','c'}
        v1 = Vec(D, {'a': 1})
        v2 = Vec(D, {'a': 0, 'b': 1})
        v3 = Vec(D, {        'b': 2})
        v4 = Vec(D, {'a': 10, 'b': 10})
        assert vec_select_sum([v1, v2, v3, v4], 'a', D) == Vec(D, {'b': 3})

    def test_scale_vecs(self):
        v1 = Vec({1,2,3}, {2: 9})
        v2 = Vec({1,2,4}, {1: 1, 2: 2, 4: 8})
        assert scale_vecs({3: v1, 5: v2}) == [Vec({1,2,3},{2: 3.0}), Vec({1,2,4},{1: 0.2, 2: 0.4, 4: 1.6})]

    def test_GF_span(self):
        D = {'a', 'b', 'c'}
        L = [Vec(D, {'a': one, 'c': one}), Vec(D, {'b': one})]
        assert len(GF2_span(D, L)) == 4
        assert Vec(D, {}) in GF2_span(D, L)
        assert Vec(D, {'b': one}) in GF2_span(D, L)
        assert Vec(D, {'a':one, 'c':one}) in GF2_span(D, L)
        assert Vec(D, {x:one for x in D}) in GF2_span(D, L)
