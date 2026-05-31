# 🚀 TGB247 - Raqamli Ta'lim Platformasi: Serverga Deploy Qilish Yo'riqnomasi

Ushbu hujjat yangi Ubuntu Server (20.04 / 22.04 LTS) operatsion tizimiga loyihani GitHub repozitoriyasidan yuklab olib, Docker yordamida to'liq deploy (ishga tushirish) qilish bosqichlarini qadam-baqadam tushuntiradi.

---

## 1. Tizim Talablari

* **Operatsion tizim:** Ubuntu Server 20.04 LTS yoki undan yuqori (tavsiya etiladi: 22.04 LTS)
* **Minimal resurslar:** 1 CPU, 1-2 GB RAM, 10 GB disk maydoni
* **Zaruriy dasturlar:** Docker, Docker Compose (V2), Git

---

## 2. Serverni Tayyorlash (O'rnatish ishlari)

Serverga SSH orqali ulaning va quyidagi buyruqlar yordamida tizim paketlarini yangilab, Docker va Git dasturlarini o'rnating.

### 2.1. Tizim paketlarini yangilash:
```bash
sudo apt update && sudo apt upgrade -y
```

### 2.2. Docker va Docker Compose o'rnatish:
```bash
# Docker-ni o'rnatish
sudo apt install docker.io -y

# Docker Compose (V2) o'rnatish
sudo mkdir -p /usr/local/lib/docker/cli-plugins/
sudo curl -SL https://github.com/docker/compose/releases/download/v2.24.1/docker-compose-linux-x86_64 -o /usr/local/lib/docker/cli-plugins/docker-compose
sudo chmod +x /usr/local/lib/docker/cli-plugins/docker-compose

# Foydalanuvchini docker guruhiga qo'shish (sudo-siz ishlatish uchun)
sudo usermod -aG docker $USER
newgrp docker
```

*O'rnatilganini tekshirish:*
```bash
docker --version
docker compose version
```

---

## 3. Loyihani Serverga Yuklash (Clone)

Loyiha kodini GitHub-dan yuklab olish uchun quyidagi buyruqni bajaring:

```bash
cd ~
git clone https://github.com/dohcgle/tgb247.git
cd tgb247
```

---

## 4. Muhit O'zgaruvchilarini Sozlash (`.env`)

Xavfsizlik nuqtai nazaridan `.env` fayli Git repozitoriyasiga yuklanmaydi. Uni serverda loyihaning asosiy papkasida qo'lda yaratishingiz kerak.

Loyiha papkasida `.env` faylini yarating:
```bash
nano .env
```

Fayl ichiga quyidagi parametrlarni o'zingizga moslab kiriting (ayniqsa, parollar va maxfiy kalitni xavfsizroq qilib o'zgartiring):

```env
DEBUG=False
SECRET_KEY=yozing_bu_yerga_juda_maxfiy_va_uzun_kalit_2026_tgb247
ALLOWED_HOSTS=server_ip_manzili,domain_nomi.uz,localhost

# PostgreSQL Sozlamalari (Docker-compose mos kelishi kerak)
DATABASE_URL=postgres://postgres:secure_db_pass_123@db:5432/tgb247
```

*Saqlash uchun:* `Ctrl+O` keyin `Enter`, chiqish uchun `Ctrl+X` bosing.

---

## 5. Konteynerlarni Yoqish va Ishga Tushirish

Docker Compose yordamida Nginx, PostgreSQL va Django ilovalarini orqa fonda (daemon rejimida) yuklang va ishga tushiring:

```bash
docker compose up -d --build
```

*Konteynerlar holatini tekshirish:*
```bash
docker compose ps
```

---

## 6. Bazani Sozlash va Test Ma'lumotlarini Qo'shish

Konteynerlar muvaffaqiyatli ishga tushgandan so'ng, tizim to'liq ishlashi uchun bazani shakllantirish, statik fayllarni yig'ish va administrator hisobini yaratish kerak.

### 6.1. Ma'lumotlar bazasi migratsiyalarini amalga oshirish:
```bash
docker compose exec web python manage.py migrate
```

### 6.2. Statik fayllarni yig'ish (katalog shakllantirish):
```bash
docker compose exec web python manage.py collectstatic --noinput
```

### 6.3. Bosh administrator (Superuser) yaratish:
```bash
docker compose exec web python manage.py createsuperuser
```
*Tizim so'ragan username, email va parolni kiriting.*

### 6.4. Test (Fake) ma'lumotlarini yuklash (Seeding):
Tizimni sinab ko'rish va to'liq ishlashini tahlil qilish uchun biz yozgan skript orqali o'qituvchilar, o'quvchilar, darslar va topshiriqlarni avtomatik yarating:
```bash
docker compose exec web python seed_db.py
```

---

## 7. Saytni Brauzerda Tekshirish

Endi brauzeringiz orqali quyidagi manzillarga kirib, tizimni tekshirishingiz mumkin:
* **Asosiy sahifa:** `http://server_ip_manzili/`
* **Admin paneli:** `http://server_ip_manzili/admin/`

---

## 8. HTTPS (SSL) Xavfsizlik Sertifikatini O'rnatish (Certbot)

Loyiha ishlab chiqarish (production) rejimida to'liq xavfsiz (HTTPS) ishlashi uchun quyidagi bosqichlarni bajarib, bepul **Let's Encrypt SSL** sertifikatini o'rnatishingiz mumkin:

1. Serveringizga domain yo'naltirilgan bo'lishi kerak.
2. Serverda `certbot` dasturini o'rnating:
   ```bash
   sudo apt install certbot -y
   ```
3. SSL sertifikatini yuklab oling:
   ```bash
   sudo certbot certonly --standalone -d domain_nomi.uz
   ```
4. Olingan sertifikatlarni Docker-compose va Nginx papkasiga yo'naltirish (Nginx default.conf fayliga SSL sozlamalarini yozish) talab etiladi.
