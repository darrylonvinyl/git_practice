# Scrabble
# In this project, you will process some data from a group of friends playing scrabble. You will use dictionaries to organize players, words, and points.

# Build your Point Dictionary
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10, 0]

letter_to_points = {letter:point for (letter,point) in zip(letters,points)}
# print(letter_to_points)

# Score a Word
def score_word(word):
  point_total = 0
  for letter in word:
    if letter in letter_to_points:
      point_total += letter_to_points[letter]
    else:
      point_total += 0
  return point_total

brownie_points = score_word("BROWNIE")
# print(brownie_points)

# Score a Game
player_to_words = {"player1":["BLUE","TENNIS","EXIT"], "wordNerd":["EARTH","EYES","MACHINE"], "Lexi Con":["ERASER","BELLY","HUSKY"], "Prof Reader":["ZAP","COMA","PERIOD"]}

player_to_points = {}

for player,words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points


# print(player_to_points)

# Ideas for Further Practice!
"""
If you want extended practice, try to implement some of these ideas with the Python you’ve learned:

play_word() — a function that would take in a player and a word, and add that word to the list of words they’ve played

update_point_totals() — turn your nested loops into a function that you can call any time a word is played

make your letter_to_points dictionary able to handle lowercase inputs as well
"""
def play_word(player,word):
  new_lst = []
  if player in player_to_words.keys():
    new_lst = player_to_words[player]
    new_lst.append(word)
    player_to_words[player] = new_lst
  else:
    player_to_words[player] = word
  

play_word("player1","RATCHET")
play_word("Desiree", "HOUSE")
# print(player_to_words)

def update_point_totals():
  for player,words in player_to_words.items():
    player_points = 0
    for word in words:
      capped_word = word.upper()
      player_points += score_word(capped_word)
    player_to_points[player] = player_points
