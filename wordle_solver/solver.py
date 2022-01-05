#!/usr/bin/python3
from collections import Counter
import sys
import re

# Defaults
len_game_chars = 5
all_letters = "abcdefghijklmnopqrstuvwxyz"
args = sys.argv

# Functions to move to a different file
def f_get_answer():
	return input().strip()

def f_set_is_letter(slot, letter):
	slot["letters"] = str(letter)

	i = all_letters.find(letter)
	slot["not_letters"] = all_letters[:i] + all_letters[i+1:]

def f_set_is_not_letter(slot, letter):
	i = slot["letters"].find(letter)

	if i >= 0:
		slot["letters"] = slot["letters"][:i] + slot["letters"][i+1:]

	slot["not_letters"] += str(letter)

def f_score(word, l_scores, l_scores_multiplier = {}):
	score = 0
	for c in word:
		score += l_scores[c] * (l_scores_multiplier if c in l_scores_multiplier else 1)
	return score

def f_create_regex(slots):
	res = ""
	for s in slots:
		res += f_create_regex_letters(s)

	return res

def f_create_regex_letters(slot):
	print("Making regex for:" + str(slot))
	letters = slot["letters"]
	not_letters = slot["not_letters"]

	# If found, just do that letter
	if len(letters) is 1:
		return letters

	# If not found, find the shorter comparisons and slap the letters in there
	with_not = True if len(not_letters) > len(letters) else False

	return "[" + ("^" if with_not else "") + (''.join(not_letters) if with_not else ''.join(letters)) + "]"

def main():
	# Defaults

	# Read in dictionary and letter scores
	d_words = {}
	l_scores = {}
	l_scores_multiplier = {}

	f_readin = open("l.1")
	for l in f_readin:
		l = l.strip().split(' ')
		l_scores[l[0]] = int(l[1])
	f_readin.close()

	f_readin = open("dictionary")
	for l in f_readin:
		l = l.strip()
		d_words[l] = f_score(l, l_scores)
	f_readin.close()

	# Create default slot values
	slots = [
			{
				"letters": all_letters,
				"not_letters":""
			}
			for i in range(len_game_chars)
		]
	
	answer = None

	# Suggest words until we can't or we find the right one
	while True:
		current_search = f_create_regex(slots)
		res = {"word":None, "score":0}
		res_unique = {"word":None, "score":0}

		r = re.compile(current_search)
		print(current_search)

		# Can't edit dictionaries as we use them, so 'remove' keys that cannot be valid now
		new_dict = {}
		for d in d_words.keys():
			if r.fullmatch(d):
				#print("Match found: " + d)
				#print(Counter(d))
				#print(len(Counter(d)))
				#print(Counter(res_unique["word"]))
				#print(len(Counter(res_unique["word"])))
				new_dict[d] = d_words[d]
				if (d_words[d] > res["score"]):
					res["word"] = d
					res["score"] = d_words[d]
				if (len(Counter(d)) > len(Counter(res_unique["word"]).keys())):
					res_unique["word"] = d
					res_unique["score"] = d_words[d]
			else:
				#print(d + " was not a match")
				pass
		d_words = new_dict

		if res["word"] is None or res["word"] == answer:
			print("No more valid words found")
			break

		# Found a word, tell the user and get its results
		if res["word"] is not res_unique["word"]:
			print("Choose between 1) " + res_unique["word"] + " (" + str(res_unique["score"]) + ") and 2) " + res["word"] + " (" + str(res["score"]) + ")")
			while True:
				answer = f_get_answer()
				if answer is not '1' and answer is not '2':
					print("Answer must be 1 or 2")
				else:
					if answer is '1':
						res = res_unique
					break

		print("Next word: " + res["word"])
		print("How did it fare? Enter for finished, _ for miss, x for wrong place, ! for right place:")
		answer = input().strip()

		# If we're done, let's bail
		if (answer is ""):
			print("!!!!!")
			return

		i = 0
		while i < len(answer) and i < len_game_chars:
			cur_c = res["word"][i]
			print("Cur_c is: " + cur_c)
			print("Slots is: ")
			print(slots)

			#switch(answer[1]):
			if answer[i] == '_':
				for s in slots:
					f_set_is_not_letter(s, cur_c)
			elif answer[i] == 'x':
				l_scores_multiplier[cur_c] = (2 if cur_c not in l_scores_multiplier else l_scores_multiplier[cur_c] + 1)
				f_set_is_not_letter(slots[i], cur_c)
			elif answer[i] == '!':
				f_set_is_letter(slots[i], cur_c)

			i += 1

if __name__ == '__main__':
	main()
