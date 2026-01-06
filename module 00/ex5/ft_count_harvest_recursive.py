def ft_count_harvest_recursive(n):
    def recursive(n):
        if n > 1:
            recursive(n - 1)
        print(n)
    print(f"Days until harvest: {n}")
    recursive(n)
    print("Harvest time!")
