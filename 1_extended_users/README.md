# Build Custom Validations

##### Description

* Continue to work on class based views
* We will also be adding custom validations

##### Objectives

* If you have not done so refactor your Users App to have [Class Based Views](https://docs.djangoproject.com/en/1.9/topics/class-based-views/intro/)
* Take your GET and POST routes and combine them
* Now add some [custom validation](https://docs.djangoproject.com/en/1.8/ref/validators/) to the Users Model
* Passwords should be greater than 7 letters
* Username needs to be unique. 
	* How can we force this constraint on the database level
* POST routes should utilize the `form.is_valid()` method
* They should also redirect, not render. 
	* Both of these are django shortcuts
