from nadia.nadia_pt_fo import check_proof

answer = """
# ~P -> P | P

1. ~P -> P  pre
2. { ~P     hip
3.  P       ->e 1, 2
4. @        ~e 2, 3
}
5. P        raa 2-4
"""

print(check_proof(answer))
