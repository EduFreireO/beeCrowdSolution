
 var average = function(salary) {
    salary = salary.sort()
    const max = salary[salary.length - 1]
    const min = salary[0]
    return (salary.reduce((acc, cur) => acc + cur) - min -max)/(salary.length - 2)
};