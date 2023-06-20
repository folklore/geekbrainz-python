def rev(**kwargs):
    return {value: key for key, value in kwargs.items()}

print(rev(ka = 'va', kb = 'vb', kc = 'vc'))

print(rev(ka = 1, kb = 2, kc = 3))

print(rev(ka = (1,), kb = (2,), kc = (3,)))

# {'va': 'ka', 'vb': 'kb', 'vc': 'kc'}
# {1: 'ka', 2: 'kb', 3: 'kc'}
# {(1,): 'ka', (2,): 'kb', (3,): 'kc'}
