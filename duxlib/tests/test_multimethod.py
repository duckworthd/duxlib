
from duxlib.multimethod import *


def test_multimethod():
  jsonify = multimethod(lambda obj: type(obj))
  jsonify.register(   int, lambda o: "I'm an int: %d" % o)
  jsonify.register( float, lambda o: "I'm a float: %f" % o)
  jsonify.register(   str, lambda o: "I'm a string: %s" % o)
  jsonify.register(  dict, lambda o: {k: jsonify(v) for k, v in o.items()})
  jsonify.register(  list, lambda o: [jsonify(v) for v in o])

  result = jsonify({
    "a": [1, 2, 3.0],
    "b": {
      "ba": ["hello"],
      "bb": [-1, -2],
    }
  })

  correct_result ={
    'a': [
      "I'm an int: 1",
      "I'm an int: 2",
      "I'm a float: 3.000000"
    ],
   'b': {
     'ba': ["I'm a string: hello"],
     'bb': ["I'm an int: -1", "I'm an int: -2"]
    }
  }

  assert result == correct_result
