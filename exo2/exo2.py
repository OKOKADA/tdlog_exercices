"""
Complete the solution so that it returns true if the first argument(string)
passed in ends with the 2nd argument (also a string).

Examples:

    solution('abc', 'bc') # returns true
    solution('abc', 'd') # returns false
"""

"""
Create unit test using those cases:
fixed_tests_True = (
    ( "samurai", "ai"    ),
    ( "ninja",   "ja"    ),
    ( "sensei",  "i"     ),
    ( "abc",     "abc"   ),
    ( "abcabc",  "bc"    ),
    ( "fails",   "ails"  ),
)

fixed_tests_False = (
    ( "sumo",    "omo"   ),
    ( "samurai", "ra"    ),
    ( "abc",     "abcd"  ),
    ( "ails",    "fails" ),
    ( "this",    "fails" ),
    ( "spam",    "eggs"  )
)
"""


def solution(string, ending):
    return string.endswith(ending)

# Unit tests


fixed_tests_False = (
    ("sumo", "omo"),
    ("samurai", "ra"),
    ("abc", "abcd"),
    ("ails", "fails"),
    ("this", "fails"),
    ("spam", "eggs"),
)
import unittest

# Testing function
class TestSolutionFunction(unittest.TestCase):
    def test_solution_function_true(self):
        fixed_tests_True = [
        ("samurai", "ai"),
        ("ninja", "ja"),
        ("sensei", "i"),
        ("abc", "abc"),
        ("abcabc", "bc"),
        ("fails", "ails"),]

        for mot,fin in fixed_tests_True:
            with self.subTest(string=mot,ending=fin):
                self.assertTrue(solution(mot,fin))

    def test_solution_function_false(self):
        fixed_tests_False = [
    ("sumo", "omo"),
    ("samurai", "ra"),
    ("abc", "abcd"),
    ("ails", "fails"),
    ("this", "fails"),
    ("spam", "eggs"),
]
        for mot,fin in fixed_tests_False:
            with self.subTest(string=mot,ending=fin):
                self.assertFalse(solution(mot,fin))  
#         for test in fixed_tests_False:
#             self.assertFalse(solution(*test))
# def run_tests():
#     for test in fixed_tests_True:
#         assert solution(*test) == True, f"Test failed for {test}"
    
#     for test in fixed_tests_False:
#         assert solution(*test) == False, f"Test failed for {test}"
#     print("All tests passed!")

# # Run the tests
# run_tests()

if __name__ == '__main__':
    unittest.main()
