def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# print_kwargs(name = "ramesh",power = "2")
print_kwargs(name = "ramesh")
# print_kwargs(name = "ramesh",power = "2",enemy = "Dr.jigo")