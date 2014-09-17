import json

data = [{"color":"red","val":"0"},{"color":"green","val":"1"},{"color":"blue","val":"2"}]

f = open("sa.json","w")
json.dump(data,f)
f.close()
