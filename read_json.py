
import pandas as pd
import json
import os

root = '/Users/laura/Documents/GitHub/Thesis/'

publishers = ['ap',
              'cnn',
              'dm',
              'fox',
              'npr',
              'nyp',
              'nyt',
              'reuters',
              'vox'
]

df = pd.DataFrame(columns=['id','publisher','label','title','link','section','data','body'])

for publisher in publishers:

    # print(publisher)

    path = root + publisher + '/'

    files = os.listdir(path)

    for file in files:
        if file == '.DS_Store': # ignore .DS_Store
            pass
        else:
            j_file = file

    filepath = path + j_file

    with open(filepath) as json_file:
        data = json.load(json_file)

    data = data['articles']

    df_pub = pd.DataFrame.from_dict(data)

    df = df.append(df_pub)

print(df['publisher'].unique())

print(df)

print(df.shape)

