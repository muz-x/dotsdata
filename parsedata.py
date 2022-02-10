# import pandas as pd;
# df = pd.DataFrame()
import json
from time import sleep

attributes = set()
counter = 0
trait_types = {"Background", "Mask", "Garmet", "Horn"}
attribute_counter = {x:{} for x in trait_types}
with open('metadata.json', 'r') as f:
    for line in f:
        metadata = json.loads(line.strip())
        attributes = metadata.get('attributes')
        for att in attributes:
            trait = att['trait_type']
            attribute_counter[trait][att['value']] = attribute_counter[trait].get(att['value'], 0) + 1
            # attributes.add(att['value'])
        counter += 1

print(counter)
print(json.dumps(attribute_counter))