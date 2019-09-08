import json

black_cards = []
white_cards = []

with open('json_cards/cah.json') as f:
  dictionary = json.load(f)
  for card in dictionary['blackCards']:
    if (card['text'].count('_') == 1):
      black_cards.append(card['text'].replace('_', '__').replace('"', '&#34;').replace("'", "&#39;"))
  
  for card in dictionary['whiteCards']:
    if card[-1] == '.':
      card = card[:-1]
    white_cards.append(card.replace('"', '&#34;').replace("'", "&#39;"))

print("let BLACK_CARDS = ", black_cards)
print("let WHITE_CARDS = ", white_cards)
