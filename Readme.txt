pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
python manage.py createsuperuser

pyinstaller app.spec --log-level=DEBUG


Manually Deleting 
python manage.py shell
and then 

from transactions.models import SaleBill, SaleItem, SaleBillDetails

# Delete related SaleItems
SaleItem.objects.filter(billno_id=31).delete()

# Delete related SaleBillDetails
SaleBillDetails.objects.filter(billno_id=31).delete()

# Delete the SaleBill
SaleBill.objects.filter(billno=31).delete()

print("Bill 31 and related items deleted.")


Permissions 
  ...: # List all permissions
   ...: for perm in Permission.objects.all():
   ...:     print(f"{perm.id}: {perm.codename} - {perm.name}")
   ...:
1: add_logentry - Can add log entry
2: change_logentry - Can change log entry
3: delete_logentry - Can delete log entry
4: view_logentry - Can view log entry
9: add_group - Can add group
10: change_group - Can change group
11: delete_group - Can delete group
12: view_group - Can view group
5: add_permission - Can add permission
6: change_permission - Can change permission
7: delete_permission - Can delete permission
8: view_permission - Can view permission
13: add_user - Can add user
14: change_user - Can change user
15: delete_user - Can delete user
16: view_user - Can view user
17: add_contenttype - Can add content type
18: change_contenttype - Can change content type
19: delete_contenttype - Can delete content type
20: view_contenttype - Can view content type
25: add_stock - Can add stock
26: change_stock - Can change stock
27: delete_stock - Can delete stock
28: view_stock - Can view stock
21: add_session - Can add session
22: change_session - Can change session
23: delete_session - Can delete session
24: view_session - Can view session
29: add_purchasebill - Can add purchase bill
30: change_purchasebill - Can change purchase bill
31: delete_purchasebill - Can delete purchase bill
32: view_purchasebill - Can view purchase bill
53: add_purchasebilldetails - Can add purchase bill details
54: change_purchasebilldetails - Can change purchase bill details
55: delete_purchasebilldetails - Can delete purchase bill details
56: view_purchasebilldetails - Can view purchase bill details
49: add_purchaseitem - Can add purchase item
50: change_purchaseitem - Can change purchase item
51: delete_purchaseitem - Can delete purchase item
52: view_purchaseitem - Can view purchase item
33: add_salebill - Can add sale bill
34: change_salebill - Can change sale bill
35: delete_salebill - Can delete sale bill
36: view_salebill - Can view sale bill
45: add_salebilldetails - Can add sale bill details
46: change_salebilldetails - Can change sale bill details
47: delete_salebilldetails - Can delete sale bill details
48: view_salebilldetails - Can view sale bill details
41: add_saleitem - Can add sale item
42: change_saleitem - Can change sale item
43: delete_saleitem - Can delete sale item
44: view_saleitem - Can view sale item
37: add_supplier - Can add supplier
38: change_supplier - Can change supplier
39: delete_supplier - Can delete supplier
40: view_supplier - Can view supplier



----------------------------
How to restart bill numbers 
1. python manage.py shell

2. 
from transactions.models import SaleBill
from django.db import connection

# Delete all existing SaleBill records
SaleBill.objects.all().delete()

# Reset the auto-incrementing sequence
with connection.cursor() as cursor:
    cursor.execute("UPDATE sqlite_sequence SET seq = 0 WHERE name = 'transactions_salebill';")

print("Bill numbering has been reset.")


pyinstaller UGS.spec

Structure 

UGS 
  core
    _pycache_
    __init__.py
    asgi.py
    settings.py
    urls.py
    wsgi.py

  homepage
    _pycache_
    static (contains 3 subfolders)
      bootstrap
      css
      js
    templates
      about.html
      base.html
      home.html
      login.html
      logout.html
    __init__.py
    apps.py
    tests.py
    urls.py
    views.py

  inventory
    _pycache_
    migrations (contains other folders)
    templates
      delete_stock.html
      edit_stock.html
      inventory.html
    __init__.py
    admin.py
    apps.py
    filters.py
    forms.py
    models.py
    tests.py
    urls.py
    views.py

  transactions
    _pycache_
    migrations
    templates
      bill (folder)
      sales (folder)
    __init__.py
    admin.py
    apps.py
    forms.py
    models.py
    tests.py
    urls.py
    views.py

  bg.ico
  bd.sqlite3
  manage.py
  Readme.txt
  requirements.txt
  ugs.bat
  UGS.spec








     