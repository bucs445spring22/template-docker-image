import requests
import random

def main():
    result = requests.get("https://opentdb.com/api.php?amount=3")
    score = 0
    data = result.json()
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
        result = requests.post("http://db:8000/save", data={name: score})
        print(result)

    result = requests.get("http://db:8000/all")
    [print(score) for score in result.json()] 
    
if __name__ == "__main__":
    main()