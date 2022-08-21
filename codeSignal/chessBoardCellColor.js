function solution(cell1, cell2) {   
    const letters = ['A','C','E','G']
    if(letters.includes(cell1[0]) != letters.includes(cell2[0]))
        return (Number(cell1[1]) % 2 != Number(cell2[1]) % 2)
    else{
        return (Number(cell1[1]) % 2 == Number(cell2[1]) % 2)
    }
      


}
