  
import json
  
# # Opening JSON file
# f = open('data.json')
  
# returns JSON object as 
# a dictionary
data = json.load(r'test\bot.json')
  
# Iterating through the json
# list
for i in data['emp_details']:
    print(i)
  
# Closing file
f.close()