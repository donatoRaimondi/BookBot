def get_book_words(content):
    """
    Returns the number of words in a book

    Args: 
        content (str): the content of book x

    Returns:
        int: number of words
    """

    return  len(content.split())


def get_letter_count(content):
    """
    Get the content of a book and returns a dictionary of how many time a character (case insensitive wise)
    appears

    Args:
        content (str): content of book x

    Returns:
        dict(String, Integer): 'p' : 6126
    """

    word_counter = {}
    for c in content.lower():
        if c not in word_counter:
            word_counter[c] = 1
        else: 
            word_counter[c] += 1

    return word_counter 


def get_report(word_counter):
    """
    Get a dicitionary of characters and their counts and returns a sorted list of dictionaries
    Skips non char

    Args:
        word_counter (dict<char, int>)

    Returns:
        a sorted list of dictionaries {"char": "a", "num": 5450405}, sorted by num key
    """

    report = []
    for k in word_counter:
        if not k.isalpha():
            continue
        report.append({"char":k,"num": word_counter[k]})
    
    report.sort(key=lambda item: item["num"], reverse=True)
    return report
