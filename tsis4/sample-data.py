import json

with open("data.json", "r") as read_file:
    data = json.load(read_file)

print("""Interface Status
===============================================================================""")
print("""DN                                                 Description           Speed    MTU """)
print("--------------------------------------------------" ,end = ' ')
print("--------------------" ,end = "  ")
print("------" ,end = "  ")
print("------")

cnt = 0
for info in data["imdata"]:
    d = info["l1PhysIf"]["attributes"]
    print("{:<51} {:<19} {:<9} {:<5}".format(d["dn"], d["descr"], d["speed"], d["mtu"]))
    cnt += 1
    if cnt == 3:
        break
