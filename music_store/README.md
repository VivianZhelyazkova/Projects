# Music store simulator


**With this project we are aiming to simulate the operation of a musical instruments store.**

There are various types of musical instruments in the store's catalog:
  - String instruments (violin, viola, double bass, harp, guitar, ...)
  - Percussion instruments (drums, tambourine, frame drum, ...)
  - Wind instruments (trumpet, trombone, tuba, flute, clarinet, ...)
  - Keyboard instruments (organ, piano, accordion, ...)
  - Electronic instruments (synthesizer, bass guitar, electric violin, ...)

Each musical instrument has a name, price, and availability in the store. The store has a cash register with money available.

The following operations can be performed in the store:

1. Selling an instrument (by name and quantity). Selling an instrument increases the money in the store and reduces the quantity of the sold instruments from the available stock. The sale can only be made if there are enough available units of the instrument. If it's not possible to sell the instruments, an appropriate message should be returned to the user.

2. Buying new instruments for sale in the store (name and quantity) if there is enough money in the cash register. The wholesale discount for the seller is 30%.

3. Generating a catalog of instruments in the store:

   - A list of instruments sorted by type.
   - A list of instruments sorted by name in alphabetical order.
   - A list of instruments sorted by price (with the option to choose ascending or descending order).
   - A list of instruments that are currently available in the store.

4. Generating reports on the store's operations:

    - Generating a list of sold instruments, sorted by the number of sales.
    - Generating the total amount received from instrument sales.
    - Providing current information about the best-selling instrument (by quantity compared to others).
    - Providing current information about the least-selling instrument.
    - Providing current information about the type of instruments that are most in demand (with the highest total quantity sold from that type).
    - Providing current information about the type of instruments from which the store has the highest revenue (with the highest total sales amount)."

### ***Ideas for future development and collaboration***

1. Create an "Instrument Supplier":

   - Create "Instrument Supplier" that offers a range of instruments, and for each instrument, it has information about the delivery time to the store.
   
2. Allow Customers to Order Instruments Not in Stock:
   - Enable customers to order instruments if they are not available in the store. In such cases, the store should place orders for the instruments (by name and quantity) with the supplier and provide the customer with information on how long the order will take to arrive.
   
3. Change the Logic for Regular Deliveries:
   - Modify the logic so that the store makes scheduled deliveries for all instruments with zero stock (for example, once a month).

```Python
Author: Vivian Zhelyazkova
```
[GitHub](https://github.com/VivianZhelyazkova)
