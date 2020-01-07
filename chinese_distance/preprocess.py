'''preprocess'''
import re
import jieba

def get_stopwords():
  '''stop words'''
  stopwords_set = set()
  with open('./data/stopwords.txt', 'r', encoding='utf-8') as file:
    for word in file:
      stopwords_set.add(word.strip('\n'))

  return  stopwords_set


def parse(input_path, output_path):
  '''parse the text'''
  regex_str = "[^<doc.*>$]|[^</doc>$]"
  input_file = open(input_path, 'r', encoding='utf-8')
  output_file = open(output_path, 'w', encoding='utf-8')

  content_line = input_file.readline()

  stopwords = get_stopwords()
  cleaned_content = ''

  while content_line:
    matched = re.match(regex_str, content_line)
    content_line = content_line.strip('\n')
    if len(content_line) > 0:
      if matched:
        words = jieba.cut(content_line, cut_all=False)
        # get rid of stop word
        for word in words:
          if word not in stopwords:
            cleaned_content += word + ' '
      else:
        if len(cleaned_content) > 0:
          output_file.write(cleaned_content+ '\n')
          cleaned_content = ''
    content_line = input_file.readline()

  input_file.close()
  output_file.close()


def merge():
  '''merge the files'''
  input_file_prefix = './data/extracted/AA/wiki'
  output_file = open('./data/wikicorpus', 'w', encoding='utf-8')
  for i in range(2):
    file_path = input_file_prefix + str(i)
    input_file = open(file_path, 'r', encoding='utf-8')

    line = input_file.readline()
    while line:
      output_file.writelines(line)
      line = input_file.readline()
    input_file.close()
  output_file.close()
