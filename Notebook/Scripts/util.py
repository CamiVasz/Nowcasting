import pandas as pd
import os

test = os.listdir('test_labels')
train = os.listdir('train_labels')

test_labels = pd.DataFrame()
train_labels = pd.DataFrame()

test_labels = pd.concat([pd.read_csv('test_labels/'+i, index_col = 0) 
                         for i in test]).drop_duplicates()
print('Hemos creado la test')

train_labels = pd.concat([pd.read_csv('train_labels/'+i, index_col = 0) 
                         for i in train]).drop_duplicates()
print('Hemos creado la train')

f = set(open('t.txt', 'r').read().split('\n'))

test_labels = test_labels[test_labels.index.to_series().apply(lambda x: x in f)]
print('Test conseguido')

train_labels = train_labels[train_labels.index.to_series().apply(lambda x: x in f)]
print('Train conseguido')

test_labels.to_csv('test_labels.csv')
train_labels.to_csv('train_labels.csv')

