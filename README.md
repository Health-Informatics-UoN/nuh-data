# NUH Data

Research datasets from **Nottingham University Hospitals NHS Trust (NUH)**, one of the largest acute NHS trusts in England, serving a population of approximately 2.5 million across Nottinghamshire and surrounding counties.

All datasets are pseudonymised research views. Access is subject to a formal data access request.

---

## Datasets

### Systemic Anti-Cancer Therapy (SACT)

> **2009–present · Quarterly**

Patient-level records of systemic anti-cancer treatments (chemotherapy, targeted therapies, immunotherapy, and other drug-based cancer treatments) administered.

**What it contains:**

| Domain | Detail |
|---|---|
| Patient | Pseudonymised NHS number, year and month of birth, gender, Lower Layer Super Output Area (LLSOA) |
| Diagnosis | Primary ICD diagnosis, ICD-O morphology, SNOMED CT diagnosis code |
| Regimen | Treatment regimen acronym, intent (curative/palliative/adjuvant), adjunctive therapy type, co-morbidity adjustment, clinical trial flag |
| Cycle | Cycle number, start date, weight, WHO performance status |
| Drug administration | Drug name (BNF), dm+d code, dose, unit of measurement, route of administration (coded and SNOMED CT), administration date, administering organisation |
| Outcomes | Dose reduction, regimen completion (curative), reason not completed, non-curative benefit, toxicity |

**Coding standards:** ICD-10, ICD-O-3, SNOMED CT, NHS dm+d

---

### Cancer Outcomes and Services Dataset (COSD)

> **Full cancer pathway · Nottinghamshire**

Patient-level records spanning the cancer care pathway at NUH.

**What it contains:**

| Domain | Detail |
|---|---|
| Patient | Pseudonymised NHS number and unique record ID, year and month of birth, gender, sexual orientation, ethnicity, GP practice, LLSOA |
| Referral and first seen | Source of referral, dates of first outpatient appointment and first cancer specialist review, organisation identifiers |
| Diagnosis | Primary ICD-10 diagnosis, ICD-O-3 morphology and topography, SNOMED CT diagnosis code, basis of diagnosis, tumour laterality, grade of differentiation, Ki-67, performance status |
| Non-primary pathway | Date of recurrence/relapse, original ICD-10 diagnosis, metastatic type and site (recurrence and progression), method of relapse detection, transformation morphology |
| Staging | Pre-treatment and integrated TNM stage (T/N/M categories and overall grouping), TNM edition and version, site-specific staging, staging organisation and date |
| Diagnostic procedures | Up to 3 procedures: OPCS-4 and SNOMED CT procedure codes, sentinel node biopsy outcome, organisation, date |
| Pathology | Secondary diagnoses, familial cancer syndrome, functional syndrome classification, metastatic type and site at diagnosis |
| Treatment | Up to 4 treatment episodes: modality, intent, adjunctive therapy, start and end dates, surgical procedures (OPCS-4 and SNOMED CT), surgeon identifiers, ASA score, surgical access, discharge destination |
| Observations | Height, weight, and BMI (up to 2 occasions) |
| Lifestyle | Tobacco smoking status and cessation, alcohol history, diabetes, menopausal status, physical activity |
| Holistic needs assessment | Assessment offered, care plan status and date, point of pathway, staff role (up to 2 assessments) |
| MDT | MDT discussion date, cancer care plan intent, planned treatment types, reason for no treatment; up to 10 MDT meetings with type and date |
| Acute oncology | Up to 3 acute oncology assessments: date, location, patient type, outcome |
| Laboratory results | LDH, beta-hCG, and AFP values (up to 3 occasions) |
| Imaging | Up to 10 imaging episodes: NICIP and SNOMED CT codes, modality, anatomical site, laterality, outcome, report text |

**Coding standards:** ICD-10, ICD-O-3, SNOMED CT, OPCS-4, NICIP

---

## Geographic and Temporal Coverage

| Dataset | Geography | Start | End | Frequency |
|---|---|---|---|---|
| SACT | Nottinghamshire, England | January 2009 | Ongoing | Quarterly |
| COSD | Nottinghamshire, England | January 2024 - December 2024 | Ongoing | TBC |

---

## Python Models

Pydantic v2 models for each dataset are published directly from this repository. Install with pip:

```bash
pip install git+https://github.com/Health-Informatics-UoN/nuh-data.git
```

Then validate or annotate your data against the schema:

```python
from nuh_data.datasets.sact import SACTResearchView
from nuh_data.datasets.cosd import COSDResearchView

# Validate a record — Pydantic will raise on type or enum mismatches
record = SACTResearchView(
    pseudo_nhs_number="abc123",
    administration_date="2023-06-01",
    drug_name="CARBOPLATIN",
    sact_administration_route="01",   # Intravenous
    intent_of_treatment="P",          # Palliative
)
```

Models are generated directly from the LinkML schemas, so field names, types, and permitted values stay in sync with the data dictionaries published in this repository.

---

## Documentation

Full data dictionaries and field-level documentation are published at **[health-informatics-uon.github.io/nuh-data](https://health-informatics-uon.github.io/nuh-data)**.
