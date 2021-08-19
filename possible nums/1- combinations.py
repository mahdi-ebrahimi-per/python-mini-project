# combinations : ABC - ACB - BCA - BAC - CAB - CBA

import itertools

for subset in itertools.combinations(range(1, 10), 6):
    print(subset)

obj = ['A','B', 'C']
for i in itertools.combinations(obj, 1):
    print(i)


