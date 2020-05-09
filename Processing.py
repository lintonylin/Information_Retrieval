import requests
import json
import csv
from nltk.tag import StanfordPOSTagger
from nltk import word_tokenize

# Add the jar and model via their path (instead of setting environment variables) to StanfordPOSTagger:
jar = '/Users/maggiemin/Downloads/stanford-postagger-2018-10-16/stanford-postagger.jar'
model = '/Users/maggiemin/Downloads/stanford-postagger-2018-10-16/models/english-left3words-distsim.tagger'
pos_tagger = StanfordPOSTagger(model, jar, encoding='utf8')

#query data
with open('/Users/maggiemin/Documents/525/re_subj_obj.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    data= [row for row in reader]
    query = []
    #print(data)
    for i in range(len(data)):
        query.append(data[i][2]+' '+data[i][1])

#crawling data
with open('/Users/maggiemin/Documents/525/articles.json','r') as f:
    text = json.load(f)

#split the article
def sentence_split(str_centence):
    list_ret = list()
    for s_str in str_centence.split('.'):
        if '?' in s_str:
            list_ret.extend(s_str.split('?'))
        elif '!' in s_str:
            list_ret.extend(s_str.split('!'))
        elif '\n'in s_str:
            list_ret.extend(s_str.split('\n'))
        else:
            list_ret.append(s_str)

    return list_ret

#get plural
def plural(word):
    if word.endswith('y'):
        return word[:-1] + 'ies'
    elif word[-1] in 'sx' or word[-2:] in ['sh', 'ch']:
        return word + 'es'
    elif word.endswith('an'):
        return word[:-2] + 'en'
    else:
        return word + 's'

#get positon
def index_of_str(s1, s2):
    n1=len(s1)
    n2=len(s2)
    for i in range(n1-n2+1):
        if s1[i:i+n2]==s2:
            return [i,i+n2-1]

#define the output
output ={}
output["token"]=[]
output["relation"]=[]
output["h"]={}
output["t"]={}

m = 0
count = 0
for q in query:
    output["relation"] = data[m][0]
    output["h"]["name"] = data[m][2]
    output["t"]["name"] = data[m][1]
    try:
        if not len(text[q]) == 0:
            for i in range(len(text[q])):
                sentences = sentence_split(text[q][i])  # article to sentences
                for sentence in sentences:
                    search_keywords = [data[m][2], data[m][1]]
                    if (all(map(lambda word: word in sentence, search_keywords))):  # sentences we want
                        token = word_tokenize(sentence + '.')
                        s_token = word_tokenize(data[m][2])
                        o_token = word_tokenize(data[m][1])
                        s_position = index_of_str(token, s_token)
                        o_position = index_of_str(token, o_token)
                        if s_position is None:
                            s_token = word_tokenize(plural(data[m][2]))
                            s_position = index_of_str(token, s_token)
                        if o_position is None:
                            o_token = word_tokenize(plural(data[m][1]))
                            o_positon = index_of_str(token, o_token)
                        if s_position is not None:
                            if o_position is not None:
                                output["token"] = token
                                output["h"]["pos"] = s_position
                                output["t"]["pos"] = o_position
                                fw = open("/Users/maggiemin/Documents/525/tacred_train.txt", 'a')
                                fw.write(json.dumps(output))
                                fw.write('\n')
                                fw.close()
                                count += 1
    except:
        m += 1
        continue
    m += 1
    #if m % 100 == 0:
        #print(m)
print(count)












