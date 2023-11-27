function solution(array, height) {
    const result = array.filter((el) => el > height)
    return result.length;
}