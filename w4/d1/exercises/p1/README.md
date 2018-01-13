## Coffee Maker

You will be designing a software implementation of a simple coffee maker. The following hardware needs to be monitored. Write the methods for:

* The heating element for the boiler. It can be turned on or off.
* The heating element for the warmer plate. It can be turned on or off.
* The sensor for the warmer plate. It has three states: warmerEmpty, potEmpty, potNotEmpty.
* A sensor for the boiler, which determines whether there is water present. It has two states: boilerEmpty or boilerNotEmpty.
* The Brew button. This is a momentary button that starts the brewing cycle. It has an indicator that lights up when the brewing cycle is over and the coffee is ready.
* A pressure-relief valve that opens to reduce the pressure in the boiler. The drop in pressure stops the flow of water to the filter. It can be opened or closed.

You should do this OO. Think about the flow of information and the flow of state. Your methods should not have to worry about each other's implementations, just their interface. Take your time to make sure everything is interacting with each other as they should. This is an exercise in design, not code. If you design well, the coding will be easy.