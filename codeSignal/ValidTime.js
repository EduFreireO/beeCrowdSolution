function solution(time) {
    return Number(time.match(/[\d]{2}/)[0]) < 24 && Number(time.match(/[\d]{2}$/)[0]) < 60
}