import re
with open ('tags.txt','r') as f:
   #for i in f:
   while True:
      pattern =('\>([\w]+)\<')
      detail = f.read()
      results = re.search(pattern,detail)
      print results.group()


