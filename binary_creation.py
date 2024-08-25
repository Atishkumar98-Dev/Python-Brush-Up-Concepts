# for x in range(2):
#   for y in range(2):
#     for z in range(2):
#       for g in range(2):
#         for h in range(2):
#             print(x,y,z,g,h)


from combi import product

for combination in product(range(2), repeat=2):
    print(combination)
