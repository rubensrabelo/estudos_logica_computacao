from nadia.nadia_pt_fo import check_proof

answer = """
# P | Q |- R -> (P | Q) & R

1. P | Q                pre
2. { R                  hip
3.  { P                 hip
4.  P | Q               |i 3
5.  (P | Q) & R         &i 4, 2
    }
6.  { Q                 hip
7.  P | Q               |i 6
8.  (P | Q) & R         &i 7, 2
    }
9. (P | Q) & R          |e 1, 3-5, 6-8
}
10. R -> (P | Q) & R    ->i 2-9
"""

print(check_proof(answer))