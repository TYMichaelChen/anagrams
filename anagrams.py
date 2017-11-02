"""
1. Given 2 words, determine if they are anagrams of each other (ex: eat and tea & )
2. Create a function that finds two words in a text that are anagrams of another two words in that text.
  a. For example:
    Happy eaters always heat their yappers.
    Would yield: happy eaters and heat yappers
  b. Rules:
    - Treat all letters as lowercase.
    - Ignore any words less than 4 characters long.
    - Treat all non-alpha-numeric characters as whitespace.
    - So "Surely. And they're completely right!" becomes four words: "surely  they completely right"
    - Neither of the words in the first pair can be repeated in the second pair.
"""

from collections import Counter
import re

# Process words is not fully functioning. What is wrong?
def process_words(text):
    """Extract words from text, count the occurrences of each letter in a word.

    Split text at non-alphanumeric characters, and convert to lowercase.
    Exclude words that have fewer than four characters. For each word, count
    how many times a letter appears in that word.
    """
    split_text = re.split('[^a-z0-9]', text)

    letter_counts = {}
    for w in split_text:
        letter_counts[w] = Counter(w)

    return split_text, letter_counts

# Complete this function
def find_pairs(processed_words, letter_counts):
    """Find two pairs of two words that are anagrams of each other.

    For each pair of two words, check if there is another pair that has the
    same combined letter count. If there is, and no word from the first pair
    appears in the second pair, the two pairs are anagrams of each other.
    """
    pass

# Main function - should be used to call the previous 2 functions.
def find_anagram(text):
    """Look for anagram pairs within given text.

    Given text, process it into words needed, count the occurrences of letters
    in each word. If a pair of words have the same combined letter count as
    another pair, and no word from first pair appears in second pair, the two
    pairs are anagrams of each other.

    Args:
        text: A string in which anagrams are to be looked for.

    Returns:
        A string that includes the two pairs of words that are anagrams. If no
        anagrams are found in text, answer also states so.
    """
    # Process text into words to be examined for anagrams, count the letters in
    # each word. Runtime O(n)
    words, letter_counts = process_words(text)

    pairs = find_pairs(words, letter_counts)

    if pairs:
        answer = pairs
    else:
        answer = 'No anagrams found.'

    return answer


if __name__ == '__main__':
    text = input('What text would you like to look for anagrams in? ')
    print(find_anagram(text))
