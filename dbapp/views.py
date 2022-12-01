from django.shortcuts import render, redirect, get_object_or_404
from django.db import connection
from .models import Club, Facility, Post
from .forms import ClubForm, FacilityForm, PostForm

def home(request):
    try:
        cursor = connection.cursor()    # SQL 문을 시작하기 위한 cursor를 열어줍니다.
        
        # 게시글 테이블에서 필요한 정보를 조회할 수 있는 SELECT 문을 작성합니다.
        sql = "SELECT id, title, image, description FROM hanseobase.dbapp_post;"
        result = cursor.execute(sql)    # 위에서 작성한 SQL 문을 실행합니다.
        datas = cursor.fetchall()       # 실행 결과를 얻어옵니다. 
        
        connection.commit()             # 모든 조회작업이 끝난 후 commit을 진행합니다.
        connection.close()              # 작업이 끝났기 때문에 connection을 닫아줍니다.
        
        post = []                       # html에서 사용할 수 있도록 데이터를 담아줄 리스트를 선언합니다.
        for data in datas:
            row = {
                'id' : data[0],         # 게시글의 id (primary key 입니다.)
                'title' : data[1],      # 게시글의 제목입니다.
                'image' : data[2],      # 게시글의 이미지 입니다.
                'description' : data[3],# 게시글의 짧은 설명입니다.
            }
            post.append(row)            # 리스트에 데이터를 추가해줍니다.
        
    except:
        connection.rollback()           # 조회 작업 중 예외가 발생하면 rollback을 진행합니다.
        print("찾고자 하는 정보가 없습니다.")
    
    return render(request, 'index.html', { 'post' : post })

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
            club = club_form.save(commit=False)
            club.user_id = request.user.id
            club.save()
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

def scholarshipView(request):
    try:
        cursor = connection.cursor()
        
        sql = "SELECT id, name, content, money FROM hanseobase.dbapp_scholarship;"
        result = cursor.execute(sql)
        datas = cursor.fetchall()
        
        connection.commit()
        connection.close()
        
        scholarship = []
        for data in datas:
            row = {
                'id' : data[0],
                'name' : data[1],
                'content' : data[2],
                'money' : data[3]
            }
            scholarship.append(row)
        
    except:
        connection.rollback()
        print("찾고자 하는 정보가 없습니다.")
    
    return render(request, 'scholarship.html', { 'scholarship' : scholarship })

def scholarshipDetailView(request, id):
    try:
        cursor = connection.cursor()
        
        sql = "SELECT id, name, content, money FROM hanseobase.dbapp_scholarship WHERE id=(%s);"
        result = cursor.execute(sql, (id,))
        data = cursor.fetchall()
        
        connection.commit()
        connection.close()
        
        scholarship = {
            'id' : data[0][0],
            'name' : data[0][1],
            'content' : data[0][2],
            'money' : data[0][3]
            }
        
    except:
        connection.rollback()
        print("찾고자 하는 정보가 없습니다.")
    
    return render(request, 'scholarship_detail.html', { 'scholarship' : scholarship })

def multimajorView(request):
    try:
        cursor = connection.cursor()
        
        sql = "SELECT id, time, document, article, notes, category FROM hanseobase.dbapp_multimajor;"
        result = cursor.execute(sql)
        datas = cursor.fetchall()
        
        connection.commit()
        connection.close()
        
        multimajor = []
        for data in datas:
            row = {
                'id' : data[0],
                'time' : data[1],
                'document' : data[2],
                'article' : data[3],
                'notes' : data[4],
                'category' : data[5]
            }
            multimajor.append(row)
        
    except:
        connection.rollback()
        print("찾고자 하는 정보가 없습니다.")
    
    return render(request, 'multimajor.html', { 'multimajor' : multimajor })

def multimajorDetailView(request, id):
    try:
        cursor = connection.cursor()
        
        sql = "SELECT id, time, document, article, notes, category FROM hanseobase.dbapp_multimajor WHERE id=(%s);"
        result = cursor.execute(sql, (id,))
        data = cursor.fetchall()
        
        connection.commit()
        connection.close()
        
        multimajor = {
            'id' : data[0][0],
            'time' : data[0][1],
            'document' : data[0][2],
            'article' : data[0][3],
            'notes' : data[0][4],
            'category' : data[0][5]
            }
        
    except:
        connection.rollback()
        print("찾고자 하는 정보가 없습니다.")
    
    return render(request, 'multimajor_detail.html', { 'multimajor' : multimajor })

# 게시글 등록에 대한 로직
def postCreate(request):
    if request.method == "POST":                                # POST 요청이 들어왔을 때
        post_form = PostForm(request.POST, request.FILES)       # PostForm에 요청받은 데이터와 파일을 인자로 넣습니다.
        context = {"post_form" : post_form}                     # html에 Rendering하기 위한 코드입니다.
        if post_form.is_valid():                                # 만약 들어온 데이터가 타당하다면
            post = post_form.save(commit=False)                 # 데이터를 저장합니다. 하지만 아직 commit 하지 않습니다.
            post.user_id = request.user.id                      # 게시글을 작성한 user의 id를 post의 user_id에 넣어줍니다.
            post.save()                                         # 게시글을 저장합니다.
            return redirect('/')                                # 저장이 성공하면 홈페이지(메인페이지)로 이동합니다.
        else:
            return render(request, 'post_create.html', context)
    else:                                                       # POST 요청이 들어오지 않았을 때
        post_form = PostForm(request.POST, request.FILES)       # PostForm을 html에 Rendering할 준비를 합니다.
        context = {"post_form" : post_form}                     # html에 Rendering하기 위한 코드입니다.
        return render(request, 'post_create.html', context)

    

def postDetailView(request, id):
    try:
        cursor = connection.cursor()        # SQL 문을 시작하기 위한 cursor를 열어줍니다.
        # 특정 id 값을 primary key로 갖는 게시글에 대한 SELECT 문을 작성해줍니다.
        sql = "SELECT title, content, image ,user_id, id FROM hanseobase.dbapp_post WHERE id=(%s)"
        cursor.execute(sql, (id,))          # 위에서 작성한 SQL 문을 실행시킵니다.
        data = cursor.fetchall()            # 실행 결과를 얻어옵니다.
        
        post = {
            'title' : data[0][0],           # 특정 게시글의 제목
            'content' : data[0][1],         # 특정 게시글의 본문 내용
            'image' : data[0][2],           # 특정 게시글의 이미지
            'user_id' : data[0][3],         # 특정 게시글을 작성한 유저의 id 값
            'id' : data[0][4],              # 특정 게시글의 id 값
        }

        user_id = data[0][3]                # html 화면에 유저에 대한 정보를 Rendering하기 위한 user의 id 값
        # 게시글의 작성한 유저의 정보를 얻어오기 위해서 SELECT 문을 작성해줍니다.
        sql = "SELECT student_id, username FROM hanseobase.accounts_user WHERE id=(%s)"
        cursor.execute(sql, (user_id,))     # 위에서 작성한 SQL문에서 WHERE 조건에 유저의 id를 넣어서 실행합니다.
        data = cursor.fetchall()            # 실행 결과를 얻어옵니다.

        user = {
            'student_id' : data[0][0],      # 게시글을 작성한 유저의 학번
            'username' : data[0][1],        # 게시글을 작성한 유저의 이름
        }

        connection.commit()                 # 조회 작업이 끝난 후 commit을 합니다.
        connection.close()                  # 모든 작업이 끝난 후 connection을 닫아줍니다.

    except:
        connection.rollback()               # 만약 조회 작업 중 예외가 발생 시 rollback 해줍니다.
        print("찾고자 하는 정보가 없습니다.")
        
    return render(request, 'post_detail.html', { "post" : post , "user" : user})

# 게시글 수정에 대한 로직
def postUpdate(request, id):
    post = Post.objects.get(pk=id)                          # 특정 id 값을 갖는 Post 객체를 가져옵니다.
    if request.method == "POST":                            # 만약 POST 요청이 들어온다면
        post_form = PostForm(request.POST, instance=post)   # PostForm에 입력받은 데이터를 인자로 넣고, 인스턴스로 기존 데이터를 가져옵니다.
        context = {"post_form" : post_form}                 # html에 Rendering하기 위한 코드입니다.
        if post_form.is_valid():                            # 만약 입력된 데이터가 타당하다면
            post = post_form.save()                         # 데이터를 저장해줍니다.
            return redirect('post_detail', post.id)
    else:                                                   # 만약 POST 요청이 들어오지 않았다면
        post_form = PostForm(instance=post)                 # PostForm에 인스턴스를 사용해 기존 데이터를 가져옵니다.
        context = {"post_form" : post_form}                 # html에 Rendering하기 위한 코드입니다.
        return render(request, 'post_update.html', context)

# 게시글 삭제에 대한 로직
def postDelete(request, id):
    post = get_object_or_404(Post, pk=id)       # 삭제하고자 하는 id 값의 Post 객체를 가져옵니다.
    post.delete()                               # 해당 Post 객체를 삭제합니다.
    return redirect('/')                        # 삭제가 완료되면 메인 페이지로 이동합니다.