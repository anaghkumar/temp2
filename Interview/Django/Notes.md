`What is Django? And why is it used?`
- Django is a high-level Python web framework that enables the rapid development of secure and maintainable websites.
- Open Source
- fast and flexible.

`New Features of Django`
- Supports asynchronous views and middleware
- Provides JSON field support for all database backends

`What is serializer.`

    Serializers in Django REST Framework are responsible for converting objects into data types understandable by javascript and front-end frameworks. Serializers also provide deserialization, allowing parsed data to be converted back into complex types, after first validating the incoming data. 

    Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON, XML or other content types. Serializers also provide deserialization, allowing parsed data to be converted back into complex types, after first validating the incoming data. Let’s start creating a serializer, in file apis/serializers.py,

`APIVIEW`

    APIView class is a base for all the views that you might choose to use in your DRF application.

    Whether it be-
    - function-based views
    - class-based views
    - mixins
    - generic view classes
    - viewsets


`Django follows a Model-View-Template (MVT) architecture. It contains three different parts:`

    Model: Logical data structure behind the entire app and signified by a database.
    View: It's a user interface. What you see when you visit a website is called a user interface. Represented by HTML/CSS/Javascript files.
    Template: Deals with the presentation of data.

` Explain the caching strategies in the Django?`

- Memcached : A memory-based cache server is the fastest and most efficient
- FileSystem Caching : Values of the cache are stored as separate files in a serialized order
- Local-memory Caching : This is used as the default cache strategy by Django if you haven’t set anything. It is per-process as well as thread-safe.
- Database Caching : Cache data will be stored in the database and works very well if you have a fast and well-indexed DB server.

`What are different model inheritance styles in the Django?
`
- Abstract Base Class Inheritance: Used when you only need the parent class to hold information that you don’t want to write for each child model.
- Multi-Table Model Inheritance:  Used when you are subclassing an existing model and need each model to have its own table in the database.
- Proxy Model Inheritance:  Used when you want to retain the model's field while altering the python level functioning of the model.

`What is mixin?`

- Mixin is a type of multiple inheritances wherein you can combine behaviors and attributes of more than one parent class. It provides us with an excellent way to reuse code from multiple classes. One drawback of using these mixins is that it becomes difficult to analyze what a class is doing and which methods to override in case of its code being too scattered between multiple classes.

`Explain Q objects in Django ORM?`

- Q objects are used to write complex queries, as in filter() functions just `AND` the conditions while if you want to `OR` the conditions you can use Q objects. Let’s see an example:

    ```from django.db import models
    from django.db.models import Q
    >> objects = Models.objects.get(
    Q(tag__startswith='Human'),
    Q(category=’Eyes’) | Q(category=’Nose’)
    )```
    ```Query Executed
    SELECT * FROM Model WHERE tag LIKE ‘Human%’ AND (category=’Eyes’ OR category=’Nose’)
    ```

`Middleware`

- Middleware is a framework of hooks into Django’s request/response processing. It’s a light, low-level “plugin” system for globally altering Django’s input or output.

```
def simple_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware
```

```
class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
```

<!-- https://docs.djangoproject.com/en/4.1/topics/http/middleware/#:~:text=Middleware%20is%20a%20framework%20of,for%20doing%20some%20specific%20function. -->

`Mixin`
- A mixin is a class that provides methods to other classes, but it’s not considered a base class itself.

-  In object-oriented programming languages, a mixin is a class which contains a combination of methods from other classes.

- Mixin is a type of multiple inheritance wherein you can combine behaviors and attributes of more than one parent class. Mixins provide an excellent way to reuse code from multiple classes. For example, generic class-based views consist of a mixin called TemplateResponseMixin whose purpose is to define render_to_response() method. When this is combined with a class present in the View, the result will be a TemplateView class.

- One drawback of using these mixins is that it becomes difficult to analyze what a child class is doing and which methods to override in case of its code being too scattered between multiple classes.

<!-- https://www.hackerearth.com/practice/notes/sachin/some-useful-mixins-in-django/#:~:text=In%20object%2Doriented%20programming%20languages,implemented%20as%20early%20as%20possible. -->


`Difference between writing sql in ORM or raw sql in django`

- It is much easier to introduce security vulnerabilities when writing raw SQL. By using ORM exclusively you are guaranteed to be safe from SQL injections. However, as soon as you start to use unsafe raw and extra methods you increase the chance of introducing SQL injection vulnerabilities into your app.

```
Person.objects.raw('SELECT id, first_name, last_name, birth_date FROM myapp_person')
```

- Class-based views are the alternatives of function-based views. It is implemented in the projects as Python objects instead of functions. Class-based views don’t replace function-based views, but they do have certain advantages over function-based views. Class-based views take care of basic functionalities such as deleting an item or add an item. 

- Using the class-based view is not easy if you’re a beginner. You will have to go through the documentation, and you will have to study it properly. Once you understand the function-based view in Django and your concepts are clear, you can move to the class-based views. Let’s discuss the class-based views in detail.

`Pros`
- The most significant advantage of the class-based view is inheritance.  In the class-based view, you can inherit another class, and it can be modified for the different use cases.
- It helps you in following the DRY principle. You won’t have to write the same code over and over in your boilerplate. Code reusability is possible in class-based views.
- You can extend class-based views, and you can add more functionalities using Mixins.
- Another advantage of using a class-based view is code structuring. In class-based views, you can use different class instance methods (instead of conditional branching statements inside function-based views) to generate different HTTP requests.
- Built-in generic class-based views.

`Cons`
- Complex to implement and harder to read
- Implicit code flow.
- Extra import or method override required in view decorators.

```

class MyCreateView(View):
  template_name = 'form.html'
  form_class = MyForm
  
  def get(self, request, *args, **kwargs):
    form = self.form_class
    return render(request, template_name, {'form': form})
  
  def post(self, request, *args, **kwargs):
    form = self.form_class(request.POST)
    if form.is_valid():
      form.save()
      return HttpResonseRedirect(reverse('list-view'))
    else:
      return render(request, self.template_name, {'form': form})
```

```
urlpatterns = [
    url(r'^new/$', MyCreateView.as_view(), name='original-create-view')
    url(r'^new_two/$', MyCreateView.as_view(template_name='other_form.html',
                    form_class='MyOtherForm'), name='modified-create-view')
  ]
```


`What are viewsets in DRF?`

- A viewset is a way to combine the logic for multiple related views into a single class. In other words, one viewset can replace multiple views. It is a class that is simply a type of class-based View, that does not provide any method handlers such as .get() or .post(), and instead provides actions such as .list() and .create().

`What are routers in DRF?`

Routers work directly with viewsets to automatically generate URL patterns for us. Django REST Framework has two default routers: SimpleRouter and DefaultRouter.

    SimpleRouter - This router includes routes for the standard set of list, create, retrieve, update, partial_update and destroy actions.
    Default Router - This router is similar to SimpleRouter, but additionally includes a default API root view, that returns a response containing hyperlinks to all the list views. It also generates routes for optional .json style format suffixes.

`What is the difference between APIViews and Viewsets in DRF?
`

DRF has two main systems for handling views:

    APIView: This provides methods handler for http verbs: get, post, put, patch, and delete.
    ViewSet: This is an abstraction over APIView, which provides actions as methods:
        list: read only, returns multiple resources (http verb: get). Returns a list of dicts.
        retrieve: read only, single resource (http verb: get, but will expect an id in the url). Returns a single dict.
        create: creates a new resource (http verb: post)
        update/partial_update: edits a resource (http verbs: put/patch)
        destroy: removes a resource (http verb: delete)

`What is the difference between GenericAPIView and GenericViewset?
`

    GenericAPIView: for APIView, this gives you shortcuts that map closely to your database models. Adds commonly required behavior for standard list and detail views. Gives you some attributes like, the serializer_class, also gives pagination_class, filter_backend, etc

    GenericViewSet: There are many GenericViewSet, the most common being ModelViewSet. They inherit from GenericAPIView and have a full implementation of all of the actions: list, retrieve, destroy, updated, etc.


`What are status codes?`

    HTTP response status codes indicate whether a specific HTTP request has been successfully completed. Responses are grouped in five classes:

    1xx: Informational – Communicates transfer protocol-level information.
    2xx: Success – Indicates that the client’s request was accepted successfully.
    3xx: Redirection – Indicates that the client must take some additional action in order to complete their request.
    4xx: Client Error – This category of error status codes points the finger at clients.
    5xx: Server Error – The server takes responsibility for these error status codes.

<!-- https://github.com/PragatiVerma18/DRF-Interview-Prep -->

`Viewsets`
- After routing has determined which controller to use for a request, your controller is responsible for making sense of the request and producing the appropriate output

- The method handlers for a ViewSet are only bound to the corresponding actions at the point of finalizing the view, using the .as_view() method.

        class UserViewSet(viewsets.ViewSet):
            def list(self,request):
                queryset = User.objects.all()
                serializer = UserSerializer(queryset, many=True)
                return Response(serializer.data)


            def retrieve(self,request,pk=None):
                queryset = User.objects.all()
                user = get_object_or_404(queryset,pk=pk)
                serializer = UserSerializer(user)
                return Response(serializer.data)

            def create(self,request):
                pass
            
            def update(self,request,pk=None):
                pass
            
            def partial_update(self,request,pk=None):
                pass

            def destroy(self,request,pk=None):
                pass
            

CSRF

    Cross-Site Request Forgery (CSRF) is an attack that forces an end user to execute unwanted actions on a web application in which they’re currently authenticated. With a little help of social engineering (such as sending a link via email or chat), an attacker may trick the users of a web application into executing actions of the attacker’s choosing. If the victim is a normal user, a successful CSRF attack can force the user to perform state changing requests like transferring funds, changing their email address, and so forth. If the victim is an administrative account, CSRF can compromise the entire web application.


Signals

    Django consists of a signal dispatcher that helps allow decoupled applications to get notified when actions occur elsewhere in the framework. Django provides a set of built-in signals that basically allow senders to notify a set of receivers when some action is executed. Some of the signals are as follows: