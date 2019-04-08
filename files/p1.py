from gensim.models import KeyedVectors

model = KeyedVectors.load_word2vec_format('/home/marcinek/zmodyfikowany.txt', binary=False)

result = model.most_similar_cosmul(positive=['woman', 'king'], negative=['man'])

man = model['man']

woman = model['woman']

man

woman

import numpy as np
import math
def euclidean_similarity(v1,v2):
    if len(v1) != len(v2):
        raise Exception
    res_v = []
    for i in range(len(v1)):
        res_v.append(v1[i] - v2[i])
        
    d = np.sqrt(np.sum(np.power(res_v,2)))
    return d

euclidean_similarity(man,woman)

def cosine_similarity(v1, v2):
    if len(v1) != len(v2):
        raise Exception
    res_x = []
    res_a = []
    res_b = []
    for i in range(len(v1)):
        res_x.append(v1[i]*v2[i])
        res_a.append(v1[i]*v1[i])
        res_b.append(v2[i]*v2[i])
    
    d = np.sum(res_x)/(np.sqrt(np.sum(res_a))*np.sqrt(np.sum(res_a)))
    return d
def cosine_similarity2(v1, v2):
    if len(v1) != len(v2):
        raise Exception
    sim = np.sum(np.dot(v1,v2)) / (np.sqrt(np.sum(np.power(v1,2))) * np.sqrt(np.sum(np.power(v2,2))))
    return sim

print(cosine_similarity2(man, woman))
cosine_similarity(man, woman)
