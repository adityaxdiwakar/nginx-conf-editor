with open("default", "r") as f:
    lines = f.readlines()

conjoined_text = "".join(lines).replace("\n", "").replace(" ", "")

blocks = []
temporary_object = []
current_depth = 0
objectified_depth_objects = []
for character in conjoined_text:
    if character   == "{":
        current_depth += 1
    if character == "}":
        print(len(objectified_depth_objects), current_depth)
        objectified_depth_objects[current_depth - 1].append(character)
        blocks.append(objectified_depth_objects[current_depth - 1])
        objectified_depth_objects.pop(current_depth - 1)
        current_depth -= 1

    for x in range(current_depth):
        try:
            objectified_depth_objects[x].append(character)
        except IndexError:
            objectified_depth_objects.append([character])

for index, block in enumerate(blocks):
    blocks[index] = "".join(block)

import json
json.dump(
    blocks,
    open("dump.json", "w"),
    indent = 4
)