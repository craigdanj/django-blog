# Mellow
A minimalistic, standalone blog built with [Django](https://www.djangoproject.com/).


### Installation:
1. Do a "pip install requirements.txt" from the projects root directory. You could optionally create a virtual environment before doing this.
2. Run the "python manage.py migrate" command to run database migrations. Currently it uses SQLite off the shelf. If you want to use another database you will have to make the appropriate changes to the settings.py file.
3. Deploy following the [deploying django](https://docs.djangoproject.com/en/2.0/howto/deployment/) guide.


### Admin panel:
1. To log into the admin panel you will have to first create a superuser using the "python manage.py createsuperuser" command.
2. After this is done you can navigate to "your-web-domain-here.com/admin" and log in with those credentials.


### To Do:

- [x] Add 'no posts found' message when post count = 0
- [x] Add Published date to post list and post details page
- [x] Conditionally render the read more link
- [x] Add pagination to post list page
- [x] Add posts list to home “/” route.
- [x] Add single post view
- [ ] Create function to fetch categories and tags. DRY code.
- [ ] Set date published to current datetime. Default value.
- [x] Add “post list for category” view
- [x] Add “post list for tag” view
- [x] Customise Django admin to allow filtering posts by taxonomies.
- [x] Admin improvements. Show post count against taxonomy listing pages.
- [ ] Add different types of users with different permissions.
- [ ] Seed above mentioned user data into database.
- [ ] Add a website name field. use in website header, footer, admin header.
- [ ] Add rich-text editor for post description.
- [ ] Document versions of python, django and dependent libraries in readme.
- [ ] Add error handling. Throw 404 if user requests page that does not exist.
- [ ] Add next post previous post on post page?
- [x] Make responsive
- [ ] Add selected style to pagination link
- [ ] Try adding url names
