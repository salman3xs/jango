import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','fist_project.settings')

import django
django.setup()

import random
from first_app.models import AccessRecord,Webpage,Topic,User
from faker import Faker

fakegen = Faker()
topics = ['Search','Social','Marketplace','Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def pop(N=5):
    
    for entry in range(N):
        
        #get topic from above topics
        top = add_topic()
        
        
        #create fake data
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        
        #create a fake webpage
        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]
        
        #create a fake access record
        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]
       
def adduser():
    fake_first_name = fakegen.name()
    fake_last_name = fakegen.name()
    fake_email = fakegen.email()
    new_user = User.objects.get_or_create(first_name=fake_first_name,last_name=fake_last_name,email=fake_email)[0]
    new_user.save()
    return new_user
        
if __name__ == '__main__':
    print('populating scrpit!')
    adduser()
    print('pop complte')
            