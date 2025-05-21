from nadia.nadia_pt_fo import check_proof

answer = """
# P -> Q, R -> S |- P | R -> Q | S

1. P -> Q           pre
2. R -> S           pre
3. { P | R          hip
4.  { P             hip
5.  Q               ->e 1, 4
6. Q | S            |i 5
    }
7. { R              hip
8. S                ->e 2, 7
9. Q | S            |i 8
    }
10. Q | S           |e 3, 4-6, 7-9
}
11. P | R -> Q | S  ->i 3-10
"""

print(check_proof(answer))