# Documentation for Webshop

Setup found in [Wiki/Hardware_Setup.md](https://github.tik.uni-stuttgart.de/IAS-MiniFactory/Wiki/blob/main/Hardware_Setup.md "Hardware_Setup.md")

* Inside the router network finde the webshop at [minifactory/](minifactory/) or [http://minifactory/](http://minifactory/)
* Select desired product and options and klick "Add to Cart"
* Shopping Cart will be displayed with the buttons Order and Cancel
  * "Order" will add the order to the database and send a mqtt message
  * "Cancel" returns to the order site
* The Reciept site shows all old orders with a "Reorder" button that adds the orders contents to the cart
* By klicking Home or the logo in the top the order site will be displayed

## MQTT messages send by the shop

When ordering a mqtt message will be send to the topic `MiniFactory/Webshop/Data`

Example message `{'name': 'nr39', 'color': 'WHITE', 'with_saw': True, 'with_PM': True}`

* `'name'`: derived from the order number is allways nr plus the number
* `'color'`: color of the product can be `RED, BLUE, WHITE`
* `'with_...'`: Selected options always with true, only the seleced options are send

## Configuration of Webshop

To configer the webshop click on "Admin" on the top right or go to [http://minifactory/admin/](http://minifactory/admin/)

* Username: `admin`
* Password: `admin`

Options in the admin pannel:

* Remove or change orders
* Change availabe Products
  * Display name on the site
  * Color of the Product (will be send by mqtt)
  * Picture of the Product should be same size and format as the current pictures
* Change available Options
  * Display name on the site
  * internal name (will be send by mqtt)
