import unittest
from main import max_sum, read_file_to_triangle

easyTriangle = [[3],
                [7, 4],
                [2, 4, 6],
                [8, 5, 9, 3]]

negEasyTriangle = [[-3],
                [-7, -4],
                [-2, -4, -6],
                [-8, -5, -9, -3]]

mixedEasyTriangle = [[5],
                     [-3,7],
                     [28,5,-8]]

def brute_force_max_sum(triangle: list[list [int]], pos_x: int, pos_y: int, carryover:int):
   if pos_y==len(triangle)-1:
       return carryover
   else:
        return max(brute_force_max_sum(triangle, pos_x, pos_y + 1), (carryover + triangle[pos_x][pos_y + 1]), brute_force_max_sum(triangle, pos_x + 1, pos_y + 1), (carryover + triangle[pos_x + 1][pos_y + 1]))


def bf_max_sum(triangle: list[list [int]]):
    if len(triangle) < 1:
        raise ValueError("empty triangle input is not supported")
    return brute_force_max_sum(triangle,0,0,triangle[0][0])
class TestMaxPathSum(unittest.TestCase):

    def test_easy_cases(self):
        self.assertEqual(max_sum(easyTriangle),23)
        self.assertEqual(bf_max_sum(easyTriangle), 23)
        self.assertEqual(max_sum(negEasyTriangle), -16)
        self.assertEqual(bf_max_sum(negEasyTriangle), -16)
        self.assertEqual(max_sum(mixedEasyTriangle), 30)
        self.assertEqual(bf_max_sum(mixedEasyTriangle), 30)

    def test_triangle_one_element(self):
        self.assertEqual(max_sum([[7]]),7)
        self.assertEqual(bf_max_sum([[7]]), 7)
        self.assertEqual(max_sum([[10]]), 10)
        self.assertEqual(bf_max_sum([[10]]), 10)
        self.assertEqual(max_sum([[-3]]), -3)
        self.assertEqual(bf_max_sum([[-3]]), -3)

    def test_empty_triangle(self):
        with self.assertRaises(ValueError):
            max_sum([])
        with self.assertRaises(ValueError):
            bf_max_sum([])

    def test_complicated_triangle(self):
        testTriangle=read_file_to_triangle("triangleTwentyLines.txt")
        ex01Triangle=read_file_to_triangle("ex01.txt")
        self.assertEqual(max_sum(testTriangle), bf_max_sum(testTriangle))
        self.assertEqual(max_sum(ex01Triangle), bf_max_sum(ex01Triangle))

class TestReadFileToTriangle(unittest.TestCase):

    def test_empty_triangle(self):
        self.assertEqual(read_file_to_triangle("empty.txt"),[])

    def test_small_triangles(self):
        triangle_four_lines_pos=[[5], [34, 5], [345, 234, 64], [456, 634, 23, 45]]
        self.assertEqual(read_file_to_triangle("triangleFourLinesPos.txt"),triangle_four_lines_pos)
        triangle_four_lines_neg= [[-5], [-34, -5], [-345, -234, -64], [-456, -634, -23, -45]]
        self.assertEqual(read_file_to_triangle("triangleFourLinesNeg.txt"),triangle_four_lines_neg)



    def test_deformed_triangle(self):
        with self.assertRaises(ValueError):
            read_file_to_triangle("triangleDeformedToMany.txt")
        with self.assertRaises(ValueError):
            read_file_to_triangle("triangleDeformedNotEnough.txt")

