
Krishikhoj App - A Django app for registration of Farmers and Tractors details of the The Fatmers

This is a Django App in aDjango Project in same name.
At First, A Welcome page are shown in the first page anwith along a button "Go To App".
If you click this button, You arived the app which contain a simple forms. The respective form is created by django model forms, django crispy forms and the forms api of Django.
If you fills all field of the forms correctly and click "Submit" button, The you arrived list page. In the list page, farmer's details are present in a tabular form in serialwise .when you fill the form,fill up all fields are mandetory.

All fields of The forms are created by django model. For receive the data of the forms, we create a post request in the "forms.py" on the submit.
Inb the list page, A "Add New" button are avialable to redirect the page on the forms page for fill up or add new records. In the forms, options of tractors atr also avilable to choose any notions of the tractor.
all propulated data are came from "postgresql" database, it is hosted on localhost. You also check all data in "/admin" router.


N.B: Updatetion and Deletation features are not available in this app for some reasone.

if you run the app in code editor:

Try this command:

cd krishikhoj

python manage.py runserver
