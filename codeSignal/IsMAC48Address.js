function solution(inputString) {
    const regex = /^([\dA-F]{2}-){5}[\dA-F]{2}$/
    return regex.test(inputString)
}
