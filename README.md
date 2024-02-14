# MyWebsite - Django Practice Project

Welcome to MyWebsite, a Django practice project inspired by Corey Schafer's website with personal modifications. This project aims to enhance My Django skills by replicating and customizing the structure of a real-world website.

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

Create a Django app named 'blog':

```bash
python manage.py startapp blog
```

### Configuration

1. Add 'blog' to the `INSTALLED_APPS` in `settings.py`:

   ```python
   INSTALLED_APPS = [
       # ...
       'blog.apps.BlogConfig',
   ]
   ```
2. Configure the URLs by adding the blog app's URLs to the project's `urls.py`.
3. Create views inside the 'blog' app.
4. Set up templates: Create 'templates' folder and add base, index, about, and other HTML files.
5. Organize static files: Create 'static' folder, and within it, create 'css' directory for your CSS files.
6. Implement template inheritance for a consistent design across pages.

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

## Customizations

1. **Responsive Navbar**: Implemented a custom responsive navbar using pure CSS for a personalized touch.
2. **Applying Concepts Learned**: Since I've learned various Django concepts, I'm actively applying and implementing them in this project. The goal is not to be a copycat but to showcase my understanding and creativity.
3. **Future Enhancements**: Add more features, pages, and improvements to make the project uniquely yours.

   ****************************

    ONGOING......
