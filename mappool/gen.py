import json

with open("mappool.txt", "r") as id_file:
    data = id_file.readlines()
    print(data)
    mod_count = int(data[0].strip())
    mods = [x.split(" ") for x in data[1:mod_count + 1]]

output_json = []
index = mod_count + 1
for mod in mods:
    mod_name = mod[0]
    count = int(mod[1])
    for i in range(count):
        output_json.append({
            "beatmapId": int(data[index].strip()),
            "mods": mod_name,
        })
        index += 1
with open("beatmaps.json", "w") as output_file:
    json.dump(output_json, output_file, indent=4)
print(output_json)
print("beatmaps.json generated successfully.")