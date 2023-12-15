from fractions import Fraction

kriteria = [
    "Jam Kerja",
    "Bobot Tugas",
    "Kesesuaian Tugas",
    "Standar Perusahaan",
    "Penerapan K3",
    "Fasilitas & Peralatan",
    "Bidang Keahlian"
]

costbenefit = ["benefit", "benefit", "benefit", "benefit", "benefit", "benefit", "benefit"]

perbandingankriteria = [
    [1, 1, 1/3, 1/2, 1/2, 1, 1/3],
    [1, 1, 1/3, 1/2, 1/2, 1, 1/3],
    [3, 3, 1, 1/2, 1/2, 3, 1],
    [2, 2, 2, 1, 1, 2, 1/2],
    [2, 2, 2, 1, 1, 2, 1/2],
    [1, 1, 1/3, 1/2, 1/2, 1, 1/3],
    [3, 3, 1, 2, 2, 3, 1]
]

alternatif = [
    "BPN",
    "BPS",
    "Bappeda",
    "BPJS Ketenagakerjaan",
    "Dinas KBPPPA",
    "Dinas Perikanan",
    "ISCI",
    "Kejaksaan Negeri",
    "Novian Collection",
    "Politeknik Negeri Cilacap",
    "PT TELKOM",
    "Sekretariat Daerah",
    "Stasiun Karantina"
]

alternatifkriteria = [
    [3.2, 3.4, 2.6, 2.8, 3.2, 3.8, 3], # alternatif 1
    [3, 2, 2, 3, 2, 3, 2], # alternatif 2
    [3, 4, 3, 3, 4, 3, 3], # alternatif 3
    [3, 3, 2.33, 3.67, 3.33, 3.67, 3.67], # alternatif 4
    [3, 3, 2.5, 3, 4, 3.5, 2.5], # alternatif 5
    [2.33, 3, 2.67, 3, 3.33, 2.67, 3], # alternatif 6
    [3, 3, 4, 3, 3, 4, 4], # alternatif 7
    [3.25, 3.75, 3, 4, 3, 3, 3.5], # alternatif 8
    [3, 2, 2, 3, 3, 2.5, 2], # alternatif 9
    [3.2, 3.55, 3.2, 3.45, 3.3, 3.45, 3.5], # alternatif 10
    [3, 3, 3.5, 3, 3, 3.5, 3.5], # alternatif 11
    [3, 3.5, 3, 3, 3.5, 3, 3], # alternatif 12
    [3.5, 4, 3, 3.5, 3, 4, 3], # alternatif 13
]

# --------------------------------------------------------------------------------------------
# Meminta input untuk mengisi matriks perbandingankriteria
# perbandingankriteria = []
# for i in range(len(kriteria)):
#     row = []
#     for j in range(len(kriteria)):
#         if i == j:
#             row.append(1)
#         elif i < j:
#             value_input = input(f"Berapa nilai kepentingan {kriteria[i]} dibandingkan {kriteria[j]} ?: ")
#             # Menggunakan modul fractions untuk mengatasi input pecahan
#             value = float(Fraction(value_input))
#             row.append(value)
#         else:
#             # Jika sudah ada nilai di matriks, gunakan nilai yang berkebalikan
#             row.append(1 / perbandingankriteria[j][i])
#     perbandingankriteria.append(row)
# # Mencetak matriks perbandingankriteria
# for row in perbandingankriteria:
#     print(row)
# --------------------------------------------------------------------------------------------

totalkolom = []
for i in range(len(kriteria)):
    totalkolom.append(0)
    for j in range(len(perbandingankriteria)):
        totalkolom[i] = totalkolom[i] + perbandingankriteria[j][i]
print("")
print("Total Kolom:", totalkolom)


normalisasi = []
for i in range(len(perbandingankriteria)):
    normalisasi.append([])
    for j in range(len(kriteria)):
        normalisasi[i].append(0)
        normalisasi[i][j] = perbandingankriteria[i][j]/totalkolom[j]
print("")
print("Normalisasi:", normalisasi)


bobotprioritas = []
for i in range(len(normalisasi)):
    bobotprioritas.append(sum(normalisasi[i]) / len(kriteria))
print("")
print("Bobot Prioritas:", bobotprioritas)


consistencymeasure = []
for i in range(len(normalisasi)):
    consistencymeasure.append(sum([perbandingankriteria[i][j] * bobotprioritas[j] for j in range(len(kriteria))]) / bobotprioritas[i])
print("")
print("Consistency Measure (CM):", consistencymeasure)
LambdaMax = sum(consistencymeasure) / len(kriteria)
n = len(kriteria)
CI = (LambdaMax - n) / (n - 1)
print("Lambda Max:", LambdaMax)
print("Consistency Index (CI):", CI)
ratioindexsaaty = [0, 0, 0.58, 0.9, 1.12, 1.24, 1.32, 1.41, 1.46, 1.49]
RI = ratioindexsaaty[n-1]
print("Ratio Index (RI):", RI)
CR = CI / RI
konsistensi_status = "Konsisten" if 0 <= CR <= 0.1 else "Tidak Konsisten"
print("Consistency Ratio (CR):", CR, ">", konsistensi_status)



# PERHITUNGAN RANKING TOPSIS
pembagi = []
for i in range(len(kriteria)):
    pembagi.append(0)
    for j in range(len(alternatif)):
        pembagi[i] = pembagi[i] + (alternatifkriteria[j][i] * alternatifkriteria[j][i])
    pembagi[i] = pembagi[i]**(1/2.0)
print("")
print("Pembagi:", pembagi)


normalisasi_topsis = []
for i in range(len(alternatif)):
    normalisasi_topsis.append([])
    for j in range(len(kriteria)):
        normalisasi_topsis[i].append(0)
        normalisasi_topsis[i][j] = alternatifkriteria[i][j]/pembagi[j]
print("")
print("Normalisasi:", normalisasi_topsis)


terbobot = []
for i in range(len(alternatif)):
    terbobot.append([])
    for j in range(len(kriteria)):
            terbobot[i].append(0)
            terbobot[i][j] = normalisasi_topsis[i][j] * bobotprioritas[j]
print("")
print("Terbobot TOPSIS:", terbobot)


aplus = []
for i in range(len(kriteria)):
    aplus.append(0)
    if costbenefit[i] == 'cost':
        for j in range(len(alternatif)):
            if j == 0:
                aplus[i] = terbobot[j][i]
            else:
                if aplus[i] > terbobot[j][i]:
                     aplus[i] = terbobot[j][i]
    else: #costbenefit[i] == 'benefit':
        for j in range(len(alternatif)):
            if j == 0:
                aplus[i] = terbobot[j][i]
            else:
                if aplus[i] < terbobot[j][i]:
                     aplus[i] = terbobot[j][i]
print("")
print("A+:", aplus)


amin = []
for i in range(len(kriteria)):
    amin.append(0)
    if costbenefit[i] == 'cost':
        for j in range(len(alternatif)):
            if j == 0:
                amin[i] = terbobot[j][i]
            else:
                if amin[i] < terbobot[j][i]:
                     amin[i] = terbobot[j][i]
    else: #costbenefit[i] == 'benefit':
        for j in range(len(alternatif)):
            if j == 0:
                amin[i] = terbobot[j][i]
            else:
                if amin[i] > terbobot[j][i]:
                     amin[i] = terbobot[j][i]
print("")
print("A-:", amin)


dplus = []
for i in range(len(alternatif)):
    dplus.append(0)
    for j in range(len(kriteria)):
        dplus[i] = dplus[i] + ((aplus[j] - terbobot[i][j]) * (aplus[j] - terbobot[i][j]))
    dplus[i] = dplus[i]**(1/2.0)
print("")
print("D+:", dplus)


dmin = []
for i in range(len(alternatif)):
    dmin.append(0)
    for j in range(len(kriteria)):
        dmin[i] = dmin[i] + ((terbobot[i][j] - amin[j]) * (terbobot[i][j] - amin[j]))
    dmin[i] = dmin[i]**(1/2.0)
print("")
print("D-:", dmin)


hasil = []
for i in range(len(alternatif)):
    hasil.append(0)
    for j in range(len(kriteria)):
        hasil[i] = dmin[i] / (dmin[i] + dplus[i])
print("")
print("Hasil TOPSIS:", hasil)


alternatifranking = []
hasilranking = []
for i in range(len(alternatif)):
    hasilranking.append(hasil[i])
    alternatifranking.append(alternatif[i])
for i in range(len(alternatif)):
    for j in range(len(alternatif)):
        if j > i:
            if hasilranking[j] > hasilranking[i]:
                tmphasil = hasilranking[j]
                tmpalternatif = alternatifranking[j]
                hasilranking[j] = hasilranking[i]
                alternatifranking[j] = alternatifranking[i]
                hasilranking[i] = tmphasil
                alternatifranking[i] = tmpalternatif
print("")
print("Rank TOPSIS:", alternatifranking)
# print("Rank TOPSIS:", hasilranking)
formatted_hasilranking = [round(value, 3) for value in hasilranking]
print("Rank TOPSIS:", formatted_hasilranking)
print("")
