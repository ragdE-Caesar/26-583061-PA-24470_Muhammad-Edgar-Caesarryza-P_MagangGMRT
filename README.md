# Forward Kinematics dan Inverse Kinematics Kaki Robot 2-DoF

## Profil

- **Nama:** Muhammad Edgar Caesarryza P
- **NIM:** 26/583061/PA/24470

## Deskripsi

Proyek ini menghitung forward kinematics (FK) dan inverse kinematics (IK) kaki
robot planar dengan dua derajat kebebasan (2-DoF), yaitu sendi Femur dan Tibia.
Program pada `main.py` meminta pilihan mode dan panjang kedua link melalui
terminal. Mode FK menerima sudut servo untuk menghitung koordinat end-effector;
mode IK menerima target X, Y untuk menghitung sudut servo. Panjang Coxa
dianggap nol.

Panjang link disesuaikan dengan NIM:

| Link  | Penentuan                       | Panjang |
| ----- | ------------------------------- | ------: |
| Femur | Dua digit terakhir NIU `583061` |   61 cm |
| Tibia | Dua digit terakhir NIF `24470`  |   70 cm |

Masukkan panjang link sesuai tabel di atas ketika program meminta panjang
link pertama dan kedua. Servo 1 mengatur sudut Femur terhadap sumbu-X positif.
Servo 2 mengatur sudut Tibia relatif terhadap Femur. Sudut positif berputar
berlawanan arah jarum jam (CCW), sedangkan sudut negatif searah jarum jam
(CW).

Rumus yang digunakan:

```text
x = L_femur cos(θ1) + L_tibia cos(θ1 + θ2)
y = L_femur sin(θ1) + L_tibia sin(θ1 + θ2)
```

Sudut dikonversi dari derajat ke radian sebelum digunakan dalam fungsi
trigonometri.

## Fitur dan Status

| Fitur                                                     | Status                                   |
| --------------------------------------------------------- | ---------------------------------------- |
| Perhitungan forward kinematics 2-DoF                      | ✅ Diimplementasikan                     |
| Input sudut Servo 1 dan Servo 2 menggunakan `input()`     | ✅ Diimplementasikan                     |
| Input panjang Femur dan Tibia berdasarkan NIM             | ✅ Masukkan 61 cm dan 70 cm saat diminta |
| Contoh pengujian Servo 1 = 40° dan Servo 2 = 30°          | ✅ Berhasil dijalankan                   |
| Mathematical proof / dokumentasi tulisan tangan           | ✅ Sudah tersedia                        |
| Sistem dengan lebih dari 2-DoF                            | ☐ Belum tersedia                         |
| Kinematika tiga dimensi (X, Y, Z)                         | ☐ Belum tersedia                         |
| Homogeneous transformation dengan library matriks         | ☐ Belum tersedia                         |
| Visualisasi postur Femur dan Tibia menggunakan Matplotlib | ✅ Diimplementasikan                     |
| Inverse kinematics (IK) interaktif dari target X, Y       | ✅ Diimplementasikan                     |

## Hasil Uji Perhitungan

Dengan panjang Femur 61 cm, panjang Tibia 70 cm, sudut Servo 1 sebesar 40°,
dan sudut Servo 2 sebesar 30°:

```text
Koordinat end-effector:
X = 70.6701 cm
Y = 104.9885 cm
```

Uji dijalankan dengan input berurutan `40`, `30`, `61`, dan `70`. Hasil tersebut
menggunakan sudut total Tibia sebesar `40° + 30° = 70°` terhadap sumbu-X positif.

Untuk menguji IK, pilih mode `2`, masukkan panjang `61` dan `70`, lalu masukkan
target `X = 70.6701` dan `Y = 104.9885`. Program akan menghitung sudut servo
yang menghasilkan posisi target tersebut.

## Cara Menjalankan

Jalankan perintah berikut dari direktori repository:

```bash
python main.py
```

Pilih mode `1` untuk FK atau `2` untuk IK. Masukkan panjang link pertama
(Femur) dan kedua (Tibia); untuk NIM ini gunakan `61` dan `70`.

- **FK:** masukkan sudut Servo 1 dan Servo 2 dalam derajat.
- **IK:** masukkan target X dan Y dalam cm. Program menampilkan satu solusi
  sudut servo dalam derajat.

Program menggunakan NumPy untuk fungsi trigonometri dan Matplotlib untuk
menampilkan plot. Pasang dependensi dengan:

```bash
python -m pip install numpy matplotlib
```
