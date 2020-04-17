'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    if len(word) < 2:
      return 0

    new_len = len(word) // 2
    fst = word[:new_len]
    snd = word[new_len:]

    if fst[-1] == 't' and snd[0] == 'h':
      return 1 + count_th(fst) + count_th(snd)
    
    return count_th(fst) + count_th(snd)