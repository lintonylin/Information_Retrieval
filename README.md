# Information_Retrieval
Directly extract relation triples from raw text. Running on Linux.
## Example
### Demo
We prepared a [demo website](http://34.105.38.103:8081/demo/). You can input some sentences to get relation triples.

### Simple Usage
```
python triple.py
```
or 
```python
import triple
triple.triple("Ivanka is the daughter of Trump. Trump is the father of Ivanka.")
```

## Prerequisites
Linux Shell

Java 1.8+ (Check with command: `java -version`) ([Download Page](http://www.oracle.com/technetwork/cn/java/javase/downloads/jdk8-downloads-2133151-zhs.html))

Python 3

CUDA >= 9.0 (Check with command: `nvcc --version`)([Download Page](https://developer.nvidia.com/cuda-downloads))

## Installation

### 1. Install OpenNRE
Clone the repository from OpenNRE github page:
```
git clone https://github.com/thunlp/OpenNRE.git --depth 1
```
Copy modified frame into OpenNRE:
```bash
cp sentence_re.py OpenNRE/opennre/framework/sentence_re.py
```
Then install OpenNRE:
```bash
cd OpenNRE
pip install -r requirements.txt
python setup.py install 
cd ..
```
Download Pretrained file:
```bash
cd pretrain
bash download_bert.sh
cd ..
```

### 2. Install Stanfordcorenlp and NLTK
Install using pip:
```
pip install stanfordcorenlp
```
Download and upzip Stanfordcore:
```
wget -c http://nlp.stanford.edu/software/stanford-corenlp-full-2018-02-27.zip
upzip stanford-corenlp-full-2018-02-27.zip
rm stanford-corenlp-full-2018-02-27.zip
```
Then install NLTK:
```
pip install nltk
```
Download tokenizer:
```python
python
import nltk
nltk.download('punkt')
exit()
```

### 3. Data Prepare
Due to copyright of the Tacred data, we are not able to share the data or our distant supervision based crawled data with you, please download it by yourself.

Get Stanford Tacred Data(https://nlp.stanford.edu/projects/tacred/) and put train.json, dev.json, test.josn under benchmark/tacred, then processing data:

```
cd ./benchmark/tacred
python data.py
cd ../../
```
If you want to crawl distant supervised data by Google search engine, please do as following steps:

1). Use Google Search API to crawl articles based on distant supervision.
Please modify the api key and filename in google_crawling.py.

```
python ./Google_Crawler/google_crawling.py
```
2).Split the target sentences from the articles.
Please modify the filename in processing.py.

```
python ./Google_Crawler/processing.py
```


## Train model(For Training Only)
If you want to train your own model, follow this step.

Run python file to start training:
```
python train_tacred_bert_softmax.py
```
Please modify batch size in line 44 in order to match the graphic memory on your machine.

## Usage
Download pretrained model file:
```bash
mkdir ckpt
cd ckpt
wget -c https://www.dropbox.com/s/7f70dy2vatmmly4/tacred_bert_softmax.pth.tar
cd ..
```
Then, simply run
```python
python triple.py
```
to get relation triples from raw sentence.


To run on a server:
```bash
python server.py --port 12345
```
Change the port and send GET request to server to get result like:
```
localhost:12345?content=Ivanka is the daughter of Trump. Trump is the father of Ivanka.
```

## Performance
model | f1-score 
:-: | :-: 
BERT-OpenNRE(Origin TARED Data) | 0.809 
BERT-OpenNRE(Crawled Data based on distant supervision) | 0.72
BERT-OpenNRE(Origin TARED Data + Crawled Data based on distant supervision) | 0.815
