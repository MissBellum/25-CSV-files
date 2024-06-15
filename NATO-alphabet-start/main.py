# import pandas
#
#
# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# # Looping through dictionaries:
# for (key, value) in student_dict.items():
#     # Access key and value
#     pass
#
#
# student_data_frame = pandas.DataFrame(student_dict)
#
# # Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     # Access index and row
#     # Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
import pandas

nato_csv = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_df = pandas.DataFrame(nato_csv)
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# Can also create a function and call it inside the except clause recursively
is_on = True
while is_on:
    user_data = input("What word do you want to translate: ").upper()
    try:
        word = [nato_dict[key] for key in user_data]
    except KeyError as k:
        print(f"{k} - Sorry, only letters allowed in the phonetic alphabet.")
    else:
        print(word)
    if user_data == "exit":
        is_on = False
        exit()
