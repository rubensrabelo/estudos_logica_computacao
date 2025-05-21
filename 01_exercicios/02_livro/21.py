from nadia.nadia_pt_fo import check_proof

answer = """
# P | (P & Q) |- P

1. P | (P & Q)      pre
2. { P              hip
3. P                copie 2
}
4. { P & Q          hip
5. P                &e 4
}
6. P                |e 1, 2-3, 4-5
"""

print(check_proof(answer))