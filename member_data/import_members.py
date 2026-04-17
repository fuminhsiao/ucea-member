import csv
import os
import django
import sys


sys.path.append('D:\\work\\ucea-member\\ucea_member')

# 設置 Django 環境
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ucea_member.settings")
django.setup()

from member_data.models import Member

def import_universities_from_csv(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            member, created = Member.objects.get_or_create(
                name=row['Text'],
                university_id=row['ID'],
                cx=row['CX'],
                cy=row['CY'],
                facebook_id=row['Facebook'],
                twitter_id=row['Twitter'],
                official_website=row['Link'],
            )
            if created:
                print(f'University {member.name} created.')
            else:
                print(f'University {member.name} already exists.')

# 導入數據
import_universities_from_csv("D:\\work\\output.csv")