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
            if self.original_list[i]=='mother' and self.original_list[j] =="She":
              print("original",self.objects_list[i].sent_num,self.objects_list[j].sent_num,self.objects_list[i].pos,self.objects_list[j].pos)
            # check the relations between the two nodes
            for mention in mentions:
              flag1=False
              flag2=False
              flag3=False
              for k in range(len(mention[1])):
                if mention[1][k]['sentNum'] == self.objects_list[i].sent_num and self.objects_list[i].pos>=mention[1][k]['startIndex'] and self.objects_list[i].pos<mention[1][k]['endIndex']:
                  print("original i",self.original_list[i],self.objects_list[i].sent_num,self.objects_list[j].sent_num,self.objects_list[i].pos,self.objects_list[j].pos)
                  flag1=True
                elif mention[1][k]['sentNum']==self.objects_list[j].sent_num and self.objects_list[j].pos>=mention[1][k]['startIndex'] and self.objects_list[j].pos<mention[1][k]['endIndex']:
                  print("original j",self.original_list[j],self.objects_list[j].sent_num,self.objects_list[j].sent_num,self.objects_list[j].pos,self.objects_list[j].pos)
                  flag2=True
                if flag1==True and flag2==True:
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
            if object.text !='0':
              self.objects_list.append(object)
              self.original_list.append(original[i])
            else :
              object.text=original[i]
              # 1- convert from plural to singular
              word=self.stem(object.text)
              print(word)
              # to avoid stemmer problems (computer -> comput)
              if len(wn.synsets(word))< len(wn.synsets(object.text)):
                  word=object.text

              # 2- getting the physical objects
              for synset in wn.synsets(word):
                  name=synset.lexname()
                  if name == 'noun.artifact' or name == 'noun.person'\
                   or name == 'noun.plant' or name =='noun.animal' \
                   or name == 'noun.food' or name == 'noun.location':
                      self.original_list.append(object.text)
                      object.text='1'
                      self.objects_list.append(object)
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
        print("printing objects list.....")
        for object in self.objects_list:
          print(object.text,object.sent_num,object.pos)



