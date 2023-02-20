import emoji
from letter_dict import alphabet_dict, letter_size


class EmojiAlphabetPrinter:
    def __init__(self, word="GM", foreground=":snake:", background=":star:"):
        self._word = word
        self._foreground = foreground
        self._background = background

    @property
    def word(self):
        return self._word

    @word.setter
    def word(self, word):
        self._word = word

    @property
    def foreground(self):
        return self._foreground

    @foreground.setter
    def foreground(self, foreground):
        self._foreground = foreground

    @property
    def background(self):
        return self._background

    @background.setter
    def background(self, background):
        self._background = background

    def convert_to_emoji(self, letter_values):
        """
        Convert True/False values to emojis
        """
        letter_emojis = []
        for row in letter_values:
            row_emojis = []
            for value in row:
                if value:
                    row_emojis.append(emoji.emojize(self._foreground))
                else:
                    row_emojis.append(emoji.emojize(self._background))
            letter_emojis.append(row_emojis)
        return letter_emojis

    def _get_letter_string(self, letter_emojis):
        """
        Convert letter emojis to a string
        """
        result = ""
        for i in range(letter_size):
            for letter in letter_emojis:
                if len(letter) < letter_size:
                    # add a space if the letter is smaller than the letter size
                    result += ''.join(emoji.emojize(self._background)) + ''.join(emoji.emojize(self._background))
                else:
                    result += ''.join(letter[i]) + ''.join(emoji.emojize(self._background))
            result += '\n'
        return result

    @property
    def result(self):
        """
        Return an emoji representation of a word
        """
        # create a list of the letters in the word
        letters = list(self._word)
        # create a list of values from the alphabet_dict for each letter in the word
        letter_values = [alphabet_dict[letter] for letter in letters]

        # convert True/False values to emojis
        letter_emojis = [self.convert_to_emoji(values) for values in letter_values]

        # get string representation of letters with spaces and false emojis
        letters_string = self._get_letter_string(letter_emojis)

        return letters_string


printer = EmojiAlphabetPrinter()
print(printer.result)

printer.word = "CELESTIA"
print(printer.result)
