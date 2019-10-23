def transaction(withdrawalAmount, Balance):
    bankCharges = 0.50

    if withdrawalAmount > Balance:
        print('Insufficient funds')
        return round(Balance,2)

    elif withdrawalAmount % 5 == 0:
        print('Successful Transaction')
        Balance = Balance - (withdrawalAmount + bankCharges)
        return round(Balance, 2)

    elif withdrawalAmount % 5 != 0:
        print('Incorrect withdrawal amount (not multiple of 5)')
        return round(Balance, 2)


withdrawal_money = int(input())
initialBalance = float(input())

result = transaction(withdrawal_money, initialBalance)
print(result)
