# twitterPositiveNegative
Sentiment analysis of tweets; determines if tweets containing a specific word are positive or negative and graphs the trend


How to Run:
1. User must install tweepy and the Natural Language toolkit (nltk)
2. First run the stream, THEN run the grapher


How it works:
-Implements twitter API with tweepy to stream tweets
-Cleans the tweets by removing usernames, links, hashtags, and emojis
-Stores the clean twitter data in CSV file
-Grapher reads the CSV file in real time and determines whether tweet has positive or negative sentiment using the nltk
-Grapher then visualizes the data in real time on a line graph
