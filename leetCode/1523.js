var countOdds = function(low, high) {
  let quant = 0
  for(let i = low; i <= high; i++)
    if(i % 2 != 0)
        quant +=  1 
  return quant  
};