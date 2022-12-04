import tkinter
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

from tkinter import *
import pandas as pd
from tkinter import ttk
from datetime import datetime


def submit_fields():
    path = "Anket.xlsx"
    df1 = pd.read_excel(path)

    Series_timestamp = df1['Zaman damgası']
    Series_name_surname = df1['Katılımcı Ad Soyad']
    Series_age = df1['Katılımcı Yaş']
    Series_education = df1['Eğitim']
    Series_vr = df1['Önceden VR tecrübeniz var mıydı?']
    Series_q1 = df1['1. Bu sistemi sık sık kullanmak isterim.']
    Series_q2 = df1['2.  Bu sistemi gereksiz yere karmaşık buldum.']
    Series_q3 = df1['3.  Sistemin kullanımının kolay olduğunu düşündüm.']
    Series_q4 = df1['4.  Bu sistemi kullanabilmek için teknik bir kişinin desteğine ihtiyacım olacağını düşünüyorum.']
    Series_q5 = df1['5.  Bu sistemdeki çeşitli fonksiyonların iyi bir şekilde entegre olduğunu gördüm.']
    Series_q6 = df1['6.  Bu sistemde çok fazla tutarsızlık olduğunu düşündüm.']
    Series_q7 = df1['7.  Çoğu insanın bu sistemi çok çabuk kullanmayı öğreneceğini hayal ediyorum.']
    Series_q8 = df1['8. Bu sistemi kullanmayı çok hantal (garip) buldum.']
    Series_q9 = df1['9.  Bu sistemi kullanırken kendimi çok güvende hissettim.']
    Series_q10 = df1['10.  Bu sisteme geçmeden önce çok şey öğrenmem gerekiyordu.']
    Series_IPQ1 = df1['IPQ1.  Bilgisayar tarafından oluşturulan dünyada bir "orada olma" duygusuna sahiptim.']
    Series_IPQ2 = df1['IPQ2.   Bir şekilde sanal dünyanın etrafımı sardığını hissettim.']
    Series_IPQ3 = df1['IPQ3.  Sadece resimleri algılıyormuş gibi hissettim.']
    Series_IPQ4 = df1['IPQ4.  Sanal uzayda kendimi mevcut hissetmiyordum.']
    Series_IPQ5 = df1['IPQ5.  Dışarıdan bir şey çalıştırmak yerine sanal alanda hareket etme duygusu vardı.']
    Series_IPQ6 = df1['IPQ6.  Sanal uzayda kendimi mevcut (oradaymış gibi) hissettim.']
    Series_IPQ7 = df1[
        'IPQ7.  Sanal dünyada gezinirken etrafınızdaki gerçek dünyanın ne kadar farkındaydınız? (yani sesler, ' \
        'oda sıcaklığı, diğer insanlar vb.)?']
    Series_IPQ8 = df1['IPQ8.  Gerçek çevremin farkında değildim.']
    Series_IPQ9 = df1['IPQ9.  Yine de gerçek çevreye dikkat ettim.']
    Series_IPQ10 = df1['IPQ10.  Tamamen sanal dünyanın büyüsüne kapıldım.']
    Series_IPQ11 = df1['IPQ11.  Sanal dünya size ne kadar gerçek göründü?']
    Series_IPQ12 = df1['IPQ12.  Sanal ortamdaki deneyiminiz, gerçek dünya deneyiminizle ne kadar tutarlı görünüyordu?']
    Series_IPQ13 = df1['IPQ13.  Sanal dünya size ne kadar gerçek göründü?']
    Series_IPQ14 = df1['IPQ14.    Sanal dünya gerçek dünyadan daha gerçekçi görünüyordu.']
    Series_SSQ1 = df1['SSQ1.  Genel rahatsızlık']
    Series_SSQ2 = df1['SSQ2.  Tükenmişlik, yorgunluk']
    Series_SSQ3 = df1['SSQ3. Baş ağrısı']
    Series_SSQ4 = df1['SSQ4. Göz yorgunluğu']
    Series_SSQ5 = df1['SSQ5.  Odaklanma zorluğu']
    Series_SSQ6 = df1['SSQ6.  Artan tükürük']
    Series_SSQ7 = df1['SSQ7. Terleme']
    Series_SSQ8 = df1['SSQ8. Mide bulantısı']
    Series_SSQ9 = df1['SSQ9. Konsantrasyon bozukluğu']
    Series_SSQ10 = df1['SSQ10. Baş dolgunluğu']
    Series_SSQ11 = df1['SSQ11. Bulanık görme']
    Series_SSQ12 = df1['SSQ12. Baş dönmesi (gözler açık)']
    Series_SSQ13 = df1['SSQ13. Baş dönmesi (gözler kapalı)']
    Series_SSQ14 = df1['SSQ14. Vertigo, kontrol kaybı']
    Series_SSQ15 = df1['SSQ15. Mide farkındalığı']
    Series_SSQ16 = df1['SSQ16. Geğirme']
    Series_TAM1 = df1['TAM1.  VR_Locomotion kullanmak, görevleri daha hızlı tamamlamamı sağladı.']
    Series_TAM2 = df1['TAM2.  VR_Locomotion kullanmak iş performansımı iyileştirdi.']
    Series_TAM3 = df1['TAM3.  VR_Locomotion kullanmak üretkenliğimi artırdı.']
    Series_TAM4 = df1['TAM4.  VR_Locomotion kullanmak etkinliğimi artırdı.']
    Series_TAM5 = df1['TAM5.  VR_Locomotion kullanmak, onunla yapmam gereken şeyleri yapmayı kolaylaştırdı.']
    Series_TAM6 = df1['TAM6. VR_Locomotion\'u faydalı buldum.']
    Series_TAM7 = df1['TAM7. VR_Locomotion\'u kullanmayı öğrenmek kolaydı.']
    Series_TAM8 = df1['TAM8. VR_Locomotion\'un yapmasını istediğim şeyi yapmasını kolay buldum.']
    Series_TAM9 = df1['TAM9. VR_Locomotion ile etkileşimim açık ve anlaşılırdı.']
    Series_TAM10 = df1['TAM 10. VR_Locomotion ile esnek bir etkileşim kurdum.']
    Series_TAM11 = df1['TAM11. VR_Locomotion kullanmakta ustalaşmak benim için kolaydı.']
    Series_TAM12 = df1['TAM12. VR_Locomotion\'un kullanımını kolay buldum.']
    Series_UMUX1 = df1['UMUX1.  VR_Locomotion\'ın yetenekleri gereksinimlerimi karşılıyor.']
    Series_UMUX2 = df1['UMUX2. VR_Locomotion\'u kullanmak sinir bozucu bir deneyimdir.']
    Series_UMUX3 = df1['UMUX3. VR_Locomotion\'un kullanımı kolaydır.']
    Series_UMUX4 = df1['UMUX4. VR_Locomotion ile bir şeyleri düzeltmek için çok fazla zaman harcamak zorundayım.']
    Series_VAS1 = df1['VAS1: (Kendi kendine hareket) Tüm vücudumun ileriye doğru hareket ettiğini hissettim.']
    Series_VAS2 = df1['VAS2: (Yürüme hissi) İleriye doğru yürüyormuş gibi hissettim.']
    Series_VAS3 = df1['VAS3: (Bacak hareketi) Ayaklarım yere çarpıyormuş gibi hissettim.']
    Series_VAS4 = df1[
        'VAS4 :  Olay yerinde varmışım gibi hissettim  (kişinin gerçek konumunun dışında bir yerde varmış gibi ' \
        'hissetmesi)  .']
    Series_email = df1['E-posta Adresi']

    timestamp = pd.Series(datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
    name_surname = pd.Series(entry2.get())
    age = pd.Series(entry3.get())
    education = pd.Series(entry4.get())
    vr = pd.Series(entry5.get())
    q1 = pd.Series(entry6.get())
    q2 = pd.Series(entry7.get())
    q3 = pd.Series(entry8.get())
    q4 = pd.Series(entry9.get())
    q5 = pd.Series(entry10.get())
    q6 = pd.Series(entry11.get())
    q7 = pd.Series(entry12.get())
    q8 = pd.Series(entry13.get())
    q9 = pd.Series(entry14.get())
    q10 = pd.Series(entry15.get())
    IPQ1 = pd.Series(entry16.get())
    IPQ2 = pd.Series(entry17.get())
    IPQ3 = pd.Series(entry18.get())
    IPQ4 = pd.Series(entry19.get())
    IPQ5 = pd.Series(entry20.get())
    IPQ6 = pd.Series(entry21.get())
    IPQ7 = pd.Series(entry22.get())
    IPQ8 = pd.Series(entry23.get())
    IPQ9 = pd.Series(entry24.get())
    IPQ10 = pd.Series(entry25.get())
    IPQ11 = pd.Series(entry26.get())
    IPQ12 = pd.Series(entry27.get())
    IPQ13 = pd.Series(entry28.get())
    IPQ14 = pd.Series(entry29.get())
    SSQ1 = pd.Series(entry30.get())
    SSQ2 = pd.Series(entry31.get())
    SSQ3 = pd.Series(entry32.get())
    SSQ4 = pd.Series(entry33.get())
    SSQ5 = pd.Series(entry34.get())
    SSQ6 = pd.Series(entry35.get())
    SSQ7 = pd.Series(entry36.get())
    SSQ8 = pd.Series(entry37.get())
    SSQ9 = pd.Series(entry38.get())
    SSQ10 = pd.Series(entry39.get())
    SSQ11 = pd.Series(entry40.get())
    SSQ12 = pd.Series(entry41.get())
    SSQ13 = pd.Series(entry42.get())
    SSQ14 = pd.Series(entry43.get())
    SSQ15 = pd.Series(entry44.get())
    SSQ16 = pd.Series(entry45.get())
    TAM1 = pd.Series(entry46.get())
    TAM2 = pd.Series(entry47.get())
    TAM3 = pd.Series(entry48.get())
    TAM4 = pd.Series(entry49.get())
    TAM5 = pd.Series(entry50.get())
    TAM6 = pd.Series(entry51.get())
    TAM7 = pd.Series(entry52.get())
    TAM8 = pd.Series(entry53.get())
    TAM9 = pd.Series(entry54.get())
    TAM10 = pd.Series(entry55.get())
    TAM11 = pd.Series(entry56.get())
    TAM12 = pd.Series(entry57.get())
    UMUX1 = pd.Series(entry58.get())
    UMUX2 = pd.Series(entry59.get())
    UMUX3 = pd.Series(entry60.get())
    UMUX4 = pd.Series(entry61.get())
    VAS1 = pd.Series(entry62.get())
    VAS2 = pd.Series(entry63.get())
    VAS3 = pd.Series(entry64.get())
    VAS4 = pd.Series(entry65.get())
    email = pd.Series(entry66.get())

    Series_timestamp = Series_timestamp.append(timestamp)
    Series_name_surname = Series_name_surname.append(name_surname)
    Series_age = Series_age.append(age)
    Series_education = Series_education.append(education)
    Series_vr = Series_vr.append(vr)
    Series_q1 = Series_q1.append(q1)
    Series_q2 = Series_q2.append(q2)
    Series_q3 = Series_q3.append(q3)
    Series_q4 = Series_q4.append(q4)
    Series_q5 = Series_q5.append(q5)
    Series_q6 = Series_q6.append(q6)
    Series_q7 = Series_q7.append(q7)
    Series_q8 = Series_q8.append(q8)
    Series_q9 = Series_q9.append(q9)
    Series_q10 = Series_q10.append(q10)
    Series_IPQ1 = Series_IPQ1.append(IPQ1)
    Series_IPQ2 = Series_IPQ2.append(IPQ2)
    Series_IPQ3 = Series_IPQ3.append(IPQ3)
    Series_IPQ4 = Series_IPQ4.append(IPQ4)
    Series_IPQ5 = Series_IPQ5.append(IPQ5)
    Series_IPQ6 = Series_IPQ6.append(IPQ6)
    Series_IPQ7 = Series_IPQ7.append(IPQ7)
    Series_IPQ8 = Series_IPQ8.append(IPQ8)
    Series_IPQ9 = Series_IPQ9.append(IPQ9)
    Series_IPQ10 = Series_IPQ10.append(IPQ10)
    Series_IPQ11 = Series_IPQ11.append(IPQ11)
    Series_IPQ12 = Series_IPQ12.append(IPQ12)
    Series_IPQ13 = Series_IPQ13.append(IPQ13)
    Series_IPQ14 = Series_IPQ14.append(IPQ14)
    Series_SSQ1 = Series_SSQ1.append(SSQ1)
    Series_SSQ2 = Series_SSQ2.append(SSQ2)
    Series_SSQ3 = Series_SSQ3.append(SSQ3)
    Series_SSQ4 = Series_SSQ4.append(SSQ4)
    Series_SSQ5 = Series_SSQ5.append(SSQ5)
    Series_SSQ6 = Series_SSQ6.append(SSQ6)
    Series_SSQ7 = Series_SSQ7.append(SSQ7)
    Series_SSQ8 = Series_SSQ8.append(SSQ8)
    Series_SSQ9 = Series_SSQ9.append(SSQ9)
    Series_SSQ10 = Series_SSQ10.append(SSQ10)
    Series_SSQ11 = Series_SSQ11.append(SSQ11)
    Series_SSQ12 = Series_SSQ12.append(SSQ12)
    Series_SSQ13 = Series_SSQ13.append(SSQ13)
    Series_SSQ14 = Series_SSQ14.append(SSQ14)
    Series_SSQ15 = Series_SSQ15.append(SSQ15)
    Series_SSQ16 = Series_SSQ16.append(SSQ16)
    Series_TAM1 = Series_TAM1.append(TAM1)
    Series_TAM2 = Series_TAM2.append(TAM2)
    Series_TAM3 = Series_TAM3.append(TAM3)
    Series_TAM4 = Series_TAM4.append(TAM4)
    Series_TAM5 = Series_TAM5.append(TAM5)
    Series_TAM6 = Series_TAM6.append(TAM6)
    Series_TAM7 = Series_TAM7.append(TAM7)
    Series_TAM8 = Series_TAM8.append(TAM8)
    Series_TAM9 = Series_TAM9.append(TAM9)
    Series_TAM10 = Series_TAM10.append(TAM10)
    Series_TAM11 = Series_TAM11.append(TAM11)
    Series_TAM12 = Series_TAM12.append(TAM12)
    Series_UMUX1 = Series_UMUX1.append(UMUX1)
    Series_UMUX2 = Series_UMUX2.append(UMUX2)
    Series_UMUX3 = Series_UMUX3.append(UMUX3)
    Series_UMUX4 = Series_UMUX4.append(UMUX4)
    Series_VAS1 = Series_VAS1.append(VAS1)
    Series_VAS2 = Series_VAS2.append(VAS2)
    Series_VAS3 = Series_VAS3.append(VAS3)
    Series_VAS4 = Series_VAS4.append(VAS4)
    Series_email = Series_email.append(email)

    df2 = pd.DataFrame({"Zaman damgası": Series_timestamp,
                        "Katılımcı Ad Soyad": Series_name_surname,
                        "Katılımcı Yaş": Series_age,
                        "Eğitim": Series_education,
                        "Önceden VR tecrübeniz var mıydı?": Series_vr,
                        "1. Bu sistemi sık sık kullanmak isterim.": Series_q1,
                        "2.  Bu sistemi gereksiz yere karmaşık buldum.": Series_q2,
                        "3.  Sistemin kullanımının kolay olduğunu düşündüm.": Series_q3,
                        "4.  Bu sistemi kullanabilmek için teknik bir kişinin desteğine ihtiyacım olacağını "
                        "düşünüyorum.": Series_q4,
                        "5.  Bu sistemdeki çeşitli fonksiyonların iyi bir şekilde entegre olduğunu gördüm.": Series_q5,
                        "6.  Bu sistemde çok fazla tutarsızlık olduğunu düşündüm.": Series_q6,
                        "7.  Çoğu insanın bu sistemi çok çabuk kullanmayı öğreneceğini hayal ediyorum.": Series_q7,
                        "8. Bu sistemi kullanmayı çok hantal (garip) buldum.": Series_q8,
                        "9.  Bu sistemi kullanırken kendimi çok güvende hissettim.": Series_q9,
                        "10.  Bu sisteme geçmeden önce çok şey öğrenmem gerekiyordu.": Series_q10,
                        "IPQ1.  Bilgisayar tarafından oluşturulan dünyada bir \"orada olma\" duygusuna sahiptim.": Series_IPQ1,
                        "IPQ2.   Bir şekilde sanal dünyanın etrafımı sardığını hissettim.": Series_IPQ2,
                        "IPQ3.  Sadece resimleri algılıyormuş gibi hissettim.": Series_IPQ3,
                        "IPQ4.  Sanal uzayda kendimi mevcut hissetmiyordum.": Series_IPQ4,
                        "IPQ5.  Dışarıdan bir şey çalıştırmak yerine sanal alanda hareket etme duygusu vardı.": Series_IPQ5,
                        "IPQ6.  Sanal uzayda kendimi mevcut (oradaymış gibi) hissettim.": Series_IPQ6,
                        "IPQ7.  Sanal dünyada gezinirken etrafınızdaki gerçek dünyanın ne kadar farkındaydınız? (yani "
                        "sesler, oda sıcaklığı, diğer insanlar vb.)?": Series_IPQ7,
                        "IPQ8.  Gerçek çevremin farkında değildim.": Series_IPQ8,
                        "IPQ9.  Yine de gerçek çevreye dikkat ettim.": Series_IPQ9,
                        "IPQ10.  Tamamen sanal dünyanın büyüsüne kapıldım.": Series_IPQ10,
                        "IPQ11.  Sanal dünya size ne kadar gerçek göründü?": Series_IPQ11,
                        "IPQ12.  Sanal ortamdaki deneyiminiz, gerçek dünya deneyiminizle ne kadar tutarlı görünüyordu?": Series_IPQ12,
                        "IPQ13.  Sanal dünya size ne kadar gerçek göründü?": Series_IPQ13,
                        "IPQ14.    Sanal dünya gerçek dünyadan daha gerçekçi görünüyordu.": Series_IPQ14,
                        "SSQ1.  Genel rahatsızlık": Series_SSQ1,
                        "SSQ2.  Tükenmişlik, yorgunluk": Series_SSQ2,
                        "SSQ3. Baş ağrısı": Series_SSQ3,
                        "SSQ4. Göz yorgunluğu": Series_SSQ4,
                        "SSQ5.  Odaklanma zorluğu": Series_SSQ5,
                        "SSQ6.  Artan tükürük": Series_SSQ6,
                        "SSQ7. Terleme": Series_SSQ7,
                        "SSQ8. Mide bulantısı": Series_SSQ8,
                        "SSQ9. Konsantrasyon bozukluğu": Series_SSQ9,
                        "SSQ10. Baş dolgunluğu": Series_SSQ10,
                        "SSQ11. Bulanık görme": Series_SSQ11,
                        "SSQ12. Baş dönmesi (gözler açık)": Series_SSQ12,
                        "SSQ13. Baş dönmesi (gözler kapalı)": Series_SSQ13,
                        "SSQ14. Vertigo, kontrol kaybı": Series_SSQ14,
                        "SSQ15. Mide farkındalığı": Series_SSQ15,
                        "SSQ16. Geğirme": Series_SSQ16,
                        "TAM1.  VR_Locomotion kullanmak, görevleri daha hızlı tamamlamamı sağladı.": Series_TAM1,
                        "TAM2.  VR_Locomotion kullanmak iş performansımı iyileştirdi.": Series_TAM2,
                        "TAM3.  VR_Locomotion kullanmak üretkenliğimi artırdı.": Series_TAM3,
                        "TAM4.  VR_Locomotion kullanmak etkinliğimi artırdı.": Series_TAM4,
                        "TAM5.  VR_Locomotion kullanmak, onunla yapmam gereken şeyleri yapmayı kolaylaştırdı.": Series_TAM5,
                        "TAM6. VR_Locomotion'u faydalı buldum.": Series_TAM6,
                        "TAM7. VR_Locomotion'u kullanmayı öğrenmek kolaydı.": Series_TAM7,
                        "TAM8. VR_Locomotion'un yapmasını istediğim şeyi yapmasını kolay buldum.": Series_TAM8,
                        "TAM9. VR_Locomotion ile etkileşimim açık ve anlaşılırdı.": Series_TAM9,
                        "TAM 10. VR_Locomotion ile esnek bir etkileşim kurdum.": Series_TAM10,
                        "TAM11. VR_Locomotion kullanmakta ustalaşmak benim için kolaydı.": Series_TAM11,
                        "TAM12. VR_Locomotion'un kullanımını kolay buldum.": Series_TAM12,
                        "UMUX1.  VR_Locomotion'ın yetenekleri gereksinimlerimi karşılıyor.": Series_UMUX1,
                        "UMUX2. VR_Locomotion'u kullanmak sinir bozucu bir deneyimdir.": Series_UMUX2,
                        "UMUX3. VR_Locomotion'un kullanımı kolaydır.": Series_UMUX3,
                        "UMUX4. VR_Locomotion ile bir şeyleri düzeltmek için çok fazla zaman harcamak zorundayım.": Series_UMUX4,
                        "VAS1: (Kendi kendine hareket) Tüm vücudumun ileriye doğru hareket ettiğini hissettim.": Series_VAS1,
                        "VAS2: (Yürüme hissi) İleriye doğru yürüyormuş gibi hissettim.": Series_VAS2,
                        "VAS3: (Bacak hareketi) Ayaklarım yere çarpıyormuş gibi hissettim.": Series_VAS3,
                        "VAS4 :  Olay yerinde varmışım gibi hissettim  (kişinin gerçek konumunun dışında bir yerde "
                        "varmış gibi hissetmesi)  .": Series_VAS4,
                        "E-posta Adresi": Series_email
                        })

    df2.to_excel(path, index=False)

    """
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    entry6.delete(0, END)
    entry7.delete(0, END)
    entry8.delete(0, END)
    entry9.delete(0, END)
    entry10.delete(0, END)
    entry11.delete(0, END)
    entry12.delete(0, END)
    entry13.delete(0, END)
    entry14.delete(0, END)
    entry15.delete(0, END)
    entry16.delete(0, END)
    entry17.delete(0, END)
    entry18.delete(0, END)
    entry19.delete(0, END)
    entry20.delete(0, END)
    entry21.delete(0, END)
    entry22.delete(0, END)
    entry23.delete(0, END)
    entry24.delete(0, END)
    entry25.delete(0, END)
    entry26.delete(0, END)
    entry27.delete(0, END)
    entry28.delete(0, END)
    entry29.delete(0, END)
    entry30.delete(0, END)
    entry31.delete(0, END)
    entry32.delete(0, END)
    entry33.delete(0, END)
    entry34.delete(0, END)
    entry35.delete(0, END)
    entry36.delete(0, END)
    entry37.delete(0, END)
    entry38.delete(0, END)
    entry39.delete(0, END)
    entry40.delete(0, END)
    entry41.delete(0, END)
    entry42.delete(0, END)
    entry43.delete(0, END)
    entry44.delete(0, END)
    entry45.delete(0, END)
    entry46.delete(0, END)
    entry47.delete(0, END)
    entry48.delete(0, END)
    entry49.delete(0, END)
    entry50.delete(0, END)
    entry51.delete(0, END)
    entry52.delete(0, END)
    entry53.delete(0, END)
    entry54.delete(0, END)
    entry55.delete(0, END)
    entry56.delete(0, END)
    entry57.delete(0, END)
    entry58.delete(0, END)
    entry59.delete(0, END)
    entry60.delete(0, END)
    entry61.delete(0, END)
    entry62.delete(0, END)
    entry63.delete(0, END)
    entry64.delete(0, END)
    entry65.delete(0, END)
    """


master = Tk()
master.title("Anket")
master.state('zoomed')

frame = tkinter.Frame(master)
frame.pack()


Label(frame, text="Katılımcı Ad Soyad").grid(row=1, column=0)
entry2 = Entry(frame)
entry2.grid(row=1, column=1)

Label(frame, text="Katılımcı Yaş").grid(row=2, column=0)
entry3 = Entry(frame)
entry3.grid(row=2, column=1)

Label(frame, text="Eğitim").grid(row=3, column=0)
entry4 = Entry(frame)
entry4.grid(row=3, column=1)

tkinter.Label(frame, text="Önceden VR tecrübeniz var mıydı?").grid(row=4, column=0)
entry5 = tkinter.StringVar()
tkinter.Radiobutton(frame, text="Var", variable=entry5, value="Var").grid(row=4, column=1)
tkinter.Radiobutton(frame, text="Yok", variable=entry5, value="Yok").grid(row=4, column=2)


def griding_questions(text, row, entry):
    tkinter.Label(frame, text=text).grid(row=row, column=0)
    tkinter.Radiobutton(frame, text="1", variable=entry, value=1).grid(row=row, column=1)
    tkinter.Radiobutton(frame, text="2", variable=entry, value=2).grid(row=row, column=2)
    tkinter.Radiobutton(frame, text="3", variable=entry, value=3).grid(row=row, column=3)
    tkinter.Radiobutton(frame, text="4", variable=entry, value=4).grid(row=row, column=4)
    tkinter.Radiobutton(frame, text="5", variable=entry, value=5).grid(row=row, column=5)


def griding_ipq_questions(text, row, entry):
    tkinter.Label(frame, text=text).grid(row=row, column=0)
    tkinter.Radiobutton(frame, text="1", variable=entry, value=1).grid(row=row, column=1)
    tkinter.Radiobutton(frame, text="2", variable=entry, value=2).grid(row=row, column=2)
    tkinter.Radiobutton(frame, text="3", variable=entry, value=3).grid(row=row, column=3)
    tkinter.Radiobutton(frame, text="4", variable=entry, value=4).grid(row=row, column=4)
    tkinter.Radiobutton(frame, text="5", variable=entry, value=5).grid(row=row, column=5)
    tkinter.Radiobutton(frame, text="6", variable=entry, value=6).grid(row=row, column=6)


def griding_ss_questions(text, row, entry):
    tkinter.Label(frame, text=text).grid(row=row, column=0)
    tkinter.Radiobutton(frame, text="Hiçbiri", variable=entry, value="Hiçbiri").grid(row=row, column=1)
    tkinter.Radiobutton(frame, text="Hafif", variable=entry, value="Hafif").grid(row=row, column=2)
    tkinter.Radiobutton(frame, text="Orta", variable=entry, value="Orta").grid(row=row, column=3)
    tkinter.Radiobutton(frame, text="Şiddetli", variable=entry, value="Şiddetli").grid(row=row, column=4)


def griding_tam_questions(text, row, entry):
    tkinter.Label(frame, text=text).grid(row=row, column=0)
    tkinter.Radiobutton(frame, text="1", variable=entry, value=1).grid(row=row, column=1)
    tkinter.Radiobutton(frame, text="2", variable=entry, value=2).grid(row=row, column=2)
    tkinter.Radiobutton(frame, text="3", variable=entry, value=3).grid(row=row, column=3)
    tkinter.Radiobutton(frame, text="4", variable=entry, value=4).grid(row=row, column=4)
    tkinter.Radiobutton(frame, text="5", variable=entry, value=5).grid(row=row, column=5)
    tkinter.Radiobutton(frame, text="6", variable=entry, value=6).grid(row=row, column=6)
    tkinter.Radiobutton(frame, text="7", variable=entry, value=7).grid(row=row, column=7)


def griding_vas_questions(text, row, entry):
    tkinter.Label(frame, text=text).grid(row=row, column=0)
    tkinter.Radiobutton(frame, text="1", variable=entry, value=1).grid(row=row, column=1)
    tkinter.Radiobutton(frame, text="2", variable=entry, value=2).grid(row=row, column=2)
    tkinter.Radiobutton(frame, text="3", variable=entry, value=3).grid(row=row, column=3)
    tkinter.Radiobutton(frame, text="4", variable=entry, value=4).grid(row=row, column=4)
    tkinter.Radiobutton(frame, text="5", variable=entry, value=5).grid(row=row, column=5)
    tkinter.Radiobutton(frame, text="6", variable=entry, value=6).grid(row=row, column=6)
    tkinter.Radiobutton(frame, text="7", variable=entry, value=7).grid(row=row, column=7)
    tkinter.Radiobutton(frame, text="8", variable=entry, value=8).grid(row=row, column=8)
    tkinter.Radiobutton(frame, text="9", variable=entry, value=9).grid(row=row, column=9)
    tkinter.Radiobutton(frame, text="10", variable=entry, value=10).grid(row=row, column=10)


entry6 = tkinter.IntVar()
griding_questions("1. Bu sistemi sık sık kullanmak isterim.", 5, entry6)

entry7 = tkinter.IntVar()
griding_questions("2.  Bu sistemi gereksiz yere karmaşık buldum.", 6, entry7)

entry8 = tkinter.IntVar()
griding_questions("3.  Sistemin kullanımının kolay olduğunu düşündüm.", 7, entry8)

entry9 = tkinter.IntVar()
griding_questions("4.  Bu sistemi kullanabilmek için teknik bir kişinin desteğine ihtiyacım olacağını düşünüyorum.", 8,
                  entry9)

entry10 = tkinter.IntVar()
griding_questions("5.  Bu sistemdeki çeşitli fonksiyonların iyi bir şekilde entegre olduğunu gördüm.", 9, entry10)

entry11 = tkinter.IntVar()
griding_questions("6.  Bu sistemde çok fazla tutarsızlık olduğunu düşündüm.", 10, entry11)

entry12 = tkinter.IntVar()
griding_questions("7.  Çoğu insanın bu sistemi çok çabuk kullanmayı öğreneceğini hayal ediyorum.", 11, entry12)

entry13 = tkinter.IntVar()
griding_questions("8. Bu sistemi kullanmayı çok hantal (garip) buldum.", 12, entry13)

entry14 = tkinter.IntVar()
griding_questions("9.  Bu sistemi kullanırken kendimi çok güvende hissettim.", 13, entry14)

entry15 = tkinter.IntVar()
griding_questions("10.  Bu sisteme geçmeden önce çok şey öğrenmem gerekiyordu.", 14, entry15)

entry16 = tkinter.IntVar()
griding_ipq_questions("IPQ1.  Bilgisayar tarafından oluşturulan dünyada bir \"orada olma\" duygusuna sahiptim.", 15,
                      entry16)

entry17 = tkinter.IntVar()
griding_ipq_questions("IPQ2.   Bir şekilde sanal dünyanın etrafımı sardığını hissettim.", 16, entry17)

entry18 = tkinter.IntVar()
griding_ipq_questions("IPQ3.  Sadece resimleri algılıyormuş gibi hissettim.", 17, entry18)

entry19 = tkinter.IntVar()
griding_ipq_questions("IPQ4.  Sanal uzayda kendimi mevcut hissetmiyordum.", 18, entry19)

entry20 = tkinter.IntVar()
griding_ipq_questions("IPQ5.  Dışarıdan bir şey çalıştırmak yerine sanal alanda hareket etme duygusu vardı.", 19,
                      entry20)

entry21 = tkinter.IntVar()
griding_ipq_questions("IPQ6.  Sanal uzayda kendimi mevcut (oradaymış gibi) hissettim.", 20, entry21)

entry22 = tkinter.IntVar()
griding_ipq_questions(
    "IPQ7.  Sanal dünyada gezinirken etrafınızdaki gerçek dünyanın ne kadar farkındaydınız? (yani sesler, oda sıcaklığı, diğer insanlar vb.)?",
    21, entry22)

entry23 = tkinter.IntVar()
griding_ipq_questions("IPQ8.  Gerçek çevremin farkında değildim.", 22, entry23)

entry24 = tkinter.IntVar()
griding_ipq_questions("IPQ9.  Yine de gerçek çevreye dikkat ettim.", 23, entry24)

entry25 = tkinter.IntVar()
griding_ipq_questions("IPQ10.  Tamamen sanal dünyanın büyüsüne kapıldım.", 24, entry25)

entry26 = tkinter.IntVar()
griding_ipq_questions("IPQ11.  Sanal dünya size ne kadar gerçek göründü?", 25, entry26)

entry27 = tkinter.IntVar()
griding_ipq_questions("IPQ12.  Sanal ortamdaki deneyiminiz, gerçek dünya deneyiminizle ne kadar tutarlı görünüyordu?",
                      26, entry27)

entry28 = tkinter.IntVar()
griding_ipq_questions("IPQ13.  Sanal dünya size ne kadar gerçek göründü?", 27, entry28)

entry29 = tkinter.IntVar()
griding_ipq_questions("IPQ14.    Sanal dünya gerçek dünyadan daha gerçekçi görünüyordu.", 28, entry29)

entry30 = tkinter.StringVar()
griding_ss_questions("SSQ1.  Genel rahatsızlık", 29, entry30)

entry31 = tkinter.StringVar()
griding_ss_questions("SSQ2.  Tükenmişlik, yorgunluk", 30, entry31)

entry32 = tkinter.StringVar()
griding_ss_questions("SSQ3. Baş ağrısı", 31, entry32)

entry33 = tkinter.StringVar()
griding_ss_questions("SSQ4. Göz yorgunluğu", 32, entry33)

entry34 = tkinter.StringVar()
griding_ss_questions("SSQ5.  Odaklanma zorluğu", 33, entry34)

entry35 = tkinter.StringVar()
griding_ss_questions("SSQ6.  Artan tükürük", 34, entry35)

entry36 = tkinter.StringVar()
griding_ss_questions("SSQ7. Terleme", 35, entry36)

entry37 = tkinter.StringVar()
griding_ss_questions("SSQ8. Mide bulantısı", 36, entry37)

entry38 = tkinter.StringVar()
griding_ss_questions("SSQ9. Konsantrasyon bozukluğu", 37, entry38)

entry39 = tkinter.StringVar()
griding_ss_questions("SSQ10. Baş dolgunluğu", 38, entry39)

entry40 = tkinter.StringVar()
griding_ss_questions("SSQ11. Bulanık görme", 39, entry40)

entry41 = tkinter.StringVar()
griding_ss_questions("SSQ12. Baş dönmesi (gözler açık)", 40, entry41)

entry42 = tkinter.StringVar()
griding_ss_questions("SSQ13. Baş dönmesi (gözler kapalı)", 41, entry42)

entry43 = tkinter.StringVar()
griding_ss_questions("SSQ14. Vertigo, kontrol kaybı", 42, entry43)

entry44 = tkinter.StringVar()
griding_ss_questions("SSQ15. Mide farkındalığı", 43, entry44)

entry45 = tkinter.StringVar()
griding_ss_questions("SSQ16. Geğirme", 44, entry45)

entry46 = tkinter.IntVar()
griding_tam_questions("TAM1.  VR_Locomotion kullanmak, görevleri daha hızlı tamamlamamı sağladı.", 45, entry46)

entry47 = tkinter.IntVar()
griding_tam_questions("TAM2.  VR_Locomotion kullanmak iş performansımı iyileştirdi.", 46, entry47)

entry48 = tkinter.IntVar()
griding_tam_questions("TAM3.  VR_Locomotion kullanmak üretkenliğimi artırdı.", 47, entry48)

entry49 = tkinter.IntVar()
griding_tam_questions("TAM4.  VR_Locomotion kullanmak etkinliğimi artırdı.", 48, entry49)

entry50 = tkinter.IntVar()
griding_tam_questions("TAM5.  VR_Locomotion kullanmak, onunla yapmam gereken şeyleri yapmayı kolaylaştırdı.", 49,
                      entry50)

entry51 = tkinter.IntVar()
griding_tam_questions("TAM6. VR_Locomotion'u faydalı buldum.", 50, entry51)

entry52 = tkinter.IntVar()
griding_tam_questions("TAM7. VR_Locomotion'u kullanmayı öğrenmek kolaydı.", 51, entry52)

entry53 = tkinter.IntVar()
griding_tam_questions("TAM8. VR_Locomotion'un yapmasını istediğim şeyi yapmasını kolay buldum.", 52, entry53)

entry54 = tkinter.IntVar()
griding_tam_questions("TAM9. VR_Locomotion ile etkileşimim açık ve anlaşılırdı.", 53, entry54)

entry55 = tkinter.IntVar()
griding_tam_questions("TAM 10. VR_Locomotion ile esnek bir etkileşim kurdum.", 54, entry55)

entry56 = tkinter.IntVar()
griding_tam_questions("TAM11. VR_Locomotion kullanmakta ustalaşmak benim için kolaydı.", 55, entry56)

entry57 = tkinter.IntVar()
griding_tam_questions("TAM12. VR_Locomotion'un kullanımını kolay buldum.", 56, entry57)

entry58 = tkinter.IntVar()
griding_tam_questions("UMUX1.  VR_Locomotion'ın yetenekleri gereksinimlerimi karşılıyor.", 57, entry58)

entry59 = tkinter.IntVar()
griding_tam_questions("UMUX2. VR_Locomotion'u kullanmak sinir bozucu bir deneyimdir.", 58, entry59)

entry60 = tkinter.IntVar()
griding_tam_questions("UMUX3. VR_Locomotion'un kullanımı kolaydır.", 59, entry60)

entry61 = tkinter.IntVar()
griding_tam_questions("UMUX4. VR_Locomotion ile bir şeyleri düzeltmek için çok fazla zaman harcamak zorundayım.", 60,
                      entry61)

entry62 = tkinter.IntVar()
griding_vas_questions("VAS1: (Kendi kendine hareket) Tüm vücudumun ileriye doğru hareket ettiğini hissettim.", 61,
                      entry62)

entry63 = tkinter.IntVar()
griding_vas_questions("VAS2: (Yürüme hissi) İleriye doğru yürüyormuş gibi hissettim.", 62, entry63)

entry64 = tkinter.IntVar()
griding_vas_questions("VAS3: (Bacak hareketi) Ayaklarım yere çarpıyormuş gibi hissettim.", 63, entry64)

entry65 = tkinter.IntVar()
griding_vas_questions(
    "VAS4 :  Olay yerinde varmışım gibi hissettim  (kişinin gerçek konumunun dışında bir yerde varmış gibi "
    "hissetmesi)  .",
    64, entry65)

Label(frame, text="E-posta Adresi").grid(row=65, column=0)
entry66 = Entry(frame)
entry66.grid(row=65, column=1)

Button(frame, text='Quit', command=frame.quit).grid(row=5, column=15, pady=4)
Button(frame, text='Submit', command=submit_fields).grid(row=8, column=15, pady=4)

mainloop()
