# You are given a Bank account having N amount and you are asked to perfrom ADD(credit) and SUBTRACT(debit) operations.
# After each operation print the amount left in the Bank account. 
# If the debit amount is greater than current balance print "Insufficient Funds"(without quotes) and the operation is skipped.


def main():
    balance = int(input())
    operations = int(input())
    for each in range(operations):
        trasaction_type, amt = map(int, input().split(' '))
        if trasaction_type == 1:
            balance = balance + amt
        else:
            if amt > balance:
                print("Insufficient Funds")
                continue
            else:
              balance = balance - amt
        print(balance)
    return 0

if __name__ == '__main__':
    main()
