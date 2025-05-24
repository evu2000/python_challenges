''' LOCATE WORDS IN A LIST CONTAINING CERTAIN CHARACTER '''

words = ["abc", "bcd", "aaaa", "cbc"]
X = "a"
res = []

def find_words(word_list: list, target: str) -> list:
    """Function that locate words containing certain character

    Args:
        word_list (list): List of words to be examined
        target (str): Character to search

    Returns:
        list: List cointaning the positions of the words in the provided list
    """
    for word in word_list:
        if target in word:
            res.append(word_list.index(word))

    return res

print(find_words(words, X))
