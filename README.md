# URL Shortener

##### Description

* Have you ever used a URL shortener like [bit.ly](http://bit.ly) or [jeff-apis](https://jeff-apis.herokuapp.com/urls/)? Check it out and see how it works because we're going to create one ourselves.

##### Objectives

***Set Up Your Django Project***

- Create your virtual environment,
- Start a new Django project with the project name tiny_url_project
- Create an app within your tiny_url_project called url_shortener.
- Make all your necessary `settings.py` changes:
    -   Set up the appropriate URLs in the project and the app
    -   Use Postgres as your DB - [https://djangogirls.gitbooks.io/django-girls-tutorial-extensions/content/optional_postgresql_installation/index.html](https://djangogirls.gitbooks.io/django-girls-tutorial-extensions/content/optional_postgresql_installation/index.html)

***DB and Models***

* Create a model called Url that will have the following fields:
    - `url`: which will hold the physical URL to our webpage.
    - `shortened`: This field can be either an integer or string that will be *unique* for each url. (Don't use the primary key, we don't want to expose that to the user. Be creative!)

***ModelForm and Views***

- Create your `forms.py` in your url app so that we can generate our ModelForm.
- Now, let's create the index view, load the ModelForm, and display it on the template.
    - Check out the [Model Forms Django documentation](https://docs.djangoproject.com/en/1.9/topics/forms/modelforms/), if you need a refresher.
- Create a new POST route for your ModelForm and send the data to it on submit. Set up its view function so that it saves the URl object in your database and redirects back to the root.

***The Shortened Url path***

* We should now be at a point where we have a form that can take in any URL and save it in our database. However, that is only half of the problem! We want to be able to visit a unique route like below:

```
www.my-url-shortener.com/xDzAtCgy // Keep in mind that localhost:8000 will replace the domain here.
```
* From there we will get re-directed to that unique links' corresponding website. How are we going to save this shortened path field if the user is only submitting a URL?
* You have a few options, but the simplest way is to over-write the `save` method as we did last week. Create a instance method in your URL model that generates a shortened url path, and call it in `save`. Take a look at your code from last week where we overwrote `save`.

###### Hint:
-   How are we going to create truly unique identifiers for each URL submitted? If we choose to identify the URL with random integers, what if we exceed the given amount specified or get the same random integer?


***Re-direct route***

* Once you have your URL and it's shortened buddy saving properly to the database, we are going to need to set up a re-direct URL that takes the unique path for a shortened URL and re-directs to the site the user selected.

***Linking it all together***

* After a user creates a shortened url, make it so they are redirected to a "success" page with the new shortened URL displayed as well as the original URL.

***Validations***

* Validate that the input going to into Url is a valid url.
* Check out the Django Docs on [validators](https://docs.djangoproject.com/en/1.9/ref/validators).
* If it is valid, do your redirect. If it isn't valid, render the form again and give the user a message that it didn't work. *

## Bonus:

***Add a hit counter***
- Add a `hits` field to URL and migrate. Write a function that increments the `hit` counter when a shortened URL is visited.
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

#### Part 1 - Validations

####**Validation on the Model**

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
Now you can apply this validator to your models.

First, you need to write a custom `save()` method in your model, and in that `save()` method, you should call `self.full_clean()`. [Checkout what `full_clean()` does here](https://docs.djangoproject.com/en/1.9/ref/models/instances/#django.db.models.Model.full_clean).

Second, you need to write your own `clean()` method. In the `clean()` method, you should call the validatator that you've previously defined.

```
class Post(models.Model):
    title = models.CharField(max_length=40)
    content = models.CharField(max_length=4000)
    slug = models.SlugField(max_length=40)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()
    user = models.ForeignKey(
        User,
        null = True,
        default = None,
        on_delete = models.SET_DEFAULT,
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.updated_at = timezone.now()
        if not self.id:
            self.created_at = timezone.now()
        self.full_clean()
        super(Post, self).save(*args, **kwargs)

    def clean(self):
        min_validation(self.title)
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

...
    def clean(self):
        min_validation(self.title)
...
```
***Research***

* [https://docs.djangoproject.com/en/1.9/ref/validators/](https://docs.djangoproject.com/en/1.9/ref/validators/)
    * Email Validator
    * URL Validator

***Refactor***

Refactor if you think you need to. (You probably do :P). What could you be done more efficiently? Is there anything from Django's built in tools you could use?

####**Validation on the Form**
You can also validate fields on a form, similar to how we validated the model above.

This time, within our `forms.py` file, we'll define out `min_validation` custom validator.

`forms.py`
```
from django.core.exceptions import ValidationError


def min_validation(value):
    if len(value) < 5:
        raise ValidationError("{} is invalid, must have more than 5 characters".format(value))
```

Now, to use the validator to check the fields of the form, we'll setup our `ModelForm` to look like this:

`forms.py`
```
class PostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(MyModelForm, self).__init__(*args, **kwargs)
        self.fields["title"].validators.append(min_validation)

    class Meta:
        model = Post
        fields = [
            "title",
            "content",
        ]
        widgets = {
            "content": Textarea(attrs={"cols": 50, "rows": 10}),
        }
```

I overwrite my forms' `__init__()` method, and I append my `min_validation` validator to the list of validators that exists on the `title` field.

####**Thought Question**

Both of these methods work to validate the input from forms. Which do you think is considered best practice? Why?
