## MAE (Mean Absolute Error)

**Kesimpulan:**
Untuk metrik MAE, hasil dapat diartikan **sangat bagus jika nilainya mendekati 0**. Nilai 0 menunjukkan bahwa tidak ada error sama sekali (prediksi model sama persis dengan data aktual). Semakin menjauhi 0 (semakin besar nilainya), maka kinerja model semakin buruk karena tingkat rata-rata kesalahan absolutnya semakin tinggi.

**Dukungan dari Jurnal:**

- **"Jurnal PeerJ Computer Science ("The coefficient of determination R-squared is more informative than SMAPE, MAE, MAPE, MSE and RMSE in regression analysis evaluation" - Chicco et al., 2021)-cs-07-623.pdf" (Halaman 5, Persamaan 6):** Secara eksplisit jurnal ini mendefinisikan batas nilai MAE dengan pernyataan: _(best value = 0; worst value = +∞)_. Hal ini menegaskan bahwa 0 adalah nilai terbaik mutlak.
- **"Jurnal Climate Research ("Advantages of the mean absolute error (MAE) over the root mean square error (RMSE) in assessing average model performance" - Willmott & Matsuura, 2005)" (Halaman 82, Bagian 4. Concluding Remarks):** Jurnal ini sangat mendukung penggunaan MAE dengan menyatakan bahwa MAE adalah _"the most natural measure of average error magnitude, and that (unlike RMSE) it is an unambiguous measure of average error magnitude"_ (ukuran yang paling alami dan tidak ambigu untuk besaran rata-rata kesalahan).

## MSE (Mean Square Error)

**Kesimpulan:**
Sama halnya dengan MAE, metrik MSE adalah ukuran tingkat kesalahan (error). Oleh karena itu, hasil MSE diartikan **sangat bagus jika nilainya mendekati 0**. Nilai MSE tidak akan pernah negatif (karena merupakan hasil pengkuadratan), dan semakin menjauhi 0 ke arah positif tak terhingga, semakin buruk model tersebut. MSE sangat sensitif terhadap _outlier_ karena kesalahannya dikuadratkan.

**Dukungan dari Jurnal:**

- **"Jurnal PeerJ Computer Science ("The coefficient of determination R-squared is more informative than SMAPE, MAE, MAPE, MSE and RMSE in regression analysis evaluation" - Chicco et al., 2021)-cs-07-623.pdf" (Halaman 5, Persamaan 4):** Jurnal ini memberikan definisi matematis MSE dan secara tertulis menyatakan batas nilainya: _(best value = 0; worst value = +∞)_. Jurnal ini juga menjelaskan bahwa nilai 0 berarti _"the linear regression model fits the data perfectly"_ (Halaman 6, Bagian _Informativeness_).

## R2 (R-squared)

**Kesimpulan:**
Berbeda dengan MAE dan MSE, R2 bukanlah ukuran tingkat error, melainkan ukuran proporsi varians yang dapat dijelaskan oleh model. Untuk metrik R2, hasil diartikan **sangat bagus jika nilainya mendekati 1 (menjauhi 0 ke arah atas)**.

- Jika R2 = 1, artinya model memprediksi dengan sempurna.
- Jika R2 = 0, artinya model tersebut sama buruknya dengan garis horizontal rata-rata (hanya menebak nilai rata-rata target untuk semua input).
- Jika R2 bernilai negatif (menjauhi 0 ke arah bawah / ke arah -∞), artinya model bekerja sangat buruk, bahkan lebih buruk daripada sekadar menebak rata-rata.

**Dukungan dari Jurnal:**

- **"Jurnal PeerJ Computer Science ("The coefficient of determination R-squared is more informative than SMAPE, MAE, MAPE, MSE and RMSE in regression analysis evaluation" - Chicco et al., 2021)-cs-07-623.pdf" (Halaman 5, Persamaan 3):** Menyatakan batas rentang metrik ini dengan sangat jelas: _(worst value = -∞; best value = +1)_.
- **"Jurnal PeerJ Computer Science ("The coefficient of determination R-squared is more informative than SMAPE, MAE, MAPE, MSE and RMSE in regression analysis evaluation" - Chicco et al., 2021)-cs-07-623.pdf" (Halaman 7, Bagian R-squared):** Jurnal ini merinci kasus-kasusnya:
  - R2 = 0: _"The fitted line (or hyperplane) is horizontal... MSE = MST"_. Ini berarti regresi gagal menangkap pola apa pun.
  - R2 < 0: Terjadi ketika model _"fits worse than a horizontal line"_.
  - Jurnal ini sangat merekomendasikan R2 sebagai standar evaluasi karena nilai seperti R2 = 0.8 jelas mengindikasikan performa yang bagus secara absolut tanpa perlu mengetahui skala distribusi datanya.
