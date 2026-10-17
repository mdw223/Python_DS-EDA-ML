Title: Text Analyzer

Function:
The program should prompt the user for the name of a text file and read all lines of text within the file. Then, it should analyze the text to determine the following characteristics:

• Total number of words and characters, including white-space characters 
• Average number of words per sentence, to 2 fractional digits 
• Average number of characters per word, to 2 fractional digits 
• Number of unique words 
• Frequency of alphabetical characters 
• Frequency of punctuation characters (.,!?;:)

Assumptions:
- assume that words can be composed of letters, digits, and special characters other than punctuation and are separated by white-space characters. Thus, “2 & 3” would be considered 3 words of 1 character each, while “2&3” will be considered 1 word composed of 3 characters.
- Sentences end with a period, question mark, or exclamation mark (‘.’, ‘?’, or ‘!’).
- Punctuation that ends a sentence as well as commas, colons, semicolons, and double quotes should not be considered part of a word.
- For a hyphenated word such as ‘white-space‘, the hyphen will be included as part of a word and its length. The same will hold true for a contraction such as “can’t”. Another exception would be a colon used to specify time, such as in “6:30”. You may assume in this case that there are no spaces on either side of the colon. A colon followed by space, such as in “apple: golden, red delicious, granny smith”, would be considered punctuation and would not be part of the word. Hyphens and single quotes will otherwise not be present in the text, although double quotes might be.
- The frequency of alphabetical characters should be case insensitive. In other words, “the” and “The” both contribute a ‘t’. The same is true for the unique word count, where “the” and “The” count as the same word. Based upon the description above, “friend.” and “friend” would also count as the same word since the period is not a part of the word. 
- If the file only contains punctuation and white-space characters, the file is considered to contain 0 words although the total number of characters will be at least 1 since each file will be terminated with a line return. White-space characters including the newline are included in the character count.

Requirements:
- [x] Exception handling for any unrecoverable issues that may occur.  For example, if the user enters an invalid filename, you should re-prompt the user for the filename until a valid filename is entered. Assume that all text within the file until the EOF is valid. 
- [x] Dictionaries, sets, and maps should be used as appropriate. You’ll be expected to have at least one of each! Hint: Before using 2 parallel lists, use a dictionary.
- [x] Global constants to replace magic numbers but no global variables
- [x] Use of only built-in Python functions and functions from the math and string libraries. No other libraries or packages should be used. 
- [x] Import the header.py file to assist with the table formatting
- [x] A main function to direct the execution of your program.  
- [x] A function named count_unique_words that returns the number of unique words used in the text.
- [x] A function named avg_word_length that returns the average length of words within the text. 
- [x] A function named avg_sentence_length that returns the average number of words in a sentence within the text.
- [x] A function named create_dict that creates a dictionary to hold alphabetical characters and their frequency of occurrence as a key-value pair.
- [x] A function named output_dict that outputs the dictionary of alphabetical characters with their frequency of occurrence. 
- [x] use a map
- [x] test comparisons
- [x] Documentation at the top of the file, at the top of each function, and throughout the main program. 
- [x] submit a single source code file named HW4LastNameFirstInitial.py

