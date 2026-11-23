# رفيق التاريخ الإسلامي — مشروع APK

التطبيق عبارة عن WebView يعرض `app/src/main/assets/index.html` (نفس المحتوى والأنشطة الأصلية بتصميم جديد).

## الطريقة 1: GitHub Actions (بدون تثبيت أي شيء)
1. ارفع محتوى هذا المجلد إلى مستودع GitHub جديد (فرع `main`).
2. افتح تبويب **Actions ← Build APK ← Run workflow**.
3. بعد دقائق نزّل `app-debug.apk` من **Artifacts** وثبّته على الهاتف (فعّل "التثبيت من مصادر غير معروفة").

## الطريقة 2: Android Studio
1. `python3 scripts/fetch_vendor.py`  (ينزّل المكتبات ليعمل التطبيق أوفلاين)
2. افتح المجلد في Android Studio ← Build ▸ Build APK(s).

## الطريقة 3: سطر الأوامر
يلزم JDK 17 + Android SDK (platform 34) + Gradle 8.7:
```
python3 scripts/fetch_vendor.py
gradle assembleDebug
# الناتج: app/build/outputs/apk/debug/app-debug.apk
```
> نسخة `release` للنشر على Google Play تحتاج توقيعاً بمفتاحك الخاص.
