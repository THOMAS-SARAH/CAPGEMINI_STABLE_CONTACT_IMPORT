
import unittest
from solution import unique_contacts


# Flawed starting implementation used for regression comparison
def flawed_unique_contacts(ids: list[str]) -> list[str]:
    return sorted(set(ids))


class TestUniqueContacts(unittest.TestCase):

    def test_example_1_order_preservation(self):
        self.assertEqual(unique_contacts(["b", "a", "b", "c", "a"]), ["b", "a", "c"])

    def test_example_2_empty_list(self):
        self.assertEqual(unique_contacts([]), [])

    def test_example_3_case_and_empty_string(self):
        self.assertEqual(unique_contacts(["A", "a", "A", ""]), ["A", "a", ""])

    def test_input_immutability(self):
        original = ["b", "a", "b", "c"]
        input_copy = list(original)
        unique_contacts(input_copy)
        self.assertEqual(input_copy, original)

    def test_regression_flawed_sorting_bug(self):
        input_ids = ["b", "a"]
        expected = ["b", "a"]
        # Correct implementation passes
        self.assertEqual(unique_contacts(input_ids), expected)
        # Flawed starting code fails (returns ['a', 'b'])
        self.assertNotEqual(flawed_unique_contacts(input_ids), expected)


if __name__ == "__main__":
    unittest.main()
