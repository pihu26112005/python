# for lists - use []
ls = [i for i in range(100) if i%3==0]
print(ls)

# for dictionary - use {}
dict1 = {i:f"item {i}" for i in range(1, 10001) if i%100==0}
dict1 = {i:f"Item {i}" for i in range(5)}
#if we want to reverse key value 
dict2 = {value:key for key,value in dict1.items()}
print(dict1,"\n", dict2)

#for set - use []
dresses = [dress for dress in ["dress1", "dress2","dress1",
                               "dress2","dress1", "dress2"]] # set me value repetition nhi hoti
print(type(dresses))

# for generators - use ()
evens = (i for i in range(100) if i%2==0)
print(evens.__next__)
print(evens.__next__)
print(evens.__next__)

for item in evens: #for accewssing all elements at one of this generator 
    print(item)
