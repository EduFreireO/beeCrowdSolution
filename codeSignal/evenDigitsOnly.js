/* What i did*/ 
function solution(n) {
    n = String(n).split('')
    for(digit of n)  
        if(Number(digit) % 2 != 0)
            return false    
    return true
}

// Better way.
function solution(n) {
    n = String(n).split('')
    return n.every(index => index % 2 == 0)
}

// Much better way
function solution(n) {
    return !(/[13579]/.test(String(n))) 
}
