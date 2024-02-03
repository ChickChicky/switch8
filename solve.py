#!/usr/bin/env python3

board:  list[int] = [ 1, 1, 1, 1, 0, 2, 2, 2, 2 ]
target: list[int] = [ 2, 2, 2, 2, 0, 1, 1, 1, 1 ]

def get_moves_part(board:list[int]) -> list[(int,int)]:
    moves: list[(int,int)] = []
    for i, p in enumerate(board):
        if p == 1 and i < len(board)-1:
            if board[i+1] == 0:
                moves.append((i,i+1))
            elif i < len(board)-2 and board[i+1] == 2 and board[i+2] == 0:
                moves.append((i,i+2))
    return moves

def get_moves(board:list[int]) -> list[(int,int)]:
    return get_moves_part(board)+[(len(board)-1-a,len(board)-1-b) for a,b in get_moves_part([{0:0,1:2,2:1}[p] for p in reversed(board)])]

def make_tree( board:list[int], target:list[int], tree:dict, solutions:list[list[(int,int)]], parents:list[(int,int)] ):
    for a,b in get_moves(board):
        sub = {}
        tree[(a,b)] = sub
        nb = [*board]
        nb[a],nb[b] = nb[b],nb[a]
        path = parents+[(a,b)]
        if nb == target:
            solutions.append(path)
        else:
            make_tree(nb,target,sub,solutions,path)
            
def print_tree(tree:dict,indent:int=0):
    for k,v in tree.items():
        print(' '*indent+str(k))
        print_tree(v,indent+1)

tree = {}
solutions = []
make_tree(board,target,tree,solutions,[])


for i,solution in enumerate(solutions):
    print('\n # SOLUTION %d # \n'%(i+1,))
    bd = [*board]
    for a,b in solution:
        print(''.join(['\x1b[37m. \x1b[39m','\x1b[38;2;0;255;0m\U000f085b\x1b[39m','\x1b[38;2;255;255;0m\U000f085b\x1b[39m'][p] for p in bd))
        print(''.join(('╰╯'[b>a] if i//2 == b and not i%2 else '╰╯'[b<a] if i//2 == a and not i%2 else '─' if i/2>min(a,b) and i/2<max(a,b) else ' ') for i in range(len(bd)*2)))
        input()
        bd[a],bd[b] = bd[b],bd[a]