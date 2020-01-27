import logging
import requests

class Hotlinks:
  
  def __init__(self):
    self.logger = logging.getLogger('bookmarks')
    self.endpoint = "http://localhost"
    
  def get_all(self):
    # Request all links
    return requests.get(f"{self.endpoint}/get").json()
  
  def get_link(self, index):
    # Request specific link
    return requests.get(f"{self.endpoint}/get/{index}").json()
    
  def clear_links(self):
    # Request clear all links
    return requests.get(f"{self.endpoint}/clear").json()
    
  def remove_link(self, index):
    # Request delete specific link
    return requests.get(f"{self.endpoint}/remove/{index}").json()
    
  def add_link(self, link_addr):
    # Request add link
    body = {
      "link": link_addr
    }
    res = requests.post(f"{self.endpoint}/add", data=body)
    return res.status_code == 200
    
