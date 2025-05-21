from nadia.nadia_pt_fo import check_proof

answer = """
#  ⊢ (¬p → q) →((¬p →¬q)→p)

1. { ~P -> Q				        hip
2.	{ ~P -> ~Q			            hip
3.		{ ~P			            hip
4.		Q			                ->e 3, 1
5.		~Q			                ->e 3, 2
6.		@			                ~e 4, 5
}
7. 	P				                raa 3-6
}
8. (~P -> ~Q) -> P		            ->i 2-7
}
9. (~P -> Q) -> ((~P -> ~Q) -> P)	->i 1-8
"""

print(check_proof(answer))
