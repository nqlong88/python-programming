# Solution to problem 5 Hw3:

def letter_count(word):
    count = {}
    for l in word:
        count[l] = count.get(l, 0) + 1
    return count


def possible_words(word_list, char_list):
    #which words in word_list can be formed from the 
    #charaters in char_list
    valid_words = []
    #iterate over word_list
    for word in word_list:
        is_word_valid = True
        #get a count of each character in word
        char_count = letter_count(word)
        #check each character in the word
        for letter in word:
            if letter not in char_list:
                is_word_valid = False
            else:
                if char_list.count(letter) != char_count[letter]:
                    is_word_valid = False
        #add valid word to a list
        if is_word_valid:
            valid_words.append(word)
    return valid_words
legal_words = ['go', 'bat', 'me', 'eat', 'goal', 'boy', 'run']
letters = ['e', 'o', 'b', 'a', 'm', 'g', 'l']