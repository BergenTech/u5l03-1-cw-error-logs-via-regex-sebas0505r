path = "logs.json"

def look_forSearch():
    pattern = r"ERROR"

with open(path) as JsonFile:
    data = json.load(JsonFile)
