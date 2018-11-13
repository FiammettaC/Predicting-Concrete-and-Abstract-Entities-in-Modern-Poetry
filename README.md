# Predicting-Concrete-and-Abstract-Entities-in-Modern-Poetry

Paul Valéry defines the "language of poetry" as a "language within a language", alluding to the fact that poetic language does not necessary reflect the conventions of every-day language.
For the same reason, it is relatively easy for most people to detect poetic language, even in the absence of rhyme and unconventional word order. At the same time, poetic language is considered mysterious and impenetrable by many, and often also idiosyncratic.

Poets often spend most of their energy on labor limae, deciding which words are more poetical, expressive and successful in conveying the intended idea. 
Poets are able to find the most poetically interesting word for a given context based on their subtle and nuanced grasp of the slight variations in meaning that each word bears upon the text.

Our aim is understanding whether a neural network is capable of learning such poetic decisions in ways that generalize across different poets. 
Specifically, we investigate whether neural language models can learn to predict entities in modern poetry based on the preceding context, and successfully do so on texts by previously unseen poets. 

Specifically, we consider the task of reconstructing the original verse of a poem, extracted from a corpus of American modern poetry, and evaluate models for this task across different poets. Our baseline model is a state-of-the-art neural language model, trained on ordinary language (Wikipedia).

Predicting the exact word used by a poet out of a vocabulary of hundreds of thousands of words is extremely hard, but we consider the task of selecting the right candidate from a set of related words, e.g., a set of synonyms or words of the same high-level semantic class. 
We evaluate our models on held-out sentences, possibly from held-out poets. Finally, we compare the performance of our models to human, professional poets.

