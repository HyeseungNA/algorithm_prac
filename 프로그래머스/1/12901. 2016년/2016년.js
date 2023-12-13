function solution(a, b) {
    day = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
    return day[new Date("2016-" + String(a) + "-" +String(b)).getDay()]
    
}