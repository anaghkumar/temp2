    queryset = Event.objects.all()
    queryset = Event.objects.filter(years_ago__gt=5)

OR AND Query
    
    filter(Q(<condition_1>)|Q(<condition_2>)
    
    queryset = User.objects.filter(first_name__startswith='R') | User.objects.filter(last_name__startswith='D')

    from django.db.models import Q
    qs = User.objects.filter(Q(first_name__startswith='R')|Q(last_name__startswith='D'))

    filter(Q(<condition_1>) & Q(<condition_2>))

NOT query

    exclude(<condition>)
    queryset = User.objects.exclude(id__lt=5)

    filter(~Q(<condition>))
    from django.db.models import Q
    queryset = User.objects.filter(~Q(id__lt=5))

Union of two querysets from same or different models

    q1 = User.objects.filter(id__gte=5)
    # <QuerySet [<User: Ritesh>, <User: Billy>]>

    q2 = User.objects.filter(id__lte=9)
    # <QuerySet [<User: Ritesh>, <User: Billy>, <User: Anagh>, <User: Rishu>]>
    
    q1.union(q2)
    # <QuerySet [<User: Ritesh>, <User: Billy>, <User: Anagh>, <User: Rishu>]>

We can use values_list to limit the selected fields then do a union.

    Hero.objects.all().values_list(
    "name", "gender"
    ).union(
    Villain.objects.all().values_list(
        "name", "gender"
    ))

How to select some fields only in a queryset?

    queryset = User.objects.filter(
    first_name__startswith='R'
    ).values('first_name', 'last_name')

How to do a subquery expression in Django?

    from django.db.models import Subquery
    users = User.objects.all()
    UserParent.objects.filter(user_id__in=Subquery(users.values('id')))
    <QuerySet [<UserParent: UserParent object (2)>, <UserParent: UserParent object (5)>, <UserParent: UserParent object (8)>]>

Filter a queryset with criteria based on comparing their field values

    - Now you can find the users where first_name==last_name
    
    User.objects.filter(last_name=F("first_name"))

How to filter FileField without any file

- A FileField or ImageField stores the path of the file or image. At the DB level they are same as a CharField

        no_files_objects = MyModel.objects.filter(Q(file='')|Q(file=None))


How to find second largest record using Django ORM

    user = User.objects.order_by('-last_login')[1]  // Second Highest record w.r.t 'last_login'

    user = User.objects.order_by('-last_login')[2] // Third Highest record w.r.t 'last_login'

Find rows which have duplicate field values
You can find duplicate records using the technique below.

    >>> duplicates = User.objects.values(
    'first_name'
    ).annotate(name_count=Count('first_name')).filter(name_count__gt=1)
    >>> duplicates
    <QuerySet [{'first_name': 'John', 'name_count': 3}]>

If you need to fill all the records, you can do

    >>> records = User.objects.filter(first_name__in=[item['first_name'] for item in duplicates])
    >>> print([item.id for item in records])
    [2, 11, 13]


How to find distinct field values from queryset?

You want to find users whose names have not been repeated. You can do this like this

    distinct = User.objects.values(
        'first_name'
    ).annotate(
        name_count=Count('first_name')
    ).filter(name_count=1)
    records = User.objects.filter(first_name__in=[item['first_name'] for item in distinct])
