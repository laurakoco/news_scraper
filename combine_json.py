
import pandas as pd
import json
import os

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
              'usatoday',
              'vox',
              'washpost'
]

for publisher in publishers:

    df = pd.DataFrame(columns=['id', 'publisher', 'label', 'title', 'link', 'section', 'date', 'body'])

    print(publisher)

    path = root + publisher + '/'

    files = os.listdir(path)

    for file in files:

        # remove existing file
        if file == publisher+'.json':
            os.remove(path+file)
            continue

        if file == '.DS_Store': # ignore .DS_Store
            continue

        else:
            j_file = file

        filepath = path + j_file

        with open(filepath) as json_file:
            data = json.load(json_file)

        data = data['articles']

        df_file = pd.DataFrame.from_dict(data)

        df = df.append(df_file)

    # df = df.sort_values('title')

    # drop duplicate titles
    df = df.drop_duplicates(subset='title')


    data = {}
    data['articles'] = []

    cnt = 0
    for index, row in df.iterrows():

        df.loc[index,'id'] = publisher + str(cnt)

        row_dict = row.to_dict()
        data['articles'].append(row_dict)

        cnt += 1



    filepath = publisher+'/'+publisher+'.json'
    with open(filepath, 'w') as outfile:
        json.dump(data, outfile, ensure_ascii=False)

