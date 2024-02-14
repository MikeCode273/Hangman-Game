import hangman_words
import random
import hangman_arts
import os

#import the hangman arts
display= hangman_arts.word_arts
print(display)
word = hangman_words.Word_list
random_word = random.choice(word)
word_length=len(random_word)

#set the lives variable to number
lives = 6

#create a variablle to iinitialize an empty list 
random_lst=[]
for _ in range(word_length):
  random_lst+="_"
#print(random_lst)
end_of_game=False
while not end_of_game:
  
  guess_character =input("Guess a letter: ").lower()

  os.system('cls')
   #a new empty set
  if guess_character in random_lst:#test presence
    print("This letter has been used already")
  

  for char in range(word_length):
    letter=random_word[char]
    # print(f"Current position {char}\n Current letter: {letter}\n Guessed Letter: {guess_character}")
    
    if letter == guess_character:
      random_lst[char]=letter
      
  
  
 #reduce the number of livws 
  if guess_character not in random_word:
    lives-=1
    print(f"You guess {guess_character},that\'s not in the word.You lose a live.")

 #join all theelements in the list and turn it into a string
  print(f"{' '.join(random_lst)}")

  if "_" not in random_lst:
    end_of_game=True
    print("You win.")
  elif lives==0:
    end_of_game=True
    print("You lose.\nGame Over!!")
    print(f"Your random word is: {random_word}")
    

#use ascii art to man suicide

  print(hangman_arts.stages[lives])
