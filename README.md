# Messenger Analyser

## Introduction
Simple tools for analysing messenger conversations and performing simple classifications.\
History of all messenger conversations can be downloaded as .jason files like described in this tutorial:
https://www.zapptales.com/en/download-facebook-messenger-chat-history-how-to/
Unpack your conversation data and place it next to scripts and tools folder.

#### Tools 
In tools folder there is small Python module that contains functions for reading and parsing messenger conversations. 
All tools work both for 1:1 conversations and group conversations. \
Identification of conversations goes always by conv_ID, string that is name of the folder that contains "messages_1.json" file. 
Usually string is Name+Surname+random characters or GroupChatName+random characters

## Generate Conversation Report
*scripts/ConversationReport.ipynb*\
It is simple Jupyter Notebook that obtains and visualize few most important information from given conversation. 
It also contains example on how to use Tools to search your conversation in more efficient way that messenger interface allows. 

## Who Wrote That? - Naive Bayes
*scripts/NaiveBayesClassif.ipynb*\
It is a simple example of messages classification using Naive Bayes, polish language stemmer and TF-IDF vectorizer. \
#### Accuracy in 1:1 convesration
Results of classification, 80% messages were used for training, 10% validation and 10% for test. Example conversation with over 100k exchanges messages was used.\
**Min. words** - Minimum number of words given message have to have to be used in classification. \
**No. train** - Amount of messages that was used to train the model.\
**Acc** - Accuracy.

| Min. words | No. train | Acc   |
| ------     | ------    | ----- |
| 5          | 28 104     |70.10% |
| 10         | 11 334     |76.39% |
| 15         | 5 505      |78.21% |
| 20         | 2 411      |78.11% |
| 25         | 2 179      |72.17% |

#### Accuracy in group conversation
Same parameters were used on 5 person group conversation. 

| Min. words | No. train | Acc   |
| ------     | ------    | ----- |
| 5          | 19 412     |37.21% |
| 10         | 3 740      |40.86% |
| 15         | 780        |32.31% |

Short messages are in general more difficult to classify. When we increase **Min. words** and take in concideration only longer messages accuracy improves. \
However as we discard more and more messages we are being left with smaller training datasets, and that decrease classification accuracy. \

## Who Wrote That? - Recurent Neural Network
*scripts/RecurentNeuralNetClassif.ipynb*\
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://drive.google.com/file/d/1fjib-peZ4cDHyL29ELGPBaCXikw0qIXX/view?usp=sharing) \
This is script uses LSTM (Long Short Term Memory) recurent neural network for performing same task.\
Since deep learning method decides by itself what features of texts are important, way less language specific processing is needed.
However some additional transformations are nessecary (like padding) and many hyper parameters need to be tuned. \
Since training required GPU for fast training Google Collabolatory was used.
#### Accuracy in 1:1 convesration
Network was tested on same conversation that Naive Bayes.\
For training with each min. numer of words some adjustments of hyperparmeters were done, however no exhaustive search was performed. 

| Min. words | No. train | Acc   |
| ------     | ------    | ----- |
| 5          | 28 104     |75.72% |
| 10         | 11 334     |78.93% |
| 15         | 5 505      |81.12% |
| 20         | 2 411      |77.82% |
| 25         | 2 179      |75.62% |

#### Accuracy in group conversation
Same parameters were used on 5 person group conversation. 

| Min. words | No. train | Acc   |
| ------     | ------    | ----- |
| 5          | 19 412     |37.21% |
| 10         | 3 740      |40.86% |
| 15         | 780        |32.31% |

\
\
\
*Data was not attached to this project as it was private. Feel free to run scripts on any messenger history.*