---
title: "Minimax Algorithm - Final Fantasy VIII - Triple Triad Card Game"  
tags:  
  - Engineering  
  - Minimax  
  - Artificial Intelligence  
  - Gaming  
header:  
  teaser: /assets/images/2021-03-26-final-fantasy-viii-triple-triad-solver/img02.png  
  og_image: /assets/images/2021-03-26-final-fantasy-viii-triple-triad-solver/img0w.png  
---

{% include gallery caption="Final Fantasy VIII - Triple Triad Solver" layout="half" %}

## Introduction

Triple Triad is an awesome card game from Final Fantasy VIII. I loved this game as child, and recently decided to play it again for nostalgic reasons. 
When playing through Triple Triad, I wanted to write a solver to help decide on optimal decision making to improve my chances of winning the game. I wrote a Minimax solver with controllable search depth. 
You can specify the game state in the `gamestate.yaml` file.

![Triple Triad Solver](/assets/images/2021-03-26-final-fantasy-viii-triple-triad-solver/img02.png)

You can find the code on my [GitHub repository](https://github.com/e-loughlin/FFVIII-CardGameAI).

## Understanding Triple Triad

For those unfamiliar, Triple Triad is a card game within Final Fantasy VIII where players take turns placing cards on a 3x3 grid. Each card has four numbers representing its strength on the top, bottom, left, and right sides. The goal is to capture your opponent’s cards by having higher numbers on adjacent sides.

The complete rules can be found [here](https://finalfantasy.fandom.com/wiki/Triple_Triad_(Final_Fantasy_VIII)).

## The Minimax Algorithm

The [Minimax algorithm](https://en.wikipedia.org/wiki/Minimax) is a decision rule for minimizing the possible loss in a worst-case scenario. It plays a pivotal role in many AI-driven games by evaluating all possible moves to determine the best course of action.

### How It Works

1. **Game State Representation**: The game state is represented as a tree of possible moves. Each node corresponds to a game state, and the branches represent possible moves.

2. **Maximizing and Minimizing**: The algorithm alternates between trying to maximize the score (for the AI) and minimize it (for the opponent).

3. **Recursive Evaluation**: The algorithm recursively evaluates each possible move, exploring future states, and assigns a score to each possible outcome.

### Code Example

```python
def minimax(game_state, depth, maximizing_player):
    if depth == 0 or game_over(game_state):
        return evaluate_state(game_state)

    if maximizing_player:
        max_eval = float('-inf')
        for move in possible_moves(game_state):
            eval = minimax(make_move(game_state, move), depth - 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in possible_moves(game_state):
            eval = minimax(make_move(game_state, move), depth - 1, True)
            min_eval = min(min_eval, eval)
        return min_eval
```

In this example, `minimax` explores all possible moves up to a certain depth, recursively evaluating the best possible outcome for the AI.


### Example of Script Usage

```txt


Player (P) Cards:
  A-P    B-P    C-P    D-P    E-P  
 | 4 |  | 6 |  | 6 |  | 3 |  | 8 | 
 |2 4|  |6 3|  |3 6|  |1 5|  |4 8| 
 | 5 |  | 1 |  | 2 |  | 2 |  | 4 | 


Opponent (O) Cards:
  V-O    W-O    X-O    Y-O    Z-O  
 | 1 |  | 6 |  | 7 |  | 3 |  | 3 | 
 |3 8|  |6 3|  |3 5|  |4 6|  |3 2| 
 | 8 |  | 1 |  | 1 |  | 4 |  | 4 | 


Board:
-------------------------------------------
Current Player: P  |  Points: P = 0, O = 0
                     
 |   |  |   |  |   | 
 |   |  |   |  |   | 
 |   |  |   |  |   | 

                     
 |   |  |   |  |   | 
 |   |  |   |  |   | 
 |   |  |   |  |   | 

                     
 |   |  |   |  |   | 
 |   |  |   |  |   | 
 |   |  |   |  |   | 


Determining best move...
* Best Move = (('A', 1), Score = 0)
Player P: Make a move:
Choose a card to place (Available = ['A', 'B', 'C', 'D', 'E'].A
Choose a position: (Available = [1, 2, 3, 4, 5, 6, 7, 8, 9])1
Player (P) Cards:
  B-P    C-P    D-P    E-P  
 | 6 |  | 6 |  | 3 |  | 8 | 
 |6 3|  |3 6|  |1 5|  |4 8| 
 | 1 |  | 2 |  | 2 |  | 4 | 


Opponent (O) Cards:
  V-O    W-O    X-O    Y-O    Z-O  
 | 1 |  | 6 |  | 7 |  | 3 |  | 3 | 
 |3 8|  |6 3|  |3 5|  |4 6|  |3 2| 
 | 8 |  | 1 |  | 1 |  | 4 |  | 4 | 


Board:
-------------------------------------------
Current Player: O  |  Points: P = 1, O = 0
                     
 |   |  |   |  |   | 
 |   |  |   |  |   | 
 |   |  |   |  |   | 

                     
 |   |  |   |  |   | 
 |   |  |   |  |   | 
 |   |  |   |  |   | 

  A-P                
 | 4 |  |   |  |   | 
 |2 4|  |   |  |   | 
 | 5 |  |   |  |   | 


Player O: Make a move:
Choose a card to place (Available = ['V', 'W', 'X', 'Y', 'Z'].W
Choose a position: (Available = [2, 3, 4, 5, 6, 7, 8, 9])2
Player (P) Cards:
  B-P    C-P    D-P    E-P  
 | 6 |  | 6 |  | 3 |  | 8 | 
 |6 3|  |3 6|  |1 5|  |4 8| 
 | 1 |  | 2 |  | 2 |  | 4 | 


Opponent (O) Cards:
  V-O    X-O    Y-O    Z-O  
 | 1 |  | 7 |  | 3 |  | 3 | 
 |3 8|  |3 5|  |4 6|  |3 2| 
 | 8 |  | 1 |  | 4 |  | 4 | 


Board:
-------------------------------------------
Current Player: P  |  Points: P = 0, O = 2
                     
 |   |  |   |  |   | 
 |   |  |   |  |   | 
 |   |  |   |  |   | 

                     
 |   |  |   |  |   | 
 |   |  |   |  |   | 
 |   |  |   |  |   | 

  A-O    W-O         
 | 4 |  | 6 |  |   | 
 |2 4|  |6 3|  |   | 
 | 5 |  | 1 |  |   | 


Determining best move...
* Best Move = (('B', 3), Score = 0)
Player P: Make a move:
Choose a card to place (Available = ['B', 'C', 'D', 'E'].B 
Choose a position: (Available = [3, 4, 5, 6, 7, 8, 9])3
Player (P) Cards:
  C-P    D-P    E-P  
 | 6 |  | 3 |  | 8 | 
 |3 6|  |1 5|  |4 8| 
 | 2 |  | 2 |  | 4 | 


Opponent (O) Cards:
  V-O    X-O    Y-O    Z-O  
 | 1 |  | 7 |  | 3 |  | 3 | 
 |3 8|  |3 5|  |4 6|  |3 2| 
 | 8 |  | 1 |  | 4 |  | 4 | 


Board:
-------------------------------------------
Current Player: O  |  Points: P = 2, O = 1
                     
 |   |  |   |  |   | 
 |   |  |   |  |   | 
 |   |  |   |  |   | 

                     
 |   |  |   |  |   | 
 |   |  |   |  |   | 
 |   |  |   |  |   | 

  A-O    W-P    B-P  
 | 4 |  | 6 |  | 6 | 
 |2 4|  |6 3|  |6 3| 
 | 5 |  | 1 |  | 1 | 


Player O: Make a move:
Choose a card to place (Available = ['V', 'X', 'Y', 'Z'].V
Choose a position: (Available = [4, 5, 6, 7, 8, 9])7
Player (P) Cards:
  C-P    D-P    E-P  
 | 6 |  | 3 |  | 8 | 
 |3 6|  |1 5|  |4 8| 
 | 2 |  | 2 |  | 4 | 


Opponent (O) Cards:
  X-O    Y-O    Z-O  
 | 7 |  | 3 |  | 3 | 
 |3 5|  |4 6|  |3 2| 
 | 1 |  | 4 |  | 4 | 


Board:
-------------------------------------------
Current Player: P  |  Points: P = 2, O = 2
  V-O                
 | 1 |  |   |  |   | 
 |3 8|  |   |  |   | 
 | 8 |  |   |  |   | 

                     
 |   |  |   |  |   | 
 |   |  |   |  |   | 
 |   |  |   |  |   | 

  A-O    W-P    B-P  
 | 4 |  | 6 |  | 6 | 
 |2 4|  |6 3|  |6 3| 
 | 5 |  | 1 |  | 1 | 


Determining best move...
* Best Move = (('C', 4), Score = 0)
Player P: Make a move:
Choose a card to place (Available = ['C', 'D', 'E'].C
Choose a position: (Available = [4, 5, 6, 8, 9])4
Player (P) Cards:
  D-P    E-P  
 | 3 |  | 8 | 
 |1 5|  |4 8| 
 | 2 |  | 4 | 


Opponent (O) Cards:
  X-O    Y-O    Z-O  
 | 7 |  | 3 |  | 3 | 
 |3 5|  |4 6|  |3 2| 
 | 1 |  | 4 |  | 4 | 


Board:
-------------------------------------------
Current Player: O  |  Points: P = 3, O = 2
  V-O                
 | 1 |  |   |  |   | 
 |3 8|  |   |  |   | 
 | 8 |  |   |  |   | 

  C-P                
 | 6 |  |   |  |   | 
 |3 6|  |   |  |   | 
 | 2 |  |   |  |   | 

  A-O    W-P    B-P  
 | 4 |  | 6 |  | 6 | 
 |2 4|  |6 3|  |6 3| 
 | 5 |  | 1 |  | 1 | 


Player O: Make a move:
Choose a card to place (Available = ['X', 'Y', 'Z'].X
Choose a position: (Available = [5, 6, 8, 9])5
Player (P) Cards:
  D-P    E-P  
 | 3 |  | 8 | 
 |1 5|  |4 8| 
 | 2 |  | 4 | 


Opponent (O) Cards:
  Y-O    Z-O  
 | 3 |  | 3 | 
 |4 6|  |3 2| 
 | 4 |  | 4 | 


Board:
-------------------------------------------
Current Player: P  |  Points: P = 3, O = 3
  V-O                
 | 1 |  |   |  |   | 
 |3 8|  |   |  |   | 
 | 8 |  |   |  |   | 

  C-P    X-O         
 | 6 |  | 7 |  |   | 
 |3 6|  |3 5|  |   | 
 | 2 |  | 1 |  |   | 

  A-O    W-P    B-P  
 | 4 |  | 6 |  | 6 | 
 |2 4|  |6 3|  |6 3| 
 | 5 |  | 1 |  | 1 | 


Determining best move...
* Best Move = (('D', 6), Score = 0)
Player P: Make a move:
Choose a card to place (Available = ['D', 'E'].D
Choose a position: (Available = [6, 8, 9])6
Player (P) Cards:
  E-P  
 | 8 | 
 |4 8| 
 | 4 | 


Opponent (O) Cards:
  Y-O    Z-O  
 | 3 |  | 3 | 
 |4 6|  |3 2| 
 | 4 |  | 4 | 


Board:
-------------------------------------------
Current Player: O  |  Points: P = 4, O = 3
  V-O                
 | 1 |  |   |  |   | 
 |3 8|  |   |  |   | 
 | 8 |  |   |  |   | 

  C-P    X-O    D-P  
 | 6 |  | 7 |  | 3 | 
 |3 6|  |3 5|  |1 5| 
 | 2 |  | 1 |  | 2 | 

  A-O    W-P    B-P  
 | 4 |  | 6 |  | 6 | 
 |2 4|  |6 3|  |6 3| 
 | 5 |  | 1 |  | 1 | 


Player O: Make a move:
Choose a card to place (Available = ['Y', 'Z'].Y
Choose a position: (Available = [8, 9])8
Player (P) Cards:
  E-P  
 | 8 | 
 |4 8| 
 | 4 | 


Opponent (O) Cards:
  Z-O  
 | 3 | 
 |3 2| 
 | 4 | 


Board:
-------------------------------------------
Current Player: P  |  Points: P = 4, O = 4
  V-O    Y-O         
 | 1 |  | 3 |  |   | 
 |3 8|  |4 6|  |   | 
 | 8 |  | 4 |  |   | 

  C-P    X-O    D-P  
 | 6 |  | 7 |  | 3 | 
 |3 6|  |3 5|  |1 5| 
 | 2 |  | 1 |  | 2 | 

  A-O    W-P    B-P  
 | 4 |  | 6 |  | 6 | 
 |2 4|  |6 3|  |6 3| 
 | 5 |  | 1 |  | 1 | 


Determining best move...
* Best Move = (('E', 9), Score = 0)
Player P: Make a move:
Choose a card to place (Available = ['E'].E
Choose a position: (Available = [9])9
Player (P) Cards:






Opponent (O) Cards:
  Z-O  
 | 3 | 
 |3 2| 
 | 4 | 


Board:
-------------------------------------------
Current Player: O  |  Points: P = 5, O = 4
  V-O    Y-O    E-P  
 | 1 |  | 3 |  | 8 | 
 |3 8|  |4 6|  |4 8| 
 | 8 |  | 4 |  | 4 | 

  C-P    X-O    D-P  
 | 6 |  | 7 |  | 3 | 
 |3 6|  |3 5|  |1 5| 
 | 2 |  | 1 |  | 2 | 

  A-O    W-P    B-P  
 | 4 |  | 6 |  | 6 | 
 |2 4|  |6 3|  |6 3| 
 | 5 |  | 1 |  | 1 | 


Winner is P. Final score: {'P': 5, 'O': 4}

```
