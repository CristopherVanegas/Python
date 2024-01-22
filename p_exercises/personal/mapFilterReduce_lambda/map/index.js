
const dollars = ["32$", "15$", "12$", "17$", "20$"] 

// map // 
/*["32$", "15$", "12$", "17$", "20$"]  -> [32, 15, 12, ..]
"32" -> 32*/ 

// Forma de los 70s 
let prices = []; 
for (let i = 0; i < dollars.length; i++) {
    prices[i] = Number(dollars[i].slice(0, dollars[i].length-1)) 
}
// Forma zoomer 
prices = []; 
for (const dollar of dollars) { 
    prices.push(Number(dollar.slice(0, dollar.length-1))) 
} 
// Forma Hacker 2021 
prices = dollars.map((dollar) => Number(dollar.slice(0, dollar.length-1))); 
console.log(prices)



// filter // 
// Forma zoomer 
let expensive = []; 
for(const price of prices) {
    if(price >= 20)  {
        expensive.push(price); 
    }
} 
// Forma Hacker 2021 
expensive = prices.filter((price) => price >= 20); 
console.log(expensive) 



// reduce = the action tu put together or accumulate thing to create a new one. //
// Forma zoomer 
let sum = 0; 
for (price of expensive) {
    sum += price; 
}

// Forma Hacker 2021 
sum = expensive.reduce((acum, list_item) => acum + list_item) 




// De una 
sum = dollars 
    .map(dollar => Number(dollar.slice(0, dollar.length-1))) 
    .filter(price => price >= 20) 
    .reduce((acum, list_item) => acum + list_item); 

// De una - Forma manual ( zoomer )
sum = 0; 
for (const dollar of dollars) {
    const price = Number(dollar.slice(0, dollar.length-1)); 
    if (price >= 20) {
        sum += price; 
    }
}
console.log(sum); 

console.log(prices.map(price => ({price, currency: '$'})).forEach(obj => obj.price += 10)); 

for (const obj of prices.map(price => ({price, currency: '$'}))) {
    obj.price += 10; 
}

