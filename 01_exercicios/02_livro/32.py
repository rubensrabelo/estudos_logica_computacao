from nadia.nadia_pt_fo import check_proof

answer = """
# ~(~P | Q) |- P

1. ~(~P | Q)    pre
2. { ~P         hip
3. ~P | Q       |i 2
4. @            ~e 1, 3
}
5. P           raa 2-4
"""

print(check_proof(answer))
