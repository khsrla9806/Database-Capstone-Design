from django.shortcuts import render, redirect, get_object_or_404
from django.db import connection
from .models import Club, Facility
from .forms import ClubForm, FacilityForm

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
        sql = "SELECT id, name, category, content, tel_number, image, url, user_id FROM hanseobase.dbapp_facility WHERE id=(%s)"
        cursor.execute(sql, (id,))
        data = cursor.fetchall()
        
        connection.commit()
        connection.close()
        
        facility = {
            'id' : data[0][0],
            'name' : data[0][1],
            'category' : data[0][2],
            'content' : data[0][3],
            'tel_number' : data[0][4],
            'image' : data[0][5],
            'url' : data[0][6],
            'user_id' : data[0][7],
        }
    except:
        connection.rollback()
        print("찾고자 하는 정보가 없습니다.")
        
    return render(request, 'facility_detail.html', { 'facility' : facility })

def facilityCreate(request):
    if request.method == "POST":
        facility_form = FacilityForm(request.POST, request.FILES)
        context = {"facility_form" : facility_form}
        if facility_form.is_valid():
            facility = facility_form.save(commit=False)
            facility.user_id = request.user.id
            facility.save()
            return redirect('facility')
        else:
            return render(request, 'facility_create.html', context)
    else:
        facility_form = FacilityForm(request.POST, request.FILES)
        context = {"facility_form" : facility_form}
        return render(request, 'facility_create.html', context)
    
def facilityUpdate(request, id):
    facility = Facility.objects.get(pk=id)
    if request.method == "POST":
        if(facility.user == request.user):
            facility_form = FacilityForm(request.POST, instance=facility)
            context = {"facility_form" : facility_form}
            if facility_form.is_valid():
                facility = facility_form.save()
                return redirect('facility_detail', facility.id)
    else:
        facility_form = FacilityForm(instance=facility)
        context = {"facility_form" : facility_form}
        return render(request, 'facility_update.html', context)
    
def facilityDelete(request, id):
    facility = get_object_or_404(Facility, pk=id)
    facility.delete()
    return redirect('facility')

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
        
        sql = "SELECT id, name, category, content, tel_number, image, url, user_id FROM hanseobase.dbapp_club WHERE id=(%s);"
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
            'url' : data[0][6],
            'user_id': data[0][7]
            }
        
    except:
        connection.rollback()
        print("찾고자 하는 정보가 없습니다.")
    
    return render(request, 'club_detail.html', { 'club' : club })

def clubCreate(request):
    if request.method == "POST":
        club_form = ClubForm(request.POST, request.FILES)
        context = {"club_form" : club_form}
        if club_form.is_valid():
            # club.user = request.user
            club = club_form.save()
            return redirect('club')
        else:
            return render(request, 'club_create.html', context)
    else:
        club_form = ClubForm(request.POST, request.FILES)
        context = {"club_form" : club_form}
        return render(request, 'club_create.html', context)

def clubUpdate(request, id):
    club = Club.objects.get(pk=id)
    if request.method == "POST":
        club_form = ClubForm(request.POST, instance=club)
        context = {"club_form" : club_form}
        if club_form.is_valid():
            club = club_form.save()
            return redirect('club_detail', club.id)
    else:
        club_form = ClubForm(instance=club)
        context = {"club_form" : club_form}
        return render(request, 'club_update.html', context)

def clubDelete(request, id):
    club = get_object_or_404(Club, pk=id)
    club.delete()
    return redirect('club')

def postCreate(request):
    return render(request, 'post_create.html')