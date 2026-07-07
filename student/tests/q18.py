OK_FORMAT = True

test = {   'name': 'q18',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': ">>> assert __import__('hashlib').sha256(repr(q18).encode()).hexdigest() == '60a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe', "
                                               "'残念、答えが違うようです。もう一度考えてみましょう'\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
