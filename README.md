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
