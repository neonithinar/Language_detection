![Banner](https://github.com/neonithinar/Language_detection/blob/main/templates/Language_detector.png)
<!-- retro visitor counter -->
<p align="center"> 
  <img src="https://profile-counter.glitch.me/{neonithinar}/count.svg" />
</p>

<!-- Welcome Message -->
<h1>Language Identifier <img src="https://media.giphy.com/media/nQjrA94PBUX9ssj9QU/giphy.gif" width="65px"></h1>

<h3>A basic web app to Identify the language using Character trigrams and neural network</h3>



**How to Use**  <img src="https://media.giphy.com/media/TKXabSgn2ouV8vmTue/giphy.gif" width="65px">

* Clone this repo
* Run _server.py_ from your terminal
* Copy the url on port 5000 in the output in your browser to run the web app locally
* Give a language string you need to identify in the input field
* Check the obtained Result !

* Language Identification Project preliminary try out.ipynb
    Notebook to generate model to categorize the language. Originally trained on Tatoeba dataset ( alhough originally comprised of 300+ languages, I'm inclined to use a subset of the original languages
* Europarl Language Detection.ipynb
  Notebook was trained on Europarl dataset. Oh.. the horror :( The dataset hosting servers are unforgiving. Since I am training the model with colab, using !wget to download the dataset takes for ever!. Downloading this 1.5GB data took me days! THE NOTEBOOK IS INCOMPLETE as of now. I was in the middle of cleaning the dataset when I found the Tatoeba dataset. With over 2 milliion sentences for each of the 20 languages, the Europarl dataset is a bit too much for language categorization.

**Techniques and Methods Used**

* An N-gram is an N-character slice of a longer string. Although in the literature the term can include the notion of any co-occurring set of characters in a string (e.g., an N-gram made up of the first and third character of a word), in this work we will use the term for continuous slices only Particularly we will be using trigrams for this project. That is 3 character slicing of a longer string.. As suggested by many literary works N-gram frequency based identifications are a very efficient, fast and robust way to categorize the language
The trigram featureset will be fed into a simple neural network with output layer activation softmax to train the model. 


I would very much like to extend my gratitude to user BobVonBob in discord (code bullet and co server, Machine Learning Channel) for suggesting the use of bigram frequencies to identify language. Which later led me to read The paper on N-gram based Text recognition (William B. Cavnar et.al) and other useful literature
