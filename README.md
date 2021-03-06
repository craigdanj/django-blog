# mellow
A minimalistic, standalone blog built with [Django](https://www.djangoproject.com/).


### Installation:
1. Do a "pip install requirements.txt" from the projects root directory. You could optionally create a virtual environment before doing this.
2. Run the "python manage.py migrate" command to run database migrations. Currently it uses SQLite off the shelf. If you want to use another database you will have to make the appropriate changes to the settings.py file.
3. Deploy following the [deploying django](https://docs.djangoproject.com/en/2.0/howto/deployment/) guide.


### The admin panel:
1. To log into the admin panel, first create a superuser using the "python manage.py createsuperuser" command.
2. After you've done this navigate to "your-web-domain-here.com/admin" and log in with those credentials.


#### To Do:

- [ ] Set date published to current datetime. Default value.
- [ ] Create function to fetch categories and tags. DRY code.
- [ ] Add different types of users with different permissions.
- [ ] Seed above mentioned user data into database.
- [ ] Add a website name field. use in website header, footer, admin header.
- [ ] Add rich-text editor for post description.
- [ ] Document versions of python, django and dependent libraries in readme.
- [ ] Add error handling. Throw 404 if user requests page that does not exist.
- [ ] Add next post previous post on post page?
- [ ] Add selected style to pagination link
- [ ] Try adding url names
