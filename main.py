import emoji
from letter_dict import alphabet_dict, letter_size


class EmojiAlphabetPrinter:
    def __init__(self):
        pass

    def convert_to_emoji(self, letter_values):
        """
        Convert True/False values to emojis
        """
        letter_emojis = []
        for row in letter_values:
            row_emojis = []
            for value in row:
                if value:
                    row_emojis.append(emoji.emojize(':snake:'))
                else:
                    row_emojis.append(emoji.emojize(':star:'))
            letter_emojis.append(row_emojis)
        return letter_emojis

    def get_letter_string(self, letter_emojis):
        """
        Convert letter emojis to a string
        """
        result = ""
        for i in range(letter_size):
            for letter in letter_emojis:
                result += ''.join(letter[i]) + ''.join(emoji.emojize(':star:'))
            result += '\n'
        return result

    def print_word(self, word):
        """
        Print an emoji representation of a word
        """
        # create a list of the letters in the word
        letters = list(word)
        # create a list of values from the alphabet_dict for each letter in the word
        letter_values = [alphabet_dict[letter] for letter in letters]

        # convert True/False values to emojis
        letter_emojis = [self.convert_to_emoji(values) for values in letter_values]

        # get string representation of letters with spaces and false emojis
        letters_string = self.get_letter_string(letter_emojis)

        # print string representation of letters with spaces and false emojis
        print(letters_string, end='')


printer = EmojiAlphabetPrinter()
printer.print_word("HELLO")