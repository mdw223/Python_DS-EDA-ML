"""
 Author: Malik Wensman
 Email: mdwensma@ncsu.edu
 Class: CSC 251-001 Fall 2026
 Program: Text Analyzer
 Purpose: The program prompts the user for the name of a text file, reads all lines of text within the file, and analyzes the text to determine certain characteristics.
 Bugs: None
 Acknowledgements: None
"""

try:
    from hw4.header import header
except ModuleNotFoundError:
    # Allow running the script directly from the hw4/ directory (e.g., for student testing).
    from header import header   

import string

ROUNDING_PRECISION = 2

# Helper functions

def split_words(text: str) -> list:
    """Split the given text into a list of words.
    Parameters:
        text (str): The text to analyze.
    Returns:
        words (list): A list of words in the text.
    """
    # split the text into words using whitespace as the delimiter
    words = text.split()
    return words

def word_count(text: str) -> int:
    """Count the number of words in the given text.
    Parameters:
        text (str): The text to analyze.
    Returns:
        count (int): The number of words in the text.
    """
    words = split_words(text)
    return len(words)

def remove_punctuation(word: str) -> str:
    """Remove punctuation from the given word.
    Strips leading and trailing punctuation characters and converts the word to lowercase.
    Parameters:
        word (str): The word to process.
    Returns:
        cleaned (str): The word with punctuation removed and converted to lowercase.
    """
    # remove punctuation from the word and convert to lowercase
    return word.strip(".,!?;:\"'()[]{}").lower()

def split_words_and_remove_punctuation(text: str) -> list:
    """Split the given text into a list of words and remove punctuation from each word.
    Parameters:
        text (str): The text to analyze.
    Returns:
        cleaned_words (list): A list of words in the text with punctuation removed.
    """
    words = split_words(text)
    cleaned_words = [remove_punctuation(word) for word in words]
    return cleaned_words

def length_of_text_in_words(text: str) -> int:
    """Calculate the total number of characters across all words in the given text.
    Punctuation is removed before counting.
    Parameters:
        text (str): The text to analyze.
    Returns:
        total_length (int): The sum of character lengths of all words in the text.
    """
    words = split_words_and_remove_punctuation(text)
    total_length = 0
    for word in words:
        total_length += len(word)
    return total_length

def split_into_sentences(text: str) -> list:
    """Split the given text into a list of sentences.
    A new sentence begins after a word ending with '.', '!', or '?'.
    Punctuation is preserved within each returned sentence string.
    Parameters:
        text (str): The text to analyze.
    Returns:
        sentences (list): A list of sentence strings in the order they appear in the text.
    """
    # must not break on concatenations like "Mr. Smith" or 3.55

    ordered_words = split_words(text)
    sentences = []
    current_sentence = ""
    for word in ordered_words:
        current_sentence += word + " "
        if word.endswith((".", "!", "?")):
            sentences.append(current_sentence.strip())
            current_sentence = ""
    if current_sentence:
        sentences.append(current_sentence.strip())
    return sentences

# core functions

def count_unique_words(text: str) -> int:
    """Count the number of unique words in the given text.
    Punctuation is removed and all words are lowercased before comparison.
    Parameters:
        text (str): The text to analyze.
    Returns:
        unique_count (int): The number of distinct words in the text.
    """

    words = split_words_and_remove_punctuation(text)
    unique_words = set(words)
    return len(unique_words)


def avg_word_length(text: str) -> float:
    """Calculate the average word length (in characters) in the given text.
    Punctuation is removed from each word before measuring its length.
    Parameters:
        text (str): The text to analyze.
    Returns:
        avg_len (float): The average number of characters per word, rounded to ROUNDING_PRECISION.
    """
    words = split_words(text)
    total_length = length_of_text_in_words(text)

    if words:
        return round(total_length / len(words), ROUNDING_PRECISION) # returns as a float not a string
    else:
        return 0.0

def avg_sentence_length(text: str) -> float:
    """Calculate the average sentence length (in words) in the given text.
    Parameters:
        text (str): The text to analyze.
    Returns:
        avg_len (float): The average number of words per sentence, rounded to ROUNDING_PRECISION.
    """
    sentences = split_into_sentences(text)
    if not sentences:
        return 0.0

    # using a map to map sentences with their words counts to then calculate the average sentence length in words
    sentence_word_counts = list(map(word_count, sentences))
    total_words = sum(sentence_word_counts)

    return round(total_words / len(sentences), ROUNDING_PRECISION)


def create_dict(text: str) -> dict:
    """Create a dictionary mapping each lowercase letter to its frequency in the text.
    Parameters:
        text (str): The text to analyze.
    Returns:
        char_freq (dict): A dictionary with lowercase letters 'a'–'z' as keys and their
            occurrence counts as values.
    """
    char_freq = dict.fromkeys(string.ascii_lowercase, 0)
    for char in text:
        if char.isalpha():
            char = char.lower()
            char_freq[char] = char_freq.get(char, 0) + 1

    return char_freq


def output_dict(word_freq: dict) -> None:
    """Print the letter frequency dictionary in a formatted two-column table.
    Entries are printed in sorted key order.
    Parameters:
        word_freq (dict): A dictionary mapping characters to their frequency counts.
    Returns:
        None
    """
    for word, freq in sorted(word_freq.items()):
        print(f"{word:>5} {freq:>12}")
    

def punctuation_frequency_table(punctuation_freq: dict) -> None:
    """Print a formatted table showing each punctuation symbol and its frequency.
    Parameters:
        punctuation_freq (dict): A dictionary mapping punctuation symbols to their
            occurrence counts in the analyzed text.
    Returns:
        None
    """
    print("-" * 23)
    print(f"{'Punctuation'} {'Frequency':>11}")
    print("-" * 23)
    for symbol, freq in punctuation_freq.items():
        print(f"{symbol:>5} {freq:>12}")


def main() -> None:
    """Prompt the user for a text file, read it, and print a statistical analysis.
    Displays total word count, character count, average sentence length, average word
    length, unique word count, a letter-frequency table, and a punctuation-frequency table.
    Parameters:
        None
    Returns:
        None
    """
    # Get filename
    filename = input("Enter filename: ")
    print(filename)
    while not filename.endswith(".txt"):
        print("Please enter a valid text file with a .txt extension.")
        filename = input("Enter filename: ")

    text = ""
    total_word_count = 0
    char_count = 0
    unique_word_count = 0
    avg_word_len = 0.0
    avg_sent_len = 0.0
    word_freq = {}
    try:
        with open(filename, "r") as file:
            text = file.read()
            print(f"Text: {text}")

        try:
            char_count = len(text)
        except Exception as e:
            print(f"An error occurred while calculating character count: {e}")

        try:
            total_word_count = word_count(text)
        except Exception as e:
            print(f"An error occurred while calculating word count: {e}")
        try:
            unique_word_count = count_unique_words(text)
        except Exception as e:
            print(f"An error occurred while calculating unique word count: {e}")

        # Analyze the text
        try:
            avg_word_len = avg_word_length(text)
        except Exception as e:
            print(f"An error occurred while calculating average word length: {e}")

        try:
            avg_sent_len = avg_sentence_length(text)
        except Exception as e:
            print(f"An error occurred while calculating average sentence length: {e}")

        try:
            word_freq = create_dict(text)
        except Exception as e:
            print(f"An error occurred while creating the word frequency dictionary: {e}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return

    # print outputs
    print(f"Text contains: {total_word_count} word{'' if total_word_count == 1 else 's'}, {char_count} character{'' if char_count == 1 else 's'}")
    print(f"Average sentence length: {avg_sent_len:.2f} word{'' if avg_sent_len == 1 else 's'}")
    print(f"Average word length: {avg_word_len:.2f} character{'' if avg_word_len == 1 else 's'}")
    print(f"Number of unique words: {unique_word_count}")

    header()
    output_dict(word_freq)

    punctuation_freq = {".": text.count("."), "?": text.count("?"), "!": text.count("!"), ",": text.count(","), ":": text.count(":"), ";": text.count(";")}
    punctuation_frequency_table(punctuation_freq)


if __name__ == "__main__":
    main()
