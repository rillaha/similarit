#! /bin/python
#-*- coding:utf-8 -*-

import parse
import alignment
import caculation
import extract_tree
import codecs
from nltk import Tree

#use stanford parser
def get_tree(sen,lang,kind):
    p = parse.Parser()
    p.setlang(lang, kind)
    tree = p.parser.raw_parse(sen.lower())
    return tree

#extract labels and leaves
def get_treeinfo(tree):
    t = extract_tree.Treeinfo()
    t.get_nodes(tree)
    return t.treelabel,t.pos,t.word



def score_similarity(htree,rtree): 

    hlabel,hpos,hword = get_treeinfo(htree)
    rlabel,rpos,rword = get_treeinfo(rtree)

    tree_score = caculation.fscore(hlabel, rlabel)
    pos_score = caculation.wer(hpos, rpos)
    vocabulary_score = caculation.fscore(hword,rword)
    score = caculation.weighted_average(0.35, 0.35, 0.3, tree_score, pos_score, vocabulary_score)  
    return score,hword,rword

def print_alignment(hyp,ref):
    a = alignment.Alignment()
    a.align(hyp,ref) #input is string!!!
    print "Formatted hypothesis: ", a.hstring
    print "Formatted reference: ", a.rstring
    print "Substitution: ",a.numSub,"Insertion: ",a.numIns,"Deletion: ",a.numDel
    

def read_treefile(hyptreefile,reftreefile):
    hfile = codecs.open(hyptreefile,"r",encoding='utf-8')
    rfile = codecs.open(reftreefile,"r",encoding='utf-8')
    scoredic = {}
    #store rtree into rtreelist suppose there are more than one reference
    rtreel = []
    for i in rfile:
        refl = []
        if i.strip() != "":
            refl.append(i.strip())
            rstr = " ".join(refl)
            rtree = Tree.fromstring(rstr)
        rtreel.append(rtree)
    #store hyptree into hyplist    
    htreel = []
    senl = []
    for i in hfile:
        if i.strip() != "":
            senl.append(i.strip())
        else:
            htreel.append(Tree.fromstring(" ".join(senl)))
            senl = []
            
    #loop and score
    for r in rtreel:
        for h in htreel:
            score,hword,rword= score_similarity(h,r)
            scoredic[" ".join(hword)] = score
            
    return scoredic     

    
def sort_scoredic(scoredic):
    order = sorted(scoredic, key=scoredic.get, reverse=True)
    #print "score time:", round(time()-t0, 3), "s"            
    for i in range(15):
        if i < len(order):
            print "key:", order[i],"value: ", scoredic[order[i]] 
                            

def read_rawfile(hyprawfile,refrawfile):
    scoredic = {}
    cnt = 0
    for i in refrawfile:
        for j in hyprawfile:
            cnt += 1
            print cnt
            hyp = j.strip()
            ref = i.strip()
            
            htree = get_tree(hyp, "English","con") #constituent parser
            rtree = get_tree(ref, "English","con")
            
            score,hword,rword = score_similarity(htree,rtree)
            scoredic[" ".join(hword)] = score
            
    return scoredic
    
if __name__ == "__main__":  
    #single sentence test
#     hyp = "The stock posted a multi-year low of under $10 in early 2009 before roaring to a recent high of nearly $75 in April 2014."
#     ref = "Before roaring to a recent high of nearly $75 in April 2014 the stock posted a multi-year low of under $10 in early 2009."
# 
#     htree = get_tree(hyp, "English","con") #constituent parser
#     rtree = get_tree(ref, "English","con")
# 
#     score,hword,rwprd = score_similarity(htree, rtree)
#     print score
#     print_alignment(hyp, ref)

    #rawfile test
#     hyprawfile = codecs.open("/home/work/Data/similartest/smallentest.txt","r",encoding='utf-8')
#     refrawfile = codecs.open("/home/work/Data/similartest/zhref.txt","r",encoding='utf-8')
#     scoredic = read_rawfile(hyprawfile, refrawfile)
#     sort_scoredic(scoredic)
    
    #treefile test
    hyptreefile = "/home/work/Data/similartest/twozhtest.parse"
    reftreefile = "/home/work/Data/similartest/onezhref.parse"
    scoredic = read_treefile(hyptreefile, reftreefile)
    sort_scoredic(scoredic)
    