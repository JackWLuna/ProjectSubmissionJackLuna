import json

file_names = ["US_category_id"]

for json_name in file_names:

    json_file = open(json_name + ".json")

    data = json.load(json_file)

    output_csv = open("pjcsv\\"+ "Category_id" + ".csv",'w')

    output_csv.write("id,etag,title\n")

    for category in data['items']:
        output_csv.write(category['id']+','+category['snippet']['title']+"\n")
        #print(category['snippet']['title'])

    json_file.close()
    output_csv.close()