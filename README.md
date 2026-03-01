# Felhő alapú elosztott rendszerek - Fotóalbum

Ez a projekt a "Fényképalbum létrehozása" feladat végleges, skálázható és többrétegű megvalósítása.

## 1. Választott környezet és technológiák
* **Nyelv / Keretrendszer:** Python és Django
* **Frontend:** Django Templates + Bootstrap
* **PaaS Szolgáltató:** Render.com (automatikus CI/CD pipeline a GitHub repóból).

## 2. Architektúra és Rétegek (Többrétegű modell)
A rendszer a modern webfejlesztési elveknek megfelelően három elkülönült rétegből áll:

1.  **Webes / Applikációs réteg (Render Web Service):** Itt fut a Django alkalmazás (Gunicorn WSGI szerverrel és WhiteNoise statikus fájlkezelővel). Ez felel a logikáért és a HTML generálásáért.
2.  **Adatbázis réteg (Render PostgreSQL):** Különálló relációs adatbázis szerver, amely a felhasználói fiókokat, a jelszó-hasheket és a képek metaadatait (cím, feltöltés ideje, feltöltő ID-ja, Cloudinary link) tárolja.
3.  **Fájltároló réteg (Cloudinary):** Mivel a PaaS környezetek nem perzisztens fájlrendszert használnak, a felhasználók által feltöltött tényleges képek egy külső, erre dedikált felhős tárhely (Cloudinary) fogadja és szolgálja ki.

## 3. Kapcsolatok működése
* Git Push -> GitHub (Webhook) -> Render (Build & Deploy automatikusan).
* A felhasználó feltölt egy képet -> A Django a memóriában feldolgozza -> A képet elküldi a Cloudinary API-n keresztül a tárhelyre -> A Cloudinary visszaküldi a publikus URL-t -> A Django ezt az URL-t és a metaadatokat elmenti a PostgreSQL adatbázisba.