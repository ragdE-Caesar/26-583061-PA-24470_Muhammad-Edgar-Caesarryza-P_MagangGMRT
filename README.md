# Forward Kinematics Tiga Dimensi Kaki Robot 3-DoF

## Profil

- **Nama:** Muhammad Edgar Caesarryza P
- **NIM:** 26/583061/PA/24470

## Deskripsi

Proyek ini menghitung forward kinematics (FK) kaki robot tiga dimensi dengan
tiga derajat kebebasan. Program menerima sudut yaw pada hip, sudut pitch Femur,
dan sudut pitch relatif Tibia untuk menghitung koordinat end-effector `(X, Y, Z)`.
Panjang Coxa dianggap nol.

Panjang link disesuaikan dengan NIM:

| Link  | Penentuan                       | Panjang |
| ----- | ------------------------------- | ------: |
| Femur | Dua digit terakhir NIU `583061` |   61 cm |
| Tibia | Dua digit terakhir NIF `24470`  |   70 cm |

Masukkan panjang link sesuai tabel di atas ketika program meminta panjang
link pertama dan kedua. Servo 1 mengatur yaw Hip terhadap sumbu-Z. Servo 2 mengatur pitch Femur dan
Servo 3 mengatur pitch Tibia relatif terhadap Femur.

Rumus yang digunakan:

```text
R = L_femur cos(θ2) + L_tibia cos(θ2 + θ3)
x = R cos(θ1)
y = R sin(θ1)
z = L_femur sin(θ2) + L_tibia sin(θ2 + θ3)
```

Semua sudut diterima langsung dalam satuan radian dan digunakan secara
langsung dalam fungsi trigonometri.

## Fitur dan Status

| Fitur                                             | Status                                   |
| ------------------------------------------------- | ---------------------------------------- |
| Perhitungan forward kinematics 3-DoF tiga dimensi | ✅ Diimplementasikan                     |
| Input tiga sudut servo menggunakan `input()`      | ✅ Diimplementasikan                     |
| Input panjang Femur dan Tibia berdasarkan NIM     | ✅ Masukkan 61 cm dan 70 cm saat diminta |
| Contoh pengujian tiga sudut servo                 | ✅ Berhasil dijalankan                   |
| Mathematical proof / dokumentasi tulisan tangan   | ✅ Sudah tersedia                        |
| Sistem dengan lebih dari 2-DoF                    | ✅ 3-DoF tersedia                        |
| Visualisasi postur 3D menggunakan Matplotlib      | ✅ Diimplementasikan                     |
| Inverse kinematics (IK)                           | ❌ Tidak digunakan                       |

## Hasil Uji Perhitungan

Dengan panjang Femur 61 cm, panjang Tibia 70 cm, hip yaw sebesar 0 rad, pitch
Femur sebesar 0.698132 rad, dan pitch Tibia sebesar 0.523599 rad:

```text
Koordinat end-effector:
X = 70.6701 cm
Y = 0.0000 cm
Z = 104.9885 cm
```

Untuk uji awal dapat menggunakan yaw `0`, pitch Femur `0.698132`, dan pitch
Tibia `0.523599` rad, dengan panjang Femur `61 cm` dan Tibia `70 cm`.

## Cara Menjalankan

Jalankan perintah berikut dari direktori repository:

```bash
python main.py
```

Masukkan panjang link pertama (Femur) dan kedua (Tibia); untuk NIM ini gunakan
`61` dan `70`. Lalu masukkan yaw Hip, pitch Femur, dan pitch Tibia dalam radian.

Program menggunakan NumPy untuk fungsi trigonometri dan Matplotlib untuk
menampilkan plot. Pasang dependensi dengan:

```bash
python -m pip install numpy matplotlib
```
