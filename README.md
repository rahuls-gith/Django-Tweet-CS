# Django-Tweet-CS

* Each project can have multiple apps (applications) which are separate from each other. These apps are reusable (they can be added to other projects instead of re-creating them)

* When we provide a route in the browser URL, Django checks in the Project's `urls.py` file for the presence of that route in the `urlpatterns` list. If it finds it, then it takes the corresponding action as mentioned by the second parameter. Since we have `include("blog.urls")` as the second argument, Django navigates the the Blog app's `urls.py` file and checks for the presence of the remainder of the route in the `urlpatterns` list (`blog/` will already match the route present in Project's `urls.py` file, so that part will get eliminated, and only the rest of the route will be passed on to the app's `urls.py` file). If a route is found, then the corresponding view (passed in as the second argument in the url mapping) will be executed

* Steps involved in creating routes:
- Create the logic in the `views.py` file (this is called a view and hence the filename is `views`)
- Create a mapping for this view (in the app's `views.py` file) to a path (in the app's `urls.py` file) so as to access this view from that particular path
- Add a final mapping to route the user from a particular path to a particular app (in the project's `urls.py` file). The app's `urls.py` file will handle the mapping for this particular app

* Always leave the trailing forward slash in any route as Django simply ignores the forward slash regardless of its presence. So it is better for the user as they can provide a forward slash or not, and still get the same result

* 