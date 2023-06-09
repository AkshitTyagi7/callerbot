import random
import json
import pickle
import numpy as np
import nltk

# nltk.download('punkt')
# nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizer_v1 import SGD
import tensorflow 
tensorflow.compat.v1.disable_eager_execution()

lemmatizer=WordNetLemmatizer() #Lemmatizer will makes the word's like asking, asked to ask
#Lemmatizer will be useful in speech to text 

intents=json.loads((open('training2.json')).read())# Here the program is reading the input training json file

words=[]
classes=[]
documents=[]
ignore_letters=['?','!']

for intent in intents['intents']:
    for pattern in intent['patterns']:
        word_list= nltk.word_tokenize(pattern) #Tokenize means making a sentence in form of token for example sentence 'Fire in the house' will become 'Fire', 'in', 'the', 'house'
        words.extend(word_list)
        documents.append((word_list, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

words=[lemmatizer.lemmatize(word) for word in words if word not in ignore_letters]
words= sorted(set(words))
print(words)
classes=sorted(set(classes))
print(classes)
pickle.dump(words,open('words.pkl','wb'))
pickle.dump(classes,open('classes.pkl','wb'))

training=[]
output_empty=[0]*len(classes)

for document in documents: 
    bag=[]
    word_patterns=document[0]
    word_patterns=[lemmatizer.lemmatize(word.lower()) for word in word_patterns]
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)

    output_row=list(output_empty)
    output_row[classes.index(document[1])]=1

    training.append([bag,output_row])

random.shuffle(training)
print(training)
training=np.array(training,dtype=object)
train_x= list(training[:, 0]) 
train_y= list(training[:, 1])

model=Sequential()
model.add(Dense(128,input_shape=(len(train_x[0]),),activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64,activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]),activation='softmax'))

sgd=SGD(lr=0.01, decay=1e-6,momentum=0.9,nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd,metrics=['accuracy'])
print(train_x)
print(train_y)
hist=model.fit(np.array(train_x), np.array(train_y),epochs=300,batch_size=5,verbose=1)
model.save('threat-detect.h5',hist)
print("Done")