OK_FORMAT = True

test = {   'name': 'p01',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': ">>> assert __import__('hashlib').sha256(repr(p01).encode()).hexdigest() == '8822d6066720966879930bcac00756635ca5a96e4111d8579f2b26a33ba042af', "
                                               "'残念、答えが違うようです。もう一度考えてみましょう'\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
