# 📘 TGB247 - Raqamli Ta'lim Platformasi: Kengaytirilgan Foydalanish Yo'riqnomasi

Ushbu yo'riqnoma **TGB247** raqamli ta'lim platformasining imkoniyatlari, uning modullari, ma'lumotlar tuzilishi va platformadan turli foydalanuvchi rollari (Administrator, O'qituvchi, O'quvchi) kesimida qanday foydalanish bo'yicha batafsil yo'l-yo'riq ko'rsatadi.

---

## 1. Kirish va Platforma Haqida

**TGB247** — zamonaviy ta'lim jarayonlarini raqamlashtirish, o'quvchilarning bilim va ko'nikmalarini baholash, amaliy loyihalar portfoliosini shakllantirish hamda akademik halollikni ta'minlashga mo'ljallangan kompleks ta'lim platformasidir.

Tizimda **RBAC (Role-Based Access Control)** — rollarga asoslangan kirish nazorati to'liq joriy qilingan bo'lib, har bir foydalanuvchi faqat o'ziga ruxsat etilgan ma'lumotlar bilan ishlaydi.

---

## 2. Tizim Arxitekturasi va Muhit Sozlamalari

Tizim kichik va o'rta hajmdagi ta'lim muassasalari, ortiqcha resurslarsiz barqaror va tez ishlashi uchun optimallashtirilgan:
* **Backend:** Django Web Framework.
* **Ma'lumotlar bazasi:** PostgreSQL (Docker-compose ichida ishlaydi).
* **Veb-server (Reverse Proxy):** Nginx (Port 80 da gvardiya vazifasini bajaradi, statik va media fayllarni to'g'ridan-to'g'ri keshlash orqali tezkor yetkazib beradi).
* **Soddalashtirish:** Katta yuklamalar talab etilmagani bois, tizimdan **Celery** va **Redis** texnologiyalari olib tashlangan. Bu esa tizimning operativ xotira (RAM) sarfini sezilarli darajada kamaytirdi va kichik serverlarda ham muammosiz ishlashini ta'minlaydi.

---

## 3. Tizim Rollari va Ruxsatnomalar

Tizimda 3 ta asosiy rol mavjud:

### A. Administrator (Superuser)
* **Vazifasi:** Tizimning to'liq egasi. Foydalanuvchilarni yaratadi, rollarni belgilaydi, xavfsizlik jurnallarini kuzatadi.
* **Kirish huquqi:** Django Admin paneliga to'liq kirish (`http://localhost/admin/`).

### B. O'qituvchi (Teacher)
* **Vazifasi:** Kurs kontentini yaratadi, topshiriqlar va testlarni shakllantiradi hamda o'quvchilarning amaliy ishlarini baholaydi.
* **Kirish huquqi:** Faqat o'ziga tegishli fanlar, modullar, darslar va talabalar javoblarini tahrirlash huquqi.

### C. O'quvchi (Student)
* **Vazifasi:** Darslarni o'rganadi, testlarni topshiradi, topshiriqlar uchun yozgan kodlarini yuklaydi va o'z portfolio loyihalarini boshqaradi.
* **Kirish huquqi:** Tizimning asosiy foydalanuvchi interfeysi orqali darslar va topshiriqlarni ko'rish hamda bajarish.

---

## 4. Modullar va Ulardan Foydalanish

### 4.1. Foydalanuvchilar va Rollar (`accounts`)
Ushbu modulda barcha foydalanuvchilar va ularning rollari saqlanadi.
* **Muhim maydonlar:**
  * `role`: Foydalanuvchining roli (`STUDENT`, `TEACHER`, `ADMIN`).
  * `digcomp_level`: Yevropa Raqamli Savodxonlik modeli (DigComp) bo'yicha foydalanuvchining darajasi (`Foundation`, `Intermediate`, `Advanced`).
* **Qanday ishlatiladi?**
  1. Admin panelda **Foydalanuvchilar** bo'limiga o'ting.
  2. Yangi foydalanuvchi qo'shish tugmasini bosing.
  3. Foydalanuvchiga tegishli rolni tanlang. Agar o'quvchi bo'lsa, uning raqamli savodxonlik darajasini belgilang.

### 4.2. Kurslar va Darslar Moduli (`courses`)
O'quv jarayonining o'zagi bo'lib, uch bosqichli tuzilishga ega: **Fan -> Modul -> Dars**.
* **Dars tarkibi:** Har bir dars o'z ichiga boy matnli kontent (`CKEditor 5` orqali), video darslik havolasi va ko'rgazmali infografika (rasm) faylini oladi.
* **Qanday ishlatiladi?**
  1. Dastlab **Fanlar** bo'limida yangi fan qo'shiladi va unga mas'ul o'qituvchi biriktiriladi.
  2. Fanning ostida **Modullar** yaratiladi (masalan: 1-Modul, 2-Modul).
  3. Har bir modul ichiga darslar qo'shiladi. Dars matnini boy interfeys orqali chiroyli shakllantirish mumkin.

### 4.3. Baholash va Viktorinalar (`assessments`)
Darslarni o'zlashtirish darajasini aniqlash uchun test tizimi.
* **Tarkibi:** Viktorina (Quiz) -> Savollar (Questions) -> Javob variantlari (Answer Choices).
* **Vaqt cheklovi:** Har bir test uchun daqiqalarda vaqt cheklovi belgilanishi mumkin.
* **Natijalar:** O'quvchi test topshirganda, tizim avtomatik ravishda uning **Viktorina urinishi** (Quiz Attempt) obyektini yaratadi va ballni hisoblab chiqadi.

### 4.4. Topshiriqlar va Loyihalar (`assignments` va `portfolios`)
Nazariy bilimlarni amaliyotda sinash va talabalarning shaxsiy portfoliosini yuritish moduli.
* **Topshiriqlar:** O'qituvchi darsga biriktirilgan topshiriq yaratadi. Agar u dasturlash fani bo'lsa, **Laboratoriya ishi** deb belgilashi mumkin.
* **Javoblar (Submissions):** O'quvchi topshiriq javobi sifatida o'zi yozgan kod matnini yoki bajarilgan ish faylini yuklaydi. O'qituvchi esa kelib buni baholaydi va fikr-mulohaza yozadi.
* **Portfolio:** Har bir o'quvchining shaxsiy yutuqlari, bajargan yirik loyihalari va bu loyihalar orqali qaysi ko'nikmalarni namoyish eta olganligi (*Skills Demonstrated*) portfolio sahifasida to'planadi.

### 4.5. Forum va Muloqot (`communication`)
O'quvchi va o'qituvchilar o'rtasida darslar yuzasidan savol-javob muhiti.
* O'quvchi ma'lum bir dars yuzasidan **Forum mavzusi** ochadi.
* O'qituvchi va boshqa talabalar ushbu mavzu ostida **Forum postlari** orqali o'zaro fikr almashadilar.

### 4.6. Analitika va Xavfsizlik (`analytics` va `security`)
Tizimni nazorat qilish va o'quvchilar faolligini tahlil qilish tizimi.
* **Foydalanuvchi faolligi:** Tizim avtomatik ravishda foydalanuvchilarning qachon tizimga kirganligi, qaysi darslarni ko'rganligini qayd etadi.
* **Samaradorlik ko'rsatkichi:** Har bir o'quvchining testlardagi o'rtacha bali va topshirgan vazifalari tahlili.
* **Kirish jurnali:** Ballar, so'rovlar (requests), IP manzillar va shubhali harakatlar tarixi.
* **Akademik halollik hisoboti:** Imtihon yoki test topshirish davomida talaba brauzer oynasidan boshqa oynalarga o'tganligi (*tab switch*) tizim tomonidan qayd etiladi va bu yerda hisobot shakllanadi.

---

## 5. Sinov va Ssenariylar (Ma'lumotlar mavjud)

Tizimni mukammal darajada tekshirib ko'rishingiz uchun biz bazaga **fake (test) ma'lumotlar** qo'shdik. Quyidagi ssenariylarni bajarib ko'ring:

### Ssenariy 1: O'qituvchi sifatida baholash
1. Brauzerda `http://localhost/admin/` sahifasini oching.
2. `temur_oqituvchi` foydalanuvchisi va `pass1234` paroli bilan kiring.
3. Chap menyudan **Topshiriqlar** bo'limidagi **Javoblar** bo'limiga o'ting.
4. U yerda o'quvchilar yuborgan javoblar va yozilgan kodlarni ko'rasiz. Baholarni o'zgartirib yoki yangi fikr yozib saqlang.

### Ssenariy 2: Xavfsizlik va Akademik Halollikni tekshirish
1. Tizimga o'zingizning **Superuser** profilingiz orqali kiring.
2. Chap menyudan **Xavfsizlik** bo'limiga o'ting.
3. **Kirish jurnallari** bo'limini ko'ring: u yerda shubhali so'rovlar qizil rangda yoki ogohlantirish belgisi bilan ajratib ko'rsatiladi.
4. **Akademik halollik hisoboti**ga o'ting: u yerda test topshirishda qoidabuzarlik qilgan talabalar ro'yxatini va sabablarini ko'rasiz.

---

## 6. Kelajakda Tizimni Kengaytirish bo'yicha Tavsiyalar

Agar kelajakda foydalanuvchilar soni ortsa va yuqori trafik yuzaga kelsa, quyidagilarni amalga oshirish tavsiya etiladi:
1. **Nginx Keshlash Sozlamalari:** Statik fayllardan tashqari tez-tez o'zgarmaydigan sahifalar uchun Nginx keshlashini yoqing.
2. **Ma'lumotlar bazasini indekslash:** Ko'p qidiriladigan maydonlar (masalan, `UserActivity`dagi `timestamp` yoki `User`dagi `role`) uchun Django modellarida `db_index=True` xususiyatini qo'shing.
3. **Arxivlash:** `AccessLog` va `UserActivity` kabi juda tez ko'payadigan jadvallarni vaqti-vaqti bilan arxivlab, asosiy bazani yuklamadan xoli qilib turing.
