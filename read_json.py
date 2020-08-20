
import pandas as pd
import json
import os
from matplotlib import pyplot as plt

def plot_things(df):

    # df = DataFr

    # percentage of articles per label
    plt.figure()
    plt.title('Article by Label')
    x = df['label'].value_counts(normalize=True)
    labels = list(x.keys())
    plt.pie(x.values,labels=labels,autopct='%1.1f%%')

    # # plot section per label
    # for label in labels:
    #     plt.figure()
    #     # colors = ['lightskyblue', 'red', 'blue', 'green', 'gold', 'orange', 'yellow']
    #     plt.title('Section by Label: ' + label)
    #     df_label = df[df['label'] == label]
    #     x = df_label['section'].value_counts(normalize=True)
    #     my_labels = list(x.keys())
    #     plt.pie(x.values, labels=my_labels, autopct='%1.1f%%')

    # percentage of articles per section
    plt.figure()
    plt.title('Article by Section')
    x = df['section'].value_counts(normalize=True)
    labels = list(x.keys())
    plt.pie(x.values,labels=labels,autopct='%1.1f%%')

    print('foo')

root = '/Users/laura/Documents/GitHub/news_scraper/'

publishers = ['ap',
              'bh',
              'chicago',
              'cnn',
              'cp',
              'dc',
              'dm',
              'guardian',
              'fox',
              'marketwatch',
              'msnbc',
              'npr',
              'nyp',
              'nyt',
              'ohio',
              'people',
              'politico',
              'reuters',
              'sun',
              'tennessee',
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