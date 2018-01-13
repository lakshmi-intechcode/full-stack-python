Warehouse Database
==================

We're going to model a warehouse database. Imagine one of Amazon's warehouses, or any warehouse that will help you think about this problem.

Specifically, we're going to model their inventory and sales system.

Warehouses have a lot of things stored around the warehouse. When an order comes, they will know where things are in the warehouse by looking up where the item with that SKU is stored. Then they will put together an order and ship it to the customer.

Below is the start of a very simple schema. You're being given some necessary tables and some columns. Feel free to build this in whatever way you think will be the best inventory management system possible.

You can model this any way you like, but know this... You will be asked to justify every decision you make in your database.

If you can't give a good reason for why you did something, I will cry. Don't make me cry.  

We will all be sharing what we come up with later today.

1. Parts
  * SKU
  * Description
  * Picture
2. Stock (Inventory)
  * SKU
  * Quantity
  * Reorder quantity (low water mark)
  * Bin Location
3. Users
  * Name
  * email
  * password
4. Orders