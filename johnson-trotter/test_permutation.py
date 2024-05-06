import unittest
import permutation

test_n = [2, 3]
test_permutations = []

test_permutations.append([[1,2], [2,1]])
test_permutations.append([[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])

class TestPermutationFunction(unittest.TestCase):

    def test_johnson_trotter(self):

        for i in range(len(test_n)):
            permutations = permutation.johnson_trotter(test_n[i])
            self.assertCountEqual(permutations, test_permutations[i])

if __name__ == '__main__':

    unittest.main()