"""
Q1: Stable Character

You are given a string `s`.

In this string, some characters may appear multiple times.

A character is called **stable** if all of its occurrences appear **together as
one continuous group**, without being interrupted by other characters.

Your task is to identify the **first stable character** you encounter when
reading the string from left to right.

If the string does not contain any stable character, return `None`.

Examples:
---------
Input: "aaabccddde"  → Output: 'a'
Input: "abccba"      → Output: 'c'
Input: "aabbcc"      → Output: 'a'
Input: "abc"         → Output: None
Input: "a"           → Output: None

Explanation:
- In "abccba", 'c' appears at positions 2,3 (continuous), while 'a' and 'b'
  are interrupted
- Single character occurrences are not considered stable (must appear at least
  twice)
"""


def first_stable_character(s):
    """
    Find the first stable character in the string.

    A character is stable if:
    1. It appears at least twice
    2. All occurrences are in one continuous group

    Args:
        s (str): Input string

    Returns:
        str or None: First stable character, or None if no stable character exists

    Examples:
        >>> first_stable_character("abccba")
        'c'
        >>> first_stable_character("abc")
        None
        >>> first_stable_character("a")
        None
    """
    # I'm tracking the first and last occurrence of each character
    first_occurrence = {}
    last_occurrence = {}
    

    for i, char in enumerate(s):
        if char not in first_occurrence:
            first_occurrence[char] = i
        last_occurrence[char] = i
    
    # Checking characters in order of appearance
    for i, char in enumerate(s):
        # character stable if (first != last)
        if first_occurrence[char] != last_occurrence[char] and i == first_occurrence[char]:
            # Checking if all occurrences are continuous
            char_count = last_occurrence[char] - first_occurrence[char] + 1
            if s[first_occurrence[char]:last_occurrence[char]+1].count(char) == char_count:
                return char
    
    return None


if __name__ == "__main__":
    # Test your solution here
    print(first_stable_character("abccba"))  # Should print: c
    print(first_stable_character("abc"))     # Should print: None
    print(first_stable_character("a"))       # Should print: None
    #additional custom tests
    print(first_stable_character("aaabccddde"))  #a
    print(first_stable_character("sdfnsddfcccdfmsdaa"))      #c