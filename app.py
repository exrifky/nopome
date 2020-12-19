import base64
import numpy as np
import streamlit as st
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
sheet = client.open("Data SMAS Islam Al Wahid").sheet1

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
    "(A)X1_Jenis_Kelamin",
    "(B)X2_Nilai_Rerata",
    "(C)X3_Mengikuti_Ekstrakurikuler",
    "(D)X4_Ikut_Bekerja",
    "(E)X5_Mengalami_Broken_Home",
    "(F)X6_Jarak_Sekolah",
    "(G)X7_Pendidikan_Ayah",
    "(H)X8_Pendidikan_Ibu",
    "(I)X9_Penghasilan_Ayah",
    "(J)X10_Penghasilan_Ibu",
    "(K)Class_Putus",
]


st.title("Sistem Prediksi Putus Sekolah")

st.write("Sistem Prediksi Siswa Putus Sekolah SMA Islam Al Wahid Kepung")

dataset_name = st.sidebar.selectbox(
    "Pilih Menu", ("Tentang Sistem", "Prediksi Perorangan",
                   "Prediksi Berkelompok")
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


df_marks = pd.DataFrame()

# memasukkan dataframe dan kelas putus ke prediksi kelompok


def dtFrame(datFrame, informasi0, informasi1, informasi2, informasi3, informasi4, informasi5, informasi6, informasi7, informasi8, informasi9):
    X9_Penghasilan_Ayah = informasi8
    X2_Nilai_Rerata = informasi1
    X3_Mengikuti_Ekstrakurikuler = informasi2
    if(X9_Penghasilan_Ayah == "Tidak_Bekerja_1" and X2_Nilai_Rerata == "C_1" and X3_Mengikuti_Ekstrakurikuler == "Tidak_0"):
        new_row = {'(A)X1_Jenis_Kelamin': informasi0, '(B)X2_Nilai_Rerata': informasi1, '(C)X3_Mengikuti_Ekstrakurikuler': informasi2, '(D)X4_Ikut_Bekerja': informasi3,
                   '(E)X5_Mengalami_Broken_Home': informasi4, '(F)X6_Jarak_Sekolah': informasi5, '(G)X7_Pendidikan_Ayah': informasi6, '(H)X8_Pendidikan_Ibu': informasi7,
                   '(I)X9_Penghasilan_Ayah': informasi8, '(J)X10_Penghasilan_Ibu': informasi9, '(K)Class_Putus': status(data1, data2)}
    elif(X9_Penghasilan_Ayah == "Tidak_Bekerja_1" and X2_Nilai_Rerata == "C_1" and X3_Mengikuti_Ekstrakurikuler == "Iya_1"):
        new_row = {'(A)X1_Jenis_Kelamin': informasi0, '(B)X2_Nilai_Rerata': informasi1, '(C)X3_Mengikuti_Ekstrakurikuler': informasi2, '(D)X4_Ikut_Bekerja': informasi3,
                   '(E)X5_Mengalami_Broken_Home': informasi4, '(F)X6_Jarak_Sekolah': informasi5, '(G)X7_Pendidikan_Ayah': informasi6, '(H)X8_Pendidikan_Ibu': informasi7,
                   '(I)X9_Penghasilan_Ayah': informasi8, '(J)X10_Penghasilan_Ibu': informasi9, '(K)Class_Putus': status(data3, data4)}
    elif(X9_Penghasilan_Ayah == "Tidak_Bekerja_1" and X2_Nilai_Rerata == "B_2" and X3_Mengikuti_Ekstrakurikuler == "Tidak_0"):
        new_row = {'(A)X1_Jenis_Kelamin': informasi0, '(B)X2_Nilai_Rerata': informasi1, '(C)X3_Mengikuti_Ekstrakurikuler': informasi2, '(D)X4_Ikut_Bekerja': informasi3,
                   '(E)X5_Mengalami_Broken_Home': informasi4, '(F)X6_Jarak_Sekolah': informasi5, '(G)X7_Pendidikan_Ayah': informasi6, '(H)X8_Pendidikan_Ibu': informasi7,
                   '(I)X9_Penghasilan_Ayah': informasi8, '(J)X10_Penghasilan_Ibu': informasi9, '(K)Class_Putus': status(data5, data6)}
    elif(X9_Penghasilan_Ayah == "Tidak_Bekerja_1" and X2_Nilai_Rerata == "B_2" and X3_Mengikuti_Ekstrakurikuler == "Iya_1"):
        new_row = {'(A)X1_Jenis_Kelamin': informasi0, '(B)X2_Nilai_Rerata': informasi1, '(C)X3_Mengikuti_Ekstrakurikuler': informasi2, '(D)X4_Ikut_Bekerja': informasi3,
                   '(E)X5_Mengalami_Broken_Home': informasi4, '(F)X6_Jarak_Sekolah': informasi5, '(G)X7_Pendidikan_Ayah': informasi6, '(H)X8_Pendidikan_Ibu': informasi7,
                   '(I)X9_Penghasilan_Ayah': informasi8, '(J)X10_Penghasilan_Ibu': informasi9, '(K)Class_Putus': status(data7, data8)}
    elif(X9_Penghasilan_Ayah == "Rendah_2" and X2_Nilai_Rerata == "C_1" and X3_Mengikuti_Ekstrakurikuler == "Tidak_0"):
        new_row = {'(A)X1_Jenis_Kelamin': informasi0, '(B)X2_Nilai_Rerata': informasi1, '(C)X3_Mengikuti_Ekstrakurikuler': informasi2, '(D)X4_Ikut_Bekerja': informasi3,
                   '(E)X5_Mengalami_Broken_Home': informasi4, '(F)X6_Jarak_Sekolah': informasi5, '(G)X7_Pendidikan_Ayah': informasi6, '(H)X8_Pendidikan_Ibu': informasi7,
                   '(I)X9_Penghasilan_Ayah': informasi8, '(J)X10_Penghasilan_Ibu': informasi9, '(K)Class_Putus': status(data9, data10)}
    elif(X9_Penghasilan_Ayah == "Rendah_2" and X2_Nilai_Rerata == "C_1" and X3_Mengikuti_Ekstrakurikuler == "Iya_1"):
        new_row = {'(A)X1_Jenis_Kelamin': informasi0, '(B)X2_Nilai_Rerata': informasi1, '(C)X3_Mengikuti_Ekstrakurikuler': informasi2, '(D)X4_Ikut_Bekerja': informasi3,
                   '(E)X5_Mengalami_Broken_Home': informasi4, '(F)X6_Jarak_Sekolah': informasi5, '(G)X7_Pendidikan_Ayah': informasi6, '(H)X8_Pendidikan_Ibu': informasi7,
                   '(I)X9_Penghasilan_Ayah': informasi8, '(J)X10_Penghasilan_Ibu': informasi9, '(K)Class_Putus': status(data11, data12)}
    elif(X9_Penghasilan_Ayah == "Rendah_2" and X2_Nilai_Rerata == "B_2" and X3_Mengikuti_Ekstrakurikuler == "Tidak_0"):
        new_row = {'(A)X1_Jenis_Kelamin': informasi0, '(B)X2_Nilai_Rerata': informasi1, '(C)X3_Mengikuti_Ekstrakurikuler': informasi2, '(D)X4_Ikut_Bekerja': informasi3,
                   '(E)X5_Mengalami_Broken_Home': informasi4, '(F)X6_Jarak_Sekolah': informasi5, '(G)X7_Pendidikan_Ayah': informasi6, '(H)X8_Pendidikan_Ibu': informasi7,
                   '(I)X9_Penghasilan_Ayah': informasi8, '(J)X10_Penghasilan_Ibu': informasi9, '(K)Class_Putus': status(data13, data14)}
    elif(X9_Penghasilan_Ayah == "Rendah_2" and X2_Nilai_Rerata == "B_2" and X3_Mengikuti_Ekstrakurikuler == "Iya_1"):
        new_row = {'(A)X1_Jenis_Kelamin': informasi0, '(B)X2_Nilai_Rerata': informasi1, '(C)X3_Mengikuti_Ekstrakurikuler': informasi2, '(D)X4_Ikut_Bekerja': informasi3,
                   '(E)X5_Mengalami_Broken_Home': informasi4, '(F)X6_Jarak_Sekolah': informasi5, '(G)X7_Pendidikan_Ayah': informasi6, '(H)X8_Pendidikan_Ibu': informasi7,
                   '(I)X9_Penghasilan_Ayah': informasi8, '(J)X10_Penghasilan_Ibu': informasi9, '(K)Class_Putus': status(data15, data16)}
    elif(X9_Penghasilan_Ayah == "Sedang_3" and X2_Nilai_Rerata == "C_1" and X3_Mengikuti_Ekstrakurikuler == "Tidak_0"):
        new_row = {'(A)X1_Jenis_Kelamin': informasi0, '(B)X2_Nilai_Rerata': informasi1, '(C)X3_Mengikuti_Ekstrakurikuler': informasi2, '(D)X4_Ikut_Bekerja': informasi3,
                   '(E)X5_Mengalami_Broken_Home': informasi4, '(F)X6_Jarak_Sekolah': informasi5, '(G)X7_Pendidikan_Ayah': informasi6, '(H)X8_Pendidikan_Ibu': informasi7,
                   '(I)X9_Penghasilan_Ayah': informasi8, '(J)X10_Penghasilan_Ibu': informasi9, '(K)Class_Putus': status(data17, data18)}
    elif(X9_Penghasilan_Ayah == "Sedang_3" and X2_Nilai_Rerata == "C_1" and X3_Mengikuti_Ekstrakurikuler == "Iya_1"):
        new_row = {'(A)X1_Jenis_Kelamin': informasi0, '(B)X2_Nilai_Rerata': informasi1, '(C)X3_Mengikuti_Ekstrakurikuler': informasi2, '(D)X4_Ikut_Bekerja': informasi3,
                   '(E)X5_Mengalami_Broken_Home': informasi4, '(F)X6_Jarak_Sekolah': informasi5, '(G)X7_Pendidikan_Ayah': informasi6, '(H)X8_Pendidikan_Ibu': informasi7,
                   '(I)X9_Penghasilan_Ayah': informasi8, '(J)X10_Penghasilan_Ibu': informasi9, '(K)Class_Putus': status(data19, data20)}
    elif(X9_Penghasilan_Ayah == "Sedang_3" and X2_Nilai_Rerata == "B_2" and X3_Mengikuti_Ekstrakurikuler == "Tidak_0"):
        new_row = {'(A)X1_Jenis_Kelamin': informasi0, '(B)X2_Nilai_Rerata': informasi1, '(C)X3_Mengikuti_Ekstrakurikuler': informasi2, '(D)X4_Ikut_Bekerja': informasi3,
                   '(E)X5_Mengalami_Broken_Home': informasi4, '(F)X6_Jarak_Sekolah': informasi5, '(G)X7_Pendidikan_Ayah': informasi6, '(H)X8_Pendidikan_Ibu': informasi7,
                   '(I)X9_Penghasilan_Ayah': informasi8, '(J)X10_Penghasilan_Ibu': informasi9, '(K)Class_Putus': status(data21, data22)}
    elif(X9_Penghasilan_Ayah == "Sedang_3" and X2_Nilai_Rerata == "B_2" and X3_Mengikuti_Ekstrakurikuler == "Iya_1"):
        new_row = {'(A)X1_Jenis_Kelamin': informasi0, '(B)X2_Nilai_Rerata': informasi1, '(C)X3_Mengikuti_Ekstrakurikuler': informasi2, '(D)X4_Ikut_Bekerja': informasi3,
                   '(E)X5_Mengalami_Broken_Home': informasi4, '(F)X6_Jarak_Sekolah': informasi5, '(G)X7_Pendidikan_Ayah': informasi6, '(H)X8_Pendidikan_Ibu': informasi7,
                   '(I)X9_Penghasilan_Ayah': informasi8, '(J)X10_Penghasilan_Ibu': informasi9, '(K)Class_Putus': status(data23, data24)}
    elif(X9_Penghasilan_Ayah == "Tinggi_4" and X2_Nilai_Rerata == "C_1" and X3_Mengikuti_Ekstrakurikuler == "Tidak_0"):
        new_row = {'(A)X1_Jenis_Kelamin': informasi0, '(B)X2_Nilai_Rerata': informasi1, '(C)X3_Mengikuti_Ekstrakurikuler': informasi2, '(D)X4_Ikut_Bekerja': informasi3,
                   '(E)X5_Mengalami_Broken_Home': informasi4, '(F)X6_Jarak_Sekolah': informasi5, '(G)X7_Pendidikan_Ayah': informasi6, '(H)X8_Pendidikan_Ibu': informasi7,
                   '(I)X9_Penghasilan_Ayah': informasi8, '(J)X10_Penghasilan_Ibu': informasi9, '(K)Class_Putus': status(data25, data26)}
    elif(X9_Penghasilan_Ayah == "Tinggi_4" and X2_Nilai_Rerata == "C_1" and X3_Mengikuti_Ekstrakurikuler == "Iya_1"):
        new_row = {'(A)X1_Jenis_Kelamin': informasi0, '(B)X2_Nilai_Rerata': informasi1, '(C)X3_Mengikuti_Ekstrakurikuler': informasi2, '(D)X4_Ikut_Bekerja': informasi3,
                   '(E)X5_Mengalami_Broken_Home': informasi4, '(F)X6_Jarak_Sekolah': informasi5, '(G)X7_Pendidikan_Ayah': informasi6, '(H)X8_Pendidikan_Ibu': informasi7,
                   '(I)X9_Penghasilan_Ayah': informasi8, '(J)X10_Penghasilan_Ibu': informasi9, '(K)Class_Putus': status(data27, data28)}
    elif(X9_Penghasilan_Ayah == "Tinggi_4" and X2_Nilai_Rerata == "B_2" and X3_Mengikuti_Ekstrakurikuler == "Tidak_0"):
        new_row = {'(A)X1_Jenis_Kelamin': informasi0, '(B)X2_Nilai_Rerata': informasi1, '(C)X3_Mengikuti_Ekstrakurikuler': informasi2, '(D)X4_Ikut_Bekerja': informasi3,
                   '(E)X5_Mengalami_Broken_Home': informasi4, '(F)X6_Jarak_Sekolah': informasi5, '(G)X7_Pendidikan_Ayah': informasi6, '(H)X8_Pendidikan_Ibu': informasi7,
                   '(I)X9_Penghasilan_Ayah': informasi8, '(J)X10_Penghasilan_Ibu': informasi9, '(K)Class_Putus': status(data29, data30)}
    elif(X9_Penghasilan_Ayah == "Tinggi_4" and X2_Nilai_Rerata == "B_2" and X3_Mengikuti_Ekstrakurikuler == "Iya_1"):
        new_row = {'(A)X1_Jenis_Kelamin': informasi0, '(B)X2_Nilai_Rerata': informasi1, '(C)X3_Mengikuti_Ekstrakurikuler': informasi2, '(D)X4_Ikut_Bekerja': informasi3,
                   '(E)X5_Mengalami_Broken_Home': informasi4, '(F)X6_Jarak_Sekolah': informasi5, '(G)X7_Pendidikan_Ayah': informasi6, '(H)X8_Pendidikan_Ibu': informasi7,
                   '(I)X9_Penghasilan_Ayah': informasi8, '(J)X10_Penghasilan_Ibu': informasi9, '(K)Class_Putus': status(data30, data31)}
        # append row to the dataframe
    datFrame = datFrame.append(new_row, ignore_index=True)
    return datFrame

# bantuan kelas untuk prediksi berkelompok


def status(proba1, proba2):
    if(proba1 > proba2):
        return("Tidak_0")
    else:
        return("Iya_1")

# menghasilkan output untuk prediksi perorangan


def cekProba(proba1, proba2):
    if(proba1 > proba2):
        st.write("Tidak")
        st.success(
            "Siswa tersebut tidak berpotensi untuk putus sekolah. Namun lebih baik untuk tetap diperhatikan ya! 👩‍🎓👨‍🎓")
    else:
        st.write("Iya")
        st.warning(
            "Siswa tersebut berpotensi untuk putus sekolah. Lebih baik untuk lebih diperhatikan lagi ya! 🙏🧐")

# menghasilkan jumlah kelompok untuk menentukan jumlah baris


def sizeKelompok(size):
    df_marks = pd.DataFrame()
    if size >= 10:
        df_marks = dtFrame(
            df_marks, x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9])
    if size >= 20:
        df_marks = dtFrame(
            df_marks, x[10], x[11], x[12], x[13], x[14], x[15], x[16], x[17], x[18], x[19])
    if size >= 30:
        df_marks = dtFrame(
            df_marks, x[20], x[21], x[22], x[23], x[24], x[25], x[26], x[27], x[28], x[29])
    if size >= 40:
        df_marks = dtFrame(
            df_marks, x[30], x[31], x[32], x[33], x[34], x[35], x[36], x[37], x[38], x[39])
    if size >= 50:
        df_marks = dtFrame(
            df_marks, x[40], x[41], x[42], x[43], x[44], x[45], x[46], x[47], x[48], x[49])
    if size >= 60:
        df_marks = dtFrame(
            df_marks, x[50], x[51], x[52], x[53], x[54], x[55], x[56], x[57], x[58], x[59])
    if size >= 70:
        df_marks = dtFrame(
            df_marks, x[60], x[61], x[62], x[63], x[64], x[65], x[66], x[67], x[68], x[69])
    if size >= 80:
        df_marks = dtFrame(
            df_marks, x[70], x[71], x[72], x[73], x[74], x[75], x[76], x[77], x[78], x[79])
    if size >= 90:
        df_marks = dtFrame(
            df_marks, x[80], x[81], x[82], x[83], x[84], x[85], x[86], x[87], x[88], x[89])
    if size >= 100:
        df_marks = dtFrame(
            df_marks, x[90], x[91], x[92], x[93], x[94], x[95], x[96], x[97], x[98], x[99])
    if size >= 110:
        df_marks = dtFrame(df_marks, x[100], x[101], x[102],
                           x[103], x[104], x[105], x[106], x[107], x[108], x[109])
    if size >= 120:
        df_marks = dtFrame(df_marks, x[110], x[111], x[112],
                           x[113], x[114], x[115], x[116], x[117], x[118], x[119])
    if size >= 130:
        df_marks = dtFrame(df_marks, x[120], x[121], x[122],
                           x[123], x[124], x[125], x[126], x[127], x[128], x[129])
    if size >= 140:
        df_marks = dtFrame(df_marks, x[130], x[131], x[132],
                           x[133], x[134], x[135], x[136], x[137], x[138], x[139])
    if size >= 150:
        df_marks = dtFrame(df_marks, x[140], x[141], x[142],
                           x[143], x[144], x[145], x[146], x[147], x[148], x[149])
    if size >= 160:
        df_marks = dtFrame(df_marks, x[150], x[151], x[152],
                           x[153], x[154], x[155], x[156], x[157], x[158], x[159])
    if size >= 170:
        df_marks = dtFrame(df_marks, x[160], x[161], x[162],
                           x[163], x[164], x[165], x[166], x[167], x[168], x[169])
    if size >= 180:
        df_marks = dtFrame(df_marks, x[170], x[171], x[172],
                           x[173], x[174], x[175], x[176], x[177], x[178], x[179])
    if size >= 190:
        df_marks = dtFrame(df_marks, x[180], x[181], x[182],
                           x[183], x[184], x[185], x[186], x[187], x[188], x[189])
    if size >= 200:
        df_marks = dtFrame(df_marks, x[190], x[191], x[192],
                           x[193], x[194], x[195], x[196], x[197], x[198], x[199])
    if size >= 210:
        df_marks = dtFrame(df_marks, x[200], x[201], x[202],
                           x[203], x[204], x[205], x[206], x[207], x[208], x[209])
    if size >= 220:
        df_marks = dtFrame(df_marks, x[210], x[211], x[212],
                           x[213], x[214], x[215], x[216], x[217], x[218], x[219])
    if size >= 230:
        df_marks = dtFrame(df_marks, x[220], x[221], x[222],
                           x[223], x[224], x[225], x[226], x[227], x[228], x[229])
    if size >= 240:
        df_marks = dtFrame(df_marks, x[230], x[231], x[232],
                           x[233], x[234], x[235], x[236], x[237], x[238], x[239])
    if size >= 250:
        df_marks = dtFrame(df_marks, x[240], x[241], x[242],
                           x[243], x[244], x[245], x[246], x[247], x[248], x[249])
    if size >= 260:
        df_marks = dtFrame(df_marks, x[250], x[251], x[252],
                           x[253], x[254], x[255], x[256], x[257], x[258], x[259])
    if size >= 270:
        df_marks = dtFrame(df_marks, x[260], x[261], x[262],
                           x[263], x[264], x[265], x[266], x[267], x[268], x[269])
    if size >= 280:
        df_marks = dtFrame(df_marks, x[270], x[271], x[272],
                           x[273], x[274], x[275], x[276], x[277], x[278], x[279])
    if size >= 290:
        df_marks = dtFrame(df_marks, x[280], x[281], x[282],
                           x[283], x[284], x[285], x[286], x[287], x[288], x[289])
    if size >= 300:
        df_marks = dtFrame(df_marks, x[290], x[291], x[292],
                           x[293], x[294], x[295], x[296], x[297], x[298], x[299])
    if size >= 310:
        df_marks = dtFrame(df_marks, x[300], x[301], x[302],
                           x[303], x[304], x[305], x[306], x[307], x[308], x[309])
    if size >= 320:
        df_marks = dtFrame(df_marks, x[310], x[311], x[312],
                           x[313], x[314], x[315], x[316], x[317], x[318], x[319])
    if size >= 330:
        df_marks = dtFrame(df_marks, x[320], x[321], x[322],
                           x[323], x[324], x[325], x[326], x[327], x[328], x[329])
    if size >= 340:
        df_marks = dtFrame(df_marks, x[330], x[331], x[332],
                           x[333], x[334], x[335], x[336], x[337], x[338], x[339])
    if size >= 350:
        df_marks = dtFrame(df_marks, x[340], x[341], x[342],
                           x[343], x[344], x[345], x[346], x[347], x[348], x[349])
    if size >= 360:
        df_marks = dtFrame(df_marks, x[350], x[351], x[352],
                           x[353], x[354], x[355], x[356], x[357], x[358], x[359])
    if size >= 370:
        df_marks = dtFrame(df_marks, x[360], x[361], x[362],
                           x[363], x[364], x[365], x[366], x[367], x[368], x[369])
    if size >= 380:
        df_marks = dtFrame(df_marks, x[370], x[371], x[372],
                           x[373], x[374], x[375], x[376], x[377], x[378], x[379])
    if size >= 390:
        df_marks = dtFrame(df_marks, x[380], x[381], x[382],
                           x[383], x[384], x[385], x[386], x[387], x[388], x[389])
    if size >= 400:
        df_marks = dtFrame(df_marks, x[390], x[391], x[392],
                           x[393], x[394], x[395], x[396], x[397], x[398], x[399])
    st.markdown(get_table_download_link(df_marks), unsafe_allow_html=True)
    st.write(df_marks)


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
    st.write("Prosedur Percobaan Prediksi 📑")
    st.write("1. Isilah semua data yang telah tersedia dengan benar")
    st.write("2. Tekan tombol ""'Prediksi Siswa'""")
    X1_Jenis_Kelamin = st.selectbox(
        "Pilih Jenis Kelamin", ("Laki_laki_1", "Perempuan_2")
    )
    X2_Nilai_Rerata = st.selectbox("Pilih Nilai Rata-rata", ("C_1", "B_2"))
    X3_Mengikuti_Ekstrakurikuler = st.selectbox(
        "Pilih Ekstrakurikuler", ("Tidak_0", "Iya_1")
    )
    X4_Ikut_Bekerja = st.selectbox("Pilih Ikut Bekerja", ("Tidak_0", "Iya_1"))
    X5_Mengalami_Broken_Home = st.selectbox(
        "Pilih Broken Home", ("Tidak_0", "Iya_1"))
    X6_Jarak_Sekolah = st.selectbox(
        "Pilih Broken Home", ("Dekat_1", "Sedang_2", "Jauh_3")
    )
    X7_Pendidikan_Ayah = st.selectbox(
        "Pilih Pendidikan Ayah",
        ("Yang_Lainnya_1", "SD_2", "SMP_3", "SMA_4", "D1_D4_5", "S1_S3_6"),
    )

    X8_Pendidikan_Ibu = st.selectbox(
        "Pilih Pendidikan Ibu",
        ("Yang_Lainnya_1", "SD_2", "SMP_3", "SMA_4", "D1_D4_5", "S1_S3_6"),
    )
    X9_Penghasilan_Ayah = st.selectbox(
        "Pilih Penghasilan Ayah",
        ("Tidak_Bekerja_1", "Rendah_2", "Sedang_3", "Tinggi_4"),
    )
    X10_Penghasilan_Ibu = st.selectbox(
        "Pilih Penghasilan Ibu", ("Tidak_Bekerja_1",
                                  "Rendah_2", "Sedang_3", "Tinggi_4")
    )

    if st.button("Prediksi Siswa"):
        if(X9_Penghasilan_Ayah == "Tidak_Bekerja_1" and X2_Nilai_Rerata == "C_1" and X3_Mengikuti_Ekstrakurikuler == "Tidak_0"):
            cekProba(data1, data2)
        elif(X9_Penghasilan_Ayah == "Tidak_Bekerja_1" and X2_Nilai_Rerata == "C_1" and X3_Mengikuti_Ekstrakurikuler == "Iya_1"):
            cekProba(data3, data4)
        elif(X9_Penghasilan_Ayah == "Tidak_Bekerja_1" and X2_Nilai_Rerata == "B_2" and X3_Mengikuti_Ekstrakurikuler == "Tidak_0"):
            cekProba(data5, data6)
        elif(X9_Penghasilan_Ayah == "Tidak_Bekerja_1" and X2_Nilai_Rerata == "B_2" and X3_Mengikuti_Ekstrakurikuler == "Iya_1"):
            cekProba(data7, data8)
        elif(X9_Penghasilan_Ayah == "Rendah_2" and X2_Nilai_Rerata == "C_1" and X3_Mengikuti_Ekstrakurikuler == "Tidak_0"):
            cekProba(data9, data10)
        elif(X9_Penghasilan_Ayah == "Rendah_2" and X2_Nilai_Rerata == "C_1" and X3_Mengikuti_Ekstrakurikuler == "Iya_1"):
            cekProba(data11, data12)
        elif(X9_Penghasilan_Ayah == "Rendah_2" and X2_Nilai_Rerata == "B_2" and X3_Mengikuti_Ekstrakurikuler == "Tidak_0"):
            cekProba(data13, data14)
        elif(X9_Penghasilan_Ayah == "Rendah_2" and X2_Nilai_Rerata == "B_2" and X3_Mengikuti_Ekstrakurikuler == "Iya_1"):
            cekProba(data15, data16)
        elif(X9_Penghasilan_Ayah == "Sedang_3" and X2_Nilai_Rerata == "C_1" and X3_Mengikuti_Ekstrakurikuler == "Tidak_0"):
            cekProba(data17, data18)
        elif(X9_Penghasilan_Ayah == "Sedang_3" and X2_Nilai_Rerata == "C_1" and X3_Mengikuti_Ekstrakurikuler == "Iya_1"):
            cekProba(data19, data20)
        elif(X9_Penghasilan_Ayah == "Sedang_3" and X2_Nilai_Rerata == "B_2" and X3_Mengikuti_Ekstrakurikuler == "Tidak_0"):
            cekProba(data21, data22)
        elif(X9_Penghasilan_Ayah == "Sedang_3" and X2_Nilai_Rerata == "B_2" and X3_Mengikuti_Ekstrakurikuler == "Iya_1"):
            cekProba(data23, data24)
        elif(X9_Penghasilan_Ayah == "Tinggi_4" and X2_Nilai_Rerata == "C_1" and X3_Mengikuti_Ekstrakurikuler == "Tidak_0"):
            cekProba(data25, data26)
        elif(X9_Penghasilan_Ayah == "Tinggi_4" and X2_Nilai_Rerata == "C_1" and X3_Mengikuti_Ekstrakurikuler == "Iya_1"):
            cekProba(data27, data28)
        elif(X9_Penghasilan_Ayah == "Tinggi_4" and X2_Nilai_Rerata == "B_2" and X3_Mengikuti_Ekstrakurikuler == "Tidak_0"):
            cekProba(data29, data30)
        elif(X9_Penghasilan_Ayah == "Tinggi_4" and X2_Nilai_Rerata == "B_2" and X3_Mengikuti_Ekstrakurikuler == "Iya_1"):
            cekProba(data31, data32)
else:
    st.write("Prosedur Percobaan Prediksi 📑")
    st.write("1. Buka https://drive.google.com/file/d/14nWK5lhK-ofkD5KvSMXBzKFFedRMKCKR/view?usp=sharing dengan akun SMA Al Wahid")
    st.write("2. Silakan merubah data sesuai kebutuhan")
    st.write("3. Copy syntax yang muncul pada kolom L dengan jumlah menyesuaikan data")
    st.write("4. Kemudian paste/tempel pada kolom yang barada di bawah ini 👇")
    st.write(
        "Pastikan anda tidak melebihi batas masukkan yakni 30 baris per percobaan")
    x = st.text_area("Data Siswa", height=300)
    dataSiswa1 = x
    df = pd
    x = x.split()
    if st.button("Prediksi Siswa"):
        if len(x) > 400:
            st.write("Mohon maaf, jumlah data melebihi maksimal masukkan (40 data)")
            totalData = int(len(x) / 10)
            st.write("Jumlah yang anda masukkan", totalData, "baris data")
        else:
            sizeKelompok(len(x))
