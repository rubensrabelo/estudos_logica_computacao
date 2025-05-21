from nadia.nadia_pt_fo import check_proof

answer = """
# P -> Q | ~Q -> ~P

1. P -> Q       pre
2. { ~Q         hip
3.  { P         hip
4.  Q           ->e 1, 3
5.  @           ~e 2, 4
    }
6. ~P           ~i 3-5
}
7. ~Q -> ~P     ->i 2-6
"""

print(check_proof(answer))