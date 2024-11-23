## Sets ##

mySet = set()
myOtherSet = {}

print(type(mySet))
print(type(myOtherSet))  # Initially is dic

myOtherSet = {"Thomas", "Carrillo", 21}
print(type(myOtherSet))

print(len(myOtherSet))

myOtherSet.add("ThomasDev")

print(myOtherSet)  # A Set is not a organize structure

myOtherSet.add("ThomasDev")  # A Set dont admit repeated data

print(myOtherSet)

print("Thomas" in myOtherSet)
print("Thomasi" in myOtherSet)

myOtherSet.remove("Thomas")
print(myOtherSet)

myOtherSet.clear()
print(myOtherSet)
