#Task 2(Intermediate Level):-

#(1)

pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup

# URL of the page we want to scrape
url = "http://books.toscrape.com/"

# Sending a GET request to the website
response = requests.get(url)

# Checking if the request was successful
if response.status_code == 200:
    # Parsing the content of the response
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Finding all book containers
    books = soup.find_all('article', class_='product_pod')
    
    # Extracting data from each book
    for book in books:
        title = book.h3.a['title']  # Book title
        price = book.find('p', class_='price_color').text  # Book price
        
        print(f'Title: {title}, Price: {price}')
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)

(2)

import random

class Hangman:
    def __init__(self, word_list):
        self.word_list = word_list
        self.word_to_guess = random.choice(self.word_list).lower()
        self.guessed_letters = []
        self.max_attempts = 6
        self.attempts = 0

    def display_hangman(self):
        stages = [
            """
               -----
               |   |
               |   O
               |  /|\\
               |  / \\
               -
            """,
            """
               -----
               |   |
               |   O
               |  /|\\
               |  /
               -
            """,
            """
               -----
               |   |
               |   O
               |  /|
               |  
               -
            """,
            """
               -----
               |   |
               |   O
               |   |
               |  
               -
            """,
            """
               -----
               |   |
               |   O
               |  
               |  
               -
            """,
            """
               -----
               |   |
               |  
               |  
               |  
               -
            """,
            """
               -----
               |   |
               |   
               |   
               |  
               -
            """
        ]
        return stages[self.attempts]

    def display_progress(self):
        progress = ''.join([letter if letter in self.guessed_letters else '_' for letter in self.word_to_guess])
        return progress

    def play(self):
        print("Welcome to Hangman!")
        print(f"The word to guess has {len(self.word_to_guess)} letters.")
        
        while self.attempts < self.max_attempts:
            print(self.display_hangman())
            print("Current progress: ", self.display_progress())
            print(f"Guessed letters: {', '.join(self.guessed_letters)}")
            guess = input("Enter a letter: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a valid letter.")
                continue

            if guess in self.guessed_letters:
                print("You already guessed that letter.")
                continue

            self.guessed_letters.append(guess)

            if guess in self.word_to_guess:
                print("Good guess!")
            else:
                print("Wrong guess!")
                self.attempts += 1

            if all(letter in self.guessed_letters for letter in self.word_to_guess):
                print(self.display_hangman())
                print("Congratulations! You've guessed the word:", self.word_to_guess)
                break
        else:
            print(self.display_hangman())
            print("Sorry, you've run out of attempts. The word was:", self.word_to_guess)

# Main Execution
if __name__ == "__main__":
    words = ["python", "hangman", "challenge", "programming", "openai", "assistant"]
    game = Hangman(words)
    game.play()