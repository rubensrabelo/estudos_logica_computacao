from nadia.nadia_pt_fo import check_proof

answer = """
# P | Q |- Q | P

1. P | Q        pre
2. { P          hip
3. Q | P        |i 2
}
4. { Q          hip
5. Q | P        |i 4
}
6. Q | P        |e 1, 2-3, 4-5
"""

print(check_proof(answer))