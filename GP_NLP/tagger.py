from nltk import word_tokenize,pos_tag

class tagger (object):
    def __init__(self):
        print("Starting tagger ...")
        self.msg=""
        self.tokens=""

    #this function apply pos tagger
    #inputs: msg
    #output: tags
    def get_tags(self,m):
        self.msg=m
        self.get_tokens()
        self.tags=pos_tag(self.tokens)
        return self.tags

    # this function get the tokens
    def get_tokens(self):
        self.tokens=word_tokenize(self.msg)

    def get_nouns(self,tags):
        nouns=[]
        for i in range(len(tags)):
            if tags[i][1]=='NN' or tags[i][1]=='NNS'\
                or tags[i][1]=='NNP' or tags[i][1]=='NNPS':
                nouns.append(tags[i][0])
        return nouns


