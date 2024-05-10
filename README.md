Installations required

  - Python
  - Django
  - Django rest Framework

To run the Assignment-> python manage.py runserver

- It will take you to the main page which would show the list of all the entries.
- To see all the entries the link is "http://127.0.0.1:8000/vendors/": need to add '/vendors' at the end of the link.
- To create a new entry for Purchase Orders: '/purchase-orders'
- To create a new entry for Historical Performance: '/historical-performance'
- To get the details of a perticular entry: 'vendors/<int:pk>/'
  -> pk: is the primary key of that entry.
  -> using this link you should be able to perform CRUD.
