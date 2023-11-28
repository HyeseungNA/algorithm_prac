function solution(array) {
    var answer = 0;
    const arr = array.sort((a,b) => b - a)
    idx = Math.floor(arr.length / 2)
    return arr[idx];
}