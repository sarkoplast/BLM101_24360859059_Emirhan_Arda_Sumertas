# html_olusturucu.py
# Bu program kullanicidan bilgi alir ve otomatik olarak bir HTML dosyasi olusturur.

# Programin ana fonksiyonu tanimlanir
def main():

    
    print("=== Otomatik HTML Sayfasi Olusturucu ===")

    # Kullanicidan ad ve soyad bilgisi alinir
    name = input("Adiniz ve Soyadiniz: ")

    # Kullanicidan aldigi dersler istenir (virgul ile ayirmasi beklenir)
    courses = input("Aldiginiz dersleri virgul ile ayirin: ")

    # Kullanicidan kisa bir biyografi bilgisi alinir
    bio = input("Kisa bir biyografi yaziniz: ")

    # Girilen dersler virgulden bolunerek bir listeye donusturulur
    course_list = courses.split(",")

    # HTML icerigi string (metin) olarak olusturulmaya baslanir
    # f-string kullanilarak Python degiskenleri HTML icine yerlestirilir
    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"> <!-- Turkce karakter sorunu olmamasi icin -->
    <title>Kisisel Web Sayfasi</title>

    <!-- Sayfanin gorunumunu duzenleyen CSS kodlari -->
    <style>
        body {{
            font-family: Arial, sans-serif;      /* Yazi tipi */
            background-color: #f4f6f8;           /* Arka plan rengi */
            margin: 40px;                         /* Sayfa kenar boslugu */
        }}
        h1 {{
            color: #2c3e50;                      /* Ana baslik rengi */
        }}
        h2 {{
            color: #34495e;                      /* Alt baslik rengi */
        }}
        p {{
            font-size: 16px;                     /* Paragraf yazi boyutu */
        }}
        ul {{
            background-color: #ffffff;          /* Liste arka plan rengi */
            padding: 15px;                       /* Liste ici bosluk */
            border-radius: 8px;                  /* Kose yuvarlatma */
        }}
        li {{
            margin-bottom: 5px;                  /* Liste elemanlari arasi bosluk */
        }}
    </style>
</head>
<body>

    <!-- Kullanicinin girdigi ad-soyad baslik olarak yazdirilir -->
    <h1>{name}</h1>

    <!-- Biyografi basligi -->
    <h2>Biyografi</h2>

    <!-- Kullanicinin girdigi biyografi paragraf olarak eklenir -->
    <p>{bio}</p>

    <!-- Dersler basligi -->
    <h2>Aldigim Dersler</h2>

    <!-- Derslerin listelenecegi HTML listesi -->
    <ul>
"""

    # Ders listesi tek tek gezilir
    for course in course_list:
        # Her ders HTML liste elemani (<li>) olarak eklenir
        html_content += f"        <li>{course.strip()}</li>\n"

    # HTML belgesinin kapanis etiketleri eklenir
    html_content += """
    </ul>

</body>
</html>
"""

    # index.html adinda bir dosya yazma modunda acilir
    # encoding utf-8 secilerek Turkce karakter destegi saglanir
    with open("index.html", "w", encoding="utf-8") as file:
        # Hazirlanan HTML icerigi dosyaya yazilir
        file.write(html_content)

    # Dosyanin basariyla olusturuldugu ekrana yazdirilir
    print("index.html dosyasi basariyla olusturuldu.")


# Python dosyasi dogrudan calistirilirsa main fonksiyonu calisir
if __name__ == "__main__":
    main()
