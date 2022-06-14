# Random Optimization Stuff

## Project List

- [ATM Problem with Integer Linear Programming](#atm-problem-with-integer-linear-programming)

## ATM Problem with Integer Linear Programming

This problem uses Integer Linear Programming approach to solve the following problem :

Given money `m` (integer) THB with the following bank notes
- 1000 THB
- 500 THB
- 100 THB
- 50 THB
- 20 THB

and following coins
- 10 THB
- 5 THB
- 2 THB
- 1 THB

The goal is to minimize the usage of coin and bank notes given that you need to get `m` THB amount of money.

This problem, at a first glance, can be solved by a simple approach using an algorithm below

```python
money = int(input("Enter Money : "))
banktypes = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
bankcount = [0 for i in range(len(banktypes))]

for i in range(len(banktypes) - 1, -1, -1):
    bankcount[i], money = divmod(money, banktypes[i])

for cnt, typ in zip(bankcount, banktypes):
    print(cnt, typ)
```

In an overcomplicated approach, we can also write a problem as

- ### Minimize **[1,1,1,1,1,1,1,1,1] * bankcount**
- ### Subject to
    - **[1,2,5,10,20,50,100,500,1000] * bankcount = m**
    - **bankcount_i >= 0** for all bankcount_i in bankcount

Which is **Integer Linear Programming** problem which we solve it using `cvxopt` package in python.
