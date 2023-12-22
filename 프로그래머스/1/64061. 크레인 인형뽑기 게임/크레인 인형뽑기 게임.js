function solution(board, moves) {
    var answer = 0;
    let stack = [];
   
    moves.forEach((idx) => {
        // 전꺼와 해당 원소가 같지 않다면 스택에 넣어주기
        for (let i = 0; i < board.length; i++) {
            if (board[i][idx - 1] !== 0) {
                if (stack.length > 0 && board[i][idx - 1] === stack[stack.length - 1]) {
                    stack.pop();
                    answer += 2;
                } else {
                    stack.push(board[i][idx - 1]);
                }
                board[i][idx - 1] = 0;
                break;
            }
        }
    });
    return answer;
}
