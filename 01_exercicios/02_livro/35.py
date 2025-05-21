from nadia.nadia_pt_fo import check_proof

answer = """
# P | Q, ~Q |- P

1. P | Q    pre
2. ~Q       pre
3. { P      hip
4. P        copie 3
}
5. { Q      hip
6. @        ~e 2, 5
7. P        @e 6
}
8. P        |e 1, 3-4, 5-7
"""

print(check_proof(answer))
