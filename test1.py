import json


str_json = """
{ "info" : "Sample JSON output from our service"\t,
    "elements": [
        { "name": "first",
        "type": "server",
        "ip": "7175"
        },
        { "name": "second",
        "type": "proxy",
        "ip" : "71.78.22.43"
        }
    ]
 }"""
print(str_json)
data = json.loads(str_json)
print(data)