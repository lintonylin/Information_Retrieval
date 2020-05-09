# Information_Retrieval
Directly extract relation triples from raw text. Running on Linux.
## Example
### Simple Usage
```
python triple.py
```
or 
```python
import triple
triple.triple("Anna Mae Pictou Aquash , a Mi ` kmaq Indian from Canada , was brutally murdered in 1975.")
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

### 2. Install Stanfordcorenlp
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

### 3. Data Prepare
Due to copyright of the Tacred data, we are not able to share the data or our distant supervision based crawled data with you, please download it by yourself.

Get Stanford Tacred Data(https://nlp.stanford.edu/projects/tacred/) and put train.json, dev.json, test.josn under benchmark/tacred, then processing data:

```
cd ./benchmark/tacred
python data.py
cd ../../
```

Use Google Search API to crawl articles based on distant supervision.
Please modify the api key and filename in google_crawling.py.

```
python google crawling.py
```
Split the target sentences from the articles.
Please modify the filename in processing.py.

```
python processing.py
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
wget -c https://www.dropbox.com/s/yphpz4m761nn729/tacred_bert_softmax.pth.tar
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
localhost:12345?content=Baidu website: http://baidu.com
```
