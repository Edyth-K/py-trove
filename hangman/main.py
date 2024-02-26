from draw import draw_hangman

def main():
    for i in range(0,7):
        print(f"Num mistakes: {i}")
        draw_hangman(i)
        print()

if __name__ == "__main__":
    main()

'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
'''