''' Activity: 1.10.2 ActiveCode (self_check_1) '''

# combines the letter of words and treat each letter as a single data object and then produces a list that only contains a single copy of each letter. 

# -------- method 1 ----------

objects = ["cat", "dog", "rabbit"]
letters = []

# this is a set and not a dict and therefore strips off copies of any element so that only one copy of the elment is present
letter_set = {""}

# append each letter to the "letter_set"
for object in objects:
    for letter in object:
        letter_set.add(letter)

# turns the set into a list
letter_set = list(letter_set)
letters = letter_set

# there's an empty string present when letter_set was initialized
if "" in letters:
    letters.remove("")
print(letters)
