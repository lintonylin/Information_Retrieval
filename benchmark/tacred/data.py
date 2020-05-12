import json
from tqdm import tqdm
import codecs

rel2id = codecs.open('tacred_rel2id.json', 'w', encoding='utf-8')

train = json.load(codecs.open('train.json', 'r', encoding='utf-8'))
dev = json.load(codecs.open('dev.json', 'r', encoding='utf-8'))
test = json.load(codecs.open('test.json', 'r', encoding='utf-8'))

train_data = codecs.open('tacred_train.txt', 'w', encoding='utf-8')
val_data = codecs.open('tacred_val.txt', 'w', encoding='utf-8')
test_data = codecs.open('tacred_test.txt', 'w', encoding='utf-8')

relations = {}

i = 0
for data in train:
    if data['relation'] == 'no_relation':
        continue
    if data['relation'] not in relations:
        relations[data['relation']] = i
        i = i + 1

json.dump(relations, rel2id)
rel2id.close()

for data in tqdm(train):
    if data['relation'] == 'no_relation':
        continue
    d = {}
    d['token'] = data['token']
    d['relation'] = data['relation']
    h = {}
    t = {}
    object = ''
    for i in range(data['obj_start'], data['obj_end'] + 1):
        object = object + data['token'][i] + ' '
    object = object[:-1]
    subject = ''
    for i in range(data['subj_start'], data['subj_end'] + 1):
        subject = subject + data['token'][i] + ' '
    subject = subject[:-1]
    h['name'] = subject
    h['pos'] = [data['subj_start'], data['subj_end']]
    t['name'] = object
    t['pos'] = [data['obj_start'], data['obj_end']]
    d['h'] = h
    d['t'] = t
    train_data.write(json.dumps(d))
    train_data.write('\n')


for data in tqdm(dev):
    if data['relation'] == 'no_relation':
        continue
    d = {}
    d['token'] = data['token']
    d['relation'] = data['relation']
    h = {}
    t = {}
    object = ''
    for i in range(data['obj_start'], data['obj_end'] + 1):
        object = object + data['token'][i] + ' '
    object = object[:-1]
    subject = ''
    for i in range(data['subj_start'], data['subj_end'] + 1):
        subject = subject + data['token'][i] + ' '
    subject = subject[:-1]
    h['name'] = subject
    h['pos'] = [data['subj_start'], data['subj_end']]
    t['name'] = object
    t['pos'] = [data['obj_start'], data['obj_end']]
    d['h'] = h
    d['t'] = t
    val_data.write(json.dumps(d))
    val_data.write('\n')


for data in tqdm(test):
    if data['relation'] == 'no_relation':
        continue
    d = {}
    d['token'] = data['token']
    d['relation'] = data['relation']
    h = {}
    t = {}
    object = ''
    for i in range(data['obj_start'], data['obj_end'] + 1):
        object = object + data['token'][i] + ' '
    object = object[:-1]
    subject = ''
    for i in range(data['subj_start'], data['subj_end'] + 1):
        subject = subject + data['token'][i] + ' '
    subject = subject[:-1]
    h['name'] = subject
    h['pos'] = [data['subj_start'], data['subj_end']]
    t['name'] = object
    t['pos'] = [data['obj_start'], data['obj_end']]
    d['h'] = h
    d['t'] = t
    test_data.write(json.dumps(d))
    test_data.write('\n')

train_data.close()
val_data.close()
test_data.close()
