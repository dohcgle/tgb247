import os
import django
import random
from datetime import datetime, timedelta
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.accounts.models import User
from apps.courses.models import Subject, Module, Lesson
from apps.assignments.models import Assignment, Submission
from apps.assessments.models import Quiz, Question, AnswerChoice, QuizAttempt
from apps.portfolios.models import Portfolio, ProjectItem
from apps.analytics.models import UserActivity, PerformanceMetric
from apps.communication.models import ForumThread, ForumPost
from apps.security.models import AccessLog, AcademicIntegrityReport

def seed():
    print("Ma'lumotlar bazasini tozalash...")
    # Delete in reverse order of dependencies
    AcademicIntegrityReport.objects.all().delete()
    AccessLog.objects.all().delete()
    ForumPost.objects.all().delete()
    ForumThread.objects.all().delete()
    PerformanceMetric.objects.all().delete()
    UserActivity.objects.all().delete()
    ProjectItem.objects.all().delete()
    Portfolio.objects.all().delete()
    QuizAttempt.objects.all().delete()
    AnswerChoice.objects.all().delete()
    Question.objects.all().delete()
    Quiz.objects.all().delete()
    Submission.objects.all().delete()
    Assignment.objects.all().delete()
    Lesson.objects.all().delete()
    Module.objects.all().delete()
    Subject.objects.all().delete()
    
    # Keep superusers, delete other mock users
    User.objects.filter(is_superuser=False).delete()

    print("Foydalanuvchilarni yaratish...")
    # Create Teachers
    teachers = []
    teacher_data = [
        {"username": "temur_oqituvchi", "first_name": "Temur", "last_name": "Rahimov", "email": "temur@example.com", "role": "TEACHER", "bio": "Dasturlash va axborot texnologiyalari bo'yicha 10 yillik tajribaga ega o'qituvchi."},
        {"username": "dilnoza_oqituvchi", "first_name": "Dilnoza", "last_name": "Sodiqova", "email": "dilnoza@example.com", "role": "TEACHER", "bio": "Raqamli texnologiyalar va pedagogika fanlari nomzodi."}
    ]
    for data in teacher_data:
        u = User.objects.create_user(
            username=data["username"],
            first_name=data["first_name"],
            last_name=data["last_name"],
            email=data["email"],
            role=data["role"],
            bio=data["bio"]
        )
        u.set_password("pass1234")
        u.save()
        teachers.append(u)

    # Create Students
    students = []
    student_data = [
        {"username": "anvar_student", "first_name": "Anvar", "last_name": "Karimov", "email": "anvar@example.com", "role": "STUDENT", "digcomp_level": "Intermediate"},
        {"username": "malika_student", "first_name": "Malika", "last_name": "Toshpulatova", "email": "malika@example.com", "role": "STUDENT", "digcomp_level": "Foundation"},
        {"username": "sardor_student", "first_name": "Sardor", "last_name": "Alimov", "email": "sardor@example.com", "role": "STUDENT", "digcomp_level": "Advanced"}
    ]
    for data in student_data:
        u = User.objects.create_user(
            username=data["username"],
            first_name=data["first_name"],
            last_name=data["last_name"],
            email=data["email"],
            role=data["role"],
            digcomp_level=data["digcomp_level"]
        )
        u.set_password("pass1234")
        u.save()
        students.append(u)

    print("Fanlar, Modullar va Darslarni yaratish...")
    # Create Subject 1
    sub1 = Subject.objects.create(
        title="Python Dasturlash Asoslari",
        description="Ushbu kurs Python dasturlash tili asoslari, sintaksisi, ma'lumotlar turlari va algoritmlashni o'rgatadi.",
        teacher=teachers[0]
    )
    
    # Modules for Subject 1
    m1 = Module.objects.create(subject=sub1, title="1-Modul: Kirish va O'zgaruvchilar", order=1)
    m2 = Module.objects.create(subject=sub1, title="2-Modul: Shartli operatorlar va Tsikllar", order=2)

    # Lessons for Module 1
    l1 = Lesson.objects.create(
        module=m1,
        title="Python o'rnatish va birinchi dastur",
        content="Python tili tarixi va uni tizimga o'rnatish. 'Hello World' dasturini yozish va ishga tushirish.",
        video_url="https://www.youtube.com/watch?v=rfscVS0vtbw"
    )
    l2 = Lesson.objects.create(
        module=m1,
        title="O'zgaruvchilar va ma'lumot turlari",
        content="Integer, Float, String va Boolean ma'lumotlar turlari bilan ishlash. O'zgaruvchilar yaratish qoidalari.",
        video_url="https://www.youtube.com/watch?v=rfscVS0vtbw"
    )

    # Lessons for Module 2
    l3 = Lesson.objects.create(
        module=m2,
        title="If-Else shart operatorlari",
        content="Shartlarni tekshirish, taqqoslash operatorlari va mantiqiy ifodalar bilan ishlash.",
        video_url="https://www.youtube.com/watch?v=rfscVS0vtbw"
    )

    # Create Subject 2
    sub2 = Subject.objects.create(
        title="Raqamli Savodxonlik (DigComp)",
        description="Raqamli dunyoda axborotni izlash, muloqot qilish, xavfsizlik va muammolarni hal qilish ko'nikmalari.",
        teacher=teachers[1]
    )
    m3 = Module.objects.create(subject=sub2, title="1-Modul: Axborot xavfsizligi", order=1)
    l4 = Lesson.objects.create(
        module=m3,
        title="Parollar xavfsizligi va shaxsiy ma'lumotlar muhofazasi",
        content="Kuchli parollar yaratish va fishing (phishing) hujumlaridan himoyalanish usullari.",
        video_url="https://www.youtube.com/watch?v=rfscVS0vtbw"
    )

    print("Viktorina va Savollarni yaratish...")
    # Quiz 1 for Module 1
    q1 = Quiz.objects.create(module=m1, title="Python Asoslari bo'yicha Test", time_limit_minutes=15)
    
    qn1 = Question.objects.create(quiz=q1, text="Python qachon yaratilgan?", points=5)
    AnswerChoice.objects.create(question=qn1, text="1991-yilda", is_correct=True)
    AnswerChoice.objects.create(question=qn1, text="1995-yilda", is_correct=False)
    AnswerChoice.objects.create(question=qn1, text="2000-yilda", is_correct=False)

    qn2 = Question.objects.create(quiz=q1, text="Qaysi kalit so'z o'zgaruvchi turini aniqlash uchun ishlatiladi?", points=5)
    AnswerChoice.objects.create(question=qn2, text="type()", is_correct=True)
    AnswerChoice.objects.create(question=qn2, text="typeof", is_correct=False)
    AnswerChoice.objects.create(question=qn2, text="print()", is_correct=False)

    # Quiz 2 for Module 3
    q2 = Quiz.objects.create(module=m3, title="Xavfsizlik testi", time_limit_minutes=10)
    qn3 = Question.objects.create(quiz=q2, text="Qaysi parol eng xavfsiz hisoblanadi?", points=10)
    AnswerChoice.objects.create(question=qn3, text="P@ssw0rd2026!", is_correct=True)
    AnswerChoice.objects.create(question=qn3, text="12345678", is_correct=False)
    AnswerChoice.objects.create(question=qn3, text="admin", is_correct=False)

    print("Topshiriqlar va Javoblarni yaratish...")
    # Assignment for Lesson 2
    a1 = Assignment.objects.create(
        lesson=l2,
        title="O'zgaruvchilar bilan amallar bajarish",
        description="Foydalanuvchidan ikkita son so'rang va ularning yig'indisini hisoblaydigan dastur tuzing.",
        is_laboratory=False,
        deadline=timezone.now() + timedelta(days=7)
    )

    # Submission for Assignment 1 by Anvar
    Submission.objects.create(
        assignment=a1,
        student=students[0],
        code_snippet="""a = int(input("Birinchi sonni kiriting: "))
b = int(input("Ikkinchi sonni kiriting: "))
print("Yig'indi:", a + b)""",
        grade=95.00,
        feedback="Ajoyib! Kod to'g'ri va chiroyli yozilgan."
    )

    # Submission for Assignment 1 by Malika
    Submission.objects.create(
        assignment=a1,
        student=students[1],
        code_snippet="""num1 = 5
num2 = 10
print(num1+num2)""",
        grade=70.00,
        feedback="Foydalanuvchidan input olishni unutgansiz, lekin hisoblash to'g'ri."
    )

    print("Portfoliolar va Loyihalarni yaratish...")
    for s in students:
        port = Portfolio.objects.create(student=s, showcase_url=f"https://github.com/{s.username}")
        ProjectItem.objects.create(
            portfolio=port,
            title="Mening Ilk Dasturim",
            description="Kalkulyator dasturi python tilida",
            skills_demonstrated="Kalkulyator dasturini yaratib o'zgaruvchilar va amallarni qo'llash ko'nikmalari."
        )

    print("Forum va Muloqotlarni yaratish...")
    thread1 = ForumThread.objects.create(
        lesson=l1,
        author=students[0],
        title="Python o'rnatishda xatolik yuz beryapti"
    )
    ForumPost.objects.create(
        thread=thread1,
        author=students[0],
        content="Windows 11 tizimiga o'rnatishda 'PATH' sozlamasini qanday qo'shaman?"
    )
    ForumPost.objects.create(
        thread=thread1,
        author=teachers[0],
        content="Python-ni o'rnatishda pastki qismdagi 'Add Python to PATH' katakchasiga belgi qo'yishingiz kerak."
    )

    print("Analitika va Xavfsizlik hisobotlarini yaratish...")
    # User Activities
    for s in students:
        UserActivity.objects.create(user=s, action_type="LOGIN")
        UserActivity.objects.create(user=s, action_type="LESSON_VIEW")
        # Metrics
        PerformanceMetric.objects.create(
            student=s,
            average_quiz_score=random.choice([75.5, 88.0, 95.0]),
            assignments_completed=1
        )

    # Access Logs & Academic Integrity
    AccessLog.objects.create(
        user=students[2],
        ip_address="192.168.1.50",
        endpoint="/admin/courses/subject/",
        was_suspicious=True
    )
    AcademicIntegrityReport.objects.create(
        student=students[2],
        incident_type="TAB_SWITCH_DURING_EXAM",
        description="Foydalanuvchi test davomida browser oynasidan 3 marta boshqa oynaga o'tdi."
    )

    print("Tabriklaymiz! Barcha ma'lumotlar muvaffaqiyatli yaratildi.")

if __name__ == "__main__":
    seed()
