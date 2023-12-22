function compare(com, target) {
    // 폰에 숫자들 넣어주기
    const phone = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    let visited = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]];
    let q = [];
    
    // 초기 위치 찾기
    let y = 0;
    let x = 0;
    for (let i = 0; i < 4; i++) {
        for (let j = 0; j < 3; j++) {
            if (phone[i][j] === com) {
                y = i;
                x = j;
                visited[y][x] = 1;
                break;
            }
        }
    }

    q.push([y, x, 0]); // y좌표, x좌표, cnt 초기값 1

    while (q.length > 0) {
        let [ny, nx, cnt] = q.shift();

        if (phone[ny][nx] === target) {
            return cnt;
        }

        const dy = [-1, 0, 1, 0];
        const dx = [0, -1, 0, 1];

        for (let i = 0; i < 4; i++) {
            const nny = ny + dy[i];
            const nnx = nx + dx[i];

            if (0 <= nny && nny < 4 && 0 <= nnx && nnx < 3 && visited[nny][nnx] === 0) {
                visited[nny][nnx] = 1;
                q.push([nny, nnx, cnt + 1]);
            }
        }
    }

    return -1; // target을 찾을 수 없는 경우 -1을 반환
}

function check(com1, com2, target,hand) {
    const leftNum = [1, 4, 7];
    const rightNum = [3, 6, 9];
    
    if (leftNum.includes(target)) {
        return 1;
    } else if (rightNum.includes(target)) {
        return 2;
    } else {
        tmp1 = compare(com1, target) // 왼손
        tmp2 = compare(com2, target) // 오른손
        // console.log(tmp1, tmp2);
        if ( tmp1 < tmp2 ) {
            return 1;
        } else if (tmp1 > tmp2){
            return 2;
        } else if (tmp1 === tmp2) {
            if (hand === 'left') {
                return 1;
            }else if (hand === 'right') {
                return 2;
            }
            
        }
    }
}

function solution(numbers, hand) {
    let result = '';
    let left = '*';
    let right = '#';

    numbers.forEach((num) => {
        // console.log(left,right,num)
        const side = check(left, right, num,hand);
        // console.log(side);
        
        if (side === 1) {
            result += 'L'
            left = num;
        } else {
            result += 'R'
            right = num;
        }
    });

    return result;
}
