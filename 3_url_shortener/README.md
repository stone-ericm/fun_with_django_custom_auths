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

***Refactor***

Refactor if you think you need to. (You probably do :P). What could you be done more efficiently? Is there anything from Django's built in tools you could use?
