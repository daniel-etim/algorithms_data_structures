# this is an alternative to exr1.py. using list comprehension

# ordinary list
my_list = ["cat", "dog", "rabbit"]
print(my_list, "\n")

# get each character of words
my_list_ch = [word[ch] for word in my_list for ch in range(len(word))]
print(my_list_ch, "\n")

# convert list to set to strip off duplicates. and convert set back to list
my_list_uniq_ch = list(set(my_list_ch))
print(my_list_uniq_ch)
