def longest_c_word(filename):
    """
    This function takes a filename as parameter.
    It returns the longest word that starts with 'c'.
    """

    fp = open(filename, "r")

    longest_word = ""

    for line in fp:
        words = line.split()

        for word in words:
            if word.startswith("c"):
                if len(word) > len(longest_word):
                    longest_word = word

    fp.close()

    return longest_word

## The function receives the location of filename, opens it and creates a variable for the longest ##word. It then splits lines into single words and compares them. The longest is stored in the ##variable longest_word. File is then closed and the longest_word returned