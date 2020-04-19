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
The IWord frequency analyzer unittest module.
This module contains IWordFrequencyAnalyzerTest class.
The IWordFrequencyAnalyzerTest class contains the unittests for the
IWordFrequencyAnalyzer module
"""

from iword_frequency_analyzer import IWordFrequencyAnalyzer, extract_valid_words_from_text_and_convert_to_lower_case
import unittest


class IWordFrequencyAnalyzerTest(unittest.TestCase):
    """
       Test class for the IWordFrequencyAnalyzer class.
       This class contains unittests for the various methods of the IWordFrequencyAnalyzer class.
       Additionally, this class contains various functional tests that test the good weather and bad weather
       conditions for the methods of the IWordFrequencyAnalyzer class, namely: Testing with valid input, testing with
       invalid input, testing with empty input and testing that the right exceptions are raised when needed.
    """

    def setUp(self) -> None:
        """
          setUp method for the IWordFrequencyAnalyzerTest class
        """
        self.word_frequency_analyzer = IWordFrequencyAnalyzer()

    def tearDown(self) -> None:
        """
          tearDown method for the IWordFrequencyAnalyzerTest class
        """
        pass

    def test_calculate_highest_frequency_returns_highest_frequency(self):
        """
          Tests that the calculate_highest_frequency method returns the highest
          word frequency in a given text.
        """
        input_text = 'abc def ghi jkl mno pqrs tuv wxyz ABC DEF GHI JKL MNO PQRS TUV WXYZ !"§ $%& /() =?* <> #|; ²³~ @`'
        expected_answer = 2
        self.assertEqual(self.word_frequency_analyzer.calculate_highest_frequency(input_text), expected_answer)

    def test_calculate_frequency_for_word_returns_the_frequency_of_the_given_word(self):
        """
           Tests that the calculate_frequency_for_word method returns the frequency
           of the given word in the text.
        """
        input_text = 'I8H70ruYfw KizcotV5vA ajlWht7Giu sledxCTcjh 49LmbhVraC nBO5eAtkpA ebBUruVaZl Ws0cDjQAfi GNijGDnVh'
        expected_answer = 1
        self.assertEqual(self.word_frequency_analyzer.calculate_frequency_for_word(input_text, 'ruyfw'),
                         expected_answer)

    def test_calculate_most_frequent_n_words_returns_a_list_of_the_most_frequent_n_words(self):
        """
          Tests that the calculate_most_frequent_n_words method returns a list containing
          the most frequent n words in the given text.
        """
        input_text = 'Ben! Ben!2 Eze?; Eze km kl0 kl jk nm 9009 )&^!@ 8977 '

        expected_answer = [('ben', 2), ('eze', 2), ('kl', 2), ('jk', 1), ('km', 1), ('nm', 1)]
        self.assertEqual(self.word_frequency_analyzer.calculate_most_frequent_n_words(input_text, 6), expected_answer)

    def test_extract_valid_words_and_convert_to_lower_case_returns_valid_words_in_lower_case(self):
        """
          Tests that the extract_valid_words_from_text_and_convert_to_lower_case method extracts
          the valid words from the text and converts them to lowercase.
        """
        input_text = 'uh0KT1HjNN CWcBi2Kgyv i5jEagI9tw YXPXmsS0ve ZsclwLHJ8R IkOcNiLsLs 14pH71XVN1 fIXckrG63MCzKPE47P2B'
        expected_answer = ['uh', 'kt', 'hjnn', 'cwcbi', 'kgyv', 'i', 'jeagi', 'tw', 'yxpxmss', 've', 'zsclwlhj', 'r',
                           'ikocnilsls', 'ph', 'xvn', 'fixckrg', 'mczkpe', 'p', 'b']
        self.assertEqual(extract_valid_words_from_text_and_convert_to_lower_case(input_text), expected_answer)

    def test_IWordFrequencyAnalyzer_methods_handle_incorrect_inputs_correctly(self):
        """
          Tests that the methods of the IWordFrequencyAnalyzer are able to handle incorrect inputs correctly
          i.e., that they are able to return a correct value even when the input contains no valid word
        """
        input_text_with_no_words = '    '
        expected_answers = [0, 0, []]

        self.assertEqual(self.word_frequency_analyzer.calculate_highest_frequency(input_text_with_no_words),
                         expected_answers[0])
        self.assertEqual(
            self.word_frequency_analyzer.calculate_frequency_for_word(input_text_with_no_words, 'testWord'),
            expected_answers[1])
        self.assertEqual(self.word_frequency_analyzer.calculate_most_frequent_n_words(input_text_with_no_words, 4),
                         expected_answers[2])

        input_text_with_no_valid_words = '789 :.,/ 099*** %$# @56'

        self.assertEqual(self.word_frequency_analyzer.calculate_highest_frequency(input_text_with_no_valid_words),
                         expected_answers[0])
        self.assertEqual(
            self.word_frequency_analyzer.calculate_frequency_for_word(input_text_with_no_valid_words, 'testWord'),
            expected_answers[1])
        self.assertEqual(
            self.word_frequency_analyzer.calculate_most_frequent_n_words(input_text_with_no_valid_words, 4),
            expected_answers[2])

    def test_IWordFrequencyAnalyzer_methods_raise_ValueError_exception_when_input_is_empty(self):
        """
          Tests that the methods of the IWordFrequencyAnalyzer are able to handle empty text input
          correctly i.e., that they raise an exception when the input is an empty string
        """
        with self.assertRaisesRegex(ValueError, 'Invalid input text: Input text should not be empty',
                                    msg='ValueError not raised by the calculate_highest_frequency_method'):
            self.word_frequency_analyzer.calculate_highest_frequency('')

        with self.assertRaisesRegex(ValueError, 'Invalid input text: Input text should not be empty',
                                    msg='ValueError not raised by the calculate_frequency_for_word method'):
            self.word_frequency_analyzer.calculate_frequency_for_word('', 'test')

        with self.assertRaisesRegex(ValueError, 'Invalid input text: Input text should not be empty',
                                    msg='ValueError not raised by the calculate_most_frequent_n_words method'):
            self.word_frequency_analyzer.calculate_most_frequent_n_words('', 2)

    def test_IWordFrequencyAnalyzer_methods_raise_TypeError_exception_when_input_is_not_a_string(self):
        """
          Tests that the methods of the IWordFrequencyAnalyzer class are able to handle
          invalid inputs correctly i.e., that they raise an exception when the input text
          is not a string.
        """
        with self.assertRaisesRegex(TypeError, 'Invalid input text: Input text should be a string',
                                    msg='TypeError not raised by the calculate_highest_frequency_method'):
            self.word_frequency_analyzer.calculate_highest_frequency(6)

        with self.assertRaisesRegex(TypeError, 'Invalid input text: Input text should be a string',
                                    msg='TypeError not raised by the calculate_frequency_for_word method'):
            self.word_frequency_analyzer.calculate_frequency_for_word(None, 'test')

        with self.assertRaisesRegex(TypeError, 'Invalid input text: Input text should be a string',
                                    msg='TypeError not raised by the calculate_most_frequent_n_words method'):
            self.word_frequency_analyzer.calculate_most_frequent_n_words(100, 2)

        with self.assertRaisesRegex(TypeError, 'Invalid input: n should be an integer',
                                    msg='TypeError not raised by the calculate_most_frequent_n_words method'):
            self.word_frequency_analyzer.calculate_most_frequent_n_words('test text', 'test')

        with self.assertRaisesRegex(TypeError, 'Invalid input: word should be a string',
                                    msg='TypeError not raised by the calculate_frequency_for_word method'):
            self.word_frequency_analyzer.calculate_frequency_for_word('Test text', 6)


if __name__ == '__main__':
    unittest.main()
