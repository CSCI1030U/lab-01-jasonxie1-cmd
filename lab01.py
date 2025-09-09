def main():
    cost_per_item = 19.99
    quantity = 5

    # Part 1 code
    subtotal_cost = cost_per_item * quantity
    tax = subtotal_cost * 0.13
    total_cost = subtotal_cost + tax

    # Part 2 code
    print(f'cost_per_item = ${cost_per_item:0.2f}')
    print(f'quantity = {quantity:f}')
    print(f'subtotal_cost = ${subtotal_cost:0.2f}')
    print(f'tax = ${tax:0.2f}')
    print(f'total_cost = ${total_cost:0.2f}')

    # Part 3 code
    initial_investment = 1000
    interest_rate = 0.035
    investment = initial_investment
    investment += investment * interest_rate
    investment += investment * interest_rate
    investment += investment * interest_rate
    investment += investment * interest_rate
    investment += investment * interest_rate
    print('After 5 years, your investment will be worth ' + str(investment) + ' dollars.')

if __name__ == "__main__":
    main()
