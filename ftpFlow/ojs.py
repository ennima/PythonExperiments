import json
with open("DownList.json") as json_file:
	json_data = json.load(json_file)
	print json_data

#print json_data[0]["color"]

for i in json_data:
	print i