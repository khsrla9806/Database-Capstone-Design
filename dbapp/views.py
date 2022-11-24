from django.shortcuts import render
from django.db import connection
from .models import Facility

def home(request):
    return render(request, 'index.html')

def post(request):
    return render(request, 'post.html')

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
    facility = Facility.objects.get(pk=id)
        
    return render(request, 'facility_detail.html', { 'facility' : facility })