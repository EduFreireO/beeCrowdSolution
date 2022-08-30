function solution(text) {
// match return --> array
    let match = text.match(/[a-zA-Z]+/g)
    let maior = match[0]
 
    match.map(index => index.length > maior.length? maior = index: index)
    return maior 
}
