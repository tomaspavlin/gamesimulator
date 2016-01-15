# GameSimulator
Program for finding winning strategy in games for two players. You can easily implement rules for some games and use the program for that game. Here it's implemented for game Quarto.

## How to use it
- In *main.py* import game you want to play.
- In *main.py* set conf variable. It is configuration of the game you want to eval winning strategy for.
- Then just run *main.py*
```
./main.py
```

## Examples

Finding winning strategy in Quarto:
```
$ ./main.py
Trying for depth 1...
No winning strategy found

1010	.	.	.	
.	0110	0100	.	
.	1001	0101	.	
0111	1000	0011	1011	
Chosed 1111


Trying for depth 2...
No winning strategy found

1010	.	.	.	
.	0110	0100	.	
.	1001	0101	.	
0111	1000	0011	1011	
Chosed 1110


1010	.	.	.	
.	0110	0100	.	
.	1001	0101	1110	
0111	1000	0011	1011	
Chosed 1111


Trying for depth 3...
Found winning strategy for FIRST player.

1010	.	.	.	
.	0110	0100	0011	
.	1001	0101	.	
0111	1000	.	1011	
Chosed 1110


1010	.	.	.	
.	0110	0100	0011	
.	1001	0101	.	
0111	1000	1110	1011	
Chosed 1111


1010	.	1111	.	
.	0110	0100	0011	
.	1001	0101	.	
0111	1000	1110	1011	
Chosed 0000
```
