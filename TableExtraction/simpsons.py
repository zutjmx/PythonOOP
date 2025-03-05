import pandas as pd

simpsons = pd.read_html('https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)')

#print(simpsons[1].head())
print(len(simpsons)) # Número de tablas en la página
print(simpsons[1].columns)
print(simpsons[1].columns.values)
print(simpsons[1].shape)
print(simpsons[1].info())
print(simpsons[1].describe())

print(simpsons[1].head())

print(simpsons[1])

print(simpsons[20])

for i in range(len(simpsons)):
    print(simpsons[i])
    
