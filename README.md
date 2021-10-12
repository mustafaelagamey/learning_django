# Contents
<details open>
<summary><b>Expand / Hide</b></summary>
<!-- MarkdownTOC -->

* ### [Terminal Commands](#teminal-commands)
* ### [Code](#code)
* ### [Templates](#templates)
* ### [Database](#database)
* ### [Model](#model)
* ### [Admin Area](#admin-area)
* ### [Forms](#forms)

<!-- /MarkdownTOC -->
</details>


### Terminal Commands<a id="teminal-commands"></a>


##### Start new project
`django-admin startproject projectname .`
* . means current directory
* if . not provided it django will create new dir

##### Running the server
`python manage.py runserver`

##### Start New App
`python manage.py startapp appname`

##### Start django interactive shell
`python manage.py shell`



### Code<a id="code"></a>
##### Add function view
1. Views.py , Add function that receive request object and return HttpResponse object
    ```
    def index(request):
        return HttpResponse('Challenges Page')
    ```

2. Add URL 
    ```
   urlpatterns = [path("", views.index)] #app.urls
   
   path('app/', include("app.urls")) #project.urls
   ```
   

##### Add dynamic link
1. Views.py , Add function that receive request object and url parameter and return HttpResponse object
    ```
        def month_challenge(request,month):
            challenge = MONTHS_CHALLENGES.get(month)
            return HttpResponse(challenge)
    ```

2. Add URL 
    ```
       path("<parameter>", views.month_challenge)
   ```
   

    
##### Add Not found response
1. In view function just return 
    ```
        def fn(request):
            return HttpResponseNotFound(challenge)
    ```
   
##### Dynamic link parameter transformation
1. In urls definition just use \<type:parameter> 
    ```
    path("<int:month>", views.month_challenge_by_number),
    path("<str:month>", views.month_challenge),
    ```
   * Note : In django try to transform parameter by order , For this example if system transform month to int if it cannot do that , it moves to second url 
   * If we reversed the order , the system will access str directly even if passing integer

    
##### Add redirect response
1. In view function just return 
    ```
        def fn(request):
            return HttpResponseRedirect("url")
    ```
   
       
##### Add named route
1. In urls pass name to path function and use django.urls.reverse in view
    ```
        path("<str:month>", views.month_challenge, name='month-ch') #app.urls
        reverse('month-ch-by-int',args=[month_number]) # resolve route name in views.py
    ```
       
##### Redirect Shortcut
1. In urls pass redirect in lambda to path function
    ```
        path('', lambda r: redirect("route-name"))
    ```
      
##### Use Templates
1. Use function to get contents 
    1. convert to string
        ```
        render_to_string('template_path_from_any_template_dir')
        ```
   2. using render function from django.shortcuts
        ```
       render(request, 'template_path')
       ```
2. Register the templates directory
    1. using templates dirs 
        ```
       'DIRS': [
            BASE_DIR/"app"/"template_folder"
        ],
       ```
   2. using template detection by registering app to `INSTALLED_APPS` list
   
### Templates<a id="templates"></a>
##### Passing variables to template
1. In view function pass variables as dict to render function
    ```
        render(request, 'template',{'var':'val'})
    ```
2. In the template use the keys of that dict as variable
    ```
        <p>{{var}}</p>
    ```
##### Using templates filters
1. In template use `|` to apply filter
    ```
        {{ var|filter_name }}
    ```

##### Using for tage in templates
1. Inside template use for tag `{% for  in  %}` 
2. At the end of for use `{% endfore %}` tag

    ```
    {% for val in iterable %}
        repeated content
    {% endfor %}
    ```

##### Using route names in templates
1. In template use tag `{% url route-name params %}`
    ```
        <a href="{% url 'route-name' param %}">text</a>
    ```

##### Using if tag in templates
1. Inside template use if tag `{% if  condition  %}` to start if 
2. You can use elif tag `{% elif condition %}` 
3. You can also use else tag `{% else %}` 
4. Finally you should use end if tag to end if statement `{% endif %}` 
    ```
    {% if condition %}
        {{ var }}
    {% else %}
        No Challenges for the selected month
    {% endif %}   
    ```

##### Template Inheritance
1. Create base file
2. Add blocks to base file using block tag `{% block block_name %}` default_val `{% endblock%}` 
3. use extends tag `{% extends template_name %}` 
4. update template block using block tag `{% block %}` content `{% endblock %}` 
5. For productivity add template folder to project templates directories `TEMPLATES` 

##### Template Including
1. Create partial file
2. Include that partial file into template using include tag `{% include 'template-path' %}` 

##### Template Including with variable
1. Inside include tage use with variable="value"
    ```
    {% include 'template_path' with var_name=val %}
    ```
    * Note : No space between var_name and val , Space will raise error in template (needs keyword argument)

##### Template 404
1. Just add to template folder html page with name 404.html
2. Raise Exception HTTP404 to move to the 404 template
    ```
   from django.http import  Http404
    raise Http404
    ```
    * Note : this will work only in production mode during `debug = False`

##### Loading static files
1. In settings.py check `STATIC_URL` 
2. In settings.py check that static app `django.contrib.staticfiles` is registered to `INSTALLED_APPS` 
3. In template use load tag with static `{% load static %}` to use static app in the template
4. In template use static tag to load the requested tag `{% static 'front-end-path-from-static' %}`
* You may need to restart development server

##### Loading general static file
1. In settings.py add main dir to list `STATICFILES_DIRS` 
2. In settings.py check that static app `django.contrib.staticfiles` is registered to `INSTALLED_APPS` 
3. In template use load tag with static `{% load static %}` to use static app in the template
4. In template use static tag to load the requested tag `{% static 'front-end-path-from-static' %}`
* You may need to restart development server

### Database<a id="database"></a>
##### Create Model
1. In app models.py file add model class that inherit from `models.Model` to be table
2. In that class initialize its properties to be the column , each one should be models.FieldType()
    ```
    class Book(models.Model):
        title = models.CharField(max_length=80)
   ```

##### Create Migrations
1. Create the model that describe the database
2. In terminal type the migrations maker command `python manage.py makemigrations `
3. That will create migration file in migrations dir , this file should represent the changes of the database
4. Migrating the database using the command `python manage.py migrate`

##### Create Db record from code
1. Save Method
    1. Create instance from model and pass columns value to its constructor 
        ```
            inst = ModelName(col1 = val , col2 = val)
       ```
    2. Save that instance `inst.save()`
2. Create Method
    1. Use model.create function directly
    columns value to its constructor 
        ```
            inst = ModelName.create(col1 = val , col2 = val)
       ```
##### Fetch Db records from code
1. Use the model manager to fetch all
    ```
        data = ModelName.objects.all()
   ```

##### Change model representation
1. change `__str__` function in the model to represent meaningful string 
    ```
    def __str__(self):
        return f"{self.title} ({self.rating})"   ```

##### Create model validations
*   This validations will work only in UI
1. In the Model Field bass keyward argument `validators` contains list of required validators 
    ```
   from django.core.validators import MinValueValidator , MaxValueValidator
   
    class Book(models.Model):
        rating = models.IntegerField(
            validators=[ MinValueValidator(1), MaxValueValidator(5) ]) 
   ```
2. Make and run migrations 

##### Edit Db record from code
1. Get the instance to delete by any way 
    ```
        inst = ModelName.objects.all()[0]
   ```
2. Edit that instance `inst.column = val`
3. Save that instance `inst.save()`

##### Delete Db record from code
1. Get the instance to delete by any way 
    ```
        inst = ModelName.objects.all()[0]
   ```
2. Save that instance `inst.delete()`

##### Fetch one record from DB
1. Get the object directly using get and passing conditions into it
    ```
        inst = ModelName.objects.get(col = val)
   ```
*   Note : This will raise error in two cases : no records found or more than one record fetched
*   Note : Id and primary key are preferred to be used in this function 

##### Fetch some records from DB
1. Get the list objects directly using filter and passing conditions into it
    ```
        inst_list = ModelName.objects.filter(col1 = val1 , col2 = val2)
   ```
2. Passing db conditions by entering col__operator
    ```
        inst_list = ModelName.objects.filter(col1__lt = val1 , col2__contains = val2)
   ```
3. Implementing DB or conditions
    ```
    from django.db.models import Q
    inst_list = ModelName.objects.filter(Q(col1__lt = val1) | Q(col2__contains = val2) )
   ```
4. Implementing DB or with and conditions
    ```
    from django.db.models import Q
    inst_list = ModelName.objects.filter(Q(col1__lt = val1) | Q(col2__contains = val2) , co3 = val3)
   ```
   * Note : keyword arguments should be in the end or raise Syntax error

* Note : filters can be chained :
 
    `Model.objects.filter().filter().filter()` 

    or 
    ```
    q = Model.objects.filter()
    q2 = q.filter()
   ```

##### Enhance Db search performance using index
1. In the wanted field pass flag `db_index = True`
2. Make and run migrations
* Note : For some reason migrations didn't run for that change only , So It will be better to add index during creating field

##### Using aggregate function count
1. In the model just call the count from the objects manager 

    ```
    count = Model.objects.count()
   ```

##### Using DB aggregate function like average 
1.  Pass model aggregate Object to model aggregate function 

    ```
    from django.db.models import Avg
    avg_col = model.aggregate(Avg("col"))
   ```

##### Using DB order by 
1. chain function order_by with columns as keys having - before colum name for desc

    ```
    model.objects.all().order_by("col1" , "-col2")
   ```
 
##### Create relation between models 
1. One-To-Many : In the many class add field with type `ForeignKey` that takes related model and on_delete action ( models.SET_NULL or models.CASCADE)

    ```
    fkey_col = models.ForeignKey(RelatedModel, on_delete=models.SET_NULL)
   ```
2. One-To-One : In any of models add field with type `OneToOne` that takes the model and on_delete action 

   ```
    fname = models.OneToOneField(RelatedModel, on_delete=models.CASCADE)
   ```
   
3. Many-To-Many : In any of models add field with type `ManyToMany` that takes the related model as argument
 
   ``` 
    fname = models.ManyToManyField(RelatedModel)
   ``` 


### Model<a id="model"></a>
##### Return model record directly
1. In the model class add `get_absolute_url` method to generate url for the record
    ```
    def get_absolute_url(self):
        return reverse("url_name", args=[self.id])
   ```
2. In template use this function as property
    ``` 
    <a href="{{book.get_absolute_url}}"> 
   ``` 
   
##### Adding slug field to model
1. In the model class add  field `slug = models.SlugField(default="", null=False)` method to generate slug field

2. Create and run migrations to apply effects to DB
3. Override save method to update slug filed using django slugify util
    ``` 
    def save(self, *args, **kwargs):
        self.slug = slugify(self.main_field_name)
        return super().save(args, kwargs)
   ``` 
##### Make field None Editable 
1. pass false editable to field

    ```
    field = models.Field(editable=False)
   ```
  

##### Using slug field
1. Update `get_absolute_url` method to generate url correctly
2. Update url parameters for better code
3. Update detail view to use slug

##### Filtering by related model 
1.  pass to filter method the relation column followed by __col=val

    ```
    ManyModel.objects.filter(relation_col__related_model_col=val)
    ```

    * Note : you can follow that and use inner conditions 

    ```
    ManyModel.objects.filter(relation_col__related_model_col__contains=val)
    ```
2. using manymodel set directly from related model

   ```
    related_model_instance.manymodel_set.all()
   ```
   * Note : you can change the the manymodel set in the foreign key Field by passing to it keyword arg `related_name="manymodel_set_alt"`

##### Using Meta to set plural 
1.  In model add class `Meta` and inside class set plural name for that class

   ```
    class ModelName(
    class Meta:
        verbose_name_plural = "new plural name"
   ```


### Admin Area<a id="admin-area"></a>
##### Access Admin area 
1. Access Admin area using '/admin' 

##### Creating super user 
1. in command line  run `python manage.py createsuperuser`

##### Show app in admin area 
1. In app admin.py file register the model to admin site

    ```
    admin.site.register(ModelName)
   ```
 
##### Customize model in admin area 
1. Add new class that inherits from ModelAdmin
2. Passing that class to admin site register fn 

##### make field readonly 
1. In customized model admin pass field names to readonly_fields list or tuple

    ```
    readonly_fields = ("field_name",)
   ```
 
##### make field prepopulated 
1. in the customized model admin pass the field to prepopulated dict 

    ```
    prepopulated_fields = {'filedname' : ("dependancy_tuple",) }
   ```
 
##### make list filter  
1. In customized model add field to filter list 
    ```
    list_filter = ("fieldname",)
   ```
 
##### Add field to list column 
1. In customized model add fields to display to list_display 
    ```
    list_display = ("field1","field2")
   ```
 
### Forms<a id="forms"></a>
##### Using django forms to auto create form
1. Add Form class usually in forms.py

   ```
    from django import forms
    class NewForm(forms.Form):
        field = forms.CharField()
   ```
2. In view create an instance from this form and pass it to template
3. In template use `{{form_name}}` to automatic implement the form inputs inside form element
4. In case of post form you should create csrf_token using `{% csrf_token %}` in the template

 