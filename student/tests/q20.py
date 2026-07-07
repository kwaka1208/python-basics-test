OK_FORMAT = True

test = {   'name': 'q20',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': ">>> assert __import__('hashlib').sha256(repr(q20).encode()).hexdigest() == '48449a14a4ff7d79bb7a1b6f3d488eba397c36ef25634c111b49baf362511afc', "
                                               "'残念、答えが違うようです。もう一度考えてみましょう'\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
