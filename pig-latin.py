ay = "ay"
way = "way"
consonant = ("B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "Y", "V", "X", "Z")
vowel = ("A", "E", "I", "O", "U")
word = input("Enter the word to translate to Pig Latin: ")
first_letter = word[0]
first_letter = str(first_letter)
first_letter=first_letter.upper()
if first_letter in consonant:
  print(first_letter,"is a consonant")
  length_of_word = len(word)
  remove_first_letter = word[1:length_of_word]
  pig_latin = remove_first_letter + first_letter + ay
  print("The word in Pig Latin is:", pig_latin)
elif first_letter in vowel:
  print(first_letter, "is a vowel")
  pig_latin = word + way
  print("The word in Pig Latin is:" , pig_latin)
else:
  print("I dont know what ", first_letter, "is ")