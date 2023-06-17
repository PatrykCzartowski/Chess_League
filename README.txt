## Simple Chess league website crated with Django framework.

# About the project:
This project is a result of my learning the Django framework. The project contains a four main pages:
	*Landing page - page that contains a two tables with record from two models "Players" and "Games".
	*Log in page - custom page that is used for authentication for Django admin.
	*Admin panel - page that u can use CRUD operations on models and view more info about the records in database.


# Database:
This project is using a postgres database. To set it up u need to download a postgres on your machine and create a User
"ladmin" with superuser privileges and create database "chess_league" and migrate a data.json file to it.


# Models:
In this project im using only two database models:
	*Players - model that contains a basic info about a player like name, surname and ranking.
	 player have also a "last update" object that just gets the current date.
	*Games - model that contains a info about played game like players names , score and a "last update" objact just like Players model.

