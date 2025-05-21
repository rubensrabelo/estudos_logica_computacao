from nadia.nadia_pt_fo import check_proof

answer = """
# P -> (Q | R), Q -> S, R -> S |- P -> S

1. P -> (Q | R)     pre
2. Q -> S           pre
3. R -> S           pre
4. { P              hip
5. Q | R            ->e 1, 4
6.  { Q             hip
7.  S               ->e 2, 6
    }
8.  { R             hip
9.  S               ->e 3, 8
    }
10. S               |e 5, 6-7, 8-9
}
11. P -> S          ->i 4-10
"""

print(check_proof(answer))