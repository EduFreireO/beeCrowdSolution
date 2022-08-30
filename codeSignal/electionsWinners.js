function solution(votes, k) {
    let maxValue = votes[0]
    
    for(vote of votes)
        if(vote > maxValue)
            maxValue = vote
            
    if(k != 0)    
        return votes.filter(value => value + k > maxValue).length
    
    const quantidade = votes.filter(vote => {
        if(vote == maxValue)
            return vote
    })
        
    return quantidade.length > 1? 0 : 1
}
