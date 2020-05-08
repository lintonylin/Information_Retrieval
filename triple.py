from stanfordcorenlp import StanfordCoreNLP
from extract_tacred_bert_softmax import extract

nlp = StanfordCoreNLP('./stanford-corenlp-full-2018-02-27')


def NER(sentence):

    tokens = nlp.word_tokenize(sentence)
    ner = nlp.ner(sentence)
    # print(ner)
    entities = []
    entity = ''
    pos = []
    i = 0
    lasttype = 'O'
    for n in ner:
        if n[1] == 'O':
            if len(entity) != 0:
                e = {}
                pos.append(i-1)
                e['name'] = entity
                e['pos'] = pos
                entities.append(e)
                entity = ''
                pos = []
        else:
            if n[1] != lasttype:
                if lasttype == 'O':
                    entity = n[0]
                    pos = [i]
                    lasttype = n[1]
                    i = i + 1
                    continue
                e = {}
                pos.append(i-1)
                e['name'] = entity
                e['pos'] = pos
                entities.append(e)
                entity = n[0]
                pos = [i]
            else:
                entity = entity + ' ' + n[0]
        lasttype = n[1]
        i = i + 1
    if lasttype != 'O' and entity not in entities and len(entity) != 0:
        e = {}
        pos.append(i-1)
        e['name'] = entity
        e['pos'] = pos
        entities.append(e)
    return tokens, entities

def triple(sentence):
    tokens, entities = NER(sentence)
    # print(entities)
    if (len(entities)) <= 1:
        return []
    maxscore = -1
    result = []
    for i in range(0, len(entities)):
        for j in range(0, len(entities)):
            if i == j:
                continue
            query = {}
            query['token'] = tokens
            query['relation'] = 'per:title'
            query['h'] = {}
            query['h']['name'] = entities[i]['name']
            query['h']['pos'] = entities[i]['pos']
            query['t'] = {}
            query['t']['name'] = entities[j]['name']
            query['t']['pos'] = entities[j]['pos']
            pred, score = extract(query)
            if score > maxscore:
                result = [entities[i]['name'], pred, entities[j]['name']]
                maxscore = score
                # print(result)

    return result


if __name__ == '__main__':
    sentence = "Baidu website: http://baidu.com"
    triples = triple(sentence)
    print('triples:')
    print(triples)
    nlp.close()
