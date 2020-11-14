# เทคโนโลยีที่ใช้
1. Docker
2. Django
3. Django rest framework
4. Postgres SQL

## เริ่มต้นโปรเจ็ค (ครั้งแรก)
 1. Build docker images
    ```bash
    make build
    ```

## เริ่มต้นโปรเจ็ค
 1. Start Server
    ```bash
    make up
    ```
 2. Migrate
    ```bash
    make migrate
    ```
 3. Make migrations
    ```bash
    make mgs
    ```
 4. Create superuser
    ```bash
    make superuser
    ```
 5. เข้าไปที่ http://localhost:8000

## docker-compose command ที่ใช้
```bash 
# ปิดการทำงาน container ทั้งหมด
    >$ docker-compose down

# หยุดการทำงานเฉพาะบาง container
    >$ docker-compose stop django

# รีสตาร์ท container
    >$ docker-compose restart django

# ดู log ของ container ทั้งหมด
    >$ docker-compose logs

# ดู log เฉพาะ container
    >$ docker-compose logs django

# ดูการใช้ทรัพยากรณ์ของ container
    >$ docker stats

# ดู container ที่เปิดอยู่
    >$ docker ps
```

เมื่อต้องการทำงานบนคำสั่งของ django (ต้องมั่นใจว่า docker ได้ทำงานอยู่หรือป่าว)
```bash
>$ docker-compose exec django python manage.py startapp <App name>
>$ docker-compose exec django python manage.py migrate
>$ docker-compose exec django python manage.py makemigrations
>$ docker-compose exec django python manage.py createsuperuser
```

## Project Guideline
1. เมื่อรันคำสั่ง 
    ```bash
    >$ docker-compose exec django python manage.py startapp <App name>
    ```
    จะได้ไฟล์ App ขึ้นมา ให้ลากไปไว้ใน โฟลเดอร์ apps

2. เข้าไปเพิ่ม App name ใน ไฟล์ **setting.py**
    ```python
    LOCAL_APPS = [
        'เพิ่มชื่อ App name ตรงนี้ โดยต้องระบุ path ให้ถูกต้อง'
    ]
    ```

3. ไฟล์ **web_urls.py** เอาไว้สำหรับใส่ url ที่ต้องการ
    ```python
    urlpatterns = [
        path('', include('web.apps.pages.urls')),
        path('user_profile/', include('web.apps.user_profile.urls')),
    ]
    ```

4. Database
    ```bash
    Database name: db
    Username: postgres
    Password: postgres
    Port: 5432
    ``` 

5. วิธีเพิ่ม Library ให้โปรเจ็ค *เข้าไปเพิ่มชื่อของ library ใน ไฟล์ requirements.txt* แล้วหลังจากนั้นรันคำสั่ง
    ```bash 
    docker-compose build --no-cache
    ```

# เอกสารเพิ่มเติม
[Django Document](https://docs.djangoproject.com/en/3.1/intro/)

[Django rest framework Document](https://www.django-rest-framework.org/tutorial/quickstart/)
