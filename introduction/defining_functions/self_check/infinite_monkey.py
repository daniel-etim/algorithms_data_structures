# You may have heard of the infinite monkey theorem? 
# The theorem states that a monkey hitting keys at random on a typewriter keyboard for an infinite amount of time will almost surely type a given text, such as the complete works of William Shakespeare. 
# Well, suppose we replace a monkey with a Python function. How long do you think it would take for a Python function to generate just one sentence of Shakespeare? 
# The sentence we’ll shoot for is: “methinks it is like a weasel”

# The way we’ll simulate this is to write a function that generates a string that is 28 characters long by choosing random letters from the 26 letters in the alphabet plus the space. 
# We’ll write another function that will score each generated string by comparing the randomly generated string to the goal. 
# A third function will repeatedly call generate and score, then if 100% of the letters are correct we are done. 
# If the letters are not correct then we will generate a whole new string.
# To make it easier to follow your program’s progress this third function should print out the best string generated so far and its score every 1000 tries.

import random

sentence = "methinks it is like a weasel"
high_score = 0
best_string = ""

def generate_strings():
    char_pool = "abcdefghijklmnopqrstuvwxyz "
    # Generate a random string of the same length as the target
    return "".join(random.choice(char_pool) for _ in range(len(sentence)))

def get_score(generated):
    score = 0
    for i in range(len(sentence)):
        if generated[i] == sentence[i]:
            score += 1
    # Return the percentage (0 to 100)
    return (score / len(sentence)) * 100

def judge():
    global high_score, best_string
    iterations = 0
    
    while high_score < 100:
        iterations += 1
        new_string = generate_strings()
        current_score = get_score(new_string)
        
        # Check if this new random string is the best we've seen so far
        if current_score > high_score:
            high_score = current_score
            best_string = new_string
        
        # Print progress every 1000 tries
        if iterations % 1000 == 0:
            print(f"Try {iterations} | Best so far: '{best_string}' | Score: {high_score:.2f}%")

    print(f"DONE! Found it in {iterations} tries: {best_string}")

# Start the simulation
judge()