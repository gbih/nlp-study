# Chapter 12: Building a Knowledge Graph

#### [Blueprints for Text Analysis Using Python](https://www.oreilly.com/library/view/blueprints-for-text/9781492074076/)
Authored by Jens Albrecht, Sidharth Ramachandran, Christian Winkler.

### Datasets
* [NLTK Reuters corpus](https://www.nltk.org/book/ch02.html)
    - The Reuters Corpus contains 10,788 news documents totaling 1.3 million words. The documents have been classified into 90 topics, and grouped into two sets, called "training" and "test"; thus, the text with fileid 'test/14826' is a document drawn from the test set. This split is for training and testing algorithms that automatically detect the topic of a document.

### Explore

* Advanced language features of spaCy.
* Pretrained neural models in combination with custom rules for named-entity recognition, coreference resolution, and relation extraction. 
* Necessary steps to perform entity linking

### Misc

* A coreference module is now built-in to Spacy 3, which means we will not use HugginfFace's `neuralcoref` package. 
    - https://github.com/huggingface/neuralcoref/issues/295 
    