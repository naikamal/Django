# MyWebsite - Django Practice Project

Welcome to MyWebsite, a Django practice project inspired by Corey Schafer's website with personal modifications. This project aims to enhance my Django skills by replicating and customizing the structure of a real-world website.

## Project Setup

### Environment

Make sure you have Python installed on your system. Create a virtual environment named 'myenv' using the following commands:

```bash
python -m venv myenv
```

Activate the virtual environment:

- On Windows:

  ```bash
  myenv\Scripts\activate
  ```
- On macOS/Linux:

  ```bash
  source myenv/bin/activate
  ```

### Project Initialization

Start a new Django project named 'mywebsite':

```bash
django-admin startproject mywebsite .
```

### App Creation

1. Create a Django app named 'blog':

   ```bash
   python manage.py startapp blog
   ```
2. Create another Django app named 'users':

   ```bash
   python manage.py startapp users
   ```

### Configuration

1. Add 'blog' and 'users' to the `INSTALLED_APPS` in `settings.py`:

   ```python
   INSTALLED_APPS = [
       # ...
       'blog.apps.BlogConfig',
       'users.apps.UsersConfig',
       # later aslo added these apps
         'crispy_forms',
         'crispy_bootstrap5',
   ]
   ```
2. Configure the URLs by adding the blog and users app's URLs to the project's `urls.py`.

   ```python
   from django.contrib import admin
   from django.urls import path,include
   from users import views as users_views

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('',include('blog.urls')),
       path('register/',users_views.register,name="register")
   ]

   ```
## Project Structure

- **mywebsite/**
  - **mywebsite/**
    - `settings.py`: Django project settings.
    - `urls.py`: Main URL configurations.
  - **blog/**
    - `views.py`: Views for the 'blog' app.
    - `urls.py`: URL configurations for the 'blog' app.
    - `templates/`: HTML templates.
    - `static/`: Static files (CSS, JavaScript, etc.).
  - **users**
    - `views.py`: Views for the 'users' app.
    - `urls.py`: URL configurations for the 'users' app.
    - `templates/`: HTML templates(register,login,logout).
    - `static/`: Static files (CSS/styles.css js/code.js, etc.).
### Blog App

#### Database Setup

1. **Create Post Model**: Define a 'Post' model in the 'blog' app's `models.py`.
2. **Register in Admin**: Register the 'Post' model in the Django admin panel.

#### Views and Templates

3. Create views inside the 'blog' app.
```python
from django.shortcuts import render
from .models import Post

def home(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request,'blog/index.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})
```
4. Set up templates: Create 'templates' folder and add base, index, about, and other HTML files.
'Django/blog/templates/blog'.
5. Organize static files: Create 'static' folder, and within it, create 'css' directory for your CSS files.
6. Implement template inheritance for a consistent design across pages.

#### Forms and Styling

1. **Create Post Model**: Define a 'Post' model in the 'blog' app's `models.py`.
2. **Register in Admin**: Register the 'Post' model in the Django admin panel.
3. **Use Default User Model**: Utilize the default Django User model for authentication.
4. **One-to-Many Relationship**: Establish a one-to-many relationship between the User and Post models.
5. **Make Migrations**: Generate migrations for the new models.
6. **Pass Actual Data**: Use Django shell to pass actual data into the database.
7. **Queries**: Practice querying data using Django's ORM.
8. **Remove Dummy Data**: Remove any dummy data initially added.
9. **Create Superuser**: Create a superuser for admin access.

### Users App

1. Configure the 'users' app and add import its views in project's `urls.py`.

2. Write the  views inside the 'users' app, including a register function.
```python
def register(request):
    if request.method== "POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()       
            username=form.cleaned_data.get("username")
            try:
                messages.success(request,f"Account is created for {username} Successfully!")
                return redirect("blog-home")
            except:
                messages.error(request,f"Invalid credential!  *Please Try Again*")
            
    else:
        form=UserRegisterForm()
    return render(request,'users/register.html',{'form':form})
```
3. Add flash messages from views to the template.

#### Forms and Styling

4. Validate the register form inside 'users/templates/users/register.html'.
5. Add CSS styles for styling.
6. Utilize Crispy Forms with Bootstrap 5 for enhanced form rendering.
7. Create a `forms.py` file inside 'users' and inherit it from `UserCreationForm` models, adding an email field.
8. Now, a new user can easily be created from 'register.html'.



## Customizations

1. **Responsive Design**: All design elements are created using pure CSS and HTML. A responsive pseudo-frontend has been implemented, taking inspiration from Corey but avoiding the use of Bootstrap.
2. **Applying Concepts Learned**: Actively applying Django concepts, dummy data is passed from views to templates. Utilizing for loops in templates, the project is a practical implementation of learned concepts.
3. **Future Enhancements**: The project is still in process, with ongoing enhancements, additions, and refinements to make it uniquely mine.

---

**ONGOING......**
