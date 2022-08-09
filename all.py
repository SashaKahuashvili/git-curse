import json ,csv
while True:
    n=int(input("Номер задачи,7-для выхода:"))
#1
    def jsontocsv():
        data = None
        with open("file.json", "r", ) as jfile:
            data = json.load(jfile, )
            print(data)
        with open("new_data.csv", "w") as csv_file:
            writer = csv.writer(csv_file)
            print(data[0].values())
            writer.writerow(key for key in data[0].keys())
            print(data[0].keys())
        # writer.writerow(value for value in data[0].values())
            for item in data:
                writer.writerow(value for value in item.values())
                print(item.values())
#2
    def addtojson():
        new= {  "name": " fff",
                "birthday": "fff",
                "height": 12,
                "weight": 13,
                "car": 14,
                "languages":["sd","sd"] }

        with open("file.json","r") as old:
            data=json.load(old)
        print(data)
        data.append(new)
        print(data)
        with open("file.json","w") as old:
            json.dump(data,old)
#3
    def namesearch():
        with open('file.json','r') as f:
            name=input("Введите имя:")
            data=json.load(f)
            for i in data:
                if name==i["name"]:
                    print(i)
#4
    def languagesearch():
        with open("file.json", "r") as f:
            lang=input("languages:")
            for i in json.load(f):
                for key in i.keys():
                    if key=="languages" and lang in i[key]:
                        print(i['name'])
#5
    def mediumheight():
        height=[]
        with open("file.json", "r") as f:
            year=int(input("Задайте возраст:"))
            for i in json.load(f):
                if int(i["birthday"][6::]) < year:
                    height.append((i["height"]))
            print(sum(height)/len(height))
#6
    def addcsv():
        new_str=['kahuashvili','28.08.1998,165,56.1','True',"['python']"]
        with open("new_data.csv","w") as file:
            writer_object = csv.writer(file)
            writer_object.writerow(new_str)
    if n==1:
        jsontocsv()
    if n==2:
        addtojson()
    if n==3:
        namesearch()
    if n==4:
        languagesearch()
    if n==5:
        mediumheight()
    if n==6:
        addcsv()
    if n==7:
        break
