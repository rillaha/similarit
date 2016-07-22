#! /bin/python
#-*- coding:utf-8 -*-

import os
from nltk.parse import stanford
from nltk.tree import Tree
from time import time

#Stanford Parser is conposed of constituent parser("con"),dependency parser("de")and nueral parser("neu")
#language choices are Chinese,English,French,German,and Spanish
class Parser():
    def __init__(self):
        self.parser = ""
    def setlang(self,lang,kind):
        os.environ['STANFORD_PARSER'] = '/home/bear/Downloads/parser/stanford-parser-full-2015-12-09/'
        os.environ['JAVA_HOME'] = '/usr/lib/jvm/jdk1.8.0_91/jre/jre/bin/'
        os.environ['STANFORD_MODELS'] = '/home/bear/Downloads/parser/stanford-parser-full-2015-12-09/stanford-parser-3.6.0-models.jar'
        if lang == "English":
            if kind == "con":
                self.parser = stanford.StanfordParser(model_path="/home/bear/Downloads/parser/stanford-parser-full-2015-12-09/stanford-parser-3.6.0-models/edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz")
            elif kind == "de":
                pass
            elif kind == "neu":
                pass
        elif lang == "Chinese":
            if kind == "con":
                self.parser = stanford.StanfordParser(model_path="/home/bear/Downloads/parser/stanford-parser-full-2015-12-09/stanford-parser-3.6.0-models/edu/stanford/nlp/models/lexparser/chineseFactored.ser.gz")
            elif kind == "de":
                pass
            elif kind == "neu":
                pass
        elif lang == "French":
            if kind == "con":
                self.parser = stanford.StanfordParser(model_path="/home/bear/Downloads/parser/stanford-parser-full-2015-12-09/stanford-parser-3.6.0-models/edu/stanford/nlp/models/lexparser/frenchFactored.ser.gz")
            elif kind == "de":
                pass
            elif kind == "neu":
                pass
        elif lang == "German":
            if kind == "con":
                self.parser = stanford.StanfordParser(model_path="/home/bear/Downloads/parser/stanford-parser-full-2015-12-09/stanford-parser-3.6.0-models/edu/stanford/nlp/models/lexparser/germanPCFG.ser.gz")
            elif kind == "de":
                pass
            elif kind == "neu":
                pass
        elif lang == "Spanish":
            if kind == "con":
                self.parser = stanford.StanfordParser(model_path="/home/bear/Downloads/parser/stanford-parser-full-2015-12-09/stanford-parser-3.6.0-models/edu/stanford/nlp/models/lexparser/spanishPCFG.ser.gz")
            elif kind == "de":
                pass
            elif kind == "neu":
                pass  
               
