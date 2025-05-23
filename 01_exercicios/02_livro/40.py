from nadia.nadia_pt_fo import check_proof

answer = """
# h) P -> (Q | R), ~Q, ~R |- ~P

1. P -> (Q | R)         pre
2. ~Q                   pre
3. ~R                   pre
4. { P                  hip
5. Q | R                ->e 4, 1
6.      { Q             hip
7.      @               ~e 6, 2
        }
8.      { R             hip
9.      @               ~e 8, 3
        }
10. @                   |e 5, 6-7, 8-9
}
11. ~P                  ~i 4-10
"""

print(check_proof(answer))
