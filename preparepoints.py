import json

isoline = json.load(open('2018-10-30 09:07:58.084221.json', 'r'))
points = isoline['response']['isoline'][0]['component'][0]['shape']
points = [p.split(',') for p in points]
points = [{'lat': float(p[0]), 'lng': float(p[1])} for p in points]

print(points)