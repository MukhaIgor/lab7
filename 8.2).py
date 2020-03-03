worker = {'Петров': {'age': 27, 'education': 'высшее', 'position': 'инженер'},
          'Смирнов': {'age': 35, 'education': 'среднее', 'position': 'технолог'},
          'Иванов': {'age': 32, 'education': 'высшее', 'position': 'инженер'}}
for k in worker:
    if worker[k]['age'] > 30 and worker[k]['education'] == 'высшее':
        print(k)
