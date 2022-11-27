from django.db import models

class Facility(models.Model):
    opt1= "카페"
    opt2= "음식점"
    opt3= "술집"
    CHOICES = ((opt1, "카페"), (opt2, "음식점"),(opt3, "술집"))
    
    name = models.CharField(max_length=30, null=False)
    category = models.CharField(choices=CHOICES, max_length=50, null=True, blank=True)
    content = models.TextField(null=True)
    tel_number = models.CharField(max_length=20, null=True)
    image = models.ImageField(upload_to='facility/', default='hanseo_logo.png', null=True, blank=True)
    url = models.URLField(null=True)
    
    def __str__(self):
        return self.name

class Club(models.Model):
    opt1 = "음악"
    opt2 = "여행"
    opt3 = "공부"
    opt4 = "종교"
    opt5 = "운동"
    opt6 = "사진"
    opt7 = "문화생활"
    opt8 = "소프트웨어"
    CHOICES = ((opt1, "음악"), (opt2, "여행"), (opt3, "공부"), (opt4, "종교"), (opt5, "운동"), (opt6, "사진"), (opt7, "문화생활"), (opt8, "소프트웨어"))
    
    name = models.CharField(max_length=30, null=False)
    category = models.CharField(choices=CHOICES, max_length=50, null=True, blank=True)
    content = models.TextField(null=True)
    tel_number = models.CharField(max_length=20, null=True)
    image = models.ImageField(upload_to='club/', default='hanseo_logo.png', null=True, blank=True)
    url = models.URLField(null=True)
    
    def __str__(self):
        return self.name

class Multimajor(models.Model):
    opt1 = "부전공"
    opt2 = "복수전공"
    CHOICES = ((opt1,"부전공"),(opt2,"복수전공"))
    #신청시기
    time = models.CharField(max_length=20, null=True)
    #구비서류
    document = models.TextField(null=True)
    #관련조항
    article = models.CharField(max_length=50,null=True)
    #참고사항
    notes = models.TextField(null=True)
    #부전공/복수전공
    category = models.CharField(choices=CHOICES, max_length=10,null=True,blank=True)

    def __str__(self):
        return self.category

class Scholarship(models.Model):
    name = models.CharField(max_length=30, null=False)
    content = models.TextField(null=True)
    money = models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.name

    