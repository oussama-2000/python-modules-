def ft_count_harvest_recursive():
    def recursive(n):
        if n > 1:
            recursive(n - 1)
        print(f"Day {n}")
    days = int(input("Days until harvest: "))
    recursive(days)
    print("Harvest time!")
