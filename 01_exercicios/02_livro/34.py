from nadia.nadia_pt_fo import check_proof

answer = """
# ~P |- P -> Q

1. ~P       pre
2. { P      hip
3. @        ~e 1, 2
4. Q        @e 3
}
5. P -> Q   ->i 2-4
"""

print(check_proof(answer))
