import unittest

from keywords import find_response_for_keyword, KwResponse, _no_keyword_found_resp
from conjegations import conjugate
from Strings import pad_string, unpad_string, remove_end_punctuation, get_text_after_keyword
from alice import Alice


class AliceTests(unittest.TestCase):
    def test_keyword_lookup_from_word(self):
        # Arrange

        # Act
        kwrd, resp = find_response_for_keyword("Can I")

        # Assert
        resp.next = 0
        self.assertEqual("CAN I", kwrd)
        self.assertEqual("Perhaps you don't want to<*", resp.get_next_response())

    def test_keyword_lookup_from_list(self):
        # Arrange

        # Act
        kwrd, resp = find_response_for_keyword("You are")

        # Assert
        resp.next = 0
        self.assertEqual("YOU ARE", kwrd)
        self.assertEqual("What makes you think I am<*", resp.get_next_response())

    def test_pad_string(self):
        # Arrange
        unpadded_str = "hello, johnny. isn't this nice?"

        # Act
        padded = pad_string(unpadded_str)

        # Assert
        self.assertEqual(" hello ,  johnny .  isn't this nice ?  ", padded)

    def test_unpad_string(self):
        # Arrange
        padded_str = " hello ,  johnny .  isn't this nice ?  "

        # Act
        unpadded_str = unpad_string(padded_str)

        # Assert
        self.assertEqual("hello, johnny. isn't this nice?", unpadded_str)

    def test_pad_unpad_string(self):
        # Arrange
        unpadded_str = "This is mine and that is yours.  But I am ok if you are."

        # Act
        padded_str = pad_string(unpadded_str)
        new_unpadded = unpad_string(padded_str)

        # Assert
        self.assertEqual(unpadded_str, new_unpadded)

    def test_remove_punctuation(self):
        # Arrange
        punctuated_str = "hello, isn't this nice? "

        # Act
        clear_str = remove_end_punctuation(punctuated_str)

        # Assert
        self.assertEqual("hello, isn't this nice", clear_str)

    def test_text_after_keyword(self):
        # Arrange
        full_str = "This sentence has a keyword in it somewhere."

        # Act
        no_keyword_str = get_text_after_keyword(full_str, "A KEYWORD")

        # Assert
        self.assertEqual(" in it somewhere.", no_keyword_str)

    def test_conjugate(self):
        # Arrange
        orig = "This is mine and that is yours. But I am ok if you are."

        # Act
        swapped = conjugate(orig)

        # Assert
        self.assertEqual("This is yours and that is mine. But you are ok if I am.", swapped)

    def test_phrase(self):
        # Arrange
        e = Alice()
        orig = "I think this works Alice."
        resp = KwResponse("THINK", ["Do you doubt that<*"])

        # Act
        ph = e.form_response_text(orig, "THINK", resp)

        # Assert
        self.assertEqual("Do you doubt that this works Alice?", ph)

    def test_no_keyword_response(self):
        # Arrange
        a = Alice()
        orig = "my dog is misbehaving"
        resp = _no_keyword_found_resp
        resp.next = 0

        # Act
        ph = a.form_response_text(orig, "DOG", resp)

        # Assert
        self.assertEqual("Say, do you have any psychological problems?", ph)

    def test_duplicate_input(self):
        # Arrange
        a = Alice()
        input = "i need a coffee with no keywords"

        # Act
        _ = a.listen(input)         # Get past the greeting
        _ = a.listen(input)         # First input
        resp = a.listen(input)      # Duplicate input

        # Assert
        self.assertEqual("Why did you repeat yourself?", resp)