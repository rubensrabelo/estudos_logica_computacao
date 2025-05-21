from nadia.nadia_pt_fo import check_proof

answer = """
# 25. ¬( ¬p ∨ ¬q ) ⊢ p ∧ q

1. ~( ~P | ~Q ) pre
2. { ~P         hip
3. ~P | ~Q      |i 2
4. @            ~e 1, 3
}
5. P            raa 2-4
6. { ~Q         hip
7. ~P | ~Q      |i 6
8. @            ~e 1, 7
}
9. Q            raa 6-8
10. P & Q       &i 5, 9
"""

print(check_proof(answer))
