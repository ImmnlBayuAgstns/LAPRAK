# Prediksi Kanker Payudara

Proyek ini merupakan implementasi pembelajaran mesin untuk memprediksi kemungkinan kanker payudara berdasarkan karakteristik demografis, gaya hidup, riwayat kesehatan, dan hasil pemeriksaan pasien.

Proyek mencakup:

- eksplorasi dan pemodelan pada notebook Jupyter;
- dataset pasien dalam format CSV;
- kamus data untuk menjelaskan setiap kolom;
- model **Gradient Boosting** yang telah dilatih dan disimpan dengan `joblib`;
- API Flask untuk melakukan prediksi melalui endpoint HTTP.

> **Penting:** Proyek ini ditujukan untuk pembelajaran dan demonstrasi teknologi. Hasil prediksi bukan diagnosis medis dan tidak boleh digunakan sebagai pengganti pemeriksaan atau keputusan tenaga kesehatan.

## Struktur Berkas

| Berkas | Keterangan |
| --- | --- |
| `breast_cancer_prediction.ipynb` | Notebook untuk membaca data, eksplorasi, prapemrosesan, pelatihan, evaluasi, dan penyimpanan model. |
| `breast_cancer_prediction.csv` | Dataset utama untuk pelatihan dan evaluasi model. |
| `data_dictionary.csv` | Penjelasan nama kolom, tipe data, deskripsi, dan contoh nilai. |
| `breast_cancer_GBC_model.pkl` | Pipeline model Gradient Boosting yang telah dilatih. |
| `data.json` | Contoh data input untuk API. |
| `deploy.py` | Aplikasi Flask yang menyediakan endpoint prediksi. |

## Dataset

Target prediksi berada pada kolom `Cancer`:

- `0` = tidak terindikasi kanker;
- `1` = terindikasi kanker.

Fitur yang digunakan oleh API adalah:

`Age`, `Gender`, `BMI`, `Family_History`, `Smoking`, `Alcohol_Consumption`, `Physical_Activity`, `Hormone_Therapy`, `Menopause_Status`, `Genetic_Mutation`, `Tumor_Size_cm`, `Lymph_Node_Involvement`, `Mammogram_Result`, `Blood_Pressure`, `Cholesterol`, `Diabetes`, `Exercise_Days_Per_Week`, `Breastfeeding_History`, dan `Annual_Income_USD`.

Informasi lengkap mengenai setiap kolom dapat dilihat pada `data_dictionary.csv`. Kolom seperti `Patient_ID`, `Biopsy_Result`, `Cancer_Stage`, dan `Cancer` tersedia pada dataset untuk kebutuhan analisis atau evaluasi, tetapi tidak dikirim sebagai fitur input API.

## Eksplorasi Data

Eksplorasi data dilakukan di dalam notebook untuk memahami karakteristik dataset dan hubungan fitur dengan target `Cancer`. Tahapan yang dilakukan meliputi:

- memeriksa struktur, tipe data, dan statistik deskriptif dataset;
- memeriksa nilai yang hilang pada setiap kolom;
- melihat distribusi target kanker (`0` dan `1`);
- membandingkan distribusi fitur kategorikal berdasarkan status kanker menggunakan count plot;
- membandingkan fitur numerik berdasarkan status kanker menggunakan box plot.

Notebook menemukan nilai yang hilang pada beberapa fitur, antara lain `BMI`, `Alcohol_Consumption`, `Physical_Activity`, `Hormone_Therapy`, dan `Tumor_Size_cm`. Penanganan nilai hilang dilakukan di dalam pipeline prapemrosesan sehingga proses pelatihan dan prediksi menggunakan aturan yang konsisten.

## Prapemrosesan dan Pemodelan

Kolom `Patient_ID`, `Biopsy_Result`, dan `Cancer_Stage` dikeluarkan dari fitur untuk mencegah penggunaan identitas pasien dan informasi yang berpotensi menjadi kebocoran target. Kolom `Cancer` digunakan sebagai target prediksi. Data kemudian dibagi menjadi data latih dan data uji dengan perbandingan 80:20 serta `random_state=42`.

Prapemrosesan dilakukan berdasarkan jenis fitur:

- fitur numerik diisi menggunakan median dan dinormalisasi dengan `StandardScaler`;
- fitur biner diisi menggunakan nilai yang paling sering muncul dan dikodekan dengan `OneHotEncoder`;
- `Physical_Activity` dikodekan secara ordinal dengan urutan `Low`, `Moderate`, dan `High`;
- fitur kategorikal nominal seperti `Mammogram_Result` dan `Breastfeeding_History` dikodekan dengan one-hot encoding;
- kategori yang belum pernah ditemui saat prediksi ditangani dengan `handle_unknown='ignore'`.

Setelah prapemrosesan, data latih memiliki 23 fitur hasil transformasi. Tiga model klasifikasi dibandingkan, yaitu Logistic Regression, Random Forest, dan Gradient Boosting.

### Hasil Perbandingan Model

Berikut hasil evaluasi pada data uji yang tercatat di notebook:

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
| --- | ---: | ---: | ---: | ---: | ---: |
| Logistic Regression | 0,915 | 0,702 | 0,929 | 0,800 | 0,974 |
| Random Forest | 0,958 | 1,000 | 0,770 | 0,870 | 0,976 |
| Gradient Boosting | **0,981** | **1,000** | **0,896** | **0,945** | **0,977** |

Gradient Boosting dipilih sebagai model yang disimpan karena memberikan hasil keseluruhan terbaik pada evaluasi notebook, terutama berdasarkan accuracy, recall, F1-score, dan ROC-AUC. Pipeline lengkapnya disimpan sebagai `breast_cancer_GBC_model.pkl` dan digunakan kembali oleh API pada `deploy.py`.

## Persyaratan

- Python 3.9 atau lebih baru
- Jupyter Notebook atau JupyterLab (untuk menjalankan notebook)
- Flask
- joblib
- pandas
- scikit-learn
- matplotlib
- seaborn

Instal dependensi dengan:

```bash
pip install flask joblib pandas scikit-learn matplotlib seaborn jupyter
```

Jika menggunakan virtual environment, disarankan membuat dan mengaktifkannya terlebih dahulu:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Windows Command Prompt:

```bat
.venv\Scripts\activate
```

## Menjalankan Notebook

1. Pastikan `breast_cancer_prediction.csv` berada di direktori yang sama dengan notebook.
2. Jalankan Jupyter:

   ```bash
   jupyter notebook
   ```

3. Buka `breast_cancer_prediction.ipynb`.
4. Jalankan sel secara berurutan.

Notebook melakukan seluruh alur analisis, mulai dari pemuatan data dan eksplorasi, pemeriksaan nilai hilang, pembagian data, prapemrosesan fitur kategorikal dan numerik, pelatihan beberapa model klasifikasi, evaluasi menggunakan accuracy, precision, recall, F1-score, ROC-AUC, dan confusion matrix, hingga penyimpanan pipeline Gradient Boosting sebagai `breast_cancer_GBC_model.pkl`.

## Menjalankan API Flask

Pastikan berkas berikut berada dalam satu direktori:

- `deploy.py`
- `breast_cancer_GBC_model.pkl`
- `data.json` (digunakan sebagai input cadangan apabila request tidak menyertakan JSON)

Jalankan aplikasi:

```bash
python deploy.py
```

Secara bawaan, Flask berjalan pada `http://127.0.0.1:5000`.

### Prediksi dengan `data.json`

Kirim request `POST` ke endpoint `/predict` tanpa body JSON. API akan membaca data dari `data.json`:

```bash
curl -X POST http://127.0.0.1:5000/predict
```

Contoh respons:

```json
{
  "prediction": [0, 1, 0]
}
```

### Prediksi dengan JSON langsung

API menerima JSON berupa array objek atau objek yang memiliki properti `data` berisi array objek.

Contoh menggunakan `curl`:

```bash
curl -X POST http://127.0.0.1:5000/predict ^
  -H "Content-Type: application/json" ^
  -d "{\"data\":[{\"Age\":45,\"Gender\":\"Female\",\"BMI\":27.2,\"Family_History\":\"No\",\"Smoking\":\"No\",\"Alcohol_Consumption\":\"No\",\"Physical_Activity\":\"Moderate\",\"Hormone_Therapy\":\"No\",\"Menopause_Status\":\"Post\",\"Genetic_Mutation\":\"Negative\",\"Tumor_Size_cm\":2.0,\"Lymph_Node_Involvement\":\"No\",\"Mammogram_Result\":\"Normal\",\"Blood_Pressure\":128,\"Cholesterol\":196,\"Diabetes\":\"No\",\"Exercise_Days_Per_Week\":5,\"Breastfeeding_History\":\"Yes\",\"Annual_Income_USD\":65000}]}"
```

Untuk PowerShell, gunakan format berikut agar body JSON diperlakukan sebagai satu string:

```powershell
$body = @{
  data = @(
    @{
      Age = 45
      Gender = "Female"
      BMI = 27.2
      Family_History = "No"
      Smoking = "No"
      Alcohol_Consumption = "No"
      Physical_Activity = "Moderate"
      Hormone_Therapy = "No"
      Menopause_Status = "Post"
      Genetic_Mutation = "Negative"
      Tumor_Size_cm = 2.0
      Lymph_Node_Involvement = "No"
      Mammogram_Result = "Normal"
      Blood_Pressure = 128
      Cholesterol = 196
      Diabetes = "No"
      Exercise_Days_Per_Week = 5
      Breastfeeding_History = "Yes"
      Annual_Income_USD = 65000
    }
  )
} | ConvertTo-Json -Depth 4

Invoke-RestMethod -Method Post `
  -Uri http://127.0.0.1:5000/predict `
  -ContentType "application/json" `
  -Body $body
```

Setiap record harus memiliki seluruh kolom fitur yang dibutuhkan model. Jika ada kolom yang hilang, API mengembalikan respons HTTP `400` beserta pesan kesalahan.

## Format Respons dan Penanganan Kesalahan

Jika prediksi berhasil, API mengembalikan:

```json
{
  "prediction": [0]
}
```

Kemungkinan kode status:

- `200` — prediksi berhasil;
- `400` — format JSON atau kolom input tidak valid;
- `404` — berkas yang diperlukan tidak ditemukan;
- `500` — terjadi kesalahan saat proses prediksi.

## Catatan Pengembangan

- Jalankan notebook dari direktori proyek agar path relatif ke dataset dan model dapat ditemukan.
- Model pada berkas `.pkl` harus dibuat dengan versi library yang kompatibel dengan environment saat API dijalankan.
- `debug=True` pada `deploy.py` cocok untuk pengembangan lokal, tetapi sebaiknya dinonaktifkan untuk deployment produksi.
- Data kesehatan bersifat sensitif. Jangan mengunggah data pasien nyata tanpa anonimisasi, izin, dan pengamanan yang sesuai.

## Lisensi

Belum ada lisensi yang ditentukan untuk proyek ini. Tambahkan berkas lisensi apabila proyek akan dibagikan atau digunakan oleh pihak lain.
