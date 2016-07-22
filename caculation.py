#! /bin/python
#-*- coding:utf-8 -*

import numpy

def wer(r, h):
    #build the matrix
    d = numpy.zeros((len(r)+1)*(len(h)+1), dtype=numpy.uint8).reshape((len(r)+1, len(h)+1))
    for i in range(len(r)+1):
        for j in range(len(h)+1):
            if i == 0: 
                d[0][j] = j
            elif j == 0:
                d[i][0] = i
    for i in range(1,len(r)+1):
        for j in range(1, len(h)+1):
            if r[i-1] == h[j-1]:
                d[i][j] = d[i-1][j-1]
            else:
                substitute = d[i-1][j-1] + 1
                insert = d[i][j-1] + 1
                delete = d[i-1][j] + 1
                d[i][j] = min(substitute, insert, delete)

    result = 1-float(d[len(r)][len(h)]) / len(r) 
    return result                  

def fscore (test,ref):
    common = []
    for i in test:
            if i in ref:
                common.append(i)
                ref.remove(i)
    
    tp = len(common)
    fp = len(test) - tp 
    fn = len(ref)
    if tp>0:
        precision=float(tp)/(tp+fp)
        recall=float(tp)/(tp+fn)
        return 2*((precision*recall)/(precision+recall))
    else:
        return 0
        

def weighted_average(alpha,beta,gamma,tree_score,pos_score,vocabulary_score):
    score = (alpha*tree_score+beta*pos_score+gamma*vocabulary_score)/(alpha+beta+gamma)
    return score
