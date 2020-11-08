import re

text = 'I like to do programming. It is awesome. I have to doing this next 3 year'

# ----------------- Metacharecters ------------------------------
# #-------------------------------------------------------------


# # [] ( Find all what ever int the [] )
# match = re.findall("[a-d]", text)
# print(match)
# # It will matched a to d characters in the text.


# # \d (Find all digit character)
# digit = re.findall("\d", text)
# print(digit)


# # . ( Search for a sequence )
# sequence = re.findall("li.e", text)
# # Start with li and then any character and then end with e.
# print(sequence)

# # ^ (String start with some character)
# start = re.findall("^I", text)
# print(start)


# # # $ (String end with some character)
# start = re.findall("year$", text)
# print(start)

# # # Find contain zero or more matched characters
# x = re.findall("d*o", text)
# print(x)

# # + (Find one or more matched character)
# x = re.findall('is+', text)
# print(x)

# # {} ( Exact number of occurrence)
# x = re.findall('is{2}', text)
# print(x)

# # | (Or operator)
# x = re.findall('is|have', text)
# print(x)

