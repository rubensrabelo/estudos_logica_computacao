from nadia.nadia_pt_fo import check_proof

answer = """
# (p ∨ q ) ∧ ( p ∨ r ) ⊢ p ∨ ( q ∧ r )

1. (P | Q) & ( P | R)		pre
2. P | Q			        &e 1
3. P | R			        &e 1
4. { P				        hip
5. P | (Q & R)			    |i 4
}
6. { Q				        hip
7.	{ P			            hip
8.	P | (Q & R)		        |i 7
    }
9. 	{ R			            hip
10.	Q & R			        &i 6, 9
11.	P | (Q & R)		        |i 10
    }
12. P | (Q & R)			    |e 3, 7-8, 9-11
}
13. P | (Q & R)			    |e 2, 4-5, 6-12
"""

print(check_proof(answer))
