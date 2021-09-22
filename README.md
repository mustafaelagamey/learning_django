# Contents
<details open>
<summary><b>Expand / Hide</b></summary>
<!-- MarkdownTOC -->

* ### [Terminal Commands](#teminal-commands)
* ### [Code](#code)
* ### [Templates](#templates)

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
