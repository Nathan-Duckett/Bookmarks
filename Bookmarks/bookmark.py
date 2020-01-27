import data
import hotlinks
import logging
import sys
import webbrowser

class Bookmarks:

    def __init__(self):
        self.logger = logging.getLogger('bookmarks')
        self.data = data.Database()
        self.hotlinks = hotlinks.Hotlinks()
        action = sys.argv[1]

        if action == 'add':
            self.process_add()
        elif action == 'load':
            self.process_load()
        elif action == 'list-names':
            self.process_list_names()
        elif action == 'list-links':
            self.process_list_full()
        elif action == 'show':
            self.process_show()
        elif action == 'delete':
            self.process_delete()
        elif action == 'hl':
            self.process_hotlink()
        else:
            self.logger.warning(f"Invalid action passed by user: {action}")

    def process_add(self):
        assert len(sys.argv) > 2

        self.data.write_to_bookmarks(sys.argv[2], sys.argv[3])
        self.logger.info(f"Writing link: {sys.argv[2]} with address {sys.argv[3]}")
        return

    def process_load(self):
        assert len(sys.argv) == 3

        link = self.data.get_bookmark(sys.argv[2])
        webbrowser.open(link, new=2)
        self.logger.info(f"Loading link {sys.argv[2]}")

        return

    def process_list_names(self):
        assert len(sys.argv) == 2
        names = self.data.get_all_names()
        for name in names:
            print(name)
        self.logger.info("Printed all bookmark names")
        return
    
    def process_list_full(self):
        assert len(sys.argv) == 2
        data = self.data.get_all_links()
        for link in data:
            print(f"{link[0]}: {link[1]}")
        self.logger.info("Printed all bookmark names and links")
        return
    
    def process_show(self):
        assert len(sys.argv) == 3
        data = self.data.get_all_links()
        try:
            index = int(sys.argv[2])
        except:
            self.logger.error(f"Error converting {sys.argv[2]} into an integer")
        print(f"{data[index][0]}:{data[index][1]}")
        self.logger.info(f"Printed bookmark at index [{index}]")
        return
                                  
    def process_delete(self):
        assert len(sys.argv) == 3

        self.data.delete_bookmark(sys.argv[2])
        self.logger.info(f"Deleting link {sys.argv[2]}")

        return
    
    def process_hotlink(self):
        assert len(sys.argv) >= 3
        
        action = sys.argv[2]
        
        if action == 'clear':
            self.hotlinks.clear_links()
        elif action == 'get_all':
            self.print_links(self.hotlinks.get_all())
        elif action == 'get':
            self.print_links(self.hotlinks.get_link(sys.argv[3]))
        elif action == 'remove':
            self.hotlinks.remove_link(sys.argv[3])           
        elif action == 'add':
            self.hotlinks.add_link(sys.argv[3])
        else:
            print("Invalid hotlink action")
            
        return
        


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Invalid arguments")
        exit(1)
    Bookmarks()
