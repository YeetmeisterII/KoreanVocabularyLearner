# KoreanVocabularyLearner
Program to learn Korean vocabulary.

Programmed in 3.8, should be 3.6+ compatible.
Dependency: https://pypi.org/project/hangul-romanize/.

The easiest way to run the program is inside the console (terminal for MacOS) and run "entry.py" with the dependency installed.

How It Works:
You can chose a unit - currently only unit one has any lessons in it - then choose a lesson from that unit.
There are two kinds of questions.
First is English to Korean where you are given an English word and have to type the equivalent Korean.
Second is Korean to English where a Korean word is given and there is an option of five English words to choose from.
Words have a weighted chance of being chosen based on how often they are spelt or selected correctly.
Word weights are stored in a SQL database to preserve your progress.

Notes:
The units and lessons are based on this website - https://www.howtostudykorean.com/
There is currently no way to end a lesson, exiting the program and restarting is the only method to choose a new lesson. This is fine and will not cause any issues.
If you have any questions feel free to message me.
