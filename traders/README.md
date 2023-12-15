## This program is a class structure representing the work of traders in Sofia.

Each trader has the following characteristics:

- Name
- Registration address
- Capital – initial amount to start the business.
- Commercial object(s) where they operate (one or several)
- Supplier(s) from whom they load goods (one or several)

The commercial objects have the following characteristics:

- Address
- Working hours
- Area
- Tax to the state.

Suppliers have the following characteristics:

- Name
- Address
- Working hours

Suppliers can be retail or wholesale. Wholesale suppliers have a 15 percent discount on the price of all goods.

Commercial objects can be:

1. Market stall – area between 2 and 10 square meters. Annual tax to the state of 50 leva.
2. Mall shop – area between 10 and 100 square meters. Annual tax to the state of 150 leva.
3. Push cart – area between 4 and 6 square meters. Annual tax to the state of 50 leva.

Various types of traders operate in Sofia:

- Travelling vendor – does not operate in a specific commercial object and works with one retail supplier.
- Sole trader – operates only with retail suppliers (no more than 5) and owns one commercial object. Sole traders may own a street kiosk or a street stall.
- Commercial chain – works with many retail and wholesale suppliers (no more than 15) and has many commercial objects (no more than 10). It owns both kiosks and shops in malls.

Each trader can perform the following actions:

- Place an order of a certain value to a supplier. The order cannot exceed 50% of the trader's capital. If the supplier offers a discount, the price difference is returned to the trader. When ordering goods from a supplier, the trader receives a list of a randomly generated number of products, each with a name and a random price between 5 and 15 leva. The total price of the products represents the value of the delivery.
- Collect turnover from the commercial object – 130% of the value of the ordered goods. (In fact, traders have a 30% markup). The turnover represents the profit from a random number of sold items.
- Pay taxes to the state for the respective commercial object.

## To implement a demo that: 

 1. Creates 10 suppliers randomly - both retail and wholesale.
  
2. Creates 20 commercial objects randomly - stalls, shops, and booths.

3. Creates one itinerant trader with a capital of 100 leva, one sole proprietorship (ET) with a capital of 500 leva, and one retail chain with a capital of 3000 leva.

4. Assigns corresponding commercial objects to the traders randomly.

5. Invokes a method that takes a list of created traders, initiating commercial activities for each trader. Commercial activities include:
placing orders for goods from suppliers for each commercial object. The list of goods should be displayed on the screen, sorted by price in ascending order.
collecting turnover from each commercial object - the total profit amount should be displayed on the screen. After a sale, the list of remaining goods in the store should be sorted by price again.
paying monthly tax to the state for each commercial object.

6. Displays the current monetary balance for each object after conducting commercial activities.

7. Outputs the trader with the highest number of sold goods for the month.

8. Outputs the trader with the highest amount of tax paid to the state.