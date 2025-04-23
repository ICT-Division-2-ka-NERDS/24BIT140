d={
    "department1":{101:4800,102:6900,103:5700},
    "department2":{201:1500,202:9200,203:8800},
    "department3":{301:3600,302:4300,303:4100}
}
for i in d:
    print("Department:",i)
    print("Minimum salary:",min(d[i].values()))
    print("Maximum salary:",max(d[i].values()))

