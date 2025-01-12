# import requests
#
# parameters = {
#     "amount": 10,
#     "type": "boolean"
# }
#
#
# # response = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")
# response = requests.get(url="https://opentdb.com/api.php", params=parameters)
# response.raise_for_status()
#
# data = response.json()
# print(data)
#
# question_data = data["results"]
# print(question_data)

data = [{'type': 'boolean', 'difficulty': 'medium', 'category': 'Entertainment: Film',
  'question': 'The color of the pills in the Matrix were Blue and Yellow.', 'correct_answer': 'False',
  'incorrect_answers': ['True']}, {'type': 'boolean', 'difficulty': 'easy', 'category': 'Animals',
                                   'question': 'A bear does NOT defecate during hibernation. ',
                                   'correct_answer': 'True', 'incorrect_answers': ['False']},
 {'type': 'boolean', 'difficulty': 'easy', 'category': 'Entertainment: Books',
  'question': 'Stephen Chbosky wrote the book &#039;The Perks of Being A Wallflower&#039;.', 'correct_answer': 'True',
  'incorrect_answers': ['False']}, {'type': 'boolean', 'difficulty': 'medium', 'category': 'Entertainment: Video Games',
                                    'question': 'TF2: The Heavy&#039;s voice actor, Gary Schwartz, voices the Demoman as well ',
                                    'correct_answer': 'True', 'incorrect_answers': ['False']},
 {'type': 'boolean', 'difficulty': 'easy', 'category': 'General Knowledge',
  'question': 'Adolf Hitler was born in Australia. ', 'correct_answer': 'False', 'incorrect_answers': ['True']},
 {'type': 'boolean', 'difficulty': 'easy', 'category': 'Entertainment: Television',
  'question': 'In Battlestar Galactica (2004), Cylons were created by man as cybernetic workers and soldiers.',
  'correct_answer': 'True', 'incorrect_answers': ['False']},
 {'type': 'boolean', 'difficulty': 'medium', 'category': 'Entertainment: Board Games',
  'question': '&quot;Rich Uncle Pennybags&quot; from the board game &quot;Monopoly&quot; wears a monocle.',
  'correct_answer': 'False', 'incorrect_answers': ['True']},
 {'type': 'boolean', 'difficulty': 'hard', 'category': 'Entertainment: Japanese Anime &amp; Manga',
  'question': 'The character Plum from &quot;No Game No Life&quot; is a girl.', 'correct_answer': 'False',
  'incorrect_answers': ['True']}, {'type': 'boolean', 'difficulty': 'hard', 'category': 'Celebrities',
                                   'question': 'Lady Gaga&#039;s real name is Stefani Joanne Angelina Germanotta.',
                                   'correct_answer': 'True', 'incorrect_answers': ['False']},
 {'type': 'boolean', 'difficulty': 'easy', 'category': 'Entertainment: Video Games',
  'question': 'The game &quot;Pocket Morty&quot; has a Morty called &quot;Pocket Mortys Morty&quot;?',
  'correct_answer': 'True', 'incorrect_answers': ['False']}]
