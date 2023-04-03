import random
import time

hiragana_dict = {
    'a': 'あ', 'i': 'い', 'u': 'う', 'e': 'え', 'o': 'お',
    'ka': 'か', 'ki': 'き', 'ku': 'く', 'ke': 'け', 'ko': 'こ',
    'sa': 'さ', 'shi': 'し', 'su': 'す', 'se': 'せ', 'so': 'そ',
    'ta': 'た', 'chi': 'ち', 'tsu': 'つ', 'te': 'て', 'to': 'と',
    'na': 'な', 'ni': 'に', 'nu': 'ぬ', 'ne': 'ね', 'no': 'の',
    'ha': 'は', 'hi': 'ひ', 'fu': 'ふ', 'he': 'へ', 'ho': 'ほ',
    'ma': 'ま', 'mi': 'み', 'mu': 'む', 'me': 'め', 'mo': 'も',
    'ya': 'や', 'yu': 'ゆ', 'yo': 'よ',
    'ra': 'ら', 'ri': 'り', 'ru': 'る', 're': 'れ', 'ro': 'ろ',
    'wa': 'わ', 'wo': 'を', 'n': 'ん'
}

score = 0
total_questions = 0
start_time = time.time()

while True:
    mode = input("Which mode do you want to practice? (1) Hiragana to Romaji, (2) Romaji to Hiragana, or (3) Exit? ")
    if mode == '1':
        hiragana = random.choice(list(hiragana_dict.keys()))
        answer = input(f"What is the Romaji equivalent of {hiragana}? ")
        total_questions += 1
        if answer == hiragana_dict[hiragana]:
            score += 1
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is {hiragana_dict[hiragana]}")
    elif mode == '2':
        english = random.choice(list(hiragana_dict.keys()))
        answer = input(f"What is the Hiragana equivalent of {english}? ")
        total_questions += 1
        if answer == hiragana_dict[english]:
            score += 1
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is {hiragana_dict[english]}")
    elif mode == '3':
        elapsed_time = time.time() - start_time
        print(f"Final score: {score}/{total_questions}")
        print(f"Elapsed time: {elapsed_time:.2f} seconds")
        break
    else:
        print("Invalid input. Please enter 1, 2, or 3.")
    
    print(f"Current score: {score}/{total_questions}")
    print("------------------------------")
