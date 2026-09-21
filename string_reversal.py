def reverse_string(s: str) -> str:
    """
    Reverses the input string and returns it.

    Args:
        s: The string to reverse

    Returns:
        The reversed string
    """
    return s[::-1]


if __name__ == "__main__":
    # Test with various inputs
    test_inputs = [
        "hello",
        "Python",
        "12345",
        "A man, a plan, a canal: Panama",
        "!@#$%",
        ""
    ]

    print("String Reversal Demonstration")
    print("=" * 50)

    for test_str in test_inputs:
        reversed_str = reverse_string(test_str)
        print(f"Original:  '{test_str}'")
        print(f"Reversed:  '{reversed_str}'")
        print()
