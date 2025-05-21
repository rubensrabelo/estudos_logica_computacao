from nadia.nadia_pt_fo import check_proof

answer = """
# |- (P -> Q) -> ((R -> S) -> (P & R -> Q & S))

1. { P -> Q                                         hip
2.  { R -> S                                        hip
3.      { P & R                                     hip
4.      P                                           &e 3
5.      R                                           &e 3
6.      Q                                           ->e 1, 4
7.      S                                           ->e 2, 5
8.      Q & S                                       &i 6, 7
        }
9.      P & R -> Q & S                              ->i 3-8
    }
10. (R -> S) -> (P & R -> Q & S)                    ->i 2-9
}
11. (P -> Q) -> ((R -> S) -> (P & R -> Q & S))      ->i 1-10
"""

print(check_proof(answer))