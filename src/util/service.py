from bson.json_util import dumps
import json

def format_json(data):
      return json.loads(dumps(data))
      