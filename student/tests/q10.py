OK_FORMAT = True

test = {   'name': 'q10',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': ">>> assert __import__('hashlib').sha256(repr(q10).encode()).hexdigest() == '44cb730c420480a0477b505ae68af508fb90f96cf0ec54c6ad16949dd427f13a', "
                                               "'残念、答えが違うようです。もう一度考えてみましょう'\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
