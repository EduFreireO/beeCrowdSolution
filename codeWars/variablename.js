function solution(name)
{
    const valid = /^[a-z_][\w_]*$/
    return valid.test(name)
}

