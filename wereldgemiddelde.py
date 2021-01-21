import itertools
import os
import random

with open('wereldgemiddelde.txt','r') as roman:
    words = " ".join(roman.readlines()).split()

print (sorted(words), file=open('alfabetisch.txt','w'))
print (sorted(words, key=len), file=open('lengte.txt','w'))

word_occurrences = {w : words.count(w) for w in words}
print({k: v for k, v in sorted(word_occurrences.items(), key=lambda item: item[1])}, file=open('voorkomens.txt','w'))



letters = [x.lower() for w in words for x in w ]
letter_occurrences= {}
total = 0
for l in letters:
    total += 1
    if l in letter_occurrences:
        letter_occurrences[l] +=1
    else:
        letter_occurrences[l] = 1

for l in letter_occurrences:
    letter_occurrences[l]=round(100*letter_occurrences[l]/total, 1)
print (sorted(letter_occurrences.items(), key=lambda item: item[1], reverse=True), file=open('letters.txt','w'))
print(total)

letter_frequentie = [('e', 15.6, 19.0), ('r', 8.5, 6,4), ('l', 8.0, 3.57), ('o', 6.5, 6.0), ('t', 6.3, 6.8), ('n', 6.0, 10.0), ('s', 5.7, 3.7), ('a', 5.2, 7.5), ('i', 5.0, 6.5), ('k', 5.0, 2.2), ('u', 4.9, 2.0), ('p', 4.1, 1.6), ('m', 3.4, 2.2), ('g', 3.0, 3.4), ('b', 2.4, 1.6), ('d', 2.1, 5.9), ('f', 2.0, 0.8), ('v', 1.6, 2.9), ('w', 1.4, 1.5), ('h', 1.3, 2.4), ('z', 1.1, 1.4), ('j', 0.7, 1.5), ('c', 0.2, 1.2), ('y', 0.0, 0.0)]
hoger = []
lager = []
for f in letter_frequentie:
    if f[1] > f[2]: hoger.append(f)
    else: lager.append(f)

with open('relatieve_frequentie.txt','w') as bestand:
    print ('Dit zijn alle letters in volgorde van frequentie in Wereldgemiddelde (WG) met ter vergelijking de frequntie in het Nederlands NL:', file=bestand)
    print ('LET\tWG\tNL', file=bestand)
    for h in letter_frequentie:
        print (f"{h[0]}\t{h[1]}\t{h[2]}", file=bestand)
    print ('Deze letters komen vaker voor in Wereldgemiddelde dan gemiddeld in het Nederlands (NL):', file=bestand)
    print ('LET\tWG\tNL', file=bestand)
    for h in hoger:
        print (f"{h[0]}\t{h[1]}\t{h[2]}", file=bestand)
    print ('Deze letters komen minder vaak voor in Wereldgemiddelde dan gemiddeld in het Nederlands:', file=bestand)
    print ('LET\tWG\tNL', file=bestand)
    for h in lager:
        print (f"{h[0]}\t{h[1]}\t{h[2]}", file=bestand)


diphtongs = [w for w in words if 'ui' in w.lower() or 'au' in w.lower() or 'ei' in w.lower() or 'ij' in w.lower()]

print(diphtongs, file=open('diftongen.txt','w')) """

""" with open('celex.txt','r') as roman:
    celex = [c.split('\\')[1] for c in " ".join(roman.readlines()).split()]

real_words = [w for w in words if w.lower() in celex]
print (sorted(real_words), file=open('echtewoorden.txt','w'))
print (len(real_words))
