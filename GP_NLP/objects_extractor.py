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

    def remove_duplicated_objects(self,mentions):
      length=len(self.objects_list)
      for i in range(len(self.objects_list)):
        # compare with each node
        for j in range(i+1,len(self.objects_list)):
            # check the relations between the two nodes
            for mention in mentions:
              flag1=False
              flag2=False
              flag3=False
              for k in range(len(mention[1])):
                if flag1==False and mention[1][k]['text'] == self.original_list[i]:
                  flag1=True
                elif flag2==False and mention[1][k]['text'] == self.original_list[j]:
                  flag2=True
                elif flag1==True and flag2==True:
                  flag3=True
                  break
              # we found a relation then we need to remove one of the nodes
              if flag3==True:
                del self.objects_list[j]
                del self.original_list[j]
                length-=1
                break
            if j+1==length:
              break
        if i+1==length:
          break





    def extract_physical_objects(self,objects,original,coref_json):
        i=0
        j=0
        self.objects_list=[]
        self.original_list=[]
        for object in objects:
          # the objects that are available in the database
            if object!='0':
              self.objects_list.append(object)
              self.original_list.append(original[i])
            else :
              object=original[i]
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
                      self.objects_list.append('1')
                      self.original_list.append(object)
                      break
                  j+=1
                  if j==3:
                      break
            j=0
            i+=1
        # remove duplicated objects based on the coref
        self.remove_duplicated_objects(coref_json)
        print("now the physical objects:",self.objects_list)
        print("now the original objects ",self.original_list)




