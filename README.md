# Information_Retrieval
Directly extract relation triples from raw text. Based on Stanford TACRED Data and Distant Supervision. Running on Linux.
## Example
### Simple Usage
```python
python triple.py
```

## Prerequisites
Linux Shell

Java 1.8+ (Check with command: `java -version`) ([Download Page](http://www.oracle.com/technetwork/cn/java/javase/downloads/jdk8-downloads-2133151-zhs.html))

Python 3

CUDA >= 9.0 (Check with command: `nvidia-smi`)([Download Page](https://developer.nvidia.com/cuda-downloads))

## Installation

### 1. Install OpenNRE
Clone the repository from OpenNRE github page:
```
git clone https://github.com/thunlp/OpenNRE.git --depth 1
```
Copy modified frame into OpenNRE:
```
cp sentence_re.py OpenNRE/opennre/framework/sentence_re.py
```
Then install OpenNRE:
```
cd OpenNRE
pip install -r requirements.txt
python setup.py install 
cd ..
```
Download Pretrained file:
```
cd pretrain
bash download_bert.sh
```

### 2. Install Stanfordcorenlp
Install using pip:
```python
pip install stanfordcorenlp
```
Download and upzip Stanfordcore:
```
wget -c http://nlp.stanford.edu/software/stanford-corenlp-full-2018-02-27.zip
upzip stanford-corenlp-full-2018-02-27.zip
```

### 3. Data Prepare(For Training Only)
If you want to train your own model, follow this step.

Due to copyright of the Tacred data, we are not able to share the data or our distant supervision based crawled data with you, please download it by yourself.

Get Stanford Tacred Data(https://nlp.stanford.edu/projects/tacred/) and put train.json, dev.json, test.josn under benchmark/tacred, then processing data:

```
cd ./benchmark/tacred
python data.py
cd ../../
```

## Train model(For Training Only)
If you want to train your own model, follow this step.

Run python file to start training:
```python
python train_tacred_bert_softmax.py
```
Please modify batch size in line 44 in order to match the graphic memory on your machine.

## Usage
Download pretrained model file:
```bash
mkdir ckpt
cd ckpt
wget -c 
```
Then, simply run
```python
python triple.py
```
to get relation triples from raw sentence.