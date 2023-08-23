function palindrome(str) {
  
  // Convert the string to lowercase and remove non-alphanumeric characters
  const cleanStr = str.toLowerCase().replace(/[\W_]/g, '');
 
  // Compare characters using array methods
   return cleanStr.split('').every((char, index) => char === cleanStr[cleanStr.length - 1 - index]);
}

console.log(palindrome("1 eye for of 1 eye."));
