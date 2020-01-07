# computational-linguistics-homework-2019

## Requirement

1. Python 3 or above
1. zhwiki-20191120-pages-articles-multistream.xml.bz2 - [zhwiki dump progress on 20191120](https://dumps.wikimedia.org/zhwiki/20191120/)
1. WikiExtractor - [A tool for extracting plain text from Wikipedia dumps](https://github.com/attardi/wikiextractor)
1. OpenCC - [Open Chinese Convert 開放中文轉換](https://github.com/BYVoid/OpenCC)
1. Stop Words - [中文常用停用词表（哈工大停用词表、百度停用词表等）](https://github.com/goto456/stopwords)

## Design

1. All the data will be saved in the `./data` directory, including the wiki data, temporary output files, and the final result.
1. `./chinese_distance/` is a Python module that encapsulate some preprocess operations.
1. `./bin/train.py` is the Python script that do the training process.
1. `./bin/predict.py` is the Python script that do the prediction process.

## Usage

### 1 Clean The Wiki Data

```sh
# Do Extract
python WikiExtractor.py -b 1000M -o extracted zhiwiki-20191120-pages-articles-multistream.xml
```

### 2 Convert the Traditional Chinese to Simple Chinese

```sh
# Install OpenCC
brew install homebrew

# Convert
opencc -i input_path -o output_path -c t2s.json
```

### 3 Tokenization (without Stop Words)

We using `jieba.cut(...)` to tokenize the words, and skip those _stop words_.

```python
        words = jieba.cut(content_line, cut_all=False)
        # get rid of stop word
        for word in words:
          if word not in stopwords:
            cleaned_content += word + ' '
```

### 4 Train Word2Vec

We are using `gensim` Python module API for `word2vec`.

```python
from gensim.models import word2vec
# ...
sentences = word2vec.LineSentence('./data/wikicorpus')
model = word2vec.Word2Vec(
    sentences,
    size=100,
    window=2,
    sg=1,
    workers=8,
)
model.save('./data/wikimodel.model')
```

### 5 Predict

```python
from gensim import models
model = models.Word2Vec.load("./data/wikimodel.model")
similarity = model.similarity(wordpair[0], wordpair[1])
```

## AUTHOR

Huan LI (李卓桓) 2018010143
