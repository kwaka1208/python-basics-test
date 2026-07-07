OK_FORMAT = True

test = {   'name': 'q15',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': ">>> assert __import__('hashlib').sha256(repr(q15).encode()).hexdigest() == '5cf4e1088a53d205c920e842619d086375200cfec49f51944f86146341219f0d', "
                                               "'残念、答えが違うようです。もう一度考えてみましょう'\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
