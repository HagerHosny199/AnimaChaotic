from nltk.parse.corenlp import *
from nltk import sent_tokenize
import json
from stanfordcorenlp import StanfordCoreNLP
import os
class parser_module(object):
    def __init__(self):
        print("Starting the server ...")
        self.nlp = StanfordCoreNLP(r'/content/stanford-corenlp-full-2018-10-05', quiet=True)
        print("The server started successfully ...")

    '''
    This function uses CoreNLP parser 
    Input: text
    Output: dependency list
    '''
    def parse(self,text):
        dep_list=[]
        props = {'annotators': 'coref'}
        result = json.loads(self.nlp.annotate(text, properties=props))
        mentions = result['corefs'].items()
        #for mention in mentions:
         #   print("we are getting the mentions",mention)
        return mentions



    def stop(self):
        # Stop the CoreNLP server# Stop the CoreNLP server
        self.server.stop()

