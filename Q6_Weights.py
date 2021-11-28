lift_wait=0
weights = [ 64, 80, 20, 110, 75, 35, 94, 70, 45, 65 ]
no_people=0
for weight_index in weights:
    lift_wait=lift_wait+weight_index
    if lift_wait>=400:
        break
    no_people+=1
print(no_people,"people can go in the first trip")
