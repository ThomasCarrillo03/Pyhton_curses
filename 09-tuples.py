## Tuples ##
## Tuples are immutable, not like lists##

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.77, "Thomas", "Carrillo", "Thomas")
my_other_tuple = (35, 60, 30)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("Thomas"))
print(my_tuple.index("Carrillo"))
print(my_tuple.index("Thomas"))

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)
print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "ThomasDev"
my_tuple.insert(1, "Azul")
print(my_tuple)
