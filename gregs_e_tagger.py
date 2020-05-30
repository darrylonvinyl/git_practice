#!/Users/capnawesome/opt/anaconda3/bin/python3

"""
Write a function called gregs_e_tagger that takes a string as an argument and inserts "greg" in the middle of the string, and then returns the new “greg-i-fied” string.

For odd length strings, consider the “middle” to be left of the middle character.
"""
word_to_greg = input("Please enter the word you want to 'greg': ")

def gregs_e_tagger(word):
  new_str = ""
  how_long = len(word)
  if how_long % 2 == 0:
    new_str = word[0:(how_long//2)] + 'greg' + word[-(how_long//2):]
  else:
    new_str = word[0:int((how_long/2))] + 'greg' + word[-int((how_long/2)+1):]
  return new_str

print(gregs_e_tagger(word_to_greg))
