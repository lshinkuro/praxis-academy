import json

with open('./file.json') as f:
    python_obj=json.loads(f.read())

    for x in python_obj:
        print(x['nama'])
        if x['nama'] == "abdullah":
             break


   


