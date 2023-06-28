import pandas as pd
from pymorphy2 import MorphAnalyzer
from nltk.tokenize import word_tokenize
from string import punctuation

ih = pd.read_csv('ih.csv', delimiter=';')
ihniy = pd.read_csv('ihniy.csv', delimiter=';')

m = MorphAnalyzer()

def analyse_first_noun(context):
    if pd.isna(context):
        return ""
    words = word_tokenize(context.strip(punctuation))
    for word in words:
        par = m.parse(word)[0]
        if par.tag.POS == 'NOUN':
            tags = par.tag
            animacy = tags.animacy if tags.animacy else ''
            number = tags.number if tags.number else ''
            gender = tags.gender if tags.gender else ''
            return ' '.join([animacy, number, gender])

ih['grammatical_categories'] = ih['Right context'].apply(analyse_first_noun)
ihniy['grammatical_categories'] = ihniy['Right context'].apply(analyse_first_noun)

ih.to_csv('ih_parsed.csv')
ihniy.to_csv('ihniy_parsed.csv')