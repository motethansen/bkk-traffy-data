# Python program to read
# json file
import glob
import json

path_to_json = '*.json'
#get all files
json_files = glob.glob(path_to_json)


for count,ele in enumerate(json_files,len(json_files)):
    # JSON file
    f = ele
    new_file_name="data_{filename}".format(filename=f)

    with open(f, 'r', encoding='utf-8') as f:
        # Reading from file
        data = json.load(f)
    
    #json_string = json.dumps(data["results"])

    with open(new_file_name, 'w', encoding='utf-8') as f:
        f.write(json.dumps(data["results"], indent=4))
