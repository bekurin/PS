def find_set(parent, x):
    if parent[x] != x:
        parent[x] = find_set(parent, parent[x])
    return parent[x]


def make_set(parent, x):
    parent[x] = x


def union(parent, a, b):
    a = find_set(parent, a)
    b = find_set(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v = 6
parent = [0] * (v + 1)
input_list = [(1, 4), (2, 3), (2, 4), (5, 6)]

for i in range(1, v + 1):
    make_set(parent, i)

for x, y in input_list:
    union(parent, x, y)

result = []
for i in range(1, v + 1):
    result.append(find_set(parent, i))

print('set of elements: {}'.format(result))
print('parent table: {}'.format(parent[1:]))