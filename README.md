# Very simple instructions for this app

# Here, client name = demo, schema name = demo and domain = demo.localhost 
# that info are stored in client and domain model
python manage.py create_tenant

schema name: demo
name: demo
domain: demo.localhost

# This cmd create super user in demo schema
(env) [shoumitro@android123 Django_Tenants]$ python manage.py create_tenant_superuser
Enter Tenant Schema ('?' to list schemas): demo
Username (leave blank to use 'shoumitro'): demo
Email address: demo@gmail.com
Password: 1234
Password (again): 1234


python manage.py create_tenant

schema name: demo2
name: demo2
domain: demo2.localhost

# This cmd create super user in demo2 schema
(env) [shoumitro@android123 Django_Tenants]$ python manage.py create_tenant_superuser
Enter Tenant Schema ('?' to list schemas): demo2
Username (leave blank to use 'shoumitro'): demo2
Email address: demo2@gmail.com
Password: 1234
Password (again): 1234



# This cmd create super user in public schema
python manage.py createsuperuser


# If there is no tenant schema, the public schema will show the data
SHOW_PUBLIC_IF_NO_TENANT_FOUND = True


# three url for django tentant
http://www.localhost:7000/admin/ => Here schema = public (default)
http://demo.localhost:7000/admin/ => Here schema = demo
http://demo2.localhost:7000/admin/ => Here schema = demo2

link:
https://www.youtube.com/watch?v=TWF7okf5Xoo&t=1291s
https://django-tenants.readthedocs.io/en/latest/install.html
https://github.com/django-tenants/django-tenants/tree/master/examples/tenant_tutorial