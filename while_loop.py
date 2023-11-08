multiplier = 1

while multiplier <= 99999: 
    num = 1
    while num <= 10:
        result = multiplier * num
        print(f"{multiplier} x {num} = {result}")
        num += 1

    # Move to the next multiplier
    multiplier += 1