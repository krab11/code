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
