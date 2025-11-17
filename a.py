my_list = [10, 20, 30, 40, 50]

print(f"Original list: {my_list}")

my_list.append(60)
print(f"After append(60): {my_list}")

my_list.insert(1, 15)
print(f"After insert(1, 15): {my_list}")

my_list.remove(30)
print(f"After remove(30): {my_list}")

popped_element = my_list.pop(2)
print(f"After pop(2): {my_list}")
print(f"Popped element: {popped_element}")

my_list.sort()
print(f"After sort(): {my_list}")
