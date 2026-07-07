OK_FORMAT = True

test = {   'name': 'q01',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': ">>> assert __import__('hashlib').sha256(repr(q01).encode()).hexdigest() == '7902699be42c8a8e46fbbb4501726517e86b22c56a189f7625a6da49081b2451', "
                                               "'残念、答えが違うようです。もう一度考えてみましょう'\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
