Word Ladder: Given a list of same-length words, a start word, and an end word, print out the list of words to move from the start word to the end word with only single-letter changes between steps.

This was an Amazon programmer question that's been itching at me. My original solution was a recursive O(n!) search over an array and I did not like it, so I'm trying to do it better here.

The word list is found in `words` by default, but may be specified when starting the program.

Usage: <word_ladder.py> <start_word> <end_word> [words_file = 'words']

I at least understand why recursion isn't a great answer here, and a graph would likely perform MUCH better, given the way that the nodes and traversal would work.
