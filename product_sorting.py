
def merge_sort(products):
    if len(products) <= 1:
        return products

    mid = len(products) // 2

    left = merge_sort(products[:mid])
    right = merge_sort(products[mid:])

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i][1] <= right[j][1]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


products = []

n = int(input("Enter number of products: "))

for i in range(n):
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    products.append((name, price))

sorted_products = merge_sort(products)

print("\nProducts sorted by price:")

for name, price in sorted_products:
    print(name, "- Rs.", price)
