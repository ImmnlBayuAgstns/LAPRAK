# Analisis Mendalam: Kategorisasi Dataset Machine Learning

Dokumen ini menjabarkan alasan spesifik mengapa setiap dataset di bawah ini diklasifikasikan ke dalam tipe Biner, Multikelas, atau Multilabel, ditinjau dari arsitektur target variabelnya (label) dan independensi antar kelas.

## 1. BINARY CLASSIFICATION (Klasifikasi Biner)

**Definisi:** Tugas untuk mengkategorikan data ke dalam salah satu dari dua kelas yang **saling eksklusif** (Himpunan Target $Y \in \{0, 1\}$).

**Analisis per Dataset:**

- **`skin-cancer-binary-classification-dataset`**
  - **Alasan Kategorisasi:** Secara histopatologis dalam konteks dataset ini, sebuah lesi kulit dievaluasi untuk satu pertanyaan utama: "Apakah ini kanker atau bukan?". Label yang tersedia hanya dua: _Benign_ (Jinak = 0) dan _Malignant_ (Ganas = 1). Karena tidak ada transisi atau kelas ketiga yang diizinkan oleh dataset ini, dan status ganas meniadakan status jinak, maka ini murni klasifikasi biner.

- **`breast-cancer-prediction-dataset-10000-patient`**
  - **Alasan Kategorisasi:** Dataset rekam medis ini menggunakan pendekatan diagnostik diskrit. Output yang diharapkan dari fitur-fitur klinis (seperti ukuran tumor, usia, dll) hanyalah memastikan satu dari dua kondisi mutual-eksklusif: Pasien "Positif" Kanker Payudara atau "Negatif". Probabilitas output direpresentasikan dengan satu nilai $p$ (positif) dan probabilitas negatif adalah $1-p$.

- **`fake-and-real-news-dataset`**
  - **Alasan Kategorisasi:** Dataset ini membagi kumpulan korpus teks secara terpisah ke dalam folder/label "Real" dan "Fake". Dalam struktur data ini, sebuah teks dibatasi oleh aturan _hard-voting_: tidak peduli seberapa ambigu isi beritanya, ia harus dikotakkan ke dalam label benar atau salah secara eksklusif.

---

## 2. MULTICLASS CLASSIFICATION (Klasifikasi Multikelas)

**Definisi:** Tugas untuk mengkategorikan data ke dalam salah satu dari $K$ kelas ($K > 2$), di mana setiap sampel **hanya bisa memiliki satu label pasti** (saling eksklusif). Himpunan Target $Y \in \{1, 2, ..., K\}$.

**Analisis per Dataset:**

- **`sports-balls-multiclass-image-classification`**
  - **Alasan Kategorisasi:** Dataset ini berisi gambar bola (basket, voli, tenis, dll). Objek fisik sebuah bola olahraga secara ontologis bersifat eksklusif; bentuk fisik bola golf tidak mungkin secara bersamaan adalah bola basket. Karena model harus memilih **satu** kelas probabilitas tertinggi dari banyak pilihan kategori bola, ia memenuhi syarat klasifikasi multikelas tunggal (menggunakan fungsi aktivasi _Softmax_).

- **`coffee-bean-dataset-resized-224-x-224`**
  - **Alasan Kategorisasi:** Tingkat sangrai (_roast level_) atau jenis biji kopi (misal: _Dark_, _Light_, _Green_) merepresentasikan _state_ (keadaan) dari biji kopi tersebut. Satu biji kopi tidak dapat berada di fase _Green_ dan _Dark_ secara bersamaan pada waktu atau titik piksel yang sama. Klasifikasi bergantung pada _mutually exclusive states_ antar lebih dari dua kelas.

- **`vechicle-dataset`**
  - **Alasan Kategorisasi:** Dataset ini mengklasifikasikan bentuk kendaraan (mobil, motor, sepeda). Walaupun ada variasi desain, secara kategori regulasi dan bentuk, sebuah kendaraan roda dua bermesin didaftarkan sebagai "Motor", bukan "Mobil". Gambar dipaksa untuk masuk ke satu _ground-truth_ laci taksonomi dari beberapa laci yang ada.

---

## 3. MULTILABEL CLASSIFICATION (Klasifikasi Multilabel)

**Definisi:** Tugas memprediksi di mana setiap instance data dikaitkan dengan **subset dari label** yang tersedia. Label-label ini **tidak saling eksklusif**; mereka dapat hadir secara bersamaan (kombinasi atribut).

**Analisis per Dataset:**

- **`multilabel-small-car-and-color-dataset`**
  - **Alasan Kategorisasi:** Disini entitas dipisahkan antara "Bentuk" (Sedan, SUV) dan "Atribut Warna" (Merah, Biru). Karena tipe kendaraan independen terhadap warnanya, satu gambar akan me-memicu lebih dari satu node output (misal: [1 untuk SUV, 1 untuk Merah, 0 untuk Biru, 0 untuk Sedan]). Karena model harus menebak lebih dari satu label _ground-truth_ pada satu waktu, ini adalah multilabel.

- **`apparel-dataset`**
  - **Alasan Kategorisasi:** Citra pakaian memiliki _meta-attributes_ yang sangat kaya. Sebuah gambar kemeja biru berlengan panjang berbahan katun memiliki setidaknya empat label yang aktif secara bersamaan (`Kemeja`, `Biru`, `Lengan Panjang`, `Katun`). Menggunakan _Softmax_ akan merusak model ini karena _Softmax_ memaksa model memilih satu; oleh karena itu, setiap label diklasifikasikan secara biner (independen) menggunakan deretan _Sigmoid_.

- **`medium-articles`**
  - **Alasan Kategorisasi:** Dalam dunia literatur dan penulisan (NLP), sebuah artikel teks tidak pernah hidup dalam satu dimensi. Artikel berjudul "Membangun Jaringan Saraf Tiruan untuk Prediksi Harga Saham" secara inheren memiliki label topik `Machine Learning`, `Finance`, `Python`, dan `Data Science` secara bersamaan. Ketiadaan eksklusivitas kategori ini menjadikannya dataset teks multilabel klasik.
