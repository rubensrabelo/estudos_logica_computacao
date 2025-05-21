from nadia.nadia_pt_fo import check_proof

answer = """
# P | Q, ~Q | R |- P | R

1. P | Q        pre
2. ~Q | R       pre
3. { P          hip
4. P | R        |i 3
}
5. { Q          hip
6.  { ~Q        hip
7.  @           ~e 5, 6
8.  R           @e 7
    }
9.  {R          hip
10. R           copie 9
    }
11. R           |e 2, 6-8, 9-10
12. P | R       |i 11
}
13. P | R           |e 1, 3-4, 5-12
"""

print(check_proof(answer))
