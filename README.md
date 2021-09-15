# Contents
<details open>
<summary><b>Expand / Hide</b></summary>
<!-- MarkdownTOC -->

* ### [Terminal Commands](#teminal-commands)
* ### [Code](#code)

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
   

    
    
