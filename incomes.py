def calcPay(file):
    """
    Calculate the total pay for each employee based on their hours worked and hourly rate.

    Args:
        file (str): The path to the input file containing employee data.
    """

    arr = {}

    with open(file, 'r') as f:
        lines = f.readlines()

    for line in lines:
        name, value, amt = line.split()
        total = float(value) * float(amt)

        if name in arr:
            arr[name] += total
        else:
            arr[name] = total

    return arr


f = calcPay('pay.txt')

for k, v in f.items():
    print(f"{k}: ${v:.2f}")  
