import unittest
import uniqueness

test_1_list = [1, 2, 3, 4, 5]
test_1_expected_result = True

test_2_list = [1, 2, 3, 4, 5, 5]
test_2_expected_result = False

class TestUniquenessFunction(unittest.TestCase):

    def test_uniqueness(self):

        test_1_result = uniqueness.isUnique(test_1_list)
        self.assertEqual(test_1_result, test_1_expected_result)

        test_2_result = uniqueness.isUnique(test_2_list)
        self.assertEqual(test_2_result, test_2_expected_result)


if __name__ == '__main__':

    unittest.main()