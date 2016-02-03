# IRONING OUT YOUR CODE

### Learning Objectives
***Students will be able to...***

* Debug Django with ease (kind of)
* Use custom validations 

---
### Context

* Continuing to become Full Stack Developers

---
### Lesson

##### Part 1 - Validations

* Django comes with a built in class called `ValidationError` inside the `django.core.exceptions`
* We can import this into our models to use their built in validations.
* We can also utilize this library to build our own custom validations.
* Open a model file, I'll be using a Post model, and add this to it.

```
from django.core.exceptions import ValidationError

def min_validation(value):
	if len(value) < 5:
		raise ValidationError("{} is invalid, must have more than 5 characters". format(value))
```
* Now you can apply this validator to your models by targeting the validation property

```
from django.core.exceptions import ValidationError

class Post(models.Model):
	brand = models.CharField(max_length = 50, validators=[min_validation])
``` 
* Now run your server 
* Go to the form
* Enter less than five characters
* If you click submit your request will not go through
* Instead you will see the validation message come up on the screen next to the input box
* If you had multiple custom validators you could make your own `validators.py` file. Use the first code again but put it in a new file.

```
from django.core.exceptions import ValidationError

def min_validation(value):
	if len(value) < 5:
		raise ValidationError("{} is invalid, must have more than 5 characters". format(value))
```
* Now in the models file delete that code (b/c you have a new file) and import that file

```
from django.core.exceptions import ValidationError
from .validators import *

class Post(models.Model):
	brand = models.CharField(max_length = 50, validators=[min_validation])
```

***Research***

* [https://docs.djangoproject.com/en/1.9/ref/validators/](https://docs.djangoproject.com/en/1.9/ref/validators/)
	* Email Validator
	* URL Validator



