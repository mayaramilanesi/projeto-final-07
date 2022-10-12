from bson import Decimal128
from bson.json_util import dumps
import json

import decimal
def format_json(data):
      return json.loads(dumps(data))
      