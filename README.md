# What-Language-is-this-
This is a basic web app that can identify languages given as input. The language Identifier uses a Neural Network trained using the Europarl Dataset and Tatoeba dataset as for the preliminary studies. 

As I understand, Language identification would be the first step in classical language translation. So it must be done with least latency and most efficiently. So the problem is to create a model that would identify the input language with least amount of processing time. Preferably it should run in the web browser itself. (we'll see how that goes). As of starting out this project I have no idea about how RNNs or NLP work. Everything you see here is learnt on the go. So please forgive my crude code.

**Files in this Notebook**
* Language Identification Project preliminary try out.ipynb
    Notebook to generate model to categorize the language. Originally trained on Tatoeba dataset ( alhough originally comprised of 300+ languages, I'm inclined to use a subset of the original languages
* Europarl Language Detection.ipynb
  Notebook was trained on Europarl dataset. Oh.. the horror :( The dataset hosting servers are unforgiving. Since I am training the model with colab, using !wget to download the dataset takes for ever!. Downloading this 1.5GB data took me days! THE NOTEBOOK IS INCOMPLETE as of now. I was in the middle of cleaning the dataset when I found the Tatoeba dataset. With over 2 milliion sentences for each of the 20 languages, the Europarl dataset is a bit too much for language categorization.

**Techniques and Methods Used**
An N-gram is an N-character slice of a longer string. Although in the literature the term can include the notion of any co-occurring set of
characters in a string (e.g., an N-gram made up of the first and third character of a word), in this work we will use the term for continuous slices only
Particularly we will be using trigrams for this project. That is 3 character slicing of a longer string.. As suggested by many literary works N-gram frequency based identifications are a very efficient, fast and robust way to categorize the language
The trigram featureset will be fed into a simple neural network with output layer activation softmax to train the model. 


I would very much like to extend my gratitude to user BobVonBob in discord (code bullet and co server, Machine Learning Channel) for suggesting the use of bigram frequencies to identify language. Which later led me to read The paper on N-gram based Text recognition (William B. Cavnar et.al) and other useful literature
