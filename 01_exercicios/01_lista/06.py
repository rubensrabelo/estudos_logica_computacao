from nadia.nadia_pt_fo import check_proof

answer = """
# p → q ⊢ ¬q → ¬p

1. P -> Q		pre
2. { ~Q			hip
3.	{ P		hip
4.	Q		->e 3, 1
5.	@		~e 4, 2
}
6. ~P			~i 3-5
}
7. ~Q -> ~P		->i 2-6
"""

print(check_proof(answer))
