import parser_module
import tagger
import objects_extractor

tag=tagger.tagger()
parse=parser_module.parser_module()
extractor=objects_extractor.objects_extractor()
objects=[]
def main():
    #text=input("Enter the text : ")
    text="John is playing football at the garden . He is happy ."
    tags=tag.get_tags(text)
    print(tags)
    # getting the initial objects list
    objects=tag.get_nouns(tags)
    print("returned objects ",objects)
    # getting the physical objects
    extractor.extract_physical_objects(objects)
    # getting the dependency list
    parse_tree=parse.parse(text)
    print(parse_tree)

    # stop the server
    #parse.stop()
if __name__== "__main__":
    main()
