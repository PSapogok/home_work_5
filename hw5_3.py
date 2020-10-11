FriendsAndCash =  {'John': 20 , 'Dan': 30 , 'Lois': 14 , 'Doug': 144 }
FriendsAndCash2 = {}
total = 0
for j in FriendsAndCash.values():
    total+=j
print('Total money we have is',total,"$")
k = max(FriendsAndCash, key=FriendsAndCash.get)
print(k, FriendsAndCash[k]) 
for i, j in FriendsAndCash.items():
    FriendsAndCash2[j] = i
print(FriendsAndCash2)