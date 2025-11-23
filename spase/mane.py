from clas import SpacePhoto
from Json_Srorage import JsonStorage
import deepl



API_KEY = "2buUh7TBSJnEtdEx13XoM5fjYBYJbaWnWbdh1JiR"


def main():
    photo = SpacePhoto(API_KEY)
    photo.load()
    photo.show_info()

    storage = JsonStorage()
    storage.save_entry(photo.load())
    print("File saved in ", storage.filrname)
    
    
if __name__ == "__main__":
        main()