import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    check=""
    for x in letters_guessed:
        if x in secret_word :
            check="True"
        else:
            check="False"         
    return check            
                    
def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    add=""
    for x in secret_word:
        if x in letters_guessed :
            add+=x
        else:
            add+=" _ "
    return add            
                
                 
def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    add=""
    if letters_guessed!="":
        for x in string.ascii_lowercase:
            if x in letters_guessed :
                x=x
            else:
                add=add+x
    else:
        add=string.ascii_lowercase           
    return add            
        
    
def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    n1=""
    n2=""
    m=n=0
    my_word=my_word.strip()
    if len(my_word)==len(other_word):
        for j in my_word:
            if j!='_':
                if j in other_word:
                     m=1
                     n1=n1+j
                else:
                     n=10
            else:
                n1=n1+"*"
        for k in other_word:
            if k in my_word:
                n2=n2+k
            else:
                n2=n2+"*"                     
    if  m==1 and n==0 and (n2)==(n1):
        return True
    else:
        return False


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    n=55900
    tat=""
    add=""
    print("These are the Similar words")
    lists=load_words()
    for i in lists:
        i=str(i)
        if match_with_gaps(my_word, i):
            tat=tat+i+" "
            n=n-1
        else:    
            my_word=my_word.strip()
            if len(my_word)==len(i):
                add=add+i+" "
    if n<55900:        
        print(tat)
    elif n==55900:
        print(add)
    
            
            

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to game Hangman!")
    countw=3
    countg=6
    unique=0
    letters_guessed=""
    word=""
    print("I am thinking of the word that is ",len(secret_word)," word long.")
    print("You have ",countw,"warnings left")
    while countw>=0 and countg>=0:
        print("------------------------")
        print("Available Leters: ",get_available_letters(letters_guessed))
        w=str(input("Please guess a letter :"))
        k=0
        if str.isalpha(w):
            w=str.lower(w)
            if w in get_available_letters(letters_guessed):
                letters_guessed=letters_guessed+w
            else:
                countw=countw-1
                k=1
                print("Oops! You already guessed that character ",countw," warnings left: ")
            if is_word_guessed(secret_word, letters_guessed)=="True":
                print("Good Guess: ")
            elif k!=1:
                print("Oops! That letter is not in my word. ")
                if w=='a'or w=='e'or w=='i' or w=='o' or w=='u':
                    countg=countg-2
                else:
                    countg=countg-1
                print("You have ",countg,"guesses left.")
                print("Please Guess a Letter: ")
        elif w=="*":
            my_word=""
            for i in word:
                if i!=" ":
                    my_word=my_word+i       
            show_possible_matches(my_word)
        else:
            countw=countw-1
            print(" Oops! That is not a valid letter. You have ",countw," warnings left: ")
        word=get_guessed_word(secret_word, letters_guessed)
        print(word)
        if word==secret_word:
            print("Congratulations, you won!")
            for y in string.ascii_lowercase:
                   for x in word:
                       if y in x:
                           unique+=1
                           break
            print("Your total score for this game is: ",unique*countg) 
            break
            
    if countg<0:
        print("You have 0 guesses left so you lose the Game")
    if countw<0:
        print("You have 0 Warnings left so you lose the Game")

if __name__ == "__main__":

    secret_word =choose_word(wordlist)
    hangman_with_hints(secret_word)

