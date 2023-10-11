# functions to be applied on a list of words (testfile(n).txt)
# By Aidan Lalonde-Novales

# global word_list variable
word_list = []

''' loads a files contents into the word_list variable '''
def load(str):

    # uses the word_list global variable, clears before every use
    global word_list
    word_list.clear()

    # opens file
    file = open(str, "r")
    file_contents = file.read()
    file.close()

    # word_list becomes a list of every word in a testfile(n).txt file
    word_list = file_contents.split()

''' checks the most common word in word_list out of those in list '''
def commonword(list):

    # return none if list is empty, or if a word is not in word_list
    if len(list) == 0:
        return None
    for word in list:
        if word not in word_list:
            return None
    
    # default most_common to the first word in list, then checks which word is most common
    most_common = list[0]
    for word in list:
        if word_list.count(word) > word_list.count(most_common):
            most_common = word
    return most_common

''' checks the most common word in word_list that follows str '''
def commonpair(str):

    # return none if the string is not in the word list
    if str not in word_list:
        return None

    # initialize word pair list
    word_pair_list = []

    # check which indicies the word occurs at, add to word_pair_list
    for i, word in enumerate(word_list):
        if word in str and i < len(word_list) - 1:
            word_pair_list.append(word_list[i + 1])

    # if nothing gets appended to the word_pair_list 
    # (i.e. the only entry is at the end, where there is no pair) return none
    if not word_pair_list:
        return None

    # check the most common word pair in word_pair_list
    most_common = word_pair_list[0]
    for word in word_pair_list:
        if word_pair_list.count(word) > word_pair_list.count(most_common):
            most_common = word
    return most_common

''' counts the number of words in the word_list variable '''
def countall():

    # returns the length of the word list
    return len(word_list)

''' counts the number of unique words in the word_list variable '''
def countunique():

    # creates a list which will contain all unique items
    unique_words = []

    # iterates through every entry and adds unique words to unique_words
    for word in word_list:
        if word not in unique_words:
            unique_words.append(word)
    return len(unique_words)