bag = []                            
bag1 = []                           
score = 0
cells = 0
seek = 'астма'
ratio = []
g = 0
things = {'в': (3, 25),
          'п': (2, 15),
          'б': (2, 15),
          'а': (2, 20),
          'и': (1, 5),
          'н': (1, 15),
          'т': (3, 20),
          'о': (1, 25),
          'ф': (1, 15),
          'д': (1, 10),
          'к': (2, 20),
          'р': (2, 20)
          }


if seek == 'астма':
    score += things['и'][1]
    cells += things['и'][0]
    bag1.append('и')
    things.pop('и')
    g += 1
elif seek == 'заражение':
    score += things['д'][1]
    cells += things['д'][0]
    bag1.append('д')
    things.pop('д')
    g += 1

for i in things:
    score += things[i][1]
maxscore = score
for i in things:
    cells += things[i][0]

for i in things:
    ratio.append([things[i][1]/things[i][0], i])
bag0 = sorted(ratio)
for i, j, k in zip(things, ratio, range(12 - g)):
    while cells > 9 - g:
        bag0.pop(0)
        score -= things[ratio[k][1]][1]
        cells -= things[ratio[k][1]][0]

cells = 0
score = 0
for i in bag0:
    bag1.append(i[1])
things['и'] = (1, 5)
for i in bag1:
    cells += things[i][0]
    score += things[i][1]
for i in bag1:
    for g in range(things[i][0]):
        bag.append([i])

g = 0
for i in range(9):
    if (i+1) % 3 == 0:
        print(bag[i], end='\n')
    else:
        print(bag[i], ', ', end='', sep='')
score = score - (maxscore - score)
print('Итоговые очки выживания:', score + 15) # 15 - начальное количество очков по условию
