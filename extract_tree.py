#! /bin/python
#-*- coding:utf-8 -*-

import nltk

class Treeinfo():
    def __init__(self):   
        self.treelabel = []
        self.pos = []
        self.ROOT = 'ROOT'
        self.orderedpos = []
        self.word = []
    def get_nodes(self,parent):

        for node in parent:
            if type(node) is nltk.Tree:
                if node.height() > 2:
                    self.treelabel.append(node.label())
                    #print "Label:", node.label()
                elif node.height() == 2:
                    self.pos.append((node.label()))
                    #print node.leaves
                    #print node.label()

                self.get_nodes(node)
            else:
                self.word.append(node)
    
                
    def ordered_pos(self,wordlist):
        for w in wordlist:
            for p in self.pos:
                if w == "".join(p[1]):
                    self.orderedpos.append(p[0])
        #print len(self.orderedpos)

if __name__ == "__main__":
    pass