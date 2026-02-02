def solution(n, w, num):
    row = (num - 1) // w
    pos = (num - 1) % w

    if row % 2 == 0:
        col = pos
    else:
        col = w - 1 - pos

    top_row = (n - 1) // w
    last_cnt = n % w

    if last_cnt != 0:
        if top_row % 2 == 0:          # 왼 → 오
            if col >= last_cnt:
                top_row -= 1
        else:                          # 오 → 왼
            if col < w - last_cnt:
                top_row -= 1

    return top_row - row + 1
