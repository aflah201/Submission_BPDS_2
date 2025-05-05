# Laporan Proyek Menyelesaikan Permasalahan Institusi Pendidikan
---
## Business Understanding

Jaya Jaya Institut adalah institusi pendidikan tinggi yang telah berdiri sejak tahun 2000 dan dikenal memiliki reputasi yang baik dalam mencetak lulusan berkualitas. Namun, dalam beberapa tahun terakhir, institusi ini menghadapi tantangan serius terkait tingginya angka siswa yang tidak menyelesaikan studi alias dropout. Fenomena ini tidak hanya berdampak pada citra dan reputasi institusi, tetapi juga memengaruhi efisiensi operasional dan keberlanjutan akademik secara keseluruhan.

Tingginya angka dropout siswa menjadi indikator bahwa terdapat ketidaksesuaian antara proses pembelajaran dan kebutuhan atau kondisi siswa. Jika tidak segera ditangani, hal ini dapat menyebabkan kerugian finansial, menurunkan akreditasi, serta mengurangi kepercayaan masyarakat terhadap institusi. Oleh karena itu, dibutuhkan sistem yang dapat secara dini mengidentifikasi siswa yang berisiko tinggi untuk dropout, sehingga dapat diberikan intervensi yang tepat waktu dan personal.

Tujuan utama dari proyek ini adalah untuk membantu pihak manajemen Jaya Jaya Institut dalam:
1. Mendeteksi siswa yang berpotensi dropout secara lebih awal.
2. Memahami faktor-faktor yang paling memengaruhi risiko dropout.
3. Menyusun strategi intervensi berdasarkan data untuk menurunkan angka dropout.
4. Menyediakan dashboard interaktif agar pihak manajemen dapat memantau performa siswa secara real-time dan membuat keputusan berbasis data (data-driven decision).

Dengan diterapkannya sistem deteksi dini dan dashboard monitoring siswa ini, diharapkan:
- Angka dropout siswa dapat ditekan secara signifikan.
- Institusi mampu menyediakan dukungan yang lebih personal dan tepat sasaran bagi siswa.
- Citra dan kualitas akademik Jaya Jaya Institut semakin meningkat.

---
## Permasalahan Bisnis
1. Permasalahan Umum (General Problem)
Jaya Jaya Institut menghadapi tingginya angka dropout mahasiswa, yang berpotensi menurunkan reputasi institusi dan efisiensi operasional.

2. Permasalahan Bisnis (Business Problem)
Bagaimana cara mendeteksi secara dini siswa yang berisiko dropout, agar dapat dilakukan intervensi tepat waktu untuk mencegahnya?

3. Tujuan Analisis (Analytical Goal)
Membangun model prediksi dropout siswa berdasarkan data historis dan profil siswa, serta mengidentifikasi faktor-faktor penting yang berkontribusi terhadap risiko dropout.

4. Output yang Diharapkan
    - Model machine learning yang dapat memprediksi kemungkinan siswa akan dropout.
    - Dashboard interaktif untuk memantau performa siswa dan memvisualisasikan hasil prediksi.
    - Rekomendasi tindakan preventif berdasarkan hasil analisis.

5. Manfaat Bisnis
    - Menurunkan angka dropout melalui intervensi dini.
    - Meningkatkan efektivitas bimbingan akademik.
    - Memperkuat reputasi dan kepercayaan publik terhadap institusi.

---
## Cakupan Proyek
Proyek ini mencakup:

1. Persiapan dataset [student`s performance](https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/refs/heads/main/students_performance/data.csv) untuk analisis data.
2. Pemrosesan dataset untuk memperbaiki dan membersihkan data agar dapat digunakan pada proses analisis data.
3. Analisis faktor penyebab dropout berdasarkan data kategori dan nominal.
4. Pembuatan Business Dashboard agar mudah dipahami dalam memantau faktor penyebab dropout.
5. Membuat kesimpulan terhadap hasil analisis data.
6. Memberi rekomendasi untuk mengurangi dropout.

---
## Persiapan
Sumber data: [Dataset - Student Performance](https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/refs/heads/main/students_performance/data.csv)

Setup Environment: Proyek ini membutuhkan lingkungan sederhana untuk menjalankan analisis data dan dashboard. Berikut langkah-langkah untuk mempersiapkan environment:
1. Persiapan Environment Pipenv
    - Buka terminal atau PowerShell.
    - Buat sebuah folder baru bernama student_dropout dengan menjalankan perintah berikut.
    ```
    mkdir student_dropout
    ```
    - Pindah ke folder terbaru tersebut menggunakan perintah berikut.
    ```
    cd student_dropout
    ```
    - Buat sebuah virtual environment dengan menjalankan perintah berikut.
    ```
    pipenv install
    ```
    - Aktifkan virtual environment dengan menjalankan perintah berikut.
    ```
    pipenv shell
    ```
    - Install dependensi, packages, library.
    ```
    pip install -r requirements.txt
    ```
2. Menjalankan berkas `notebook.ipynb`
    - Pastikan dependensi, packages, library yang dibutuhkan sudah tersedia (lihat file requirements.txt untuk melihat dependensi yang dibutuhkan).
    - Jalankan seluruh isi file notebook.ipynb menggunakan Google Colab/Jupyter Notebook untuk melihat hasil analisis data, temuan, dan insight yang diperoleh.
3. Menjalankan Dashboard: Untuk melihat isi dashboard secara langsung, dapat menggunakan metabase dengan bantuan Docker (pastikan Docker sudah terinstall)
    - Jalankan perintah berikut:
        ```
        docker pull metabase/metabase:v0.46.4
        ```
    - Jalankan container Metabase menggunakan perintah:
        ```
        docker run -p 3000:3000 --name metabase metabase/metabase
        ```
    - Login ke Metabase menggunakan username dan password berikut:
        ```
        username: aflah@dicoding.com
        password: dicoding1234;
        ```

---
## Business Dashboard

![Student Analysis](<aflahazzaky-dashboard1.jpg>)
![Student Analysis](<aflahazzaky-dashboard2.jpg>)

Dashboard ini menyajikan gambaran komprehensif mengenai karakteristik dan performa mahasiswa berdasarkan status kelulusan (Graduated vs Dropout). Dari total 4.424 mahasiswa, sebanyak 32% dinyatakan dropout dan 68% berhasil lulus. Rasio ini menunjukkan bahwa sepertiga dari mahasiswa tidak berhasil menyelesaikan pendidikannya, angka yang cukup tinggi untuk sebuah institusi pendidikan.

1. **Usia dan Status Mahasiswa**

    Rata-rata usia mahasiswa yang dropout (26.07 tahun) lebih tinggi dibandingkan yang lulus (21.94 tahun). Hal ini mengindikasikan bahwa usia bisa menjadi salah satu faktor risiko, di mana mahasiswa yang lebih tua cenderung memiliki kemungkinan lebih tinggi untuk tidak menyelesaikan studi, mungkin karena beban pekerjaan atau tanggung jawab keluarga.

2. **Jenis Kelamin**
    
    Data menunjukkan bahwa mahasiswa laki-laki memiliki jumlah dropout yang lebih tinggi dibandingkan perempuan. Ini bisa menjadi sinyal bahwa pendekatan pembelajaran atau pendampingan akademik perlu disesuaikan berdasarkan gender.

3. **Status Pernikahan**
    
    Mahasiswa yang masih lajang memiliki angka dropout tertinggi (1.184 orang). Namun yang mengejutkan, mahasiswa yang sudah menikah atau bercerai juga menunjukkan jumlah dropout yang cukup signifikan. Ini bisa disebabkan oleh tekanan hidup dan kurangnya waktu untuk studi.

4. **Jurusan**
    
    Jurusan dengan tingkat kelulusan tertinggi adalah Social Science dan Health Science, sementara jurusan Business & Management menjadi penyumbang dropout terbesar. Hal ini mungkin menunjukkan adanya tantangan akademik atau kurangnya minat di program tersebut yang perlu dievaluasi.

5. **Nilai Akademik**
    - Mahasiswa yang dropout memiliki rata-rata:
        - Jumlah mata kuliah terdaftar yang lebih rendah,
        - Evaluasi dan tingkat kelulusan yang lebih rendah,
        - Nilai akhir (grade) yang jauh lebih rendah dibandingkan mahasiswa yang lulus, baik di semester 1 maupun semester 2.
    
    Ini mengindikasikan bahwa performa akademik yang buruk menjadi indikator kuat risiko dropout.

6. **Pekerjaan Orang Tua**
    
    Mayoritas mahasiswa dropout berasal dari orang tua yang bekerja sebagai buruh atau pekerja kasar, baik ayah (2.202 dropout) maupun ibu (835 dropout). Ini mengindikasikan bahwa latar belakang sosial-ekonomi turut memengaruhi keberhasilan studi mahasiswa.

---
## Menjalankan Sistem Machine Learning
1. Pastikan sudah menginstall streamlit di komputer Anda.
2. Buka terminal atau command prompt.
3. Jalankan perintah streamlit run app.py.
4. atau Akses Online Sistem Machine Learning: [Sistem Prediksi Siswa](https://submissionbpds2-aflah.streamlit.app/)

---
## Conclusion
Dashboard menunjukkan bahwa dropout mahasiswa cenderung berkorelasi dengan faktor usia yang lebih tua, performa akademik rendah, latar belakang sosial-ekonomi menengah ke bawah, serta program studi tertentu seperti Business & Management. Temuan ini sangat penting untuk dijadikan dasar dalam menyusun strategi intervensi yang lebih personal dan berbasis data guna menekan angka dropout dan meningkatkan kualitas pendidikan secara keseluruhan.

---
## Recomendation Action
Berikut daftar rekomendasi yang bisa segera dipertimbangkan oleh manajemen Jaya Jaya Institut:

1. ✅ Early Warning System: Kembangkan sistem prediksi berbasis data untuk mengidentifikasi mahasiswa berisiko dropout di awal semester.

2. 👥 Bimbingan Akademik Intensif: Fokus pada mahasiswa dengan performa rendah dan dari jurusan berisiko tinggi (misalnya Business & Management).

3. 💼 Pendampingan Sosial-Ekonomi: Berikan dukungan beasiswa atau konseling bagi mahasiswa dari keluarga buruh.

4. 📊 Evaluasi Kurikulum: Tinjau ulang kesesuaian kurikulum dan metode pengajaran di jurusan dengan dropout tinggi.

5. 🧑‍🏫 Pelatihan Dosen dan Tutor: Tingkatkan kompetensi pengajar dalam memahami karakteristik mahasiswa dan pendekatan pembelajaran yang adaptif.

6. 💬 Monitoring dan Feedback Berkala: Gunakan dashboard untuk memantau perkembangan mahasiswa secara rutin dan kirimkan feedback secara personal.

7. 🧠 Program Penguatan Soft Skills: Tingkatkan motivasi belajar melalui pelatihan manajemen waktu, pengaturan stres, dan pengembangan diri.