var subtractProductAndSum = function(n) {
    n = n.toString().split('')
    const mult = n.reduce((acc, curr) => Number(acc) * Number(curr))
    const sum = n.reduce((acc, curr) => Number(acc) + Number(curr))
    return mult - sum 
};

