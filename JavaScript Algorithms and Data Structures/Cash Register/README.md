# Cash Register

💰 A JavaScript Function to Calculate Change in a Cash Register

Greetings! This is a JavaScript function I developed as part of the Cash Register activity in the freeCodeCamp JavaScript curriculum.

## Function Description

The provided JavaScript function simulates a cash register by calculating the change to be given back to a customer. It takes into account the cash in the drawer (cid) and returns the appropriate change and status.

## How It Works

1. The `currencyValues` object holds the value of each currency denomination for calculations.
2. The function `changer(changeDue, cid)` calculates the change due using the provided change amount and the cash in the drawer (cid).
3. The `checkCashRegister(price, cash, cid)` function is the main function that calculates the change based on the provided price, cash given, and cash in the drawer.
4. It calculates the total amount in the cash register using the `cid` array.
5. Depending on the calculated total and other conditions, the function determines the status of the register and the change to be given.
6. The `changer` function uses the `currencyValues` object to calculate the optimal number of each currency denomination to give as change.
7. If the total change amount is insufficient, the status is set as "INSUFFICIENT_FUNDS". If the change is exact, the status is "CLOSED". Otherwise, the status is "OPEN".

Feel free to test the function with different inputs for price, cash, and the cash-in-drawer array. Observe how the function accurately calculates the change and determines the status of the register.

Happy coding! 💻🚀
