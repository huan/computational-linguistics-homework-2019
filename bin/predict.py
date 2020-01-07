'''
predict
'''
from gensim import models


if __name__ == '__main__':
  predict()


def predict() -> None:
  '''
  predict
  '''
  model = models.Word2Vec.load("./data/wikimodel.model")

  data_file = open('./data/pku_sim_test.txt', 'r+', encoding='utf-8')
  result = open("./data/result.txt", 'w', encoding='utf-8')

  for line in data_file.readlines():
    wordpair = line.strip('\n').encode('utf-8').decode('utf-8-sig').split()
    if wordpair[0] in model and wordpair[1] in model:
      similarity = model.similarity(wordpair[0], wordpair[1])
      result.write(
          str(wordpair[0])+
          '\t'+
          str(wordpair[1])+
          '\t'+
          str(similarity)+
          '\n'
      )
    else:
      result.write(
          str(wordpair[0])+
          '\t'+
          str(wordpair[1])+
          '\t'+
          'OOV'+
          '\n'
      )

  data_file.close()
  result.close()
