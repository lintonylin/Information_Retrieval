import requests
import json
import csv
from newspaper import Article

with open('/Users/maggiemin/Documents/525/re_subj_obj.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    data= [row for row in reader]
    query = []
    #print(data)
    for i in range(len(data)):
        query.append(data[i][2]+' '+data[i][1])

url = "https://google-search5.p.rapidapi.com/get-results"
#https://rapidapi.com/19venture/api/google-search5

headers = {
    'x-rapidapi-host': "google-search5.p.rapidapi.com",
    'x-rapidapi-key': "******"
    }

text = {}
i = 0
for q in query:
    querystring = {"country":"us","offset":"0","hl":"en-US","q":q}
    try:
        response = requests.request("GET", url, headers=headers, params=querystring)
    except:
        print('failed to search')
        text[q] = []
        i+=1
        continue
    try:
        results = response.json()['results']['organic_results']
        text[q] = []
    except:
        print('failed to search')
        text[q] =[]
        i+=1
        continue
    for result in results:
        URL = result['url']
        #print(URL)
        article = Article(URL)
        try:
            article.download()
            article.parse()
            article.nlp()
            text[q].append(article.text)
        except:
            print('***FAILED TO DOWNLOAD***', article.url)
            continue
    with open('/Users/maggiemin/Documents/525/articles.json', 'w') as f:
        json.dump(text, f)

    print(i)
    i+=1

print(text[query[0]])
print(len(text))



