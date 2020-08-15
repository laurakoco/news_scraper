
import pandas as pd
import json
import os
from matplotlib import pyplot as plt

def plot_things(df):

    # percentage of articles per label
    plt.figure()
    x = df['label'].value_counts(normalize=True)
    plt.pie(x.values,labels=list(x.keys()),autopct='%1.1f%%')

    # percentage of articles per section
    plt.figure()
    x = df['section'].value_counts(normalize=True)
    plt.pie(x.values,labels=list(x.keys()),autopct='%1.1f%%')


    print('foo')


root = '/Users/laura/Documents/GitHub/news_scraper/'

publishers = ['ap',
              'bh',
              'cnn',
              'cp',
              'dm',
              'guardian',
              'fox',
              'msnbc',
              'npr',
              'nyp',
              'nyt',
              'politico',
              'reuters',
              'vox',
              'washpost'
]

df = pd.DataFrame(columns=['id','publisher','label','title','link','section','date','body'])

for publisher in publishers:

    # print(publisher)

    path = root + publisher + '/'

    files = os.listdir(path)

    for file in files:

        if file == publisher+'.json':
            j_file = file

    filepath = path + j_file

    with open(filepath) as json_file:
        data = json.load(json_file)

    data = data['articles']

    df_pub = pd.DataFrame.from_dict(data)

    df = df.append(df_pub)

df = df.drop_duplicates(subset='title')
df.reset_index()

print(df['publisher'].unique())

print(df)

print(df.shape)

plot_things(df)

# df.to_csv('data.csv',encoding='utf-8-sig',index=False)

plt.show()