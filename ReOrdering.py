# ReOrdering

# There is a sentence that has a mistake in its ordering.
#
# The part with a capital letter should be the first word.
#
# Please write a function to re-order the words, so that the word starting with a capital letter is moved to the front.
#
# Each word in the string is separated by a single space.
#
# In the string, there will always be exactly one word with a capital letter in it.

# Examples
# "ming Yao" --> "Yao ming"
# "Mano donowana" --> "Mano donowana"
# "wario LoBan hello" --> "LoBan wario hello"
# "bull color pig Patrick" --> "Patrick bull color pig"


def re_ordering(text):
    words = text.split()
    for index, word in enumerate(words):
        if word[0].isupper():
            capitalized_word = words.pop(index)
            words.insert(0, capitalized_word)

    return " ".join(words)

print(re_ordering("wario LoBan hello"))
