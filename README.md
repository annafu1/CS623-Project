# CS623-Project

Product, Depot and Stock relations/ tables are stored using PostgreSQL. 
T
he following image shows the data that is stored in the tables.

<img width="241" alt="image" src="https://github.com/annafu1/CS623-Project/assets/104175541/6dac76bb-45f4-4052-b8f9-da9fa391bc03">

A few things to notes:
- The key of product is #prod (prodid).
- The key of depot is #dep (depid).
- The key of stock is #prod, #dep. #prod and #dep are foreign keys.

In this project, I am using Python to write a code for a transaction to be implemented: The product p1 changes its name to pp1 in Product and Stock.
