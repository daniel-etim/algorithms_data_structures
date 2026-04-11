''' Activity: 1.10.2 ActiveCode (self_check_1) '''

# combines the letter of words and treat each letter as a single data object and then produces a list that only contains a single copy of each letter. 

# -------- method 1 ----------

objects = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
letters = []

# this is a set and not a dict and therefore strips of copies of any element so that only one copy of the elment is present
letter_set = {""}

# append each letter to the "letter_set"
for object in objects:
    for letter in object:
        letter_set.add(letter)
        # letters.append(sep)

# turns the set into a list
letter_set = list(letter_set)
letters = letter_set

# if empty string is present in list, remove
if "" in letters:
    letters.remove("")
print(letters)

# interestingly, it contains all 26 alphabets
print(len(letters))