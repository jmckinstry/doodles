#!/usr/bin/python3
import sys
import math

def f_load_words(word_file):
	words = []
	len_words = None
	
	f = open(word_file, 'r')
	for l in f:
		l = l.strip()
		if not len_words:
			len_words = len(l)
		
		# All words in a file must be of equal length
		assert(len_words == len(l))
		
		words.append(l)
	
	f.close()
	
	return words

def f_get_word_distance(w1, w2, max_value = math.inf, error_value = math.nan):
	assert(len(w1) == len(w2))
	
	res = 0
	
	for x in range(len(w1)):
		if w1[x] != w2[x]:
			res += 1
			
			# Allow short-cutting if max_value is specified
			if res > max_value:
				return error_value
				
	return res

def f_build_word_map(word_map, word_list):
	# This build is n^2, can I do better?
	# Initialize the map
	for w in word_list:
		if not w in word_map:
			word_map[w] = []
	
	# For each map entry, add nodes for each acceptable ladder step
	for k,v in word_map.items():
		for w,x in word_map.items():
			if f_get_word_distance(w, k) == 1:
				v.append(w)
	
	return word_map

def f_get_word_ladders(word_map, word_start, word_end):
	res = []
	len_winners = math.inf
	last_word = None
	
	ladder = [word_start]
	answer = f_get_word_ladder_step(word_map, ladder, word_end, len_winners, False)
	
	while answer:		
		if len(answer) < len_winners:
			len_winners = len(answer)
			res = []
			
		print("Answer found: " + str(len_winners) + ", " + ','.join(answer))
		res.append(answer)
		
		answer = f_get_word_ladder_step(word_map, ladder, word_end, len_winners)
	
	return res
	
def f_get_word_ladder_step(word_map, ladder, word_end, max_length = math.inf, in_progress = True, depth = 1):
	# If we don't have room for an answer, short-circuit
	if len(ladder) == 0 or len(ladder) >= max_length:
		return None
		
	print('New Ladder Step:')
	
	last_winner = None
	
	# If last_winner is set, we pull it off of the ladder and cut it and all else before it from our list search so we can continue our DFS efficiently
	if in_progress and len(ladder) > 1:
		last_winner = ladder.pop()
		
	# Ladder's last entry is our current word
	cur = ladder[len(ladder)-1]
	m = word_map[cur]
	
	if last_winner:
		m = word_map[cur][word_map[cur].index(last_winner)+1:]
	
	# If we can reach the end word from our current ladder, return that result
	print(ladder)
	print(m)
	
	if word_end in m:
		answer = ladder.copy()
		answer.append(word_end)
		
		return answer
	# If it's not reachable, recurse our ladder looking for the next step of solutions
	else:
			
		for w in m:
			print('\t'*depth + w)
			if w not in ladder:
				ladder.append(w)
				answer = f_get_word_ladder_step(word_map, ladder, word_end, max_length, in_progress, depth+1)
				if answer:
					#print("recursing...")
					return answer
				ladder.pop()
	
	return None
	
if __name__ == "__main__":
	# Always need at least start and end word
	len_argv = len(sys.argv)
	assert(len_argv >= 3)
	
	word_start = sys.argv[1]
	word_end = sys.argv[2]
	word_file = len_argv > 3 and sys.argv[3] or 'words'
	
	word_list = f_load_words(word_file)
	assert(word_start in word_list)
	assert(word_end in word_list)
	word_map = {}
	
	f_build_word_map(word_map, word_list)
	del word_list
	
	res = f_get_word_ladders(word_map, word_start, word_end)
	
	if res:
		print('Word Ladder Found: ' + ', '.join(res[0]))
		print('Total Answers: ' + str(len(res)))
		print(res)
	else:
		print('No valid ladder found')




