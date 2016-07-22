#! /bin/python
#-*- coding:utf-8 -*-

import numpy
class Alignment():
    def __init__(self):
        self.ar = []
        self.ah = []            
        self.numSub = 0;
        self.numDel = 0;
        self.numIns = 0;
        self.rstring = ""
        self.hstring = ""
    
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
        while i > 0 or j > 0:#     treeinfo2 = Treeinfo()
#     print treeinfo2.get_nodes(rtree)
#     print treeinfo2.ordered_pos(rtree)
            if backtrace[i][j] == OK:
                self.ar.insert(0,r[i-1].lower())
                self.ah.insert(0,h[j-1].lower())
                i = i-1
                j = j-1
                
            elif backtrace[i][j] == SUB:
                self.ar.insert(0,r[i-1].upper()+">SUB")
                self.ah.insert(0,h[j-1].upper()+">SUB")
                i = i-1
                j = j-1
                self.numSub = self.numSub+1
                
            elif backtrace[i][j] == INS:
                self.ar.insert(0,"NONE")
                self.ah.insert(0,h[j-1]+">INS")
                j = j-1
                self.numIns = self.numIns+1
                
            elif backtrace[i][j] == DEL:
                self.ar.insert(0,r[i-1].upper()+">DEL")
                self.ah.insert(0,"NONE")
                i = i-1
                self.numDel = self.numDel+1
        self.rstring = " ".join(self.ar)
#         for a in self.ah:
#             print a
        self.hstring = " ".join(self.ah)

def testalign():
   
    tl = "This is the surprise"
    rl = "this is a big surprise"
    alignment = Alignment()
    alignment.align(tl,rl)
    print alignment.ah
    print alignment.ar
    print "Substitution: ",alignment.numSub,"Insertion: ",alignment.numIns,"Deletion: ",alignment.numDel
                    
if __name__ == "__main__":
    testalign()