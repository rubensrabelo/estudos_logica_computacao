from nadia.nadia_pt_fo import check_proof

answer = """
# ~(P -> Q) |- Q -> P

1. ~(P -> Q)        pre
2. { Q              hip
3.  { P             hip
4.  Q               copie 2
    }
5. P -> Q           ->i 3-4
6. @                ~e 1, 5
7. P                @e 6
}
8. Q -> P           ->i 2-7
"""

print(check_proof(answer))
