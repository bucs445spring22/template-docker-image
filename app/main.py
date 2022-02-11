import requests
import time
import random
from threading import Thread
from dataclasses import dataclass

@dataclass
class Config:
    num_seconds: int = 3
    time_remaining: int = 0

def guess_answer():
    return int(input("Which is your guess?"))

def main():
    result = requests.get("https://opentdb.com/api.php?amount=5")
    score = 0
    data = result.json()
    config = Config()
    for k in data['results']:
        print(f'{k["question"]}')
        answers = k['incorrect_answers']+[k['correct_answer']]
        random.shuffle(answers)
        [print(f"\t{i}) {a}") for i, a in enumerate(answers)]
        guess = int(input("Which answer do you think is correct?"))
        if answers[guess] == k['correct_answer']:
            score += 1
        input("[press any key to continue]")

    if input("Would you like to save your score? [Y/n]").lower() == 'y':
        name = input("What is your name?")
        result = requests.post("http://app_net:5000/save", data={name: score})
        print(result)
    
        
if __name__ == "__main__":
    main()