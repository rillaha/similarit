#! /bin/python
#-*- coding:utf-8 -*-

import numpy

def wer(h,r):
    d = numpy.zeros((len(h)+1)*(len(r)+1), dtype=numpy.uint8)
    d = d.reshape((len(h)+1, len(r)+1))
    for i in range(len(h)+1):
        for j in range(len(r)+1):
            if i == 0:
                d[0][j] = j
            elif j == 0:
                d[i][0] = i

    # computation
    for i in range(1, len(h)+1):
        for j in range(1, len(r)+1):
            if h[i-1] == r[j-1]:
                d[i][j] = d[i-1][j-1]
            else:
                substitution = d[i-1][j-1] + 1
                insertion    = d[i][j-1] + 1
                deletion     = d[i-1][j] + 1
                d[i][j] = min(substitution, insertion, deletion)
                

    return d[len(h)][len(r)]
class Alignment():
    def __init__(self):
        self.ar = []
        self.ah = []            
        self.numSub = 0;
        self.numDel = 0;
        self.numIns = 0;
    
    def align(self,h,r):
        OK = 0
        SUB = 1
        INS = 2
        DEL = 3
    
        h = h.split(" ")
        r = r.split(" ")
        cost = numpy.zeros((len(r)+1)*(len(h)+1), dtype=numpy.uint8)
        cost = cost.reshape((len(r)+1, len(h)+1))
    
        backtrace = numpy.zeros((len(r)+1)*(len(h)+1), dtype=numpy.uint8)
        backtrace = backtrace.reshape((len(r)+1, len(h)+1))
    
        for i in range(len(r)+1):
            for j in range(len(h)+1):
                if i == 0:
                    cost[0][j] = j
                    backtrace[0][j] = INS
                elif j == 0:
                    cost[i][0] = i
                    backtrace[i][0] = DEL    
        
        for i in range(1,len(r)+1):
            for j in range(1,len(h)+1):
                subOp = ""
                cs = ""
                if r[i-1] == h[j-1]:
                    subOp = OK
                    cs = cost[i-1][j-1]
                else:
                    subOp = SUB
                    cs = cost[i-1][j-1]+1
                ci = cost[i][j-1] +1
                cd = cost[i-1][j] +1
                mincost = min(cs, min(ci, cd));
                if cs == mincost:
                    cost[i][j] = cs;
                    backtrace[i][j] = subOp;
                elif ci == mincost:
                    cost[i][j] = ci;
                    backtrace[i][j] = INS;                    
                else :
                    cost[i][j] = cd;
                    backtrace[i][j] = DEL; 
        
        i = len(r);
        j = len(h);            
        while i > 0 or j > 0:
            if backtrace[i][j] == OK:
                self.ar.insert(0,r[i-1].lower())
                self.ah.insert(0,h[j-1].lower())
                i = i-1
                j = j-1
                
            elif backtrace[i][j] == SUB:
                self.ar.insert(0,r[i-1].upper())
                self.ah.insert(0,h[j-1].upper())
                i = i-1
                j = j-1
                self.numSub = self.numSub+1
                
            elif backtrace[i][j] == INS:
                self.ar.insesrt(0,None)
                self.ah.insert(0,h[j-1])
                j = j-1
                self.numIns = self.numIns+1
                
            elif backtrace[i][j] == DEL:
                self.ar.insert(0,r[i-1].upper())
                self.ah.insert(0,None)
                i = i-1
                self.numDel = self.numDel+1

def fscore (test,ref):

    tp = 0.0
    for t in test:
        if t in ref:
            tp +=1
    
    precision = tp/len(ref)
    recall = tp/len(test)
    fscore = 2*precision*recall/(precision+recall)
        
    return fscore

def weighted_average(alpha,beta,gamma,tree_score,pos_score,vacabulary_score):
    score = (alpha*tree_score+beta*pos_score+gamma*vacabulary_score)/(alpha+beta+gamma)
    return score
    
if __name__ == "__main__":
    print weighted_average(10, 3, 4, 0.8, 0.3, 0.8)