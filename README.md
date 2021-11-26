# Political-Party-Classifier

## Description

This is a classifier (trained on reddit commments) which takes in political text and outputs the political party associated with the comment as well as the model's confidence. The goal of this project is to help conservative and liberal politicans find subreddits to advertise in. Since there are many region based subreddits, this can also help politicans determine the current political views of a location of interest.

## Technologies

• Python (Numpy, Pandas, Scikit-Learn)<br/>
• Flask<br/>
• HTML/CSS<br/>
• TailwindCSS<br/>

## Jupyter Notebook Code Explanation

1. Started by using the Reddit API through the praw library in python to collect a few hundred comments from both conservative and liberal subreddits
2. Labeled each comment with its party by checking which subreddit it came from
3. Used scikit-learn's CountVectorizer (Bag of Words model) to transform the dataset into a matrix with each column as a possible word and each row containing the frequency of that word in the given comment
4. Summed up those frequencies column wise to create a word cloud of the most frequent words
5. Chose logistic regression model and tuned hyperparameters using GridSearchCV
6. Created pipeline which takes in a string and applies the vectorizer transformation on the string (making it into a series that contains the frequency of each possible word in the string) and then uses the trained logistic regression model to make a prediction
7. Tested the model and then saved it using pickle


## [Try It Out]()