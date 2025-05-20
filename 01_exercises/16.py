from nadia.nadia_pt_fo import check_proof

answer = """
# 16. p∨q ⊢ ¬p → q

1. P | Q        pre
2. { ~P         hip
3.      { P     hip
4.      @       ~e 2, 3
5.      Q       @e 4
        }
6.      { Q     hip
7.      Q       copie 6
        }
8.  Q           |e 1, 3-5, 6-7
}
9. ~P -> Q      ->i 2-8
"""

print(check_proof(answer))
