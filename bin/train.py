'''
train
'''
from gensim.models import word2vec
from chinese_distance import preprocess


if __name__ == '__main__':
  train()


def train():
  '''train'''
  preprocess.parse(
      './data/extracted/AA/wiki_00/wiki0',
      './data/extracted/AA/wiki0',
  )
  print('1/3')

  preprocess.parse(
      './data/extracted/AA/wiki_01/wiki_1',
      './data/extracted/AA/wiki1',
  )
  print('2/3')

  preprocess.merge()
  print('3/3')

  sentences = word2vec.LineSentence('./data/wikicorpus')
  model = word2vec.Word2Vec(
      sentences,
      size=100,
      window=2,
      sg=1,
      workers=8,
  )
  model.save('./data/wikimodel.model')

  print('done')
