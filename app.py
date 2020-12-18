import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]
creds = ServiceAccountCredentials.from_json_keyfile_name(
    "bayes-17e255d53554.json", scope
)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("siswa").sheet1

namaIndex = [
    "X1_Jenis_Kelamin",
    "X2_Nilai_Rerata",
    "X3_Mengikuti_Ekstrakurikuler",
    "X4_Ikut_Bekerja",
    "X5_Mengalami_Broken_Home",
    "X6_Jarak_Sekolah",
    "X7_Pendidikan_Ayah",
    "X8_Pendidikan_Ibu",
    "X9_Penghasilan_Ayah",
    "X10_Penghasilan_Ibu",
    "Class_Putus",
]

# Extract and print all of the values
list_of_hashes = sheet.get_all_records()
print(type(list_of_hashes))
df = pd.DataFrame(list_of_hashes, columns=namaIndex)
totalValue = df.shape[0]
print(totalValue)

# X3 Mengikuti Ekstrakurikuler
hitung1 = df[
    (df["X6_Jarak_Sekolah"] == "Dekat_1")
    & (df["X5_Mengalami_Broken_Home"] == "Tidak_0")
    & (df["X4_Ikut_Bekerja"] == "Tidak_0")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Tidak_0")
].shape[0]
hitung2 = df[
    (df["X6_Jarak_Sekolah"] == "Dekat_1")
    & (df["X5_Mengalami_Broken_Home"] == "Tidak_0")
    & (df["X4_Ikut_Bekerja"] == "Tidak_0")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Iya_1")
].shape[0]
hitung3 = df[
    (df["X6_Jarak_Sekolah"] == "Dekat_1")
    & (df["X5_Mengalami_Broken_Home"] == "Tidak_0")
    & (df["X4_Ikut_Bekerja"] == "Iya_1")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Tidak_0")
].shape[0]
hitung4 = df[
    (df["X6_Jarak_Sekolah"] == "Dekat_1")
    & (df["X5_Mengalami_Broken_Home"] == "Tidak_0")
    & (df["X4_Ikut_Bekerja"] == "Iya_1")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Iya_1")
].shape[0]
hitung5 = df[
    (df["X6_Jarak_Sekolah"] == "Dekat_1")
    & (df["X5_Mengalami_Broken_Home"] == "Iya_1")
    & (df["X4_Ikut_Bekerja"] == "Tidak_0")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Tidak_0")
].shape[0]
hitung6 = df[
    (df["X6_Jarak_Sekolah"] == "Dekat_1")
    & (df["X5_Mengalami_Broken_Home"] == "Iya_1")
    & (df["X4_Ikut_Bekerja"] == "Tidak_0")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Iya_1")
].shape[0]
hitung7 = df[
    (df["X6_Jarak_Sekolah"] == "Dekat_1")
    & (df["X5_Mengalami_Broken_Home"] == "Iya_1")
    & (df["X4_Ikut_Bekerja"] == "Iya_1")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Tidak_0")
].shape[0]
hitung8 = df[
    (df["X6_Jarak_Sekolah"] == "Dekat_1")
    & (df["X5_Mengalami_Broken_Home"] == "Iya_1")
    & (df["X4_Ikut_Bekerja"] == "Iya_1")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Iya_1")
].shape[0]
#
hitung9 = df[
    (df["X6_Jarak_Sekolah"] == "Sedang_2")
    & (df["X5_Mengalami_Broken_Home"] == "Tidak_0")
    & (df["X4_Ikut_Bekerja"] == "Tidak_0")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Tidak_0")
].shape[0]
hitung10 = df[
    (df["X6_Jarak_Sekolah"] == "Sedang_2")
    & (df["X5_Mengalami_Broken_Home"] == "Tidak_0")
    & (df["X4_Ikut_Bekerja"] == "Tidak_0")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Iya_1")
].shape[0]
hitung11 = df[
    (df["X6_Jarak_Sekolah"] == "Sedang_2")
    & (df["X5_Mengalami_Broken_Home"] == "Tidak_0")
    & (df["X4_Ikut_Bekerja"] == "Iya_1")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Tidak_0")
].shape[0]
hitung12 = df[
    (df["X6_Jarak_Sekolah"] == "Sedang_2")
    & (df["X5_Mengalami_Broken_Home"] == "Tidak_0")
    & (df["X4_Ikut_Bekerja"] == "Iya_1")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Iya_1")
].shape[0]
hitung13 = df[
    (df["X6_Jarak_Sekolah"] == "Sedang_2")
    & (df["X5_Mengalami_Broken_Home"] == "Iya_1")
    & (df["X4_Ikut_Bekerja"] == "Tidak_0")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Tidak_0")
].shape[0]
hitung14 = df[
    (df["X6_Jarak_Sekolah"] == "Sedang_2")
    & (df["X5_Mengalami_Broken_Home"] == "Iya_1")
    & (df["X4_Ikut_Bekerja"] == "Tidak_0")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Iya_1")
].shape[0]
hitung15 = df[
    (df["X6_Jarak_Sekolah"] == "Sedang_2")
    & (df["X5_Mengalami_Broken_Home"] == "Iya_1")
    & (df["X4_Ikut_Bekerja"] == "Iya_1")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Tidak_0")
].shape[0]
hitung16 = df[
    (df["X6_Jarak_Sekolah"] == "Sedang_2")
    & (df["X5_Mengalami_Broken_Home"] == "Iya_1")
    & (df["X4_Ikut_Bekerja"] == "Iya_1")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Iya_1")
].shape[0]
#
hitung17 = df[
    (df["X6_Jarak_Sekolah"] == "Jauh_3")
    & (df["X5_Mengalami_Broken_Home"] == "Tidak_0")
    & (df["X4_Ikut_Bekerja"] == "Tidak_0")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Tidak_0")
].shape[0]
hitung18 = df[
    (df["X6_Jarak_Sekolah"] == "Jauh_3")
    & (df["X5_Mengalami_Broken_Home"] == "Tidak_0")
    & (df["X4_Ikut_Bekerja"] == "Tidak_0")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Iya_1")
].shape[0]
hitung19 = df[
    (df["X6_Jarak_Sekolah"] == "Jauh_3")
    & (df["X5_Mengalami_Broken_Home"] == "Tidak_0")
    & (df["X4_Ikut_Bekerja"] == "Iya_1")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Tidak_0")
].shape[0]
hitung20 = df[
    (df["X6_Jarak_Sekolah"] == "Jauh_3")
    & (df["X5_Mengalami_Broken_Home"] == "Tidak_0")
    & (df["X4_Ikut_Bekerja"] == "Iya_1")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Iya_1")
].shape[0]
hitung21 = df[
    (df["X6_Jarak_Sekolah"] == "Jauh_3")
    & (df["X5_Mengalami_Broken_Home"] == "Iya_1")
    & (df["X4_Ikut_Bekerja"] == "Tidak_0")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Tidak_0")
].shape[0]
hitung22 = df[
    (df["X6_Jarak_Sekolah"] == "Jauh_3")
    & (df["X5_Mengalami_Broken_Home"] == "Iya_1")
    & (df["X4_Ikut_Bekerja"] == "Tidak_0")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Iya_1")
].shape[0]
hitung23 = df[
    (df["X6_Jarak_Sekolah"] == "Jauh_3")
    & (df["X5_Mengalami_Broken_Home"] == "Iya_1")
    & (df["X4_Ikut_Bekerja"] == "Iya_1")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Tidak_0")
].shape[0]
hitung24 = df[
    (df["X6_Jarak_Sekolah"] == "Jauh_3")
    & (df["X5_Mengalami_Broken_Home"] == "Iya_1")
    & (df["X4_Ikut_Bekerja"] == "Iya_1")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Iya_1")
].shape[0]

if hitung1 == 0 or hitung2 == 0:
    hitung1 += 1
    hitung2 += 1
if hitung3 == 0 or hitung4 == 0:
    hitung3 += 1
    hitung4 += 1
if hitung5 == 0 or hitung6 == 0:
    hitung5 += 1
    hitung6 += 1
if hitung7 == 0 or hitung8 == 0:
    hitung7 += 1
    hitung8 += 1
if hitung9 == 0 or hitung10 == 0:
    hitung9 += 1
    hitung10 += 1
if hitung11 == 0 or hitung12 == 0:
    hitung11 += 1
    hitung12 += 1
if hitung13 == 0 or hitung14 == 0:
    hitung13 += 1
    hitung14 += 1
if hitung15 == 0 or hitung16 == 0:
    hitung15 += 1
    hitung16 += 1
if hitung17 == 0 or hitung18 == 0:
    hitung17 += 1
    hitung18 += 1
if hitung19 == 0 or hitung20 == 0:
    hitung19 += 1
    hitung20 += 1
if hitung21 == 0 or hitung22 == 0:
    hitung21 += 1
    hitung22 += 1
if hitung23 == 0 or hitung24 == 0:
    hitung23 += 1
    hitung24 += 1

data1 = hitung1 / (hitung1 + hitung2)
data2 = hitung2 / (hitung1 + hitung2)
data3 = hitung3 / (hitung3 + hitung4)
data4 = hitung4 / (hitung3 + hitung4)
data5 = hitung5 / (hitung5 + hitung6)
data6 = hitung6 / (hitung5 + hitung6)
data7 = hitung7 / (hitung7 + hitung8)
data8 = hitung8 / (hitung7 + hitung8)
data9 = hitung9 / (hitung9 + hitung10)
data10 = hitung10 / (hitung9 + hitung10)
data11 = hitung11 / (hitung11 + hitung12)
data12 = hitung12 / (hitung11 + hitung12)
data13 = hitung13 / (hitung13 + hitung14)
data14 = hitung14 / (hitung13 + hitung14)
data15 = hitung15 / (hitung15 + hitung16)
data16 = hitung16 / (hitung15 + hitung16)
data17 = hitung17 / (hitung17 + hitung18)
data18 = hitung18 / (hitung17 + hitung18)
data19 = hitung19 / (hitung19 + hitung20)
data20 = hitung20 / (hitung19 + hitung20)
data21 = hitung21 / (hitung21 + hitung22)
data22 = hitung22 / (hitung21 + hitung22)
data23 = hitung23 / (hitung23 + hitung24)
data24 = hitung24 / (hitung23 + hitung24)

# Class Putus
hitung1 = df[
    (df["X9_Penghasilan_Ayah"] == "Tidak_Bekerja_1")
    & (df["X2_Nilai_Rerata"] == "C_1")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Tidak_0")
    & (df["Class_Putus"] == "Tidak_0")
].shape[0]
hitung2 = df[
    (df["X9_Penghasilan_Ayah"] == "Tidak_Bekerja_1")
    & (df["X2_Nilai_Rerata"] == "C_1")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Tidak_0")
    & (df["Class_Putus"] == "Iya_1")
].shape[0]
hitung3 = df[
    (df["X9_Penghasilan_Ayah"] == "Tidak_Bekerja_1")
    & (df["X2_Nilai_Rerata"] == "C_1")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Iya_1")
    & (df["Class_Putus"] == "Tidak_0")
].shape[0]
hitung4 = df[
    (df["X9_Penghasilan_Ayah"] == "Tidak_Bekerja_1")
    & (df["X2_Nilai_Rerata"] == "C_1")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Iya_1")
    & (df["Class_Putus"] == "Iya_1")
].shape[0]
hitung5 = df[
    (df["X9_Penghasilan_Ayah"] == "Tidak_Bekerja_1")
    & (df["X2_Nilai_Rerata"] == "B_2")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Tidak_0")
    & (df["Class_Putus"] == "Tidak_0")
].shape[0]
hitung6 = df[
    (df["X9_Penghasilan_Ayah"] == "Tidak_Bekerja_1")
    & (df["X2_Nilai_Rerata"] == "B_2")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Tidak_0")
    & (df["Class_Putus"] == "Iya_1")
].shape[0]
hitung7 = df[
    (df["X9_Penghasilan_Ayah"] == "Tidak_Bekerja_1")
    & (df["X2_Nilai_Rerata"] == "B_2")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Iya_1")
    & (df["Class_Putus"] == "Tidak_0")
].shape[0]
hitung8 = df[
    (df["X9_Penghasilan_Ayah"] == "Tidak_Bekerja_1")
    & (df["X2_Nilai_Rerata"] == "B_2")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Iya_1")
    & (df["Class_Putus"] == "Iya_1")
].shape[0]
#
hitung9 = df[
    (df["X9_Penghasilan_Ayah"] == "Rendah_2")
    & (df["X2_Nilai_Rerata"] == "C_1")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Tidak_0")
    & (df["Class_Putus"] == "Tidak_0")
].shape[0]
hitung10 = df[
    (df["X9_Penghasilan_Ayah"] == "Rendah_2")
    & (df["X2_Nilai_Rerata"] == "C_1")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Tidak_0")
    & (df["Class_Putus"] == "Iya_1")
].shape[0]
hitung11 = df[
    (df["X9_Penghasilan_Ayah"] == "Rendah_2")
    & (df["X2_Nilai_Rerata"] == "C_1")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Iya_1")
    & (df["Class_Putus"] == "Tidak_0")
].shape[0]
hitung12 = df[
    (df["X9_Penghasilan_Ayah"] == "Rendah_2")
    & (df["X2_Nilai_Rerata"] == "C_1")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Iya_1")
    & (df["Class_Putus"] == "Iya_1")
].shape[0]
hitung13 = df[
    (df["X9_Penghasilan_Ayah"] == "Rendah_2")
    & (df["X2_Nilai_Rerata"] == "B_2")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Tidak_0")
    & (df["Class_Putus"] == "Tidak_0")
].shape[0]
hitung14 = df[
    (df["X9_Penghasilan_Ayah"] == "Rendah_2")
    & (df["X2_Nilai_Rerata"] == "B_2")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Tidak_0")
    & (df["Class_Putus"] == "Iya_1")
].shape[0]
hitung15 = df[
    (df["X9_Penghasilan_Ayah"] == "Rendah_2")
    & (df["X2_Nilai_Rerata"] == "B_2")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Iya_1")
    & (df["Class_Putus"] == "Tidak_0")
].shape[0]
hitung16 = df[
    (df["X9_Penghasilan_Ayah"] == "Rendah_2")
    & (df["X2_Nilai_Rerata"] == "B_2")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Iya_1")
    & (df["Class_Putus"] == "Iya_1")
].shape[0]
#
hitung17 = df[
    (df["X9_Penghasilan_Ayah"] == "Sedang_3")
    & (df["X2_Nilai_Rerata"] == "C_1")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Tidak_0")
    & (df["Class_Putus"] == "Tidak_0")
].shape[0]
hitung18 = df[
    (df["X9_Penghasilan_Ayah"] == "Sedang_3")
    & (df["X2_Nilai_Rerata"] == "C_1")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Tidak_0")
    & (df["Class_Putus"] == "Iya_1")
].shape[0]
hitung19 = df[
    (df["X9_Penghasilan_Ayah"] == "Sedang_3")
    & (df["X2_Nilai_Rerata"] == "C_1")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Iya_1")
    & (df["Class_Putus"] == "Tidak_0")
].shape[0]
hitung20 = df[
    (df["X9_Penghasilan_Ayah"] == "Sedang_3")
    & (df["X2_Nilai_Rerata"] == "C_1")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Iya_1")
    & (df["Class_Putus"] == "Iya_1")
].shape[0]
hitung21 = df[
    (df["X9_Penghasilan_Ayah"] == "Sedang_3")
    & (df["X2_Nilai_Rerata"] == "B_2")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Tidak_0")
    & (df["Class_Putus"] == "Tidak_0")
].shape[0]
hitung22 = df[
    (df["X9_Penghasilan_Ayah"] == "Sedang_3")
    & (df["X2_Nilai_Rerata"] == "B_2")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Tidak_0")
    & (df["Class_Putus"] == "Iya_1")
].shape[0]
hitung23 = df[
    (df["X9_Penghasilan_Ayah"] == "Sedang_3")
    & (df["X2_Nilai_Rerata"] == "B_2")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Iya_1")
    & (df["Class_Putus"] == "Tidak_0")
].shape[0]
hitung24 = df[
    (df["X9_Penghasilan_Ayah"] == "Sedang_3")
    & (df["X2_Nilai_Rerata"] == "B_2")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Iya_1")
    & (df["Class_Putus"] == "Iya_1")
].shape[0]
#
hitung25 = df[
    (df["X9_Penghasilan_Ayah"] == "Tinggi_4")
    & (df["X2_Nilai_Rerata"] == "C_1")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Tidak_0")
    & (df["Class_Putus"] == "Tidak_0")
].shape[0]
hitung26 = df[
    (df["X9_Penghasilan_Ayah"] == "Tinggi_4")
    & (df["X2_Nilai_Rerata"] == "C_1")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Tidak_0")
    & (df["Class_Putus"] == "Iya_1")
].shape[0]
hitung27 = df[
    (df["X9_Penghasilan_Ayah"] == "Tinggi_4")
    & (df["X2_Nilai_Rerata"] == "C_1")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Iya_1")
    & (df["Class_Putus"] == "Tidak_0")
].shape[0]
hitung28 = df[
    (df["X9_Penghasilan_Ayah"] == "Tinggi_4")
    & (df["X2_Nilai_Rerata"] == "C_1")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Iya_1")
    & (df["Class_Putus"] == "Iya_1")
].shape[0]
hitung29 = df[
    (df["X9_Penghasilan_Ayah"] == "Tinggi_4")
    & (df["X2_Nilai_Rerata"] == "B_2")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Tidak_0")
    & (df["Class_Putus"] == "Tidak_0")
].shape[0]
hitung30 = df[
    (df["X9_Penghasilan_Ayah"] == "Tinggi_4")
    & (df["X2_Nilai_Rerata"] == "B_2")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Tidak_0")
    & (df["Class_Putus"] == "Iya_1")
].shape[0]
hitung31 = df[
    (df["X9_Penghasilan_Ayah"] == "Tinggi_4")
    & (df["X2_Nilai_Rerata"] == "B_2")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Iya_1")
    & (df["Class_Putus"] == "Tidak_0")
].shape[0]
hitung32 = df[
    (df["X9_Penghasilan_Ayah"] == "Tinggi_4")
    & (df["X2_Nilai_Rerata"] == "B_2")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Iya_1")
    & (df["Class_Putus"] == "Iya_1")
].shape[0]

if hitung1 == 0 or hitung2 == 0:
    hitung1 += 1
    hitung2 += 1
if hitung3 == 0 or hitung4 == 0:
    hitung3 += 1
    hitung4 += 1
if hitung5 == 0 or hitung6 == 0:
    hitung5 += 1
    hitung6 += 1
if hitung7 == 0 or hitung8 == 0:
    hitung7 += 1
    hitung8 += 1
if hitung9 == 0 or hitung10 == 0:
    hitung9 += 1
    hitung10 += 1
if hitung11 == 0 or hitung12 == 0:
    hitung11 += 1
    hitung12 += 1
if hitung13 == 0 or hitung14 == 0:
    hitung13 += 1
    hitung14 += 1
if hitung15 == 0 or hitung16 == 0:
    hitung15 += 1
    hitung16 += 1
if hitung17 == 0 or hitung18 == 0:
    hitung17 += 1
    hitung18 += 1
if hitung19 == 0 or hitung20 == 0:
    hitung19 += 1
    hitung20 += 1
if hitung21 == 0 or hitung22 == 0:
    hitung21 += 1
    hitung22 += 1
if hitung23 == 0 or hitung24 == 0:
    hitung23 += 1
    hitung24 += 1
if hitung25 == 0 or hitung26 == 0:
    hitung25 += 1
    hitung26 += 1
if hitung27 == 0 or hitung28 == 0:
    hitung27 += 1
    hitung28 += 1
if hitung29 == 0 or hitung30 == 0:
    hitung29 += 1
    hitung30 += 1
if hitung31 == 0 or hitung32 == 0:
    hitung31 += 1
    hitung32 += 1

data1 = hitung1 / (hitung1 + hitung2)
data2 = hitung2 / (hitung1 + hitung2)
data3 = hitung3 / (hitung3 + hitung4)
data4 = hitung4 / (hitung3 + hitung4)
data5 = hitung5 / (hitung5 + hitung6)
data6 = hitung6 / (hitung5 + hitung6)
data7 = hitung7 / (hitung7 + hitung8)
data8 = hitung8 / (hitung7 + hitung8)
data9 = hitung9 / (hitung9 + hitung10)
data10 = hitung10 / (hitung9 + hitung10)
data11 = hitung11 / (hitung11 + hitung12)
data12 = hitung12 / (hitung11 + hitung12)
data13 = hitung13 / (hitung13 + hitung14)
data14 = hitung14 / (hitung13 + hitung14)
data15 = hitung15 / (hitung15 + hitung16)
data16 = hitung16 / (hitung15 + hitung16)
data17 = hitung17 / (hitung17 + hitung18)
data18 = hitung18 / (hitung17 + hitung18)
data19 = hitung19 / (hitung19 + hitung20)
data20 = hitung20 / (hitung19 + hitung20)
data21 = hitung21 / (hitung21 + hitung22)
data22 = hitung22 / (hitung21 + hitung22)
data23 = hitung23 / (hitung23 + hitung24)
data24 = hitung24 / (hitung23 + hitung24)
data25 = hitung25 / (hitung25 + hitung26)
data26 = hitung26 / (hitung25 + hitung26)
data27 = hitung27 / (hitung27 + hitung28)
data28 = hitung28 / (hitung27 + hitung28)
data29 = hitung29 / (hitung29 + hitung30)
data30 = hitung30 / (hitung29 + hitung30)
data31 = hitung31 / (hitung31 + hitung32)
data32 = hitung32 / (hitung31 + hitung32)

namaIndex = [
    "X1_Jenis_Kelamin",
    "X2_Nilai_Rerata",
    "X3_Mengikuti_Ekstrakurikuler",
    "X4_Ikut_Bekerja",
    "X5_Mengalami_Broken_Home",
    "X6_Jarak_Sekolah",
    "X7_Pendidikan_Ayah",
    "X8_Pendidikan_Ibu",
    "X9_Penghasilan_Ayah",
    "X10_Penghasilan_Ibu",
    "Class_Putus",
]


import streamlit as st
import numpy as np

st.title("Sistem Prediksi Putus Sekolah")

st.write("Sistem Prediksi Siswa Putus Sekolah SMA Islam Al Wahid Kepung")

dataset_name = st.sidebar.selectbox(
    "Pilih Menu", ("Tentang Sistem", "Prediksi Perorangan", "Prediksi Berkelompok")
)

st.write(f"## {dataset_name}")


def get_table_download_link(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(
        csv.encode()
    ).decode()  # some strings <-> bytes conversions necessary here
    return f'<a href="data:file/csv;base64,{b64}" download="prediksiSiswa.csv">Unduh file .csv</a>'


if dataset_name == "Tentang Sistem":
    st.write(
        "Sistem prediksi merupakan sebuah sistem yang digunakan untuk melakukan prediksi siswa yang berpotensi mengalami putus sekolah khususnya di SMA Islam Al Wahid."
    )
    st.write("Atribut yang digunakan antara lain")
    st.write("1. Jenis Kelamin")
    st.write("2. Nilai Rerata")
    st.write("3. Ketertarika Mengikuti Ekstrakurikuler")
    st.write("4. Ikut Bekerja")
    st.write("5. Mengalami Masalah Keluarga")
    st.write("6. Jarak ke Sekolah")
    st.write("7. Pendidikan Terakhir Ayah")
    st.write("8. Pendidikan Terakhir Ibu")
    st.write("9. Penghasilan Ayah")
    st.write("10. Penghasilan Ibu")
    st.text("")
    st.write(
        "Kemampuan sistem prediksi dapat terus diperbarui dengan cara mengakses spreadsheet yang sudah disediakan pada tautan berikut : https://docs.google.com/spreadsheets/d/1-_ouhVDZD9OO-Wm3PK_aclvIvZLiy2K_C66k81tbvIQ/edit?usp=sharing"
    )
    st.write("Silakan gunakan akun email sekolahan yang sudah didaftarkan")
    st.text("")
    st.write("Terima kasih, semoga bermanfaat. 😊👨‍🎓👩‍🎓")
elif dataset_name == "Prediksi Perorangan":
    X1_Jenis_Kelamin = st.selectbox(
        "Pilih Jenis Kelamin", ("1_Laki_laki", "2_Perempuan")
    )
    X2_Nilai_Rerata = st.selectbox("Pilih Nilai Rata-rata", ("1_C", "2_B"))
    X3_Mengikuti_Ekstrakurikuler = st.selectbox(
        "Pilih Ekstrakurikuler", ("0_Tidak", "1_Iya")
    )
    X4_Ikut_Bekerja = st.selectbox("Pilih Ikut Bekerja", ("0_Tidak", "1_Iya"))
    X5_Mengalami_Broken_Home = st.selectbox("Pilih Broken Home", ("0_Tidak", "1_Iya"))
    X6_Jarak_Sekolah = st.selectbox(
        "Pilih Broken Home", ("1_Dekat", "2_Sedang", "3_Jauh")
    )
    X7_Pendidikan_Ayah = st.selectbox(
        "Pilih Pendidikan Ayah",
        ("1_Yang_Lainnya", "2_SD", "3_SMP", "4_SMA", "5_D1_D4", "6_S1_S3"),
    )

    X8_Pendidikan_Ibu = st.selectbox(
        "Pilih Pendidikan Ibu",
        ("1_Yang_Lainnya", "2_SD", "3_SMP", "4_SMA", "5_D1_D4", "6_S1_S3"),
    )
    X9_Penghasilan_Ayah = st.selectbox(
        "Pilih Penghasilan Ayah",
        ("1_Tidak_Bekerja", "2_Rendah", "3_Sedang", "4_Tinggi"),
    )
    X10_Penghasilan_Ibu = st.selectbox(
        "Pilih Penghasilan Ibu", ("1_Tidak_Bekerja", "2_Rendah", "3_Sedang", "4_Tinggi")
    )
    if st.button("Prediksi Siswa"):
        if(X9_Penghasilan_Ayah == "1_Tidak_Bekerja" and X2_Nilai_Rerata == "1_C" and X3_Mengikuti_Ekstrakurikuler == "0_Tidak"):
            if(data1 > data2):
                st.write("Ok1")
            else:
                st.write("ok2")
            


    


      