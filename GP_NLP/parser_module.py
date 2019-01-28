from nltk.parse.corenlp import *
from nltk import sent_tokenize
import json
from stanfordcorenlp import StanfordCoreNLP
import os
class parser_module(object):
    def __init__(self):
        '''
        The server needs to know the location of the following files:
            - stanford-corenlp-X.X.X.jar
            - stanford-corenlp-X.X.X-models.jar
        '''
        print("Starting the server ...")
        STANFORD = os.path.join("F:\\fourth_year\GP", "stanford-corenlp-full-2018-10-05")
        print(STANFORD)
        # Create the server
        server = CoreNLPServer(
        os.path.join(STANFORD, "stanford-corenlp-3.9.2.jar"),
        os.path.join(STANFORD, "stanford-corenlp-3.9.2-models.jar"),
        )

        # Start the server in the background
        #server.start()
        print("The server started successfully ...")

    '''
    This function uses CoreNLP parser 
    Input: text
    Output: dependency list
    '''
    def parse(self,text):
        dep_list=[]
        nlp = StanfordCoreNLP(r'F:\\fourth_year\GP\stanford-corenlp-full-2018-10-05', quiet=False)
        props = {'annotators': 'coref', 'pipelineLanguage': 'en'}
        result = json.loads(nlp.annotate(text, properties=props))
        num, mentions = result['corefs'].items()[0]
        for mention in mentions:
            print("we are getting the mentions",mention)

        sentences=sent_tokenize(text)
        for sentence in sentences:

            # getting the dependency tree
            parser = CoreNLPDependencyParser()
            parse = next(parser.raw_parse(sentence))
            # convert it to list
            dep_list.append(list(parse.triples()))
        return dep_list



    def stop(self):
        # Stop the CoreNLP server# Stop the CoreNLP server
        self.server.stop()



