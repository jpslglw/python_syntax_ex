def print_upper_words1(words):
    """ This function prints all given words, that are given in a list-argument
    back in upper-case. 

    # this should print "HELLO", "HEY", "YO", and "YES"

    print_upper_words(["hello", "hey", "yo", "yes"])
    """

    # 2:
    for word in words:
        print(word.upper())

def print_upper_words2(words, must_start_with="E"):
    """ This function prints all given words, that are given in a list-argument
    back in upper-case. Only the words are given back, that start with letter e.

    # this should print "Erik", "Evan" and "Erica"

    print_upper_words(["Erik", "Brenda", "erik", "lisa", "Erica"],
                   must_start_with="e")
    """

    # 3:
    for word in words:
        if word[0].upper() == must_start_with:
            print(word.upper())

def print_upper_words(words, must_start_with):
    """ This function prints all given words, that are given in a list-argument
    back in upper-case. Only the words are given back, that start with 2 given letters.

    # this should print "HELLO", "HEY", "YO", and "YES"

    print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], 
                    must_start_with={"h", "y"})
    """

    # 4:
    for word in words:
        for letter in must_start_with:
            if word[0] == letter or word[0] == letter.upper():
                print(word.upper())

print_upper_words1(["hello", "hey", "goodbye", "yo", "yes"])
print_upper_words2(["Erik", "Brenda", "erik", "lisa", "Erica"], must_start_with="E")
print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})