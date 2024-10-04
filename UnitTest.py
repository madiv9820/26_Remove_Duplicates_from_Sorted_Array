from Solution import Solution
import unittest
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.__testCases = {
            1: {'nums': [1,1,2], 'output_size': 2, 'output_nums': [1,2]},
            2: {'nums': [0,0,1,1,1,2,2,3,3,4],
                'output_size': 5, 'output_nums': [0,1,2,3,4]}
        }
        self.__obj = Solution()
        return super().setUp()

    def test_Case1(self):
        case = self.__testCases[1]
        nums, output_size, output_nums = case.values()
        res = self.__obj.removeDuplicates(nums)
        self.assertIsInstance(res, int)
        self.assertEqual(res, output_size)
        self.assertEqual(nums[:res], output_nums)

    def test_Case2(self):
        case = self.__testCases[2]
        nums, output_size, output_nums = case.values()
        res = self.__obj.removeDuplicates(nums)
        self.assertIsInstance(res, int)
        self.assertEqual(res, output_size)
        self.assertEqual(nums[:res], output_nums)

if __name__ == '__main__':
    unittest.main()