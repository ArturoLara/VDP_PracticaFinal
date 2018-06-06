# Practica final

Python version: 2.x

Practica para uso de test y desarrollo siguiendo BDD donde en el producto desarrollado se separa por palabras y cuenta cuantas veces aparece en un texto

You can install the dependencies using:

```bash
make bootstrap
```

You can execute unit tests using
```bash
./runUnitTestShell.sh
```
been in the folder tests

And you can execute bdd browser tests using
```
lettuce
```
been in the folder tests, and the server been active

## How it works

As first step you should start Django server, usando
```bash
python manage.py runserver 0.0.0.0:8000
```
been in the virtualenv

then you can access to web page with two text field and 2 buttons.

In order to use the application:

* 1º You have to put your url on url-text box.
* 2º Press "execute" button for request to server.
* 3º You will see the words in the url and the number of that word apeared above the forms.

* 1º You have to put your date on date-text box.
* 2º Press "seeDate" button for request to server.
* 3º You will see the words and the number of that word apeared in urls that day above the forms.
