# Contents
<details open>
<summary><b>Expand / Hide</b></summary>
<!-- MarkdownTOC -->

* ### [Terminal Commands](#teminal-commands)
* ### [Code](#code)
* ### [Templates](#templates)
* ### [Database](#database)

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
