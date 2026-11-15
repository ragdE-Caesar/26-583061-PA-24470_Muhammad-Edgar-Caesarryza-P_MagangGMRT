# Forward Kinematics Kaki Robot 2-DoF

## Profil

- **Nama:** Muhammad Edgar Caesarryza P
- **NIM:** 26/583061/PA/24470

## Deskripsi

Proyek ini menghitung forward kinematics (FK) kaki robot planar dengan dua
derajat kebebasan (2-DoF), yaitu sendi Femur dan Tibia. Program pada `main.py`
meminta sudut kedua servo dan panjang kedua link melalui terminal, lalu
menghitung koordinat ujung Tibia (end-effector) terhadap titik pangkal `(0, 0)`.
Panjang Coxa dianggap nol.

Panjang link disesuaikan dengan NIM:

| Link | Penentuan | Panjang |
|---|---|---:|
| Femur | Dua digit terakhir NIU `583061` | 61 cm |
| Tibia | Dua digit terakhir NIF `24470` | 70 cm |

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

| Fitur | Status |
|---|---|
| Perhitungan forward kinematics 2-DoF | ✅ Diimplementasikan |
| Input sudut Servo 1 dan Servo 2 menggunakan `input()` | ✅ Diimplementasikan |
| Input panjang Femur dan Tibia berdasarkan NIM | ✅ Masukkan 61 cm dan 70 cm saat diminta |
| Contoh pengujian Servo 1 = 40° dan Servo 2 = 30° | ✅ Berhasil dijalankan |
| Mathematical proof / dokumentasi tulisan tangan | ☐ Belum tersedia |
| Sistem dengan lebih dari 2-DoF | ☐ Belum tersedia |
| Kinematika tiga dimensi (X, Y, Z) | ☐ Belum tersedia |
| Homogeneous transformation dengan library matriks | ☐ Belum tersedia |
| Visualisasi GUI atau plot | ☐ Belum diimplementasikan |
| Inverse kinematics (IK) | ☐ Belum tersedia |

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

## Cara Menjalankan

Jalankan perintah berikut dari direktori repository:

```bash
python main.py
```

Ikuti prompt di terminal. Masukkan sudut Servo 1, sudut Servo 2, panjang link
pertama (Femur), lalu panjang link kedua (Tibia). Untuk nilai berdasarkan NIM
ini, masukkan panjang `61` dan `70`.

Program menggunakan NumPy untuk fungsi trigonometri. Pasang dependensinya dengan:

```bash
python -m pip install numpy
```
