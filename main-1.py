# import pandas module
import pandas
# open and read CSV file data
nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
# loop file data and transform To a dictionary
nato_data_to_dict ={row.letter:row.code for (index, row) in nato_data.iterrows()}
# ask user to input word
word = input("text word: ").upper()
# there is a output List 
# word split by letter and append to list as NATO word 
# like A ==  ALFA , B == BRAVO ...
hash_code = [nato_data_to_dict[letter] for letter in word]
# print out result
print(hash_code)

