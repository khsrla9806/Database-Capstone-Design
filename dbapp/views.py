from django.shortcuts import render
from django.db import connection
from .models import Facility

def home(request):
    return render(request, 'index.html')

def facilityView(request):
    try:
        cursor = connection.cursor()
        
        sql = "SELECT id, name, category, content, tel_number, image, url FROM hanseobase.dbapp_facility;"
        result = cursor.execute(sql)
        datas = cursor.fetchall()
        
        connection.commit()
        connection.close()
        
        facilities = []
        for data in datas:
            row = {
                'id' : data[0],
                'name' : data[1],
                'category' : data[2],
                'content' : data[3],
                'tel_number' : data[4],
                'image' : data[5],
                'url' : data[6]
            }
            facilities.append(row)
        
    except:
        connection.rollback()
        print("찾고자 하는 정보가 없습니다.")
    
    return render(request, 'facility.html', { 'facilities' : facilities })

def facilityDetailView(request, id):
    try:
        cursor = connection.cursor()
        sql = "SELECT name, category, content, tel_number, image, url FROM hanseobase.dbapp_facility WHERE id=(%s)"
        cursor.execute(sql, (id,))
        data = cursor.fetchall()
        
        connection.commit()
        connection.close()
        
        facility = {
            'name' : data[0][0],
            'category' : data[0][1],
            'content' : data[0][2],
            'tel_number' : data[0][3],
            'image' : data[0][4],
            'url' : data[0][5]
        }
    except:
        connection.rollback()
        print("찾고자 하는 정보가 없습니다.")
        
    return render(request, 'facility_detail.html', { 'facility' : facility })

def clubView(request):
    try:
        cursor = connection.cursor()
        
        sql = "SELECT id, name, category, content, tel_number, image, url FROM hanseobase.dbapp_club;"
        result = cursor.execute(sql)
        datas = cursor.fetchall()
        
        connection.commit()
        connection.close()
        
        clubs = []
        for data in datas:
            row = {
                'id' : data[0],
                'name' : data[1],
                'category' : data[2],
                'content' : data[3],
                'tel_number' : data[4],
                'image' : data[5],
                'url' : data[6]
            }
            clubs.append(row)
        
    except:
        connection.rollback()
        print("찾고자 하는 정보가 없습니다.")
    
    return render(request, 'club.html', { 'clubs' : clubs })

def clubDetailView(request, id):
    try:
        cursor = connection.cursor()
        
        sql = "SELECT id, name, category, content, tel_number, image, url FROM hanseobase.dbapp_club WHERE id=(%s);"
        result = cursor.execute(sql, (id,))
        data = cursor.fetchall()
        
        connection.commit()
        connection.close()
        
        club = {
            'id' : data[0][0],
            'name' : data[0][1],
            'category' : data[0][2],
            'content' : data[0][3],
            'tel_number' : data[0][4],
            'image' : data[0][5],
            'url' : data[0][6]
            }
        
    except:
        connection.rollback()
        print("찾고자 하는 정보가 없습니다.")
    
    return render(request, 'club_detail.html', { 'club' : club })

def postCreate(request):
    return render(request, 'post_create.html')