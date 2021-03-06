import sys

if __name__ == '__main__':
    n, k = map(int, input().strip().split(" "))
    rq, cq = map(int, input().strip().split(" "))

    up_squares = n - rq
    right_squares = n - cq
    down_squares = rq - 1
    left_squares = cq - 1
    left_up_squares = min(left_squares, up_squares)
    right_up_squares = min(up_squares, right_squares)
    left_down_squares = min(down_squares, left_squares)
    right_down_squares = min(right_squares, down_squares)

    for _ in range(0, k):
        ro, co = map(int, input().strip().split(" "))

        if ro == rq and co < cq and abs(co - cq) - 1 < left_squares:
            left_squares = abs(co - cq) - 1
        if ro == rq and co > cq and abs(co - cq) - 1 < right_squares:
            right_squares = abs(co - cq) - 1
        if co == cq and ro < rq and abs(ro - rq) - 1 < down_squares:
            down_squares = abs(ro - rq) - 1
        if co == cq and ro > rq and abs(ro - rq) - 1 < up_squares:
            up_squares = abs(ro - rq) - 1

        if abs(ro - rq) == abs(co - cq):
            if ro > rq and co < cq and abs(ro - rq) - 1 < left_up_squares:
                left_up_squares = abs(ro - rq) - 1
            if ro < rq and co < cq and abs(ro - rq) - 1 < left_down_squares:
                left_down_squares = abs(ro - rq) - 1
            if ro < rq and co > cq and abs(ro - rq) - 1 < right_down_squares:
                right_down_squares = abs(ro - rq) - 1
            if ro > rq and co > cq and abs(ro - rq) - 1 < right_up_squares:
                right_up_squares = abs(ro - rq) - 1

    total_moves = right_squares + left_squares + up_squares + down_squares + left_down_squares + left_up_squares + right_up_squares + right_down_squares

    print(total_moves)
