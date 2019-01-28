from nltk import word_tokenize,pos_tag
from nltk import PorterStemmer
class tagger (object):
    def __init__(self):
        print("Starting tagger ...")
        self.msg=""
        self.tokens=""
        self.models=[]
        self.p=PorterStemmer()
        f=open("/content/models.txt", "r")
        fl =f.readlines()
        for x in fl:
          self.models.append(x)
        print(self.models)

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

    # this function finds the object name in the models list
    def find_model(self,name):
      name=name.lower()
      name=name.strip()
      name_stem=self.p.stem(name)
      for model in self.models:
        model=model.strip()
        if model==name:
          print(name,"founnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnd")
          return 1,model
        elif model==name_stem :
          print(name,"founnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnd")
          return 2,model
      print(name,"NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
      return 0,0

    # this functions modifies the nouns to have the database objects names
    def modify_objects(self,nouns):
      i=0
      for noun in nouns:
        out,model=self.find_model(noun)
        if out == 0:
          nouns[i]='0'
        else:
          nouns[i]=model
        i+=1
      return nouns



    # this function gets the nouns in the text based on their tags
    def get_nouns(self,tags):
        nouns=[]
        original=[]
        for i in range(len(tags)):
            if tags[i][1]=='NN' or tags[i][1]=='NNS' or tags[i][1]=='NNP' or tags[i][1]=='NNPS':
              #check if the noun is person (here we will add the NER)
              if tags[i][0]=='John':
                nouns.append('Boy')
              elif tags[i][0]=='Anne':
                nouns.append('Girl')
              else:
                nouns.append(tags[i][0])
              original.append(tags[i][0])
            #check personal pronouns
            elif tags[i][1]=='PRP':
              #adding a boy object
              if tags[i][0]=='He' or tags[i][0]=='He' or tags[i][0]=='HE':
                nouns.append('Boy')
                original.append(tags[i][0])
              elif tags[i][0]=='She' or tags[i][0]=='SHE' or tags[i][0]=='she':
                nouns.append('Girl')
                original.append(tags[i][0])

        nouns=self.modify_objects(nouns)
        return nouns,original


