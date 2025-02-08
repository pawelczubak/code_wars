# First
# Complete the solution so that it returns true if the first argument(string) passed in ends
# with the 2nd argument (also a string).
#
# Examples:
#
# solution('abc', 'bc') # returns true
# solution('abc', 'd') # returns false

def solution(text, ending):
    x = len(ending)
    if text[-x:] == ending:
        return True
    else:
        return False


print(solution('123456789', '2244'))