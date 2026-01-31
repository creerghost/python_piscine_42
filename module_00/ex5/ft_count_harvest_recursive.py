def ft_count_harvest_recursive(days=None, days_start=None):
    if days is None:
        days = int(input("Days until harvest: "))
    if days != 0:
        ft_count_harvest_recursive(days - 1, 0)
        print(f"Day {days}")
        if days_start is None:
            print("Harvest time!")
