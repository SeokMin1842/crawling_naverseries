import pandas as pd
from sklearn.metrics.pairwise import linear_kernel
from scipy.io import mmread
import pickle
from konlpy.tag import Okt
import re
from gensim.models import Word2Vec

def getRecommendation(cosin_sim):
    simScore = list(enumerate(cosin_sim[-1]))
    simScore = sorted(simScore, key=lambda x:x[1], reverse=True)
    simScore = simScore[:11]
    movieIdx = [i[0] for i in simScore]
    recMovieList = df_reviews.iloc[movieIdx, 0]
    return recMovieList

df_reviews = pd.read_csv('./crawling_data/')
Tfidf_matrix = mmread('./models/').tocsr()
with open('./models/', 'rb') as f:
    Tfidf = pickle.load(f)

okt = Okt()
sentence = '화려한 액션과 소름 돋는 반전이 있는 영화'
review = re.sub('[^가-힣 ]', ' ', sentence)

token = okt.pos(review, stem=True)

df_token = pd.DataFrame(token, columns=['word', 'class'])
df_token = df_token[(df_token['class'] == 'Noun') |
                    (df_token['class'] == 'Verb') |
                    (df_token['class'] == 'Adjective')]
words = []
for word in df_token.word:
    if 1 < len(word):
        words.append(word)
cleaned_sentence = ' '.join(words)
print(cleaned_sentence)
sentence_vec = Tfidf.transform([cleaned_sentence])
cosine_sim = linear_kernel(sentence_vec, Tfidf_matrix)
recommendation = getRecommendation(cosine_sim)
print(recommendation)