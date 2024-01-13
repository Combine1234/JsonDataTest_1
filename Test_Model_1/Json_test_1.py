import json

js_string = '''
    {
        "students":[
            {
                "id": 1,
                "name": "BillGay",
                "age": 16,
                "full-time": false
            },
            {
                "id": 2,
                "name": "MusicGay",
                "age": 16,
                "full-time": true
            }
        ]
    }
'''
data = json.loads(js_string)
print(data['students'][0])

nissan = json.dumps(data, indent=4, sort_keys=True)
print(nissan)