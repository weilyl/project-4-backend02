# Project Overview

## Project

Link to completed project [here](https://goodhooks.herokuapp.com/)

Link to project frontend [here]()

Link to project backend [here](https://github.com/weilyl/project-4-backend02)

## Project Schedule

This schedule will be used to keep track of your progress throughout the week and align with our expectations.

You are **responsible** for scheduling time with your squad to seek approval for each deliverable by the end of the corresponding day, excluding `Saturday` and `Sunday`.

| Day   | Deliverable                                                      | Status     |
| ----- | ---------------------------------------------------------------- | ---------- |
| Day 1 | Project Description                                              | Complete   |
| Day 1 | Wireframes / Priority Matrix / Timeline `backend` and `frontend` | Complete   |
| Day 2 | Backend: Functioning auth, models                                | Complete   |
| Day 3 | Backend: Functioning RESTful API                                 | Complete   |
| Day 4 | Frontend: MVP Vue components & auth methods                      | Complete   |
| Day 5 | Frontend: MVP Vue CRUD methods                                   | Complete   |
| Day 6 | Frontend: Finishing touches                                      | Complete   |

## Project Description

User Model: 
- username
- password
- email
- first name
- last name

List Model
- name
- owner
- description

Link Model
- list
- name
- description
- image URL

## Time/Priority Matrix

[Here]() is a full list of features that have been prioritized based on the `Time and Priority` Matix.

### MVP/PostMVP

#### MVP

- JWT Authentication/Authorization testing
- User model, serializers, views, urls
- Link model, serializers, views, urls
- List model, serializers, views, urls
- Migration
- Deploy and test on Heroku
- Test on Postman/Django Admin

#### PostMVP

- tags per link (public and/or private)
- image scraping from URL for each link
- filter by difficulty (user-assigned), medium (video/text), project type (blanket, scarf, hat, etc.) 

#### Post-Post-MVP
- public reviews (rate: technical difficulty, ease of comprehension, aesthetic)
- contact form to remove copyrighted patterns

## Functional Components

#### MVP

| Component               | Priority | Estimated Time | Time Invested | Actual Time |
| ----------------------- | :------: | :------------: | :------------: | :---------: |
| JWT Auth                |    H     |      3hr       |      10hr      |     1hr     |
| User model              |    H     |      1hr       |      5hr       |     -hr     |
| User serializers        |    M     |      1hr       |      -hr       |     -hr     |
| User views              |    H     |      1hr       |      5hr       |     -hr     |
| User urls               |    M     |      1hr       |      2hr       |     -hr     |
| List Model              |    M     |      2hrs      |      -hr       |     -hr     |
| List serializers        |    M     |      2hr       |      -hr       |     -hr     |
| List views              |    H     |      2hr       |      -hr       |     -hr     |
| List urls               |    M     |      1hr       |      -hr       |     -hr     |
| Link Model              |    M     |      2hrs      |      -hr       |     -hr     |
| Link serializers        |    M     |      2hr       |      -hr       |     -hr     |
| Link views              |    H     |      2hr       |      -hr       |     -hr     |
| Link urls               |    M     |      1hr       |      -hr       |     -hr     |
| Test on Postman         |    L     |      5hr       |      -hr       |     -hr     |
| Deploy                  |    L     |      10hr      |      -hr       |     3hr     |
| Total                   |    H     |    27.5 hrs    |      -hrs      |    7hrs     |

#### PostMVP

| Component                                        | Priority | Estimated Time | Time Invested  | Actual Time |
| ------------------------------------------------ | :------: | :------------: | :------------: | :---------: |
| Tag model, serializers, views, urls              |    M     |      3hr       |      -hr       |     -hr     |
| Review model, serializers, views, urls           |    H     |      2hr       |      2hrs      |     2hrs    |
| Filters                                          |    M     |      5hr       |      -hr       |     -hr     |
| Contact form                                     |    H     |      5hr       |      -hr       |     -hr     |
| Image scraper                                    |    L     |      10hr      |      -hr       |     -hr     |
| Total                                            |    H     |     25hrs      |      2hrs      |    2hrs     |

## Additional Libraries

- Django

## Code Snippet


```

```


## Issues and Resolutions

**ERROR**: 

**RESOLUTION**:

**ERROR**: 

**RESOLUTION**:

`Uncaught (in promise) SyntaxError: Unexpected token < in JSON at position 0`

**ERROR**: When logging in on the frontend, Chrome Inspect Element returns this error:
```
Access to fetch at 'http://127.0.0.1:8000/auth/api/users/login/' from origin 'http://localhost:8080' has been blocked by CORS policy: Response to preflight request doesn't pass access control check: No 'Access-Control-Allow-Origin' header is present on the requested resource. If an opaque response serves your needs, set the request's mode to 'no-cors' to fetch the resource with CORS disabled.
```
**RESOLUTION**: 
1. `pip install django-cors-header`
2. `pip freeze > requirements.txt`
3. settings.py: add `'corsheaders.middleware.CorsMiddleware',` to Middleware
4. Add the following after Middleware:
```
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = ['http://localhost:8080'],
```

**ERROR**: `'links'` property of 'list' model does not show up in Postman.

**RESOLUTION**: Removed "source" from `link_id = LinkSerializer(many=True, required=False, read_only=True)`


**ERROR**: While still working on view to add a public link to a user-specific list: `AttributeError: 'ListLinks' object has no attribute 'save'`

**RESOLUTION**: Using [this](https://stackoverflow.com/questions/35543695/type-object-x-has-no-attribute-objects) as a reference, updated many-to-many serializer:

```
class ListLinks(models.Model):
    list_id = models.ForeignKey(List, on_delete=models.DO_NOTHING, default=None)
    link_id = models.ForeignKey(Link, on_delete=models.DO_NOTHING, default=None)
    objects = models.Manager()
```

and created an object for the data base: `tied = Membership.objects.create(list_id=user_list, link_id=user_link)` that can be saved with `tied.save()`

**ERROR**: When editing get_queryset method to form relation between existing database items:
`AttributeError: 'ManyRelatedManager' object has no attribute 'append'`

**RESOLUTION**: Using & [Django docs](https://docs.djangoproject.com/en/3.1/topics/db/managers/) & [this](https://stackoverflow.com/questions/8095813/attributeerror-manyrelatedmanager-object-has-no-attribute-add-i-do-like-in), a 'through' relationship using the many-to-many model was used.

**ERROR**: When trying to obtain a specific link related to a user-specific list (to confirm whether relationship was successfully created or not) using this query (`            queryset = List.links.through.objects.filter(
` based on this [link from Suresh](https://www.peterbe.com/plog/efficient-m2m-django-rest-framework), received this error:

```
AttributeError: Got AttributeError when attempting to get a value for field `name` on serializer `ListSerializer`.
The serializer field might be named incorrectly and not match any attribute or key on the `List_links` instance.
Original exception text was: 'List_links' object has no attribute 'name'.
```
Conclusion: It could be that Postgres is not properly creating the third table that holds the many-to-many relationship (assuming `List_links` refers to the third table).

**RESOLUTION**: Reconfigured settings.py with SQLite3 rather than local Postgres database in order to visualize schema.


**ERROR**: Changed query methods back to .get() to use dot & bracket notation to access object attributes.

`AssertionError: .accepted_renderer not set on Response`


**RESOLUTION**: Tried [this solution](https://stackoverflow.com/questions/55416471/how-to-resolve-assertionerror-accepted-renderer-not-set-on-response-in-django) adding renderer classes as a class decorator. Got a different error: `AssertionError: The `request` argument must be an instance of `django.http.HttpRequest`, not `apps.api.views.AddLinkToListView`.
`


**ERROR**: `AttributeError: 'dict' object has no attribute 'links'` after successfully returning a single object from a query, even though the "links" attribute is set as a many-to-many field in the List model.

**RESOLUTION**: Tried to print `'id'` instead of `'links'` and also ran into an AttributeError even though every object has an id (and id is clearly visible when the object result of the query is printed).




**ERROR**: `.get` queries were only returning names. 

**RESOLUTION**: Ebony told me `.get` would only return names and I needed to return a queryset. This meant I needed to find a way around the Attribute Error I kept running into whenever my queries returned a QuerySet. Using [this](https://stackoverflow.com/questions/14456503/how-to-get-a-particular-attribute-from-queryset-in-django-in-view), changed `.get` back to `.filter` and added `.values`. 
Additionally, I read these sources ([1](https://docs.djangoproject.com/en/dev/ref/models/querysets/
), [2](https://stackoverflow.com/questions/37205793/django-values-list-vs-values), [3](https://djangobook.com/mdj2-advanced-models/), [4](https://amittbhardwj.wordpress.com/2015/10/26/django-queryset-values/)), and added `.first()` to get the first dictionary out of the queryset list.


**ERROR**: 2020-09-19 After below error fixes, the print statements printed in the terminal for the first time. However, this error was also shown instead of returning the user-specific list:

```
Traceback (most recent call last):
  File "/mnt/c/Users/weily/Documents/seir-6-29/student/unit04/project04/p04backend/p04env/lib/python3.8/site-packages/django/core/handlers/exception.py"
, line 47, in inner
    response = get_response(request)
  File "/mnt/c/Users/weily/Documents/seir-6-29/student/unit04/project04/p04backend/p04env/lib/python3.8/site-packages/django/core/handlers/base.py", lin
e 179, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/mnt/c/Users/weily/Documents/seir-6-29/student/unit04/project04/p04backend/p04env/lib/python3.8/site-packages/django/views/decorators/csrf.py",
line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/mnt/c/Users/weily/Documents/seir-6-29/student/unit04/project04/p04backend/p04env/lib/python3.8/site-packages/django/views/generic/base.py", lin
e 70, in view
    return self.dispatch(request, *args, **kwargs)
  File "/mnt/c/Users/weily/Documents/seir-6-29/student/unit04/project04/p04backend/p04env/lib/python3.8/site-packages/rest_framework/views.py", line 507
, in dispatch
    self.response = self.finalize_response(request, response, *args, **kwargs)
  File "/mnt/c/Users/weily/Documents/seir-6-29/student/unit04/project04/p04backend/p04env/lib/python3.8/site-packages/rest_framework/views.py", line 419
, in finalize_response
    assert isinstance(response, HttpResponseBase), (
AssertionError: Expected a `Response`, `HttpResponse` or `HttpStreamingResponse` to be returned from the view, but received a `<class 'apps.api.models.L
ist'>`
[19/Sep/2020 21:17:49] "GET /auth/api/add-to-list/2/1 HTTP/1.1" 500 79576
```


**RESOLUTION**: Instead of returning the variable for a user-specific list, returned a `Response({})` with a message and status. However, the message indicates that the link was not successfully added to the user-specific list.


**ERROR**: 2020-09-19 `TypeError: get() got an unexpected keyword argument 'list_pk'` when testing new route `http://127.0.0.1:8000/auth/api/lists/2/add/1` to add relation between link and user-specific list (route confirmed using `django-extensions` command: `python manage.py show_urls`. Hat tip to Jendri)

**RESOLUTION**: According to [this](https://stackoverflow.com/questions/30243865/django-get-got-an-unexpected-keyword-argument-pk-error), the error is in my view method arguments. I additionally thought I might need to adjust the regex in my url, so I followed [this](https://simpleisbetterthancomplex.com/references/2016/10/10/url-patterns.html) and changed the URL to `http://127.0.0.1:8000/auth/api/add-to-list/2/1` so that the keyword arguments would be adjacent and hopefully be captured as a dictionary.

**ERROR**: 2020-09-18 ` return serializer_class(*args, **kwargs) 
TypeError: 'tuple' object is not callable` when trying to iterate through a many to many field.

**RESOLUTION**: Tried to use two serializers and interpreter saw it as a tuple. Removed `ListSerializer` as only links were being returned and only LinkSerializer would be needed


**ERROR**: 2020-09-18 `TypeError: 'ManyRelatedManager' object is not iterable` when attempting to resolve ListLinks.get_queryset() to view all links in a list.

**RESOLUTION**: For the code block: 
```
 if self.kwargs.get('list_pk'):
    user_list = List.objects.get(pk=self.kwargs['list_pk'])
    user_links = []
    for link_id in user_list.links:
        user_link_singular = Link.objects.get(pk=link_id)
        user_links.append(user_link_singular)
    return user_links
```
the snippet `user_list.links` was changed to `user_list.links.all()` to return a QuerySet, which is iterable [source](https://stackoverflow.com/questions/45768190/typeerror-manyrelatedmanager-object-is-not-iterable)

**ERROR**: get_queryset method in SingleLinkPerList viewset successfully returns the intended list and link, but they are not related. Potentially need to call `add_link_to_list()` first.

**RESOLUTION**: 


**ERROR**: In editing the get_queryset method for the SingleLinkPerList viewset, one attempt to define the foreign key value for the property links in the list yielded this error:

```
    raise ValueError(
ValueError: The QuerySet value for an exact lookup must be limited to one result using slicing.

```

**RESOLUTION**: Removed the "links=" search parameter from the SQL query for a specific list & changed .get() to .filter() in the same query.


**ERROR**: Attempting Postman GET request on `http://127.0.0.1:8000/auth/api/lists/1/links/1`:

```
raise FieldError("Cannot resolve keyword '%s' into field. "
django.core.exceptions.FieldError: Cannot resolve keyword 'list' into field. Choices are: added, created_at, description, favorited, id, i
mage, is_favorite, is_public, is_saved, name, saved, updated_at

```

**RESOLUTION**: SingleLinkPerList viewset was referencing the property 'list' that had been removed from the models & fields of the Link class.


**ERROR**: API urls not showing up in Django Admin.

**RESOLUTION**: `path('api/', include('apps.api.urls'))` was added to `authentication/urls.py`



**ERROR**: After registering models in admin.py to test API views & routes in Django Admin:

```    raise RuntimeError(
RuntimeError: Model class apps.api.models.Tag doesn't declare an explicit app_label and isn't in an application in INSTALLED_APPS.
```

**RESOLUTION**: Tried to unregister unused (post-MVP) models, but same error occurred. 
Tried to follow [this](https://stackoverflow.com/questions/55553252/runtimeerror-model-class-xxx-doesnt-declare-an-explicit-app-label-and-isnt-in) and use absolute import rather than relative import, but same error occurred.
Tried to be more explicit in settings.py > INSTALLED_APPS by using `'apps.api.apps.APIConfig'` and `'apps.api.apps' instead of `'apps.api'`.
Further down in above link, suggestions are to add class Meta & app_label attribute but the following error occurred:

```
raise ImproperlyConfigured(
django.core.exceptions.ImproperlyConfigured: Cannot import 'api'. Check that 'apps.api.apps.APIConfig.name' is correct.
```

Note: `apps.api` in INSTALLED_APPS did not raise any errors in previous migrations. 
Final Resolution: Returned to using `'apps.api'` in INSTALLED_APPS.

**ERROR**: 2020-09-16 When attempting to make migrations after fixing below errors: 

```
ERROR: 
SystemCheckError: System check identified some issues:

ERRORS:
api.List.owner: (fields.E300) Field defines a relation with model 'authorization.User', which is either not installed, or is abstract.
api.List.owner: (fields.E307) The field api.List.owner was declared with a lazy reference to 'authorization.user', but app 'authorization' isn'
t installed.
```

**RESOLUTION**: Fixed a spelling error - "authorization.user" reference in the API models should have been "authentication.user".


**ERROR**: 2020-09-16 When trying to make migrations after adding new Tag class to models:
```
SystemCheckError: System check identified some issues:

ERRORS:
api.List.owner: (fields.E300) Field defines a relation with model 'authorization.User', which is either not installed, or is abstract.
api.List.owner: (fields.E307) The field api.List.owner was declared with a lazy reference to 'authorization.user', but app 'authorization' isn'
t installed.
authentication.User.favorites: (fields.E304) Reverse accessor for 'User.favorites' clashes with reverse accessor for 'User.saved'.
        HINT: Add or change a related_name argument to the definition for 'User.favorites' or 'User.saved'.
authentication.User.saved: (fields.E304) Reverse accessor for 'User.saved' clashes with reverse accessor for 'User.favorites'.
        HINT: Add or change a related_name argument to the definition for 'User.saved' or 'User.favorites'.
```

**RESOLUTION**: Added `related_name` for favorites & saved items in User model.


**ERROR**: 2020-09-16 When making migration file:

```
File "/mnt/c/Users/weily/Documents/seir-6-29/student/unit04/project04/p04backend/apps/api/models.py", line 22, in Link
    tags = models.ManyToManyField(blank=True)
TypeError: __init__() missing 1 required positional argument: 'to'
```

**RESOLUTION**: Following [this link](https://viblo.asia/p/make-simple-tag-function-with-djangos-manytomany-relationship-model-V3m5WbnblO7), new class Tag was added to models.py so that tags attribute in Link model can refer to a table in the ManyToManyField arguments

**ERROR**: 2020-09-16 11:54am Fixed previous error, still attempting to make migrations files:

```
File "/mnt/c/Users/weily/Documents/seir-6-29/student/unit04/project04/p04backend/authentication/models.py", line 5, in <module>
    from apps.api.models import Link, List
  File "/mnt/c/Users/weily/Documents/seir-6-29/student/unit04/project04/p04backend/apps/api/models.py", line 2, in <module>
    from authentication.models import User
ImportError: cannot import name 'User' from partially initialized module 'authentication.models' (most likely due to a circular import) (/mnt/c
/Users/weily/Documents/seir-6-29/student/unit04/project04/p04backend/authentication/models.py)
```

Attempted resolution: commenting out User model to write one migration file at a time

**RESOLUTION**: Thanks to Ebony for having the same issue before me & Jeremy for helping her resolve it, I removed the User model import into the api models.py and instead used a string of "authentication.user" as the reference in the Links model.

Result of above error (prior to fixing circular import): 

```
  File "/mnt/c/Users/weily/Documents/seir-6-29/student/unit04/project04/p04backend/authentication/models.py", line 9, in <module>
    import apps.api.models
  File "/mnt/c/Users/weily/Documents/seir-6-29/student/unit04/project04/p04backend/apps/api/models.py", line 17, in <module>
    class Link(models.Model):
  File "/mnt/c/Users/weily/Documents/seir-6-29/student/unit04/project04/p04backend/apps/api/models.py", line 18, in Link
    list = models.ForeignKey(List, related_name='lists')
TypeError: __init__() missing 1 required positional argument: 'on_delete'
```

Attempt: Added an `on_delete=DO_NOTHING()` argument

Result: `TypeError: DO_NOTHING() missing 4 required positional arguments: 'collector', 'field', 'sub_objs', and 'using'`

**RESOLUTION**: Removed `()` from `DO_NOTHING`


**ERROR**: 2020-09-16 11:45am Edited User model, then made migrations files: `TypeError: __init__() got an unexpected keyword argument 'Null'`

**RESOLUTION**: Learned that URLField in Django cannot have `blank=True`


**ERROR**: 2020-09-15 12:04pm When deploying to Heroku after authentication successfully tested locally via Postgres:
```
/app/.heroku/python/lib/python3.6/site-packages/environ/environ.py:630: UserWarning: /app/p04backend/.env doesn't exist - if you're not configuring your environment separately, create one.
  "environment separately, create one." % env_file)
Traceback (most recent call last):
  File "manage.py", line 22, in <module>
    main()
  File "manage.py", line 18, in main
    execute_from_command_line(sys.argv)
  File "/app/.heroku/python/lib/python3.6/site-packages/django/core/management/__init__.py", line 401, in execute_from_command_line
    utility.execute()
  File "/app/.heroku/python/lib/python3.6/site-packages/django/core/management/__init__.py", line 395, in execute
    self.fetch_command(subcommand).run_from_argv(self.argv)
  File "/app/.heroku/python/lib/python3.6/site-packages/django/core/management/base.py", line 330, in run_from_argv
    self.execute(*args, **cmd_options)	
  File "/app/.heroku/python/lib/python3.6/site-packages/django/core/management/base.py", line 371, in execute
    output = self.handle(*args, **options)
  File "/app/.heroku/python/lib/python3.6/site-packages/django/core/management/base.py", line 85, in wrapped
    res = handle_func(*args, **kwargs)
  File "/app/.heroku/python/lib/python3.6/site-packages/django/core/management/commands/makemigrations.py", line 101, in handle
    loader.check_consistent_history(connection)
  File "/app/.heroku/python/lib/python3.6/site-packages/django/db/migrations/loader.py", line 306, in check_consistent_history
    connection.alias,
django.db.migrations.exceptions.InconsistentMigrationHistory: Migration admin.0001_initial is applied before its dependency authentication.0001
_initial on database 'default'.
```

**RESOLUTION**: Reset database on heroku side: `sudo heroku pg:reset --app=goodhooks`


**ERROR**: `ModuleNotFound`

**RESOLUTION**: Added authentication directory to `INSTALLED_APPS` list in `settings.py`


**ERROR**: 2020-09-12 to 2020-09-15: Python requirements kept disappearing when configuring interpreter for virtual environment in PyCharm settings.

**RESOLUTION**: PyCharm Pro does not support Python interpreters installed on WSL2 for virtual environments, only globally. A second backend repo was made from scratch, with a virtual environment created and activated in Ubuntu.
