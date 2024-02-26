# n = number of wrong guesses
def draw_hangman(n):

    print("  +---+")
    print("  |   |")
    if n>0:
        print("  O   |")
    else:
        print("      |")
    if n<2:
        print("      |")
    elif n==2:
        print("  |   |")
    elif n==3:
        print(" /|   |")
    else:
        print(" /|\  |")
    if n<5:
        print("      |")
    elif n==5:
        print(" /    |")
    else:
        print(" / \  |")
    print("      |")
    print("=========")

'''
  +---+
  |   |
      | 1
 /|\  | 2 3 4 
 /    | 5 6 -> dead!
      |
========
'''

'''
"  +---+"
"  |   |"
"  O   |"
" /|\  |"
" / \  |"
"      |"
"========="
'''