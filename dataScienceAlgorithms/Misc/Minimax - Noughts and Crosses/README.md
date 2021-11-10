
# **Minimax - Noughts and Crosses**
### An AI vs AI simulator using the minimax algorithm.

You should know this game, as everybody plays it as a kid until they master it and it becomes boring. But in case your childhood is a little fuzzy around the edges, here is a reminder. Two players take turns to place symbols on a 3x3 grid. First one to make a line (horizontal, vertical, or diagonal) of three of their symbol wins. Tradition is that the crosses (x) go first, the noughts (o) second.

Here is an example game (rendered using ascii art, with only the vertical lines!):
```
 | |       | |      | |x     | |x     |x|x    o|x|x    o|x|x
 |x|  ->   |x|o ->  |x|o ->  |x|o ->  |x|o ->  |x|o ->  |x|o
 | |       | |      | |     o| |     o| |     o| |     o|x|
 ```
x ultimately wins with a vertical line. As for when o lost, they did so with their very first move, even though it took x a few moves to force the win.

### Minimax Algorithm

Minimax is best understood by starting at the end of a game. Imagine the board looks like this:
```
o|x|x
 |x|o
o|x|
```
The game has ended, and x has won. Lets say that the value is +1 when x wins, -1 when y wins, and 0 for a draw. So this state (of the board) has a score of +1.

Key to minimax is the realisation that if we can assign a score to the end states then we can assign a score to any other state by assuming the players always play the best move available. For x that means the move that maximises the score, for o that means the move that minimises the score.

Lets go back a move:
```
o|x|x
 |x|o
o| |
```
How do we assign a score? It is the turn of x and they have three choices:
```
o|x|x    o|x|x    o|x|x
x|x|o     |x|o     |x|o
o| |     o|x|     o| |x
```
If we assume the score is defined for each of these states then naturally x will play the move associated with ending in the highest scoring state.

We know the score for the middle state is +1, as it is a winning state. What about the other two? The score of the left and right states can be calculated in the exact same way as for this state, the one difference being it will then be the turn of o, who will want to minimise the score.

The left state has two choices for o:
```
o|x|x    o|x|x
x|x|o    x|x|o
o|o|     o| |o
```
which will be immediately followed by x taking the only move it has left and ending the game. On the left this is a draw (score=0), and on the right a win for x (score=+1). o wants to minimise so it will choose the left choice - a draw is preferable to a loss. So the left state scores 0 when x looks at it, because x assumes o will do the best they can. The same argument holds for the right choice. So when x is taking its move it will always choose the middle option, because it has the highest score, corresponding to victory.

This pattern repeats. Going right back to the start of the game x will consider every possible game that can be played, all the way to the end. And by assuming that it always takes the best move, and the opposition always takes the best move available to it (worst move for x because it's a zero sum game), it can calculate the score for every state as the minimum or maximum of the next move, depending on whose turn it is. The name of the algorithm, minimax, comes from this repeating pattern of selecting the minimum and maximum score.
