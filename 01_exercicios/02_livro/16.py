from nadia.nadia_pt_fo import check_proof

answer = """
# |- Q -> (P -> (P -> (Q -> P)))

1. { Q                              hip
2.  { P                             hip
3.      { P                         hip
4.          { Q                     hip
5.           P                      copie 2
            }
6.      Q -> P                      ->i 4-5 
        }
7.  P -> (Q -> P)                   ->i 3-6
    }
8. P -> (P -> (Q -> P))            ->i 2-7
}
9. Q -> (P -> (P -> (Q -> P)))      ->i 1-8
"""

print(check_proof(answer))