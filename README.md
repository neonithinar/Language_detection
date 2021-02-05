# What-Language-is-this-
This is a basic web app that can identify languages given as input. The language Identifier uses a Neural Network trained using the Europarl Dataset and Tatoeba dataset as for the preliminary studies. 

As I understand, Language identification would be the first step in classical language translation. So it must be done with least latency and most efficiently. So the problem is to create a model that would identify the input language with least amount of processing time. Preferably it should run in the web browser itself. (we'll see how that goes). As of starting out this project I have no idea about how RNNs or NLP work. Everything you see here is learnt on the go. So please forgive my crude code.

An N-gram is an N-character slice of a longer string. Although in the literature the term can include the notion of any co-occurring set of
characters in a string (e.g., an N-gram made up of the first and third character of a word), in this work we will use the term for continuous slices only
Particularly we will be using trigrams for this project. That is 3 character slicing of a longer string.. As suggested by many literary works N-gram frequency based identifications are a very efficient, fast and robust way to categorize the language


I would very much like to extend my gratitude to user BobVonBob in discord (code bullet and co server, Machine Learning Channel) for suggesting the use of bigram frequencies to identify language. Which later led me to read The paper on N-gram based Text recognition (William B. Cavnar et.al) and other useful literature
