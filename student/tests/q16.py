OK_FORMAT = True

test = {   'name': 'q16',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': ">>> assert __import__('hashlib').sha256(repr(q16).encode()).hexdigest() == '3cbc87c7681f34db4617feaa2c8801931bc5e42d8d0f560e756dd4cd92885f18', "
                                               "'残念、答えが違うようです。もう一度考えてみましょう'\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
