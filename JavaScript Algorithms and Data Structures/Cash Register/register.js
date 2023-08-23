// Declare the array as a global variable
const currencyValues = {
  "PENNY": 0.01,
  "NICKEL": 0.05,
  "DIME": 0.1,
  "QUARTER": 0.25,
  "ONE": 1,
  "FIVE": 5,
  "TEN": 10,
  "TWENTY": 20,
  "ONE HUNDRED": 100,
};

// Function to calculate the change
function changer(changeDue, cid) {
  let changeArray = [];

  for (let i = cid.length - 1; i >= 0; i--) {
    const [currency, amount] = cid[i];
    const value = currencyValues[currency];
    let count = Math.floor(amount / value);
    let toGive = 0;

    while (changeDue >= value && count > 0) {
      changeDue -= value;
      changeDue = changeDue.toFixed(2);
      count--;
      toGive++;
    }

    if (toGive > 0) {
      changeArray.push([currency, toGive * value]);
    }
  }

  return changeArray;
}

// Main function
function checkCashRegister(price, cash, cid) {
  let stat = { status: "OPEN", change: [] };
  let tot = 0;

  // Calculate the total amount in the cash register
  for (let coin of cid) {
    tot += coin[1];
  }

  let total = tot.toFixed(2);

  // Check if the cash-in-drawer is less than the change due
  if (total < cash - price) {
    stat.status = "INSUFFICIENT_FUNDS";
  }
  // Check if the cash-in-drawer is equal to the change due
  else if (total == cash - price) {
    stat.status = "CLOSED";
    stat.change = cid;
  } else {
    // Calculate the change and update the status and change array
    stat.change = changer(cash - price, cid);
    let changeTotal = stat.change.reduce((acc, [_, value]) => acc + value, 0);

    if (changeTotal < cash - price) {
      stat.status = "INSUFFICIENT_FUNDS";
      stat.change = [];
    }
  }

  return stat;
}

console.log(checkCashRegister(19.5, 20, [["PENNY", 0.01], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 1], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]));
