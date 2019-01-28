from nltk.corpus import wordnet as wn
from nltk import PorterStemmer
class objects_extractor(object):
    def __init__(self):
        print("Starting objects extractor....")
        self.p=PorterStemmer()
        self.objects_list=[]
        #for synset in wn.synsets('match'):
        #    print(synset.lexname())

    def stem (self,word):
        return self.p.stem(word)

    def extract_physical_objects(self,objects):
        i=0
        j=0
        for object in objects:
            # 1- convert from plural to singular
            word=self.stem(object)
            print(word)
            # to avoid stemmer problems (computer -> comput)
            if len(wn.synsets(word))< len(wn.synsets(object)):
                word=object

            # 2- getting the physical objects
            for synset in wn.synsets(word):
                name=synset.lexname()
                if name == 'noun.artifact' or name == 'noun.person'\
                 or name == 'noun.plant' or name =='noun.animal' \
                 or name == 'noun.food' or name == 'noun.location':
                    self.objects_list.append(object)
                    break
                j+=1
                if j==3:
                    break
            j=0
            i+=1
        print("now the physical objects:",self.objects_list)




