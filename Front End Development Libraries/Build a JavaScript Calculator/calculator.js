const calculator = document.getElementById('calculator');
const display = document.getElementById('display');
const displaySpan = display.querySelector('span');

let expression = '0';

function handleClear() {
  expression = '0';
  updateDisplay();
}

function handleNumberClick(value) {
  if (expression === '0' || expression === 'Error') {
    expression = value;
  } else {
    expression += value;
  }
  updateDisplay();
}

function handleOperatorClick(operator) {
  if (expression === 'Error') return;

  const lastChar = expression[expression.length - 1];
  if (!Number.isNaN(Number(lastChar))) {
    expression += operator;
  } else if (operator === '-' && lastChar !== '-') {
    expression += operator;
  } else if (lastChar !== '.') {
    expression = expression.slice(0, expression.length - 1) + operator;
  }
  updateDisplay();
}

function handleDecimalClick() {
  if (expression === 'Error') return;

  const lastNum = expression.split(/[-+*/]/).pop();
  if (!lastNum.includes('.')) {
    expression += '.';
  }
  updateDisplay();
}

function handleEqualsClick() {
  if (expression === 'Error') return;

  try {
    const result = eval(expression);
    expression = result.toString();
  } catch (error) {
    expression = 'Error';
  }
  updateDisplay();
}

function handleButtonClick(value) {
  switch (value) {
    case 'AC':
      handleClear();
      break;
    case '/':
    case '*':
    case '-':
    case '+':
      handleOperatorClick(value);
      break;
    case '=':
      handleEqualsClick();
      break;
    case '.':
      handleDecimalClick();
      break;
    default:
      handleNumberClick(value);
      break;
  }
}

function updateDisplay() {
  displaySpan.textContent = expression;
}

// Add event listeners to all buttons
const buttons = calculator.getElementsByTagName('button');
for (const button of buttons) {
  button.addEventListener('click', () => {
    handleButtonClick(button.textContent);
  });
}

updateDisplay();
