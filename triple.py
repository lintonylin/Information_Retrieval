from stanfordcorenlp import StanfordCoreNLP
import extract_tacred_bert_softmax

nlp = StanfordCoreNLP('./stanford-corenlp-full-2018-02-27')


def NER(sentence):

    tokens = nlp.word_tokenize(sentence)
    ner = nlp.ner(sentence)
    entities = []
    entity = ''
    pos = []
    lasttype = 'O'
    i = 0
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
    return tokens, entities

def triple(sentence):
    tokens, entities = NER(sentence)
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
            pred, score = extract_tacred_bert_softmax.extract(query)
            if score > maxscore:
                result = [entities[i]['name'], pred, entities[j]['name']]
                maxscore = score
                # print(result)

    return result


if __name__ == '__main__':
    sentence = "Anna Mae Pictou Aquash , a Mi ` kmaq Indian from Canada , was brutally murdered in 1975."
    triples = triple(sentence)
    print('triples:')
    print(triples)
