import os
import yaml

class Database:

    def __init__(self):
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(f'{self.dir_path}/../data/bookmarks.yaml', 'r') as stream:
            self.data = yaml.safe_load(stream)

    def write_to_bookmarks(self, linkTag, link):
        self.data[linkTag] = link
        self.update_data_file()

    def update_data_file(self):
        with open(f'{self.dir_path}/../data/bookmarks.yaml', 'w') as stream:
            yaml.dump(self.data, stream)

    def get_bookmark(self, linkTag):
        return self.data[linkTag]

    def get_all_names(self):
        list = []
        for k in self.data:
            list.append(k)
           
        return list
    
    def get_all_links(self):
        return [
            [k, v]
            for k, v in self.data.items()
        ]
        
    
    def delete_bookmark(self, linkTag):
        self.data.popitem(linkTag)
        self.update_data_file()
