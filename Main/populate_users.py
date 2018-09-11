import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'Main.settings')

import django
django.setup()
from relation.models import userInfo
from faker import Faker

fakegen = Faker()

def populate(N=5):
	# create fake info
	for entry in range(N):
		fake_name = fakegen.name().split()
		fake_first_name = fake_name[0]
		fake_last_name = fake_name[1]
		fake_email = fakegen.email()
	# entry fake info
	user = userInfo.objects.get_or_create(firstName =fake_first_name,
											lastName = fake_last_name,
											email = fake_email)[0]
if __name__ == '__main__':
	print("POPULATING DATABASES")
	populate(20)
	print("COMPLATE!")