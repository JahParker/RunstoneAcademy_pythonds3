"""
Instructions:
Here's a self check that really covers everything so far. You may have heard of the infinite monkey theorem? The theorem states that a monkey hitting keys at random on a typewriter keyboard for an infinite amount of time will almost surely type a given text, such as the complete works of William Shakespeare. Well, suppose we replace a monkey with a Python function. How long do you think it would take for a Python function to generate just one sentence of Shakespeare? The sentence we'll shoot for is: “methinks it is like a weasel”

You're not going to want to run this one in the browser, so fire up your favorite Python IDE. The way we'll simulate this is to write a function that generates a string that is 28 characters long by choosing random letters from the 26 letters in the alphabet plus the space. We'll write another function that will score each generated string by comparing the randomly generated string to the goal.

A third function will repeatedly call generate and score, then if 100% of the letters are correct we are done. If the letters are not correct then we will generate a whole new string.To make it easier to follow your program's progress this third function should print out the best string generated so far and its score every 1000 tries.

Challenge:
See if you can improve upon the program in the self check by keeping letters that are correct and only modifying one character in the best string so far. This is a type of algorithm in the class of 'hill climbing' algorithms, that is we only keep the result if it is better than the previous one.
"""
import random
# This could have also been made by just using a string and using a 
# random number to select a character Ex: alphabet[random_number]
def add_character(character_id):
    match character_id:
        case 0:
            return 'a'
        case 1:
            return 'b'
        case 2:
            return 'c'
        case 3:
            return 'd'
        case 4:
            return 'e'
        case 5:
            return 'f'
        case 6:
            return 'g'
        case 7:
            return 'h'
        case 8:
            return 'i'
        case 9:
            return 'j'
        case 10:
            return 'k'
        case 11:
            return 'l'
        case 12:
            return 'm'
        case 13:
            return 'n'
        case 14:
            return 'n'
        case 15:
            return 'o'
        case 16:
            return 'p'
        case 17:
            return 'q'
        case 18:
            return 'r'
        case 19:
            return 's'
        case 20:
            return 't'
        case 21:
            return 'u'
        case 22:
            return 'w'
        case 23:
            return 'x'
        case 24:
            return 'y'
        case 25:
            return 'z'
        case 26:
            return ' '


def generate_new_string():
    monkey_string = ''
    characters = []

    # Creates a sentence that is 28 characters long
    for i in range(28):
        character_id = random.randint(0, 26)
        characters.append(add_character(character_id))

    # Created this try catch due to previously not numbering the 
    # match case function properly. This was used to 
    # be able to detect which number was causing an issue
    try:
        return monkey_string.join(characters)
    except:
            print(character_id)
            print(add_character(character_id))
            print("None type detected")


def score_monkey_string(string_to_score, target_sentence):
    score = 0.0
    # Increases the score when a letter in the created string is in the
    # same position as a letter in the target sentence
    for char_position in range(len(string_to_score)):
        if string_to_score[char_position] == target_sentence[char_position]:
            score += 1
    return (score/28) * 100
    
def typewriter_monkeys(target_sentence):
    count = 0
    # The best score and string is created to have a starting value
    best_string = generate_new_string()
    best_score = score_monkey_string(best_string, target_sentence)
    # This will continue to run until a perfect score is achieved
    while best_score != 100:
        string_to_score = generate_new_string()
        score = score_monkey_string(string_to_score, target_sentence)

        if score > best_score:
            best_score = score
            best_string = string_to_score
        # The best string found and its score will be shown every
        # 100000 iterations
        if count % 100000 == 1:
            print(best_string)
            print(best_score)

        count += 1

    print('Whew! That sure took a while!')
    print(f'It took {count} times to recreate "{target_sentence}".')
    print("Maybe it's a better idea to not outsource your work to monkeys...")


typewriter_monkeys("methinks it is like a weasel")
    

"""
First idea:
- Generate string
Use a match and case to assign each number to a character in the alphabet and 
then a space. 
Create a for loop that will continue to add characters to a string 28 times.
Return this string to be used in the scoring method
- Score string
Create a for loop that will check each position of the characters and tally how close it is the the intended string
Return the float value as the score
- Print progress
Until there is a score of 100%, print the best score and the string every 1000 iterations
"""