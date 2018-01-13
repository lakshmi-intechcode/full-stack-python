Text Adventure
===============

For this challenge we'll be programming a videogame called "The Adventure of the Barren Moor".

In "The Adventure of the Barren Moor" the player is in the middle of an infinite grey swamp. This grey swamp has few distinguishing characteristics, other than the fact that it is large and infinite and dreary. 

However, the player DOES have a magic compass that tells the player how far away the next feature of interest is. The player can choose north, south, east or west every move towards the feature.

Here is an example playthrough:

		You awaken to find yourself in a barren moor.  Try "look"

`>look`

		Grey foggy clouds float oppressively close to you, 
		reflected in the murky grey water which reaches up your shins.
		Some black plants barely poke out of the shallow water.

		Try "north","south","east",or "west"

		You notice a small watch-like device in your left hand.  
		It has hands like a watch, but the hands don't seem to tell time. 


		The dial reads '5m'

`>north`

		The dial reads '4.472m'
`>north`

		The dial reads '4.123m'
`>n`

		The dial reads '4m'
`>n`

		The dial reads '4.123m'
`>south`

		The dial reads '4m'
`>e`

		The dial reads '3m'
`>e`

		The dial reads '2m'

`>look`
	
		Grey blackness as far as the eye can see.

`>e`

		The dial reads '1m'
`>e`

		You see a box sitting on the plain.

		The dial reads '0m'

`look` 

		The box is filled with treasure!  You win!  The end.


#### First Iteration

Write the game to play as it does above. The player's starting location should be randomly generated, as well as the point of interest's location.

When the player reaches the point of interest, the game ends.

#### Second Iteration

Create the necessary data for two more points of interest. In addition to the location of the point of interest being randomly generated, the data should be as well. 

When the player reaches the point of interest, another one should be generated and the "magic compass" should guide the player there.