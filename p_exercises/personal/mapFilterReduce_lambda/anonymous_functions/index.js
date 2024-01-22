
function apply(num, f) {
    return f(num); 
} 

function double(num) {
    return 2 * num; 
} 

// Anonymous func. 
console.log(apply(5, function (num) {return 2 * num; })); 


// Arrow func - One liner. 
console.log(apply(5, (num) => 2 * num)) 

