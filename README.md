# Messenger Analyser

## Introducation 
Simple tools for analysing messenger conversations and simple classification.

History of all messenger conversations can be downloaded as .jason files like described in this tutorial:
https://www.zapptales.com/en/download-facebook-messenger-chat-history-how-to/
Unpack your conversation data and place it next to scripts and tools folder.

### Tools 
In tools folder there is small Python module that contains functions for reading and parsing messenger conversations. 
All tools work both for 1:1 conversations and group conversations. 

Identification of conversations goes always by conv_ID, string that is name of the folder that contains "messages_1.json" file stroing conversations. 
Usually string is Name+Surname+random characters or GroupChatName+random characters

## Generate Conversation Report
*scripts/ConversationReport.ipynb*
It is simple Jupyter Notebook that obtains and visualize few most important information from given conversation. 
It also contains example on how to use Tools to search your conversation in more efficient way that messenger interface allows. 

## Who Wrote That? - Naive Bayes
*scripts/NaiveBayesClassif.ipynb*
It is simple example of messages classification using Naive Bayes, polish language stemmer and TF-IDF vectorizer. 
**On Example Conversaion for +15 words messages it reached accuracy of 77.8%**