import unittest
from string_reversal import reverse_string


class TestStringReversal(unittest.TestCase):
    """Comprehensive tests for the reverse_string function."""

    def test_normal_string(self):
        """Test reversing a normal string."""
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("world"), "dlrow")
        self.assertEqual(reverse_string("Python"), "nohtyP")

    def test_empty_string(self):
        """Test reversing an empty string."""
        self.assertEqual(reverse_string(""), "")

    def test_single_character(self):
        """Test reversing a single character."""
        self.assertEqual(reverse_string("a"), "a")
        self.assertEqual(reverse_string("Z"), "Z")
        self.assertEqual(reverse_string("5"), "5")

    def test_two_characters(self):
        """Test reversing two characters."""
        self.assertEqual(reverse_string("ab"), "ba")
        self.assertEqual(reverse_string("xy"), "yx")

    def test_palindrome(self):
        """Test reversing palindromic strings."""
        self.assertEqual(reverse_string("racecar"), "racecar")
        self.assertEqual(reverse_string("level"), "level")
        self.assertEqual(reverse_string("noon"), "noon")
        self.assertEqual(reverse_string("a"), "a")

    def test_numeric_string(self):
        """Test reversing numeric strings."""
        self.assertEqual(reverse_string("12345"), "54321")
        self.assertEqual(reverse_string("9876543210"), "0123456789")

    def test_string_with_spaces(self):
        """Test reversing strings with spaces."""
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")
        self.assertEqual(reverse_string("a b c"), "c b a")
        self.assertEqual(reverse_string("  spaces  "), "  secaps  ")

    def test_string_with_special_characters(self):
        """Test reversing strings with special characters."""
        self.assertEqual(reverse_string("!@#$%"), "%$#@!")
        self.assertEqual(reverse_string("hello!"), "!olleh")
        self.assertEqual(reverse_string("@home"), "emoh@")

    def test_string_with_mixed_content(self):
        """Test reversing strings with mixed letters, numbers, and special characters."""
        self.assertEqual(reverse_string("abc123!@#"), "#@!321cba")
        self.assertEqual(reverse_string("Test-123"), "321-tseT")
        self.assertEqual(reverse_string("a1b2c3"), "3c2b1a")

    def test_string_with_punctuation(self):
        """Test reversing strings with punctuation."""
        self.assertEqual(reverse_string("Hello, World!"), "!dlroW ,olleH")
        self.assertEqual(reverse_string("a.b.c"), "c.b.a")
        self.assertEqual(reverse_string("(test)"), ")tset(")

    def test_string_with_newlines_and_tabs(self):
        """Test reversing strings with newlines and tabs."""
        self.assertEqual(reverse_string("a\tb\tc"), "c\tb\ta")
        self.assertEqual(reverse_string("line1\nline2"), "2enil\n1enil")

    def test_unicode_characters(self):
        """Test reversing strings with unicode characters."""
        self.assertEqual(reverse_string("café"), "éfac")
        self.assertEqual(reverse_string("😀😁😂"), "😂😁😀")
        self.assertEqual(reverse_string("日本語"), "語本日")

    def test_whitespace_only_string(self):
        """Test reversing strings with only whitespace."""
        self.assertEqual(reverse_string("   "), "   ")
        self.assertEqual(reverse_string("\t\n"), "\n\t")

    def test_repeated_characters(self):
        """Test reversing strings with repeated characters."""
        self.assertEqual(reverse_string("aaa"), "aaa")
        self.assertEqual(reverse_string("aaabbb"), "bbbaaa")

    def test_case_sensitivity(self):
        """Test that case is preserved during reversal."""
        self.assertEqual(reverse_string("AbC"), "CbA")
        self.assertEqual(reverse_string("HeLLo"), "oLLeH")


if __name__ == "__main__":
    unittest.main()
