import datetime
import time
import json

data_example = {"pla_test_tag": [{"tt": "2022-10-14T17:52:40-03:00", "vv": 11.123, "qq": "GOOD", "ss": "GOOD"}]}
print(data_example)

data = {}
li = []
pla_test_tag = {}
content = {}
pla_test_tag["tt"] = "2022-10-21 09:12:27.129834"
pla_test_tag["vv"] = 12
pla_test_tag["qq"] = "good"
pla_test_tag["ss"] = "good"
li.append(pla_test_tag)
data["pla_test_tag"] = li
print(json.dumps(data))


for x in range(15):
    # ts = datetime.datetime.now().replace(microsecond=0)
    ts = datetime.datetime.utcnow().isoformat()[:-3]+'Z'
    data = {}
    li = []
    pla_test_tag = {}
    content = {}
    pla_test_tag["tt"] = str(ts)
    pla_test_tag["vv"] = 12
    pla_test_tag["qq"] = "good"
    pla_test_tag["ss"] = "good"
    li.append(pla_test_tag)
    data["pa_test_tag"] = li
    print(json.dumps(data))
    time.sleep(1)
