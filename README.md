I've always been interested in astrophysics so today I decided to do a little ML project for the sake of curiosity

I have very very little background knowledge in astrophysics, but after finding some datasets in kaggle my interest was peaked

Link to the dataset: https://www.kaggle.com/datasets/fedesoriano/stellar-classification-dataset-sdss17

While I was reading through the features in the data one feature stuck out; redshift.
After watching some videos and reading some papers (namely “A review of redshift and its interpretation in cosmology and
astrophysics" by Gray & Dunning-Davies) I was hooked.

From my understanding, an object's redshift says simply how fast an object is traveling away from us due to universal expansion.
I wanted to see if there was any significant correlation between an objects redshift and wether that object is a star, galaxy or quasar

Turns out: There (probably) is. 

As of today (July 6th) using the random forest model with input as "redshift" and output as "class", I was able to get the following results:
Galaxies and Stars were able to be classified with 0.93 and 1.0 respectively within precision, accuracy & recall.
However quasars landed on a 0.79 for all the metrics

Overall I dont think the results are very reliable, but for a quick project with limited astrophysics knowledge, I would call this a success

What I learned:
- Interesting lessons in astrophysics
- Cleaning and implementing real world data using kaggle

What I wish to improve:
- learn more and to see if i can pair the redshift with another input to get a more accurate score
- Also get more comfortable at cleaning data 
