import json , csv
data = None
with open("data_file.json","r") as jfile:
    data = json.load(jfile)

print(data)
with open("new_data.csv","w") as csv_file:
    writer=csv.writer(csv_file)
    print(data[0].values())
    writer.writerow(key for key in data[0].keys())
    #writer.writerow(value for value in data[0].values())
    for item in data:
        writer.writerow(value for value in item.values())



