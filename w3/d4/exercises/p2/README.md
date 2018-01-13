## Terminal Trader

Now it's time to make our stock trader game - remember, greed is good.

First, import the wrapper you wrote around the Markit API. We're going to need that functionality.

Our game is going to give users a starting amount of money - maybe $100,000? and let them buy and sell stocks based on the current market info we get from the Markit API. It should update their earnings whenever they login. There should be an admin who can log in and get an up to date leaderboard.

#### Step 1: Database
Design your schema. We're definitely going to need a users table. What else?

#### Step 2: Implement Functionality
To play our game, our users want to be able to search companies and get the exact stock ticker symbol we want. Our users also want to retreive the market data for a stock before they purchase it - we should obviously show them today's price, but we have alot more information at our disposal that will help the player make an informed decision. Start with just an interface that lets the users access and see this data.

#### Step 3: Game Logic
Now make it so users have the option to "buy" and "sell" stocks. Buying should subtract from their funds and not let them buy more than they can afford, selling should return money to their cash funds and not let them sell more than they have. Of course, users will need to buy and sell at the current rate.

#### Step 4: More Game Logic
Create a user dashboard that lets the users view their portfolio, the amount they have earned or lost, the amount of liquid cash they have available, etc. Make sure they are never looking at stale data. Think of some cool extras - maybe how their portfolio compares to the market average for the year?

#### Step 5: Leaderboard
Create a superuser who can see a leaderboard that displays the top 10 users by portfolio earnings. Copy their strategy. Make millions!