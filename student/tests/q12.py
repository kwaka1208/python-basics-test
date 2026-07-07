OK_FORMAT = True

test = {   'name': 'q12',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': ">>> assert __import__('hashlib').sha256(repr(q12).encode()).hexdigest() == '4a44dc15364204a80fe80e9039455cc1608281820fe2b24f1e5233ade6af1dd5', "
                                               "'残念、答えが違うようです。もう一度考えてみましょう'\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
