import json

def avg(lst):
    temp = 0
    for i in lst:
        temp += i
    return temp / len(lst)

with open('Scores.json') as f:
    data = json.load(f)

data['User Average'] = avg(data['User Scores'])
data['Version1 Average'] = avg(data['Version1 Scores'])
data['Version2 Average'] = avg(data['Version2 Scores'])
data['User Max'] = max(data['User Scores'])
data['Version1 Max'] = max(data['Version1 Scores'])
data['Version2 Max'] = max(data['Version2 Scores'])

data['# of User Scores'] = len(data['User Scores'])
data['# of Version 1 Scores'] = len(data['Version1 Scores'])
data['# of Version 2 Scores'] = len(data['Version2 Scores'])

print(data)

with open('Scores.json', 'w') as f:
    json.dump(data, f, indent=2)