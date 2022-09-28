import random

WORDLIST = "dictionary_of_words.txt"
PIC = "pic.txt"

class HangMan(object):
    # Hangman game

    infStr = '_-*\'*-_-*\'*-_-*\'*-_-*\'*-_-*\'*-_-*\'*-_-*\'*-_-*\'*-_-*\'*-_-*\''

    def __init__(self, *args, **kwargs):
        """
                        initializing Hangman class
        """

    def loadWords(self):
        """
                Returns the list of words from text file.
        """
        words_list = []
        # reading file having words
        with open(WORDLIST, 'r+') as f:
            for line in f.readlines():
                wordlist = line.split()
                for word in wordlist:
                    words_list.append(word)

        print("  ", len(words_list), "words loaded.")
        return words_list

    def loadPicture(self, idx):
        """
                Returns the picture content from text file.
        """
        lines = []
        with open(PIC, 'r') as fp:
            # reading image from txt based on the number of mistake
            x = fp.readlines()[idx]
            for i in x.split(','):
                lines.append(i)
        return lines

    def pickWord(self):
        """
                Choosing random words from txt file for the game
        """
        words = self.loadWords()
        return random.choice(words)

    def printPic(self, idx, wordLen):
        """
                Printing picture on every wrong attempt
        """
        lines = self.loadPicture(idx)
        for line in lines:
            print(line)

    def askAndEvaluate(self, word, result, missed):
        """
                Checking for input key if it belongs to the chosen word or not.
        """
        guess = input()
        # returning none if the guessed word is correct
        if guess == None or len(guess) != 1 or (guess in result) or (guess in missed):
            return None, False
        i = 0
        right = guess in word
        for c in word:
            if c == guess:
                result[i] = c
            i += 1
        return guess, right

    def info(self, info):
        """
                Printing final results
        """
        ln = len(self.infStr)
        print(self.infStr[:-3])
        print(info)
        print(self.infStr[3:])

    def start(self):
        """
                Starting point of the game
        """
        print('Welcome to Hangman !')

        # choosing a random word for game
        word = list(self.pickWord())
        result = list('*' * len(word))
        print('The word is: ', result)

        success, i, missed = False, 0, []

        # starting the game with 7 possible chances of mistake.
        while i < 7:
            print('Guess the word: ', end='')
            guess, right = self.askAndEvaluate(word, result, missed)
            if guess == None:
                print('You\'ve already entered this character.')
                continue
            print(''.join(result))
            if result == word:
                self.info('Congratulations ! You\'ve just saved a life !')
                success = True
                break
            if not right:
                missed.append(guess)
                i += 1
                self.printPic(i, len(word))
            print('Missed characters: ', missed)

        if not success:
            self.info('The word was \'' + ''.join(word) + '\' ! You\'ve just killed a man, yo !')
def main():
    """
            Starting Game
    """

    HangMan().start()


if __name__ == "__main__":
    """
        it is the main function which is the starting point of the program, 
        interpreter starts reading programfrom here.
    """
    main()

