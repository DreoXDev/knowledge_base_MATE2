from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

lecture_reports = {
    "01_curve.pdf": "1_lezione_II_2022_23_SDM_ingestion_report.md",
    "02_funzioni_due_variabili_curve_livello.pdf": "2_lezione_funzioni_due_variabili_curve_livello_ingestion_report.md",
    "03_massimi_minimi_locali.pdf": "3_lezione_massimi_minimi_locali_ingestion_report.md",
    "04_superfici.pdf": "4_lezione_superfici_ingestion_report.md",
    "05_lagrange.pdf": "5_lezione_moltiplicatori_lagrange_ingestion_report.md",
    "06_massimi_minimi_assoluti_funzione_implicita.pdf": "6_lezione_massimi_minimi_assoluti_ingestion_report.md",
    "07_integrali_linea_I_specie.pdf": "7_lezione_integrali_linea_I_specie_ingestion_report.md",
    "08_integrali_linea_II_specie.pdf": "8_lezione_integrali_linea_II_specie_ingestion_report.md",
    "09_campi_conservativi_green.pdf": "9_lezione_campi_vettoriali_conservativi_ingestion_report.md",
    "10_integrali_multipli.pdf": "10_lezione_integrali_multipli_ingestion_report.md",
    "11_calcolo_vettoriale.pdf": "11_lezione_calcolo_vettoriale_ingestion_report.md",
    "1_lezione_II_2022_23_SDM.pdf": "1_lezione_II_2022_23_SDM_ingestion_report.md",
    "2_lezione_funzioni_due_variabili_curve_livello.pdf": "2_lezione_funzioni_due_variabili_curve_livello_ingestion_report.md",
    "3_lezione_massimi_minimi_locali.pdf": "3_lezione_massimi_minimi_locali_ingestion_report.md",
    "4_lezione_superfici.pdf": "4_lezione_superfici_ingestion_report.md",
    "5_lezione_moltiplicatori_lagrange.pdf": "5_lezione_moltiplicatori_lagrange_ingestion_report.md",
    "6_lezione_massimi_minimi_assoluti.pdf": "6_lezione_massimi_minimi_assoluti_ingestion_report.md",
    "7_lezione_integrali_linea_I_specie.pdf": "7_lezione_integrali_linea_I_specie_ingestion_report.md",
    "8_lezione_integrali_linea_II_specie.pdf": "8_lezione_integrali_linea_II_specie_ingestion_report.md",
    "9_lezione_campi_vettoriali_conservativi.pdf": "9_lezione_campi_vettoriali_conservativi_ingestion_report.md",
    "10_lezione_integrali_multipli.pdf": "10_lezione_integrali_multipli_ingestion_report.md",
    "11_lezione_calcolo_vettoriale.pdf": "11_lezione_calcolo_vettoriale_ingestion_report.md",
}

exam_cards = {
    "esame_2022_07_14.pdf": "2022_07_14.md",
    "esame_2022_09_24_or_27.pdf": "2022_09_24_or_27.md",
    "esame_2022_11_22.pdf": "2022_11_22.md",
    "esame_2023_02_22.pdf": "2023_02_22.md",
    "esame_2023_04_13.pdf": "2023_04_13.md",
    "esame_2023_07_19.pdf": "2023_07_19.md",
}

missing = []

for pdf, report in lecture_reports.items():
    pdf_path = ROOT / "01_sources" / "official_slides" / pdf
    report_path = ROOT / "02_ingestion_reports" / report
    if not pdf_path.exists() or not report_path.exists():
        missing.append((pdf, report, pdf_path.exists(), report_path.exists()))

for pdf, card in exam_cards.items():
    pdf_path = ROOT / "01_sources" / "exams" / pdf
    card_path = ROOT / "11_exams" / "by_year" / card
    if not pdf_path.exists() or not card_path.exists():
        missing.append((pdf, card, pdf_path.exists(), card_path.exists()))

if missing:
    print("MISSING source coverage:")
    for source, target, source_ok, target_ok in missing:
        print(f"{source} -> {target}: source={source_ok} target={target_ok}")
    raise SystemExit(1)

print("OK: source coverage complete.")
