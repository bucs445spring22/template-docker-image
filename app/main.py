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
            print("Correct!")
        else:
            print(f"nope: {k['correct_answer']}")

        input("[press any key to continue]")

    print(f"You got {score} right!")
    
if __name__ == "__main__":
    main()