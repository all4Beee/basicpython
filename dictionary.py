scores = {
    'john': 1200,
    'bobby': 2000,
    'janny': 4200
}

print(scores)
print(scores['bobby'])

scores['roger'] = 3200

print(scores)

points = {}

points['mr_a'] = 10.2
points['mr_b'] = 15.4
points['mr_c'] = 22.8

print(points)

for k, v in scores.items():
    print(k, v)
