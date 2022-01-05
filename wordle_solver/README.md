These files are used to swiftly solve Wordle problems, for a very limited (configurable) word library.

#Installation

Unzip wordle_solver_bulk_files.zip.

#Running

`python3 solver.py`

#Files
`dictionary` is the list of words to consider as source words.
All lines should be the same length.
Each line is a single dictionary entry in lower-case.

`l.1` is the letter scoring file.
Each line should contain a unique character, a space, then its integer weight.

`word_counter.py` is used to generate character counts from existing corpuses. Corpii?
l.1 was generated with this script.
Call it with the file to count characters of.
Any corpus is acceptable, but as only a-z are considered. If the corpus has mixed case, convert it to lower first.

#External sources
The primary dictionary for this file comes from http://corpus.leeds.ac.uk/list.html. It has been trimmed and reduced in length, and only the top 20,000 entries were used.