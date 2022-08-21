function solution(s) {
    let letras = []
    for(let aux of s){
        if(!letras.includes(aux))
            letras.push(aux)
    }
    return letras.length()
}
