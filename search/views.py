from importlib.resources import contents
from django.shortcuts import render
from django.db.models import Q 
from django.db import connection
from dbapp.models import Club,Facility;



def searchResult(request):
    if 'kw' in request.GET:
        query = request.GET.get('kw')
        club = Club.objects.all().filter(
            Q(name__icontains=query) 
        )
        facility = Facility.objects.all().filter(
            Q(name__icontains=query) 
        )
        reseult = club.union(facility)
    return render(request, 'search.html', {'query':query, 'reseult':reseult})

# def searchResult(request):
#     if request.method=='GET':
#         searchs =[]
#         try:
#             target = request.GET['kw']
#             print("1")
#             cursor = connection.cursor()
#             sql = "SELECT name, content, image FROM hanseobase.dbapp_club WHERE name=(%s);"
#             # sql = "SELECT name, content FROM hanseobase.dbapp_facility WHERE name LIKE '(%s)' UNION SELECT name, content FROM hanseobase.dbapp_club WHERE name LIKE '(%s)';"
#             print("")
#             result = cursor.execute(sql,[target,])
#             print("3")
#             datas = cursor.fetchall()
#             print("4")
#             connection.commit()
#             connection.close()

#             # searchs =[]
#             for data in datas:
#                 row = {
#                     'name' : data[0],
#                     'content': data[1],
#                 }
#                 searchs.append(row)
#         except:
#             connection.rollback()
#             print("찾고자 하는 정보가 없습니다.")

#         return render(request,'search.html',{'searchs':searchs})
