#!/usr/bin/env konira
import hw0

describe "Problem 1":

    it "returns list of odd numbers":
        test_list = [_ for _ in range(10)]
        num = 2
        assert hw0.myFilter(test_list, num) == [_ for _ in range(1, 10, 2)]


describe "Problem 2":

    it "returns a list of lists that for each element x contain 1,2,..,x":
        L = [1,2,3,4,5,6,7,8,9,10]
        result = [[1], [1,2], [1,2,3], [1,2,3,4], [1,2,3,4,5], [1,2,3,4,5,6],
                  [1,2,3,4,5,6,7], [1,2,3,4,5,6,7,8], [1,2,3,4,5,6,7,8,9],
                  [1,2,3,4,5,6,7,8,9,10]]
        assert hw0.myLists(L) == result

describe "Problem 3":

    it "g o f":
        f = {0: 'a', 1: 'b', 2: 'c', 3: 'd'}
        g = {'a': 'apple', 'b': 'banana', 'c': 'coconut', 'd': 'durian'}
        result = {0: 'apple', 1: 'banana', 2: 'coconut', 3: 'durian'}
        assert hw0.myFunctionComposition(f, g) == result
