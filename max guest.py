def max_guests_at_any_instance(T,e,l):
    max_guests = 0
    current_guests = 0
    for i in range(T):
        current_guests += e[i]-l[i]
        max_guests = max(max_guests, current_guests)
    return max_guests
T=5
e=[7, 0, 5, 1, 3]
l=[1, 2, 1, 3, 4]
result= max_guests_at_any_instance(T,e,l)
print(result) 
