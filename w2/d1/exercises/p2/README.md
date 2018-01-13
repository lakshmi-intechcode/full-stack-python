Nested Arrays
=============

### Dynamically create a game board

Dynamically create a sort of game board that appears like so:

	[28, 47, 39, 36]  
	[3, 41, 46, 1]  
	[34, 10, 20, 2]  
	[19, 9, 26, 10]  

Hold this game board inside a GameBoard class. Create board and values inside on instantiation of a GameBoard class object. Use random for the values inside.

### First Method - Print Board
Create an instance method that prints the whole board, similarly to how it is presented above.

### More Methods

Create four more instance methods- getRow(), getCol(), getCoords() and getSurround()

getRow should take a row numbers (starting at the top from 0) and return the row. For the example above:

		board.getRow(1) >>> 3,41,46,1  

getCol should take a col number (starting at the left from 0) and should return the column. For the example above:

		board.getCol(2) >>> 39, 46, 20, 26

getCoords should take a number on the board, and check for its existence. If it does exist, it should return the row and column.

		board.getCoords(9) >>> (3, 1)  
		board.getCoords(10) >>> (2, 1) #returns the first one it finds
		board.getCoords(99) >>> False

getSurround should take the row and column coordinates and return all surrounding values, or more specifically, values of all the coordinates that touch the input coordinates.

		board.getSurround(1,1) >>> 28, 37, 39, 46, 20, 10, 34, 3
		board.getSurround(0,3) >>> 1, 46, 39

