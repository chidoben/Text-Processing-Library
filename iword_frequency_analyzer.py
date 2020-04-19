#  Copyright (c) 2020 Benjamin Ezepue
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

"""
The IWord frequency analyzer module.
This module contains IWordFrequencyAnalyzer class.
The IWordFrequencyAnalyzer class is part of a text processing library. It implements methods
for calculating the highest frequency in a text, calculating the frequency of a given word in a text
and for calculating the N most frequent words in a text.
"""

from operator import itemgetter
from collections import Counter
from typing import List, Tuple
import re


def extract_valid_words_from_text_and_convert_to_lower_case(text: str) -> List[str]:
    """Helper function to extract valid words from the input text and convert the words
       to lower case.
    Parameters:
       text(str): The input text
    Returns:
       A list of the valid words extracted out of the input text
    Return type:
       List[str]
    Raises:
        A TypeError exception if the input text is not a string
        A ValueError exception if the input text is empty
    """
    if not isinstance(text, str):
        raise TypeError('Invalid input text: Input text should be a string')

    if not text:
        raise ValueError('Invalid input text: Input text should not be empty')

    valid_words_list = re.findall(r'[A-Za-z]+', text)
    return [valid_word.lower() for valid_word in valid_words_list]


IWordFrequency = List[Tuple[str, int]]


class IWordFrequencyAnalyzer:
    """
    The IWordFrequencyAnalyzer implements methods for calculating the highest frequency in a text,
    calculating the frequency of a given word in a text and for calculating the N most frequent words in a text.

    The following are assumptions and definitions that limit the scope of the task:
    Word: To simplify, a word is represented by a sequence of one or more characters between "a‟ and "z‟ or between "A‟
    and "Z‟. For example “agdfBh”.
    Letter Case: When counting frequencies, we are interested in the case insensitive frequency (i.e. in the text “The
    sun shines over the lake”, the library should count 2 occurrences for any of the words “the” or “The” or “tHE” etc).
    Input Text: The input text contains words separated by various separator characters. Note that the characters from
    "a‟ and "z‟ and from "A‟ and "Z‟ can only appear within words.
    """

    def __init__(self):
        pass

    @staticmethod
    def calculate_highest_frequency(text: str) -> int:
        """calculate_highest_frequency calculates and returns the highest frequency
        in the text (several words might actually have this frequency)
        Parameter:
          text (str): The text for which the highest frequency should be calculated
        Returns:
          A number representing the highest frequency in the text
        Return type:
          int
        """
        valid_words_list = extract_valid_words_from_text_and_convert_to_lower_case(text)
        word_frequencies = Counter(valid_words_list)
        sorted_word_frequencies = sorted(word_frequencies.items(), key=itemgetter(1), reverse=True)
        if not sorted_word_frequencies:
            return 0
        else:
            return sorted_word_frequencies[0][1]

    @staticmethod
    def calculate_frequency_for_word(text: str, word: str) -> int:
        """calculate_frequency_for_word calculates and returns the frequency of
           the given word in the text.
        Parameters:
          text (str): The text to be used for calculating the frequency of the word
          word (str): The word for which the frequency should be calculated
        Returns:
           A number representing the frequency of the given word in the text
        Return type:
           int
         Raises:
            A TypeError exception if word is not a string
        """
        if not isinstance(word, str):
            raise TypeError('Invalid input: word should be a string')
        valid_words_list = extract_valid_words_from_text_and_convert_to_lower_case(text)
        word_frequencies = Counter(valid_words_list)
        return word_frequencies[word]

    @staticmethod
    def calculate_most_frequent_n_words(text: str, n: int) -> IWordFrequency:
        """Calculates and returns a list of the most frequent "n‟ words in the input text, all the
        words returned in lower case. If several words have the same frequency, this method
        should return them in ascendant alphabetical order (for input text “The sun shines
        over the lake” and n = 3, it should return the list { (“the”, 2), (“lake”, 1), (“over”, 1) }
        Parameters:
           text(str): The text to be used for calculating the most frequent n words
           n(int): The number of the most frequent words which should be returned
        Returns:
           A list containing the most frequent 'n' words and their frequencies
        Return type:
           IWordFrequency
         Raises:
            A TypeError exception if n is not an integer
        """
        if not isinstance(n, int):
            raise TypeError('Invalid input: n should be an integer')
        valid_words_list = extract_valid_words_from_text_and_convert_to_lower_case(text)
        word_frequencies = Counter(valid_words_list)
        sorted_word_frequencies = sorted(word_frequencies.items(), key=lambda x: (-x[1], x[0]))
        return sorted_word_frequencies[:n]
