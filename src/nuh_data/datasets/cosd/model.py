from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.11.0"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'annotations': {'access_request_type': {'tag': 'access_request_type',
                                             'value': 'Data Access Request'},
                     'access_status': {'tag': 'access_status',
                                       'value': 'In Progress'},
                     'created_by_name': {'tag': 'created_by_name',
                                         'value': 'Nottingham University Hospitals '
                                                  'NHS Trust'},
                     'data_custodian': {'tag': 'data_custodian',
                                        'value': 'Nottingham University Hospitals '
                                                 'NHS Trust'},
                     'data_standards': {'tag': 'data_standards',
                                        'value': 'COSD, OTHER'},
                     'geographic_coverage': {'tag': 'geographic_coverage',
                                             'value': 'Nottinghamshire, England'}},
     'created_by': 'https://github.com/Health-Informatics-UoN',
     'default_prefix': 'cosd',
     'default_range': 'string',
     'description': 'Clinical dataset documenting cancer outcomes and services for '
                    'patients diagnosed and treated at Nottingham University '
                    'Hospitals NHS Trust. Covers the full cancer pathway from '
                    'referral through diagnosis, staging, treatment, and '
                    'follow-up, including both primary and non-primary '
                    '(recurrence/relapse) pathways.',
     'id': 'https://health-informatics-uon.github.io/nuh-data/datasets/cosd',
     'imports': ['linkml:types'],
     'keywords': ['cancer outcomes',
                  'COSD',
                  'oncology',
                  'NHS',
                  'Nottingham',
                  'cancer pathway',
                  'clinical'],
     'license': 'https://opensource.org/license/mit',
     'name': 'cosd',
     'prefixes': {'ICD': {'prefix_prefix': 'ICD',
                          'prefix_reference': 'http://id.who.int/icd/entity/'},
                  'NICIP': {'prefix_prefix': 'NICIP',
                            'prefix_reference': 'https://www.datadictionary.nhs.uk/nhs_business_definitions/nicip_code/'},
                  'OPCS': {'prefix_prefix': 'OPCS',
                           'prefix_reference': 'https://datadictionary.nhs.uk/attributes/opcs_code/'},
                  'SNOMED': {'prefix_prefix': 'SNOMED',
                             'prefix_reference': 'http://snomed.info/id/'},
                  'cosd': {'prefix_prefix': 'cosd',
                           'prefix_reference': 'https://health-informatics-uon.github.io/nuh-data/datasets/cosd/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'}},
     'source_file': 'schemas/datasets/cosd/cosd.yaml',
     'title': 'NUH Cancer Outcomes and Services Dataset (COSD)'} )

class AdjunctiveTherapy(str, Enum):
    """
    Adjunctive therapy is therapy given in addition to the main therapy to maximize its effectiveness.
This field allows for the accurate recording of these to determine if Adjunctive therapy was Adjuvant (After the main therapy) or Neo-Adjuvant (Before the main therapy) or not applicable.
    """
    number_1 = "1"
    """
    Adjuvant
    """
    number_2 = "2"
    """
    Neoadjuvant
    """
    number_3 = "3"
    """
    Not Applicable (Primary Treatment)
    """
    number_9 = "9"
    """
    Not Known
    """


class AnatomicalSideImaging(str, Enum):
    """
    The side of the body that is the subject of an Imaging or Radiodiagnostic Event.
    """
    L = "L"
    """
    Left
    """
    R = "R"
    """
    Right
    """
    M = "M"
    """
    Midline
    """
    B = "B"
    """
    Bilateral
    """
    number_8 = "8"
    """
    Not applicable
    """
    number_9 = "9"
    """
    Not Known
    """


class AsaScore(str, Enum):
    """
    The ASA physical status classification system is a system for assessing the fitness of patients before surgery.
    """
    number_1 = "1"
    """
    A normal healthy patient.
    """
    number_2 = "2"
    """
    A patient with mild systemic disease.
    """
    number_3 = "3"
    """
    A patient with severe systemic disease.
    """
    number_4 = "4"
    """
    A patient with severe systemic disease that is a constant threat to life.
    """
    number_5 = "5"
    """
    A moribund patient who is not expected to survive without the operation.
    """
    number_6 = "6"
    """
    A declared brain-dead patient whose organs are being removed for donor purposes.
    """


class AssessmentCarePlanPointOfPathway(str, Enum):
    """
    The point of the pathway where a Holistic Needs Assessment or Personalised Care and Support Plan is offered, declined, completed, not required, or unable to be completed
    """
    number_01 = "01"
    """
    Initial cancer diagnosis
    """
    number_02 = "02"
    """
    Start of treatment
    """
    number_03 = "03"
    """
    During treatment
    """
    number_04 = "04"
    """
    End of treatment
    """
    number_05 = "05"
    """
    Diagnosis of recurrence
    """
    number_06 = "06"
    """
    Transition to palliative care
    """
    number_07 = "07"
    """
    Prehabilitation
    """
    number_08 = "08"
    """
    In palliative or end of life care
    """
    number_97 = "97"
    """
    Other
    """


class AssessmentCarePlanStatus(str, Enum):
    """
    An indication of whether a PATIENT has completed a Holistic Needs Assessment (HNA) and /or Personalised Care and Support Plan (PCSP) was offered/completed
    """
    number_01 = "01"
    """
    Assessment completed and care plan not offered
    """
    number_02 = "02"
    """
    Assessment completed and care plan offered
    """
    number_03 = "03"
    """
    Assessment completed and care plan completed
    """
    number_04 = "04"
    """
    Assessment completed and care plan declined
    """
    number_05 = "05"
    """
    Assessment completed and care plan unable to be completed
    """
    number_06 = "06"
    """
    Assessment completed and care plan not required (no concerns from HNA)
    """


class AssessmentLocation(str, Enum):
    """
    The location where the Acute Oncology (AO) assessment was performed within the health care provider
    """
    number_01 = "01"
    """
    Emergency Care Department
    """
    number_02 = "02"
    """
    Medical Assessment Unit
    """
    number_03 = "03"
    """
    Same Day Emergency Care Service
    """
    number_04 = "04"
    """
    Ward
    """
    number_05 = "05"
    """
    Out-Patient Clinic
    """
    number_06 = "06"
    """
    Dedicated Acute Oncology Bed/Chair
    """
    number_07 = "07"
    """
    Day Case Unit
    """
    number_08 = "08"
    """
    Chemotherapy Unit
    """
    number_09 = "09"
    """
    Health Care Provider Telephone Assessment
    """
    number_10 = "10"
    """
    Radiotherapy Department
    """
    number_97 = "97"
    """
    Other
    """
    number_98 = "98"
    """
    Other
    """


class AssessmentOffered(str, Enum):
    """
    An indication of whether a PATIENT has been offered a Holistic Needs Assessment (HNA)
    """
    number_01 = "01"
    """
    Offered and Undecided
    """
    number_02 = "02"
    """
    Offered and Declined
    """
    number_03 = "03"
    """
    Offered and Accepted
    """
    number_04 = "04"
    """
    Not Offered
    """
    number_05 = "05"
    """
    Offered but Patient Unable to Complete
    """


class BasisOfDiagnosisCancer(str, Enum):
    """
    This is the method used to confirm the cancer.
    """
    number_0 = "0"
    """
    Death certificate only (DCO): Information provided is from a death certificate
    """
    number_1 = "1"
    """
    Clinical: Diagnosis made before death, but without any of the following codes
    """
    number_2 = "2"
    """
    Clinical Investigation: All diagnostic techniques, including X-ray, endoscopy, imaging, ultrasound, exploratory surgery (such as laparotomy), and autopsy, without a tissue diagnosis
    """
    number_4 = "4"
    """
    Specific tumour markers: Includes biochemical and/or immunological markers which are specific for a tumour site
    """
    number_5 = "5"
    """
    Cytology: Examination of cells from a primary or secondary site, including fluids aspirated by endoscopy or needle; also includes the microscopic examination of peripheral blood and bone marrow aspirates, immunophenotyping by flow cytometry and a liquid biopsy in the absence of pathology
    """
    number_6 = "6"
    """
    Histology of a metastasis
    """
    number_7 = "7"
    """
    Histology of a primary tumour
    """
    number_7FULL_STOP1 = "7.1"
    """
    Histology of the primary tumour: Histologic examination of tissue from the primary tumour, however obtained, including all cutting techniques and bone marrow biopsies
    """
    number_7FULL_STOP2 = "7.2"
    """
    Histology of a metastasis: No histology of the primary tumour
    """
    number_7FULL_STOP3 = "7.3"
    """
    Histology at autopsy: No histology before autopsy
    """
    number_8 = "8"
    """
    Cytogenetic and/or molecular testing: Detection of tumour-specific genetic abnormalities or genetic changes in the tumour, including techniques such as karyotyping, FISH (fluorescent in situ hybridization), PCR (polymerase chain reaction), DNA sequencing
    """
    number_9 = "9"
    """
    Unknown: No information on how the diagnosis has been made (e.g. PAS or HISS record only)
    """


class CancerCarePlanIntent(str, Enum):
    """
    The intention of a Cancer Care Plan developed within a Cancer Care Spell.
    """
    C = "C"
    """
    Curative
    """
    Z = "Z"
    """
    Non Curative
    """
    X = "X"
    """
    No active treatment
    """
    number_9 = "9"
    """
    Not Known
    """


class CancerImagingModality(str, Enum):
    """
    The type of imaging procedure used during an Imaging or Radiodiagnostic Event for a Cancer Care Spell. NB: PET Scan also includes PET-CT Scan.
    """
    C01X = "C01X"
    """
    Standard Radiography
    """
    C01M = "C01M"
    """
    Mammogram
    """
    C02X = "C02X"
    """
    CT Scan
    """
    C02C = "C02C"
    """
    Virtual colonoscopy
    """
    C03X = "C03X"
    """
    MRI Scan
    """
    C04X = "C04X"
    """
    PET Scan
    """
    C05X = "C05X"
    """
    Ultrasound Scan
    """
    C06X = "C06X"
    """
    Nuclear Medicine imaging
    """
    C08A = "C08A"
    """
    Angiography
    """
    C08B = "C08B"
    """
    Barium
    """
    C08U = "C08U"
    """
    Urography (IV and retrograde)
    """
    C09X = "C09X"
    """
    Intervention radiography
    """
    CXXX = "CXXX"
    """
    Other
    """


class CancerTreatmentIntent(str, Enum):
    """
    The intention of the cancer treatment provided during a Cancer Care Spell.
* Disease Modification is Drug Specific ** Diagnostic and Staging are Surgery Specific
    """
    number_01 = "01"
    """
    Curative
    """
    number_02 = "02"
    """
    Palliative
    """
    number_03 = "03"
    """
    Disease Modification *
    """
    number_04 = "04"
    """
    Diagnostic **
    """
    number_05 = "05"
    """
    Staging **
    """
    number_06 = "06"
    """
    Uncertain of Treatment Intent
    """
    number_09 = "09"
    """
    Not Known
    """
    number_98 = "98"
    """
    Other
    """


class CancerTreatmentModalityRegistration(str, Enum):
    """
    The type of treatment or care which was delivered in a Cancer Treatment Period.
This is subset of Cancer Treatment Modality, which supports Cancer Registration in England
    """
    number_01 = "01"
    """
    Surgery
    """
    number_02 = "02"
    """
    Anti-cancer drug regimen (Cytotoxic Chemotherapy)
    """
    number_03 = "03"
    """
    Anti-cancer drug regimen (Hormone Therapy)
    """
    number_04 = "04"
    """
    Chemoradiotherapy
    """
    number_05 = "05"
    """
    External Beam Radiotherapy (excluding Proton Therapy)
    """
    number_06 = "06"
    """
    Brachytherapy
    """
    number_07 = "07"
    """
    Specialist Palliative Care
    """
    number_08 = "08"
    """
    Active Monitoring (excluding non-specialist Palliative Care)
    """
    number_09 = "09"
    """
    Non-specialist Palliative Care (excluding Active Monitoring)
    """
    number_10 = "10"
    """
    Radio Frequency Ablation (RFA)
    """
    number_11 = "11"
    """
    High Intensity Focussed Ultrasound (HIFU)
    """
    number_12 = "12"
    """
    Cryotherapy
    """
    number_13 = "13"
    """
    Proton Therapy
    """
    number_14 = "14"
    """
    Anti-cancer drug regimen (other)
    """
    number_15 = "15"
    """
    Anti-cancer drug regimen (Immunotherapy)
    """
    number_16 = "16"
    """
    Light Therapy (including Photodynamic Therapy and Psoralen and Ultra Violet A (PUVA) Therapy)
    """
    number_17 = "17"
    """
    Hyperbaric Oxygen Therapy
    """
    number_19 = "19"
    """
    Radioisotope Therapy (including Radioiodine)
    """
    number_20 = "20"
    """
    Laser Treatment (including Argon Beam therapy)
    """
    number_21 = "21"
    """
    Biological Therapies (excluding Immunotherapy)
    """
    number_22 = "22"
    """
    Radiosurgery
    """
    number_97 = "97"
    """
    Other Treatment (not listed)
    """
    number_98 = "98"
    """
    All treatment declined
    """


class ClinicalNurseSpecialistIndicationCode(str, Enum):
    """
    Record if and when the patient saw an appropriate site specific clinical nurse specialist.
    """
    Y1 = "Y1"
    """
    Yes - Clinical Nurse Specialist present when PATIENT given diagnosis
    """
    Y3 = "Y3"
    """
    Yes - Clinical Nurse Specialist not present when PATIENT given diagnosis but saw PATIENT during same Consultant Clinic Session
    """
    Y4 = "Y4"
    """
    Yes - Clinical Nurse Specialist not present during Consultant Clinic Session when PATIENT given diagnosis but saw PATIENT at other time
    """
    Y5 = "Y5"
    """
    Yes - Clinical Nurse Specialist not present when PATIENT given diagnosis but the patient was seen by a trained member of the Clinical Nurse Specialist team
    """
    NI = "NI"
    """
    No - PATIENT not seen at all by Clinical Nurse Specialist but Clinical Nurse Specialist informed of diagnosis
    """
    NN = "NN"
    """
    No - PATIENT not seen at all by Clinical Nurse Specialist and Clinical Nurse Specialist not informed of diagnosis
    """
    number_99 = "99"
    """
    Not Known (Not recorded)
    """


class DestinationOfDischargeHospitalProviderSpell(str, Enum):
    """
    This records the destination of a PATIENT on completion of the Hospital Provider Spell. It can also indicate that the PATIENT died.
    """
    number_19 = "19"
    """
    Usual place of residence unless listed below, for example, a private dwelling whether owner occupied or owned by Local Authority, housing association or other landlord. This includes wardened accommodation but not residential accommodation where health care is provided. It also includes PATIENTS with no fixed abode.
    """
    number_29 = "29"
    """
    Temporary place of residence when usually resident elsewhere (includes hotel, residential educational establishment)
    """
    number_30 = "30"
    """
    Repatriation from high security psychiatric accommodation in an NHS Hospital Provider (NHS Trust or NHS Foundation Trust)
    """
    number_37 = "37"
    """
    Court
    """
    number_40 = "40"
    """
    Penal establishment
    """
    number_42 = "42"
    """
    Police Station / Police Custody Suite
    """
    number_48 = "48"
    """
    High Security Psychiatric Hospital, Scotland
    """
    number_49 = "49"
    """
    NHS other hospital provider - high security psychiatric accommodation
    """
    number_50 = "50"
    """
    NHS other hospital provider - medium secure unit
    """
    number_51 = "51"
    """
    NHS other hospital provider - ward for general PATIENTS or the younger physically disabled
    """
    number_52 = "52"
    """
    NHS other hospital provider - ward for maternity PATIENTS or neonates
    """
    number_53 = "53"
    """
    NHS other hospital provider - ward for PATIENTS who are mentally ill or have learning disabilities
    """
    number_55 = "55"
    """
    Care Home With Nursing
    """
    number_56 = "56"
    """
    Care Home Without Nursing
    """
    number_66 = "66"
    """
    Local Authority foster care
    """
    number_79 = "79"
    """
    PATIENT died or still birth
    """
    number_84 = "84"
    """
    Independent Sector Healthcare Provider run hospital - medium secure unit
    """
    number_87 = "87"
    """
    Independent Sector Healthcare Provider run hospital - excluding medium secure unit
    """
    number_88 = "88"
    """
    Hospice
    """
    number_89 = "89"
    """
    ORGANISATION responsible for forced repatriation
    """
    number_98 = "98"
    """
    Not applicable - Hospital Provider Spell not finished at episode end (i.e. not discharged) or current episode unfinished
    """
    number_99 = "99"
    """
    DESTINATION OF DISCHARGE not known
    """


class DiabetesMellitusType1AndType2Indicator(str, Enum):
    """
    Does the patient have a diagnosis of type 1 or type 2 diabetes mellitus?
    """
    number_1 = "1"
    """
    Type 1 diabetes mellitus
    """
    number_2 = "2"
    """
    Type 2 diabetes mellitus
    """
    number_3 = "3"
    """
    Other diabetes mellitus not categorised as type 1 or type 2
    """
    number_4 = "4"
    """
    No patient diagnosis of diabetes mellitus has been made
    """
    number_9 = "9"
    """
    Not known
    """


class EthnicCategory(str, Enum):
    """
    The ethnicity of a PERSON, as specified by the PERSON. The 16+1 ethnic data categories defined in the 2001 census is the national mandatory standard for the collection and analysis of ethnicity.
(The Office for National Statistics has developed a further breakdown of the group from that given, which may be used locally.)
    """
    A = "A"
    """
    (White) British
    """
    B = "B"
    """
    (White) Irish
    """
    C = "C"
    """
    Any other White background
    """
    D = "D"
    """
    White and Black Caribbean
    """
    E = "E"
    """
    White and Black African
    """
    F = "F"
    """
    White and Asian
    """
    G = "G"
    """
    Any other mixed background
    """
    H = "H"
    """
    Indian
    """
    J = "J"
    """
    Pakistani
    """
    K = "K"
    """
    Bangladeshi
    """
    L = "L"
    """
    Any other Asian background
    """
    M = "M"
    """
    Caribbean
    """
    N = "N"
    """
    African
    """
    P = "P"
    """
    Any other Black background
    """
    R = "R"
    """
    Chinese
    """
    S = "S"
    """
    Any other ethnic group
    """
    Z = "Z"
    """
    Not stated
    """
    number_99 = "99"
    """
    Not Known
    """


class FamilialCancerSyndrome(str, Enum):
    """
    Indicate whether there is a possible or confirmed familial cancer syndrome
    """
    Y = "Y"
    """
    Yes
    """
    N = "N"
    """
    No
    """
    P = "P"
    """
    Possible
    """
    number_9 = "9"
    """
    Not Known
    """


class FunctionalSyndromeClassificationIndicator(str, Enum):
    """
    Indicate whether there is a possible or confirmed Functional syndrome classification
    """
    Y = "Y"
    """
    Yes
    """
    N = "N"
    """
    No
    """
    number_9 = "9"
    """
    Not Known
    """


class FunctionalSyndromeClassificationType(str, Enum):
    """
    Specify the type of functional syndrome classification the patient is diagnosed with.
For Neuroendocrine tumours (NET) only.
    """
    number_98 = "98"
    """
    Other functional syndrome
    """


class GradeOfDifferentiationAtDiagnosis(str, Enum):
    """
    GRADE OF DIFFERENTIATION (AT DIAGNOSIS) is the definitive grade of the Tumour at the time of PATIENT DIAGNOSIS.
    """
    GX = "GX"
    """
    Grade of differentiation is not appropriate or cannot be assessed
    """
    G1 = "G1"
    """
    Well differentiated
    """
    G2 = "G2"
    """
    Moderately differentiated
    """
    G3 = "G3"
    """
    Poorly differentiated
    """
    G4 = "G4"
    """
    Undifferentiated / anaplastic
    """


class HistoryOfAlcoholCurrent(str, Enum):
    """
    Specify the current history of alcohol consumption for the patient (≤3 months) from date of diagnosis
These are based on the UK Chief Medical Officers' Alcohol Guideline Review (Jan 2016)
    """
    number_1 = "1"
    """
    Heavy (>14 Units per week)
    """
    number_2 = "2"
    """
    Light (≤14 Units per week)
    """
    number_3 = "3"
    """
    None in this period
    """
    Z = "Z"
    """
    Not Stated (Patient asked but declined to provide a response)
    """
    number_9 = "9"
    """
    Not Known (Not recorded)
    """


class HistoryOfAlcoholPast(str, Enum):
    """
    Specify the past history of alcohol consumption for the patient (>3 months) from date of diagnosis
These are based on the UK Chief Medical Officers' Alcohol Guideline Review (Jan 2016)
    """
    number_1 = "1"
    """
    Heavy (>14 Units per week)
    """
    number_2 = "2"
    """
    Light (≤14 Units per week)
    """
    number_3 = "3"
    """
    None ever
    """
    Z = "Z"
    """
    Not Stated (Patient asked but declined to provide a response)
    """
    number_9 = "9"
    """
    Not Known (Not recorded)
    """


class ImagingOutcome(str, Enum):
    """
    Record the outcome for the imaging event as agreed with the radiologist or clinical team
    """
    number_01 = "01"
    """
    Abnormal
    """
    number_02 = "02"
    """
    Normal
    """
    number_03 = "03"
    """
    Benign
    """
    number_04 = "04"
    """
    Non-Diagnostic
    """
    number_05 = "05"
    """
    Inadequate
    """
    number_09 = "09"
    """
    Not Known
    """


class MenopausalStatus(str, Enum):
    """
    Record the Menopausal Status (at the point of diagnosis) of female patients only
    """
    number_1 = "1"
    """
    Premenopausal
    """
    number_2 = "2"
    """
    Perimenopausal
    """
    number_3 = "3"
    """
    Postmenopausal
    """
    number_9 = "9"
    """
    Not Known
    """


class MetastaticSite(str, Enum):
    """
    The site of the metastatic disease, if any
More than one site can be recorded
    """
    number_02 = "02"
    """
    Brain
    """
    number_03 = "03"
    """
    Liver
    """
    number_04 = "04"
    """
    Lung
    """
    number_07 = "07"
    """
    Unknown metastatic site
    """
    number_08 = "08"
    """
    Skin
    """
    number_09 = "09"
    """
    Distant lymph nodes
    """
    number_10 = "10"
    """
    Bone (excluding Bone Marrow)
    """
    number_11 = "11"
    """
    Bone marrow
    """
    number_12 = "12"
    """
    Regional lymph nodes
    """
    number_97 = "97"
    """
    Not Applicable
    """
    number_98 = "98"
    """
    Other metastatic site
    """


class MetastaticType(str, Enum):
    """
    Indicate the type of metastatic disease diagnosed by the clinical team
    """
    number_01 = "01"
    """
    Local
    """
    number_02 = "02"
    """
    Regional
    """
    number_03 = "03"
    """
    Distant
    """


class MultidisciplinaryTeamMeetingDiscussion(str, Enum):
    """
    Record if the patient was not discussed within a MDT Meeting
    """
    number_1 = "1"
    """
    Not discussed
    """
    number_2 = "2"
    """
    Discussion Status Not Known
    """


class MultidisciplinaryTeamMeetingDiscussionType(str, Enum):
    """
    Record if the patient was discussed within a Multidisciplinary Team Meeting (MDTM)
    """
    number_1 = "1"
    """
    Discussed within Trust MDTM
    """
    number_2 = "2"
    """
    Patient on predefined Standard of Care
    """
    number_3 = "3"
    """
    Discussed at MDTM at another Trust
    """


class MultidisciplinaryTeamMeetingType(str, Enum):
    """
    Record the type of MDT meeting at which the patient was discussed. Please provide the most detailed level of information that is possible.
Note: the codes at the high level (shown in bold) are Tumour groups and the items below each high-level code are Multidisciplinary Teams. ORGANISATIONS should only use the high-level code if the Multidisciplinary Team is not listed.
    """
    number_0100 = "0100"
    """
    Breast
    """
    number_0101 = "0101"
    """
    Breast MDT
    """
    number_0102 = "0102"
    """
    Metastatic Breast MDT
    """
    number_0200 = "0200"
    """
    Brain/Central Nervous System
    """
    number_0201 = "0201"
    """
    Brain Central Nervous System (CNS)/Neuroscience MDT
    """
    number_0202 = "0202"
    """
    Rehabilitation and Non-Surgical (Network) MDT
    """
    number_0203 = "0203"
    """
    Pituitary MDT
    """
    number_0204 = "0204"
    """
    Skull base MDT
    """
    number_0205 = "0205"
    """
    Spinal cord MDT
    """
    number_0206 = "0206"
    """
    Low grade glioma MDT
    """
    number_0207 = "0207"
    """
    Metastasis to brain MDT
    """
    number_0208 = "0208"
    """
    Stereotactic Radiosurgery (SRS) MDT
    """
    number_0209 = "0209"
    """
    Genetic subtypes MDT
    """
    number_0300 = "0300"
    """
    Colorectal
    """
    number_0301 = "0301"
    """
    Colorectal MDT
    """
    number_0302 = "0302"
    """
    Anal MDT
    """
    number_0400 = "0400"
    """
    CTYA
    """
    number_0401 = "0401"
    """
    Paediatric Combined Diagnostic and Treatment MDT
    """
    number_0402 = "0402"
    """
    Paediatric Haematology only MDT
    """
    number_0403 = "0403"
    """
    Paediatric non-CNS solid tumours only MDT
    """
    number_0404 = "0404"
    """
    Paediatric CNS malignancy only MDT
    """
    number_0405 = "0405"
    """
    Paediatric Late Effects MDT
    """
    number_0406 = "0406"
    """
    Paediatric (POSCU) MDT
    """
    number_0407 = "0407"
    """
    Teenage and Young Adult MDT
    """
    number_0408 = "0408"
    """
    Teenage and Young Adult Late Effects MDT
    """
    number_0500 = "0500"
    """
    Gynaecology
    """
    number_0501 = "0501"
    """
    Gynaecology local MDT
    """
    number_0502 = "0502"
    """
    Gynaecology Specialist MDT
    """
    number_0600 = "0600"
    """
    Haematology
    """
    number_0601 = "0601"
    """
    Haematology MDT
    """
    number_0602 = "0602"
    """
    Lymphoma MDT
    """
    number_0603 = "0603"
    """
    Plasma Cell MDT
    """
    number_0604 = "0604"
    """
    Myeloid MDT
    """
    number_0605 = "0605"
    """
    Bone marrow transplant MDT
    """
    number_0700 = "0700"
    """
    Head and Neck (including Thyroid)
    """
    number_0701 = "0701"
    """
    Upper Aerodigestive Tract (UAT) only MDT
    """
    number_0702 = "0702"
    """
    Upper Aerodigestive Tract (UAT) and Thyroid MDT
    """
    number_0703 = "0703"
    """
    Thyroid Only MDT
    """
    number_0800 = "0800"
    """
    Lung
    """
    number_0801 = "0801"
    """
    Lung MDT
    """
    number_0802 = "0802"
    """
    Mesothelioma Specialist MDT
    """
    number_0900 = "0900"
    """
    Sarcoma
    """
    number_0901 = "0901"
    """
    Bone and Soft tissue MDT
    """
    number_0902 = "0902"
    """
    Bone MDT
    """
    number_0903 = "0903"
    """
    Soft tissue MDT
    """
    number_1000 = "1000"
    """
    Skin
    """
    number_1001 = "1001"
    """
    Skin Local MDT
    """
    number_1002 = "1002"
    """
    Skin Specialist MDT
    """
    number_1003 = "1003"
    """
    Melanoma MDT
    """
    number_1004 = "1004"
    """
    Supra T-Cell Lymphoma MDT
    """
    number_1100 = "1100"
    """
    Upper GI
    """
    number_1101 = "1101"
    """
    Upper GI Local MDT
    """
    number_1102 = "1102"
    """
    Oesophago-Gastric Specialist MDT
    """
    number_1103 = "1103"
    """
    Hepatobiliary and Pancreatic (HPB) Specialist MDT
    """
    number_1104 = "1104"
    """
    Pancreatic/Biliary (PB) Specialist MDT
    """
    number_1105 = "1105"
    """
    Hepatic Specialist MDT
    """
    number_1200 = "1200"
    """
    Urology
    """
    number_1201 = "1201"
    """
    Urology Local MDT
    """
    number_1202 = "1202"
    """
    Urology Specialist MDT
    """
    number_1203 = "1203"
    """
    Testicular Supranetwork MDT
    """
    number_1204 = "1204"
    """
    Penile Supranetwork MDT
    """
    number_1300 = "1300"
    """
    Other
    """
    number_1301 = "1301"
    """
    CUP MDT
    """
    number_1302 = "1302"
    """
    Neuroendocrine MDT
    """
    number_1303 = "1303"
    """
    Palliative Care MDT
    """
    number_1304 = "1304"
    """
    Enhanced Supportive Care MDT
    """
    number_1305 = "1305"
    """
    Stereotactic Radiotherapy (SRT) only (all sites)
    """
    number_1306 = "1306"
    """
    Adrenal MDT
    """


class NhsNumberStatusIndicatorCode(str, Enum):
    """
    The NHS NUMBER STATUS INDICATOR CODE is the trace status of the NHS NUMBER
    """
    number_01 = "01"
    """
    Number present and verified
    """
    number_02 = "02"
    """
    Number present but not traced
    """
    number_03 = "03"
    """
    Trace required
    """
    number_04 = "04"
    """
    Trace attempted - No match or multiple match found
    """
    number_05 = "05"
    """
    Trace needs to be resolved - (NHS Number or PATIENT detail conflict)
    """
    number_06 = "06"
    """
    Trace in progress
    """
    number_07 = "07"
    """
    Number not present and trace not required
    """
    number_08 = "08"
    """
    Trace postponed (baby under six weeks old)
    """


class NoCancerTreatmentReason(str, Enum):
    """
    The main reason why no active cancer treatment is specified within a Cancer Care Plan.
    """
    number_01 = "01"
    """
    Patient declined treatment
    """
    number_02 = "02"
    """
    Unfit: poor performance status
    """
    number_03 = "03"
    """
    Unfit: significant co-morbidity
    """
    number_04 = "04"
    """
    Unfit: advanced stage cancer
    """
    number_05 = "05"
    """
    Unknown primary site
    """
    number_06 = "06"
    """
    Died before treatment
    """
    number_07 = "07"
    """
    No active treatment available
    """
    number_08 = "08"
    """
    Other
    """
    number_10 = "10"
    """
    Monitoring only
    """
    number_99 = "99"
    """
    Not Known
    """


class Outcome(str, Enum):
    """
    Record the outcome of the acute oncology episode
    """
    number_1 = "1"
    """
    Not Admitted
    """
    number_2 = "2"
    """
    Admitted
    """
    number_3 = "3"
    """
    Remained Admitted
    """
    number_4 = "4"
    """
    Discharged
    """
    number_5 = "5"
    """
    Patient Died
    """
    number_8 = "8"
    """
    Other
    """
    number_10 = "10"
    """
    Not Admitted
    """
    number_11 = "11"
    """
    Admitted
    """
    number_12 = "12"
    """
    Remained Admitted
    """
    number_13 = "13"
    """
    Discharged from hospital
    """
    number_14 = "14"
    """
    Patient Died
    """
    number_15 = "15"
    """
    Advised to attend for assessment
    """
    number_16 = "16"
    """
    Discharged from acute oncology service (AOS)
    """
    number_17 = "17"
    """
    Discharged to specialist centre
    """
    number_18 = "18"
    """
    Telephone Assessment
    """
    number_98 = "98"
    """
    Other
    """


class PalliativeCareSpecialistSeenIndicatorCancerRecurrence(str, Enum):
    """
    Record whether the patient was seen by a palliative care specialist. This would be a member of the specialist palliative care team led by a consultant in palliative medicine for a recurrence of cancer.
    """
    Y = "Y"
    """
    Yes
    """
    N = "N"
    """
    No
    """
    number_9 = "9"
    """
    Not Known
    """


class PatientType(str, Enum):
    """
    Record the type each patient presentation is grouped within, as a result of the acute oncology assessment.
A table is available within the user guide to provide additional information.
    """
    number_01 = "01"
    """
    New Presentation
    """
    number_02 = "02"
    """
    Treatment Complication
    """
    number_03 = "03"
    """
    Suspected or Confirmed Neutropenic Sepsis
    """
    number_04 = "04"
    """
    Cancer Complication
    """
    number_05 = "05"
    """
    Cancer Recurrence/Progression (Local or Regional)
    """
    number_06 = "06"
    """
    Cancer Recurrence/Progression (Distant)
    """
    number_07 = "07"
    """
    Cancer Transformation
    """
    number_08 = "08"
    """
    Suspected or Confirmed Metastatic Spinal Cord Compression (MSCC)
    """
    number_09 = "09"
    """
    Comorbidity Complications
    """
    number_98 = "98"
    """
    Other
    """


class PerformanceStatusAdult(str, Enum):
    """
    A World Health Organisation classification indicating a PERSON's status relating to activity / disability.
    """
    number_0 = "0"
    """
    Able to carry out all normal activity without restriction
    """
    number_1 = "1"
    """
    Restricted in strenuous activity but ambulatory and able to carry out light work
    """
    number_2 = "2"
    """
    Ambulatory and capable of all self-care but unable to carry out any work activities; up and about more than 50% of waking hours
    """
    number_3 = "3"
    """
    Symptomatic and in a chair or in bed for greater than 50% of the day but not bedridden
    """
    number_4 = "4"
    """
    Completely disabled; cannot carry out any self-care; totally confined to bed or chair
    """
    number_9 = "9"
    """
    Not recorded
    """


class PersonSexualOrientationCodeAtDiagnosis(str, Enum):
    """
    Person's sexual orientation as self-declared at the time of the PATIENT DIAGNOSIS.
This complies with the information standard DCB2094.
    """
    number_1 = "1"
    """
    Heterosexual or Straight
    """
    number_2 = "2"
    """
    Gay or Lesbian
    """
    number_3 = "3"
    """
    Bisexual
    """
    number_4 = "4"
    """
    Other sexual orientation not listed
    """
    U = "U"
    """
    PERSON asked and does not know or is not sure
    """
    Z = "Z"
    """
    Not Stated (PERSON asked but declined to provide a response)
    """
    number_9 = "9"
    """
    Not Known (Not Recorded)
    """


class PersonStatedGenderCode(str, Enum):
    """
    Person's gender as self-declared (or inferred by observation for those unable to declare their PERSON STATED GENDER).
    """
    number_1 = "1"
    """
    Male
    """
    number_2 = "2"
    """
    Female
    """
    number_9 = "9"
    """
    Indeterminate (Unable to be classified as either male or female)
    """
    X = "X"
    """
    Not Known (PERSON STATED GENDER CODE not recorded)
    """


class PhysicalActivityCurrent(str, Enum):
    """
    Specify the current physical activity level
    """
    number_1 = "1"
    """
    Achieves guidance level of physical activity
    """
    number_2 = "2"
    """
    Does not achieve guidance level of physical activity
    """
    Z = "Z"
    """
    Not Stated (Patient asked but declined to provide a response)
    """
    number_9 = "9"
    """
    Not Known (Not recorded)
    """


class PlannedCancerTreatmentType(str, Enum):
    """
    This is the clinically proposed treatment, usually agreed at a Multi Disciplinary Team Meeting, and may not be the same as the treatment which is subsequently agreed with the patient. More than one planned treatment type may be recorded and these may either be alternative or sequential treatments.
    """
    number_01 = "01"
    """
    Surgery
    """
    number_02 = "02"
    """
    External Beam Radiotherapy (excluding Proton Therapy)
    """
    number_03 = "03"
    """
    Chemotherapy
    """
    number_04 = "04"
    """
    Hormone therapy
    """
    number_05 = "05"
    """
    Specialist palliative care
    """
    number_06 = "06"
    """
    Brachytherapy
    """
    number_07 = "07"
    """
    Biological Therapy
    """
    number_10 = "10"
    """
    Other Active Treatment
    """
    number_11 = "11"
    """
    No active treatment
    """
    number_12 = "12"
    """
    Bisphosphonates
    """
    number_13 = "13"
    """
    Anti Cancer Drug - Other
    """
    number_14 = "14"
    """
    Radiotherapy - Other
    """
    number_99 = "99"
    """
    Not Known
    """


class ProfessionalRegistrationIssuerCodeConsultantFirstSeen(str, Enum):
    """
    A code which identifies the PROFESSIONAL REGISTRATION BODY for the Consultant or health care professional who first sees the patient following the initial referral which leads to the cancer diagnosis.
    """
    number_02 = "02"
    """
    General Dental Council
    """
    number_03 = "03"
    """
    General Medical Council
    """
    number_04 = "04"
    """
    General Optical Council
    """
    number_08 = "08"
    """
    Health and Care Professions Council
    """
    number_09 = "09"
    """
    Nursing and Midwifery Council
    """


class ProfessionalRegistrationIssuerCodeConsultantSurgeon(str, Enum):
    """
    A code which identifies the PROFESSIONAL REGISTRATION BODY for the Consultant or health care professional who is responsible for the treatment of the patient. If he/she is part of a surgical team, add all consultant surgeons responsible for the procedure.
    """
    number_02 = "02"
    """
    General Dental Council
    """
    number_03 = "03"
    """
    General Medical Council
    """
    number_04 = "04"
    """
    General Optical Council
    """
    number_08 = "08"
    """
    Health and Care Professions Council
    """
    number_09 = "09"
    """
    Nursing and Midwifery Council
    """


class ProfessionalRegistrationIssuerCodeConsultantTreatment(str, Enum):
    """
    A code which identifies the PROFESSIONAL REGISTRATION BODY for the Consultant or health care professional responsible for the treatment of the patient.
    """
    number_02 = "02"
    """
    General Dental Council
    """
    number_03 = "03"
    """
    General Medical Council
    """
    number_04 = "04"
    """
    General Optical Council
    """
    number_08 = "08"
    """
    Health and Care Professions Council
    """
    number_09 = "09"
    """
    Nursing and Midwifery Council
    """


class RelapseMethodOfDetection(str, Enum):
    """
    Indicate the method of detection for the patients relapse
    """
    number_1 = "1"
    """
    Morphology
    """
    number_2 = "2"
    """
    Flow
    """
    number_3 = "3"
    """
    Molecular
    """
    number_4 = "4"
    """
    Clinical Examination
    """
    number_9 = "9"
    """
    Other
    """


class SentinelNodeBiopsyOutcome(str, Enum):
    """
    Record the outcome of the Sentinel Node Biopsy
    """
    P = "P"
    """
    Malignant
    """
    N = "N"
    """
    No Malignancy
    """


class SnomedVersionDiagnosis(str, Enum):
    """
    The version of SNOMED used to encode MORPHOLOGY (SNOMED) DIAGNOSIS
    """
    number_01 = "01"
    """
    SNOMED II
    """
    number_02 = "02"
    """
    SNOMED 3
    """
    number_03 = "03"
    """
    SNOMED 3.5
    """
    number_04 = "04"
    """
    SNOMED RT
    """
    number_05 = "05"
    """
    SNOMED CT
    """
    number_99 = "99"
    """
    Not Known
    """


class SnomedVersionTransformation(str, Enum):
    """
    The version of SNOMED used to encode MORPHOLOGY (SNOMED) TRANSFORMATION
    """
    number_01 = "01"
    """
    SNOMED II
    """
    number_02 = "02"
    """
    SNOMED 3
    """
    number_03 = "03"
    """
    SNOMED 3.5
    """
    number_04 = "04"
    """
    SNOMED RT
    """
    number_05 = "05"
    """
    SNOMED CT
    """
    number_99 = "99"
    """
    Not Known
    """


class SourceOfReferralForNonPrimaryCancerPathway(str, Enum):
    """
    (Non Primary Cancer Pathway only.) This identifies the source of referral for a non primary cancer pathway.
    """
    number_01 = "01"
    """
    following an emergency admission
    """
    number_02 = "02"
    """
    following a Domiciliary Consultation
    """
    number_10 = "10"
    """
    following an Emergency Care Attendance (including Minor Injuries, Walk In Centres and Urgent Treatment Centres)
    """
    number_11 = "11"
    """
    Other (not listed)
    """
    number_03 = "03"
    """
    referral from a GENERAL MEDICAL PRACTITIONER
    """
    number_92 = "92"
    """
    referral from a GENERAL DENTAL PRACTITIONER
    """
    number_12 = "12"
    """
    referral from a General Practitioner with an Extended Role (GPwER) or Dentist with Enhanced Skills (DES)
    """
    number_04 = "04"
    """
    referral from an Emergency Care Department (including Minor Injuries Units, Walk In Centres and Urgent Treatment Centres)
    """
    number_05 = "05"
    """
    referral from a CONSULTANT, other than in an Emergency Care Department
    """
    number_06 = "06"
    """
    self-referral
    """
    number_07 = "07"
    """
    referral from a Prosthetist
    """
    number_13 = "13"
    """
    referral from a Specialist NURSE (Secondary Care)
    """
    number_14 = "14"
    """
    referral from an Allied Health Professional
    """
    number_15 = "15"
    """
    referral from an OPTOMETRIST
    """
    number_16 = "16"
    """
    referral from an Orthoptist
    """
    number_17 = "17"
    """
    referral from a National Screening Programme
    """
    number_93 = "93"
    """
    referral from a Community Dental Service
    """
    number_97 = "97"
    """
    referral: Other (not listed)
    """


class SourceOfReferralForOutPatients(str, Enum):
    """
    This identifies the source of referral of each Consultant Out-Patient Episode.
(See User Guide for further details)
    """
    number_01 = "01"
    """
    following an emergency admission
    """
    number_02 = "02"
    """
    following a Domiciliary Consultation
    """
    number_10 = "10"
    """
    following an Emergency Care Attendance (including Minor Injuries, Walk In Centres and Urgent Treatment Centres)
    """
    number_11 = "11"
    """
    Other (not listed)
    """
    number_03 = "03"
    """
    referral from a GENERAL MEDICAL PRACTITIONER
    """
    number_92 = "92"
    """
    referral from a GENERAL DENTAL PRACTITIONER
    """
    number_12 = "12"
    """
    referral from a General Practitioner with an Extended Role (GPwER) or Dentist with Enhanced Skills (DES)
    """
    number_04 = "04"
    """
    referral from an Emergency Care Department (including Minor Injuries Units, Walk In Centres and Urgent Treatment Centres)
    """
    number_05 = "05"
    """
    referral from a CONSULTANT, other than in an Emergency Care Department
    """
    number_06 = "06"
    """
    self-referral
    """
    number_07 = "07"
    """
    referral from a Prosthetist
    """
    number_13 = "13"
    """
    referral from a Specialist NURSE (Secondary Care)
    """
    number_14 = "14"
    """
    referral from an Allied Health Professional
    """
    number_15 = "15"
    """
    referral from an OPTOMETRIST
    """
    number_16 = "16"
    """
    referral from an Orthoptist
    """
    number_17 = "17"
    """
    referral from a National Screening Programme
    """
    number_93 = "93"
    """
    referral from a Community Dental Service
    """
    number_97 = "97"
    """
    referral: Other (not listed)
    """


class StaffRoleOfferingTheAssessment(str, Enum):
    """
    Record the role of the individual offering the Holistic Needs Assessment (Secondary Care Only)
    """
    number_01 = "01"
    """
    Cancer Nurse Specialist
    """
    number_02 = "02"
    """
    Other nurse
    """
    number_03 = "03"
    """
    Allied health Professional
    """
    number_04 = "04"
    """
    Support worker/Care Navigator (band 3 or 4)
    """
    number_05 = "05"
    """
    Mental health care professional
    """
    number_06 = "06"
    """
    Consultant/Associate Specialist/Junior Doctor
    """
    number_08 = "08"
    """
    Other
    """
    number_09 = "09"
    """
    Not Known
    """


class StaffRoleOfferingThePlanning(str, Enum):
    """
    Record the role of the individual offering the Personalised Care and Support Planning (Secondary Care Only)
    """
    number_01 = "01"
    """
    Cancer Nurse Specialist
    """
    number_02 = "02"
    """
    Other nurse
    """
    number_03 = "03"
    """
    Allied health Professional
    """
    number_04 = "04"
    """
    Support worker/Care Navigator (band 3 or 4)
    """
    number_05 = "05"
    """
    Mental health care professional
    """
    number_06 = "06"
    """
    Consultant/Associate Specialist/Junior Doctor
    """
    number_08 = "08"
    """
    Other
    """
    number_09 = "09"
    """
    Not Known
    """


class SurgicalAccessType(str, Enum):
    """
    The surgical access type used to perform the main procedure.
    """
    number_1 = "1"
    """
    Open Surgery
    """
    number_2 = "2"
    """
    Laparoscopic/Thoracoscopic with planned conversion to open surgery
    """
    number_3 = "3"
    """
    Laparoscopic/Thoracoscopic with unplanned conversion to open surgery
    """
    number_4 = "4"
    """
    Laparoscopic/Thoracoscopic completed
    """
    number_5 = "5"
    """
    Robotic surgery
    """
    Z = "Z"
    """
    Not applicable
    """


class SurgicalAdmissionType(str, Enum):
    """
    The type of Surgical Admission
    """
    number_1 = "1"
    """
    Elective
    """
    number_2 = "2"
    """
    Emergency
    """
    number_9 = "9"
    """
    Not known
    """


class TnmCodingEdition(str, Enum):
    """
    The TNM Coding edition in use
    """
    number_1 = "1"
    """
    UICC (Union for International Cancer Control)
    """
    number_2 = "2"
    """
    AJCC (American Joint Committee on Cancer)
    """
    number_3 = "3"
    """
    ENETS (European Neuroendocrine Tumour Society)
    """


class TobaccoSmokingCessation(str, Enum):
    """
    Was treatment for tobacco addiction/cessation given to the patient
    """
    number_1 = "1"
    """
    Patient treated
    """
    number_2 = "2"
    """
    Patient not treated
    """
    number_3 = "3"
    """
    Patient offered treatment but declined
    """
    number_8 = "8"
    """
    Not Applicable (Not current tobacco user)
    """
    number_9 = "9"
    """
    Not Known (Not recorded)
    """


class TobaccoSmokingStatus(str, Enum):
    """
    Specify the current tobacco smoking status of the patient.
    """
    number_1 = "1"
    """
    Current smoker
    """
    number_2 = "2"
    """
    Ex smoker
    """
    number_4 = "4"
    """
    Never smoked
    """
    number_9 = "9"
    """
    Unknown
    """


class TumourLaterality(str, Enum):
    """
    Tumour laterality identifies the side of the body for a tumour relating to paired organs within a PATIENT.
    """
    L = "L"
    """
    Left
    """
    R = "R"
    """
    Right
    """
    M = "M"
    """
    Midline
    """
    B = "B"
    """
    Bilateral
    """
    number_8 = "8"
    """
    Not applicable
    """
    number_9 = "9"
    """
    Not Known
    """


class UnplannedReturnToTheatreIndicator(str, Enum):
    """
    Whether or not the patient required a second (unplanned) operation during the same admission as the primary procedure
    """
    Y = "Y"
    """
    Yes
    """
    N = "N"
    """
    No
    """
    number_9 = "9"
    """
    Not known
    """



class COSDResearchView(ConfiguredBaseModel):
    """
    Flat research view combining file metadata, patient demographics, primary pathway, non-primary pathway, diagnostic procedures, staging, treatment, and outcomes data. Corresponds to RVW.COSD_RESEARCH_VIEW in the source database. Each row represents one COSD record.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://health-informatics-uon.github.io/nuh-data/datasets/cosd',
         'tree_root': True})

    etl_id: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column', 'value': 'ETL_ID'},
                         'sql_type': {'tag': 'sql_type', 'value': 'INT'}},
         'domain_of': ['COSDResearchView']} })
    etl_date: Optional[datetime ] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column', 'value': 'ETL_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATETIME'}},
         'domain_of': ['COSDResearchView']} })
    direct_care_published_runid: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'DIRECT_CARE_PUBLISHED_RUNID'},
                         'sql_type': {'tag': 'sql_type', 'value': 'INT'}},
         'domain_of': ['COSDResearchView']} })
    dataset_name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column', 'value': 'DATASET_NAME'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(300)'}},
         'domain_of': ['COSDResearchView']} })
    ndo_run_date: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column', 'value': 'NDO_RUN_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    file_name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column', 'value': 'FILE_NAME'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(1000)'}},
         'domain_of': ['COSDResearchView']} })
    c000010_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column', 'value': 'C000010_ID'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(36)'}},
         'domain_of': ['COSDResearchView']} })
    c000020_id_submitting_org: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'C000020_ID_SUBMITTING_ORG'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(6)'}},
         'domain_of': ['COSDResearchView']} })
    c000030_record_count: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'C000030_RECORD_COUNT'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(7)'}},
         'domain_of': ['COSDResearchView']} })
    c000040_reporting_period_start_date: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'C000040_REPORTING_PERIOD_START_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    c000050_reporting_period_end_date: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'C000050_REPORTING_PERIOD_END_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    c000060_file_creation_datetime: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'C000060_FILE_CREATION_DATETIME'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(19)'}},
         'domain_of': ['COSDResearchView']} })
    record_type: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column', 'value': 'RECORD_TYPE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(100)'}},
         'domain_of': ['COSDResearchView']} })
    pseudo_c000070_unique_record_id: Optional[str] = Field(default=None, description="""The universal unique identifier (UUID) for the record""", json_schema_extra = { "linkml_meta": {'annotations': {'sensitivity': {'tag': 'sensitivity',
                                         'value': 'pseudonymised'},
                         'sql_column': {'tag': 'sql_column',
                                        'value': 'PSEUDO_C000070_UNIQUE_RECORD_ID'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARBINARY(100)'}},
         'domain_of': ['COSDResearchView']} })
    pseudo_cr0010_nhs_number: Optional[str] = Field(default=None, description="""The NHS NUMBER, the primary identifier of a PERSON, is a unique identifier for a PATIENT within the NHS in England and Wales. This will not vary by any ORGANISATION of which a PERSON is a PATIENT.""", json_schema_extra = { "linkml_meta": {'annotations': {'sensitivity': {'tag': 'sensitivity',
                                         'value': 'pseudonymised'},
                         'sql_column': {'tag': 'sql_column',
                                        'value': 'PSEUDO_CR0010_NHS_NUMBER'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARBINARY(100)'}},
         'domain_of': ['COSDResearchView']} })
    cr1350_nhs_num_stat_code: Optional[NhsNumberStatusIndicatorCode] = Field(default=None, description="""The NHS NUMBER STATUS INDICATOR CODE is the trace status of the NHS NUMBER""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR1350_NHS_NUM_STAT_CODE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    date_of_birth_year: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'DATE_OF_BIRTH_YEAR'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    date_of_birth_month: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'DATE_OF_BIRTH_MONTH'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    date_of_birth_mid_month: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'DATE_OF_BIRTH_MID_MONTH'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr0030_provider_id: Optional[str] = Field(default=None, description="""The ORGANISATION IDENTIFIER of the Organisation acting as a Health Care Provider. (an6 not applicable to COSD)""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0030_PROVIDER_ID'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(5)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr0370_diag_primary_diag_icd: Optional[str] = Field(default=None, description="""The International Classification of Diseases (ICD) code used to identify the PRIMARY DIAGNOSIS""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR0370_DIAG_PRIMARY_DIAG_ICD'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(6)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr0380_diag_tumour_laterality: Optional[TumourLaterality] = Field(default=None, description="""Tumour laterality identifies the side of the body for a tumour relating to paired organs within a PATIENT.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR0380_DIAG_TUMOUR_LATERALITY'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr2030_diag_date_of_primary_diag_clin_agreed: Optional[date] = Field(default=None, description="""Record the date where the primary cancer was confirmed or diagnosis agreed.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR2030_DIAG_DATE_OF_PRIMARY_DIAG_CLIN_AGREED'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    npp_cr6500_date_diagnosis_clinically_agreed: Optional[date] = Field(default=None, description="""Record the date where the non primary cancer diagnosis was confirmed or agreed.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'NPP_CR6500_DATE_DIAGNOSIS_CLINICALLY_AGREED'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    npp_cr7100_diag_original_primary_diagnosis_icd: Optional[str] = Field(default=None, description="""Record the ICD10 code of the original primary diagnosis. This will normally be agreed at the MDT by the clinical team.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'NPP_CR7100_DIAG_ORIGINAL_PRIMARY_DIAGNOSIS_ICD'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(6)'}},
         'domain_of': ['COSDResearchView']} })
    npp_cr6520_rec1_metastatic_type1: Optional[MetastaticType] = Field(default=None, description="""Indicate the type of metastatic disease diagnosed by the clinical team""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'NPP_CR6520_REC1_METASTATIC_TYPE1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    npp_cr1590_rec1_metastatic_site1: Optional[MetastaticSite] = Field(default=None, description="""The site of the metastatic disease, if any
More than one site can be recorded""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'NPP_CR1590_REC1_METASTATIC_SITE1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    npp_cr6520_rec1_metastatic_type2: Optional[MetastaticType] = Field(default=None, description="""Indicate the type of metastatic disease diagnosed by the clinical team""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'NPP_CR6520_REC1_METASTATIC_TYPE2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    npp_cr1590_rec1_metastatic_site2: Optional[MetastaticSite] = Field(default=None, description="""The site of the metastatic disease, if any
More than one site can be recorded""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'NPP_CR1590_REC1_METASTATIC_SITE2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    npp_cr1550_diag_palliative_care_specialist_seen_indicator_cancer_recurrence: Optional[PalliativeCareSpecialistSeenIndicatorCancerRecurrence] = Field(default=None, description="""Record whether the patient was seen by a palliative care specialist. This would be a member of the specialist palliative care team led by a consultant in palliative medicine for a recurrence of cancer.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'NPP_CR1550_DIAG_PALLIATIVE_CARE_SPECIALIST_SEEN_INDICATOR_CANCER_RECURRENCE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    npp_cr9000_diag_relapse_method_of_detection_1: Optional[RelapseMethodOfDetection] = Field(default=None, description="""Indicate the method of detection for the patients relapse""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'NPP_CR9000_DIAG_RELAPSE_METHOD_OF_DETECTION_1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    npp_cr9000_diag_relapse_method_of_detection_2: Optional[RelapseMethodOfDetection] = Field(default=None, description="""Indicate the method of detection for the patients relapse""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'NPP_CR9000_DIAG_RELAPSE_METHOD_OF_DETECTION_2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    npp_cr6900_progression_icd: Optional[str] = Field(default=None, description="""Where a cancer has progressed, record the ICD10 code of the original diagnosis. This will normally be agreed at the MDT by the clinical team.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'NPP_CR6900_PROGRESSION_ICD'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(6)'}},
         'domain_of': ['COSDResearchView']} })
    npp_cr6520_prog_metastatic_type_progression1: Optional[MetastaticType] = Field(default=None, description="""Indicate the type of metastatic disease diagnosed by the clinical team""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'NPP_CR6520_PROG_METASTATIC_TYPE_PROGRESSION1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    npp_cr1590_prog_metastatic_site_progression1: Optional[MetastaticSite] = Field(default=None, description="""The site of the metastatic disease, if any
More than one site can be recorded""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'NPP_CR1590_PROG_METASTATIC_SITE_PROGRESSION1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    npp_cr6520_prog_metastatic_type_progression2: Optional[MetastaticType] = Field(default=None, description="""Indicate the type of metastatic disease diagnosed by the clinical team""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'NPP_CR6520_PROG_METASTATIC_TYPE_PROGRESSION2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    npp_cr1590_prog_metastatic_site_progression2: Optional[MetastaticSite] = Field(default=None, description="""The site of the metastatic disease, if any
More than one site can be recorded""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'NPP_CR1590_PROG_METASTATIC_SITE_PROGRESSION2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    npp_cr7200_trans_original_morphologyicd_o_3: Optional[str] = Field(default=None, description="""Record the morphology ICD-O-3 code of the original diagnosis. This will normally be agreed at the MDT by the clinical team.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'NPP_CR7200_TRANS_ORIGINAL_MORPHOLOGYICD_O_3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(7)'}},
         'domain_of': ['COSDResearchView']} })
    npp_cr7210_trans_original_morphology_snomed: Optional[str] = Field(default=None, description="""Record the SNOMED morphology code of the original diagnosis. This will normally be agreed at the MDT by the clinical team.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'NPP_CR7210_TRANS_ORIGINAL_MORPHOLOGY_SNOMED'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    npp_cr7010_trans_morphology_icd_o_3_trans: Optional[str] = Field(default=None, description="""The morphology code for the transformation of the cancer as defined by ICD-O-3. This can be recorded as well as or instead of MORPHOLOGY (SNOMED) TRANSFORMATION.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'NPP_CR7010_TRANS_MORPHOLOGY_ICD_O_3_TRANS'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(7)'}},
         'domain_of': ['COSDResearchView']} })
    npp_cr7000_trans_morphology_snomed_trans: Optional[str] = Field(default=None, description="""This is the TRANSFORMATION DIAGNOSIS using the SNOMED International / SNOMED CT code for the cell type of the tumour recorded as part of a Cancer Care Spell. This can be recorded as well as or instead of MORPHOLOGY (ICD-O-3) TRANSFORMATION.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'NPP_CR7000_TRANS_MORPHOLOGY_SNOMED_TRANS'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    npp_cr7030_trans_snomed_version_current_trans: Optional[SnomedVersionTransformation] = Field(default=None, description="""The version of SNOMED used to encode MORPHOLOGY (SNOMED) TRANSFORMATION""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'NPP_CR7030_TRANS_SNOMED_VERSION_CURRENT_TRANS'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    llsoa: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column', 'value': 'LLSOA'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(9)'}},
         'domain_of': ['COSDResearchView']} })
    cr3170_person_stated_gender_code: Optional[PersonStatedGenderCode] = Field(default=None, description="""Person's gender as self-declared (or inferred by observation for those unable to declare their PERSON STATED GENDER).""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3170_PERSON_STATED_GENDER_CODE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr6840_person_sexual_orientation_code_at_diagnosis: Optional[PersonSexualOrientationCodeAtDiagnosis] = Field(default=None, description="""Person's sexual orientation as self-declared at the time of the PATIENT DIAGNOSIS.
This complies with the information standard DCB2094.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6840_PERSON_SEXUAL_ORIENTATION_CODE_AT_DIAGNOSIS'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr0110_general_medical_practitioner_specified: Optional[str] = Field(default=None, description="""GENERAL MEDICAL PRACTITIONER (SPECIFIED) is the GENERAL MEDICAL PRACTITIONER PPD CODE of the GENERAL MEDICAL PRACTITIONER specified by the PATIENT.
This GENERAL MEDICAL PRACTITIONER works within the General Medical Practitioner Practice with which the PATIENT is registered.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0110_GENERAL_MEDICAL_PRACTITIONER_SPECIFIED'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(8)'}},
         'domain_of': ['COSDResearchView']} })
    cr0120_general_medical_practice_code_patient_registration: Optional[str] = Field(default=None, description="""The GENERAL MEDICAL PRACTICE (PATIENT REGISTRATION) is an ORGANISATION CODE. This is the code of the GP Practice that the PATIENT is registered with.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0120_GENERAL_MEDICAL_PRACTICE_CODE_PATIENT_REGISTRATION'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(8)'}},
         'domain_of': ['COSDResearchView']} })
    cr0150_ethnic_category: Optional[EthnicCategory] = Field(default=None, description="""The ethnicity of a PERSON, as specified by the PERSON. The 16+1 ethnic data categories defined in the 2001 census is the national mandatory standard for the collection and analysis of ethnicity.
(The Office for National Statistics has developed a further breakdown of the group from that given, which may be used locally.)""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0150_ETHNIC_CATEGORY'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr9060_ethnic_category_2021: Optional[str] = Field(default=None, description="""The ethnicity of a PERSON, as specified by the PERSON.
ETHNIC CATEGORY 2021 is the classification used for the 2021 census.
Note: This item has not been approved by the Data Alliance Partnership Board. It has been introduced to provide advance notice to data providers and system suppliers of the intention to report this item at a later date. This item should not be submitted until further development by NHS England has been undertaken.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR9060_ETHNIC_CATEGORY_2021'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr1600_source_of_referral_op: Optional[SourceOfReferralForOutPatients] = Field(default=None, description="""This identifies the source of referral of each Consultant Out-Patient Episode.
(See User Guide for further details)""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR1600_SOURCE_OF_REFERRAL_OP'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr0230_date_first_seen: Optional[date] = Field(default=None, description="""This is the date that the PATIENT is first seen in the Trust that receives the first referral.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR0230_DATE_FIRST_SEEN'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr7300_prof_reg_issuer_code_cons_first_seen: Optional[ProfessionalRegistrationIssuerCodeConsultantFirstSeen] = Field(default=None, description="""A code which identifies the PROFESSIONAL REGISTRATION BODY for the Consultant or health care professional who first sees the patient following the initial referral which leads to the cancer diagnosis.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR7300_PROF_REG_ISSUER_CODE_CONS_FIRST_SEEN'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr7310_prof_reg_entry_id_cons_first_seen: Optional[str] = Field(default=None, description="""The registration identifier allocated by a Professional Registration Body for the Consultant or health care professional who first sees the patient following the initial referral which leads to the cancer diagnosis.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR7310_PROF_REG_ENTRY_ID_CONS_FIRST_SEEN'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(32)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr1410_org_site_prov_first_seen: Optional[str] = Field(default=None, description="""The ORGANISATION IDENTIFIER of the Organisation Site of the Health Care Provider at the first contact with the PATIENT.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR1410_ORG_SITE_PROV_FIRST_SEEN'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(9)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr1360_date_first_seen_cancer_specialist: Optional[date] = Field(default=None, description="""This is the date that the PATIENT is first seen by the appropriate specialist for cancer care within a Cancer Care Spell. This is the PERSON or PERSONS who are most able to progress the diagnosis of the primary tumour.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR1360_DATE_FIRST_SEEN_CANCER_SPECIALIST'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr1400_org_site_id_prov_first_cancer_specialist: Optional[str] = Field(default=None, description="""The ORGANISATION IDENTIFIER of the Organisation Site where the PATIENT is first seen by an appropriate cancer specialist on the DATE FIRST SEEN (CANCER SPECIALIST).""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR1400_ORG_SITE_ID_PROV_FIRST_CANCER_SPECIALIST'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(9)'}},
         'domain_of': ['COSDResearchView']} })
    npp_cr0300_source_of_referral: Optional[SourceOfReferralForNonPrimaryCancerPathway] = Field(default=None, description="""(Non Primary Cancer Pathway only.) This identifies the source of referral for a non primary cancer pathway.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'NPP_CR0300_SOURCE_OF_REFERRAL'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    npp_cr7400_date_first_seen: Optional[date] = Field(default=None, description="""This is the date that the PATIENT is first seen in the Trust that receives the first referral.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'NPP_CR7400_DATE_FIRST_SEEN'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    npp_cr7410_org_site_id_prov_first_seen: Optional[str] = Field(default=None, description="""The ORGANISATION IDENTIFIER of the Organisation Site of the Health Care Provider at the first contact with the PATIENT, where the patient is on a non primary cancer pathway.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'NPP_CR7410_ORG_SITE_ID_PROV_FIRST_SEEN'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(9)'}},
         'domain_of': ['COSDResearchView']} })
    cr7500_diag_proc1_org_site_id: Optional[str] = Field(default=None, description="""This is the ORGANISATION IDENTIFIER of the Organisation site where the diagnostic procedure took place.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7500_DIAG_PROC1_ORG_SITE_ID'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(9)'}},
         'domain_of': ['COSDResearchView']} })
    cr7510_diag_proc1_procedure_date: Optional[date] = Field(default=None, description="""The DATE the diagnostic procedure was carried out.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7510_DIAG_PROC1_PROCEDURE_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr7520_diag_proc1_opcs1: Optional[str] = Field(default=None, description="""Record the diagnostic procedure(s) carried out using OPCS. This maybe recorded in addition to DIAGNOSTIC PROCEDURE (SNOMED CT)""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7520_DIAG_PROC1_OPCS1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr7520_diag_proc1_opcs2: Optional[str] = Field(default=None, description="""Record the diagnostic procedure(s) carried out using OPCS. This maybe recorded in addition to DIAGNOSTIC PROCEDURE (SNOMED CT)""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7520_DIAG_PROC1_OPCS2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr7520_diag_proc1_opcs3: Optional[str] = Field(default=None, description="""Record the diagnostic procedure(s) carried out using OPCS. This maybe recorded in addition to DIAGNOSTIC PROCEDURE (SNOMED CT)""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7520_DIAG_PROC1_OPCS3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr7520_diag_proc1_opcs4: Optional[str] = Field(default=None, description="""Record the diagnostic procedure(s) carried out using OPCS. This maybe recorded in addition to DIAGNOSTIC PROCEDURE (SNOMED CT)""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7520_DIAG_PROC1_OPCS4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr7520_diag_proc1_opcs5: Optional[str] = Field(default=None, description="""Record the diagnostic procedure(s) carried out using OPCS. This maybe recorded in addition to DIAGNOSTIC PROCEDURE (SNOMED CT)""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7520_DIAG_PROC1_OPCS5'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr7530_diag_proc1_snomedct1: Optional[str] = Field(default=None, description="""Record the diagnostic procedure(s) carried out using SNOMED CT. This maybe recorded in addition to DIAGNOSTIC PROCEDURE (OPCS).""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7530_DIAG_PROC1_SNOMEDCT1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr7530_diag_proc1_snomedct2: Optional[str] = Field(default=None, description="""Record the diagnostic procedure(s) carried out using SNOMED CT. This maybe recorded in addition to DIAGNOSTIC PROCEDURE (OPCS).""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7530_DIAG_PROC1_SNOMEDCT2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr7530_diag_proc1_snomedct3: Optional[str] = Field(default=None, description="""Record the diagnostic procedure(s) carried out using SNOMED CT. This maybe recorded in addition to DIAGNOSTIC PROCEDURE (OPCS).""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7530_DIAG_PROC1_SNOMEDCT3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr7530_diag_proc1_snomedct4: Optional[str] = Field(default=None, description="""Record the diagnostic procedure(s) carried out using SNOMED CT. This maybe recorded in addition to DIAGNOSTIC PROCEDURE (OPCS).""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7530_DIAG_PROC1_SNOMEDCT4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr7530_diag_proc1_snomedct5: Optional[str] = Field(default=None, description="""Record the diagnostic procedure(s) carried out using SNOMED CT. This maybe recorded in addition to DIAGNOSTIC PROCEDURE (OPCS).""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7530_DIAG_PROC1_SNOMEDCT5'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr7540_sentinel_node_biopsy_outcome1: Optional[SentinelNodeBiopsyOutcome] = Field(default=None, description="""Record the outcome of the Sentinel Node Biopsy""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7540_SENTINEL_NODE_BIOPSY_OUTCOME1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr7500_diag_proc2_org_site_id: Optional[str] = Field(default=None, description="""This is the ORGANISATION IDENTIFIER of the Organisation site where the diagnostic procedure took place.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7500_DIAG_PROC2_ORG_SITE_ID'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(9)'}},
         'domain_of': ['COSDResearchView']} })
    cr7510_diag_proc2_procedure_date: Optional[date] = Field(default=None, description="""The DATE the diagnostic procedure was carried out.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7510_DIAG_PROC2_PROCEDURE_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr7520_diag_proc2_opcs1: Optional[str] = Field(default=None, description="""Record the diagnostic procedure(s) carried out using OPCS. This maybe recorded in addition to DIAGNOSTIC PROCEDURE (SNOMED CT)""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7520_DIAG_PROC2_OPCS1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr7520_diag_proc2_opcs2: Optional[str] = Field(default=None, description="""Record the diagnostic procedure(s) carried out using OPCS. This maybe recorded in addition to DIAGNOSTIC PROCEDURE (SNOMED CT)""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7520_DIAG_PROC2_OPCS2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr7520_diag_proc2_opcs3: Optional[str] = Field(default=None, description="""Record the diagnostic procedure(s) carried out using OPCS. This maybe recorded in addition to DIAGNOSTIC PROCEDURE (SNOMED CT)""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7520_DIAG_PROC2_OPCS3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr7520_diag_proc2_opcs4: Optional[str] = Field(default=None, description="""Record the diagnostic procedure(s) carried out using OPCS. This maybe recorded in addition to DIAGNOSTIC PROCEDURE (SNOMED CT)""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7520_DIAG_PROC2_OPCS4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr7520_diag_proc2_opcs5: Optional[str] = Field(default=None, description="""Record the diagnostic procedure(s) carried out using OPCS. This maybe recorded in addition to DIAGNOSTIC PROCEDURE (SNOMED CT)""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7520_DIAG_PROC2_OPCS5'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr7530_diag_proc2_snomedct1: Optional[str] = Field(default=None, description="""Record the diagnostic procedure(s) carried out using SNOMED CT. This maybe recorded in addition to DIAGNOSTIC PROCEDURE (OPCS).""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7530_DIAG_PROC2_SNOMEDCT1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr7530_diag_proc2_snomedct2: Optional[str] = Field(default=None, description="""Record the diagnostic procedure(s) carried out using SNOMED CT. This maybe recorded in addition to DIAGNOSTIC PROCEDURE (OPCS).""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7530_DIAG_PROC2_SNOMEDCT2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr7530_diag_proc2_snomedct3: Optional[str] = Field(default=None, description="""Record the diagnostic procedure(s) carried out using SNOMED CT. This maybe recorded in addition to DIAGNOSTIC PROCEDURE (OPCS).""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7530_DIAG_PROC2_SNOMEDCT3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr7530_diag_proc2_snomedct4: Optional[str] = Field(default=None, description="""Record the diagnostic procedure(s) carried out using SNOMED CT. This maybe recorded in addition to DIAGNOSTIC PROCEDURE (OPCS).""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7530_DIAG_PROC2_SNOMEDCT4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr7530_diag_proc2_snomedct5: Optional[str] = Field(default=None, description="""Record the diagnostic procedure(s) carried out using SNOMED CT. This maybe recorded in addition to DIAGNOSTIC PROCEDURE (OPCS).""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7530_DIAG_PROC2_SNOMEDCT5'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr7540_sentinel_node_biopsy_outcome2: Optional[SentinelNodeBiopsyOutcome] = Field(default=None, description="""Record the outcome of the Sentinel Node Biopsy""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7540_SENTINEL_NODE_BIOPSY_OUTCOME2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr7500_diag_proc3_org_site_id: Optional[str] = Field(default=None, description="""This is the ORGANISATION IDENTIFIER of the Organisation site where the diagnostic procedure took place.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7500_DIAG_PROC3_ORG_SITE_ID'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(9)'}},
         'domain_of': ['COSDResearchView']} })
    cr7510_diag_proc3_procedure_date: Optional[date] = Field(default=None, description="""The DATE the diagnostic procedure was carried out.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7510_DIAG_PROC3_PROCEDURE_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr7520_diag_proc3_opcs1: Optional[str] = Field(default=None, description="""Record the diagnostic procedure(s) carried out using OPCS. This maybe recorded in addition to DIAGNOSTIC PROCEDURE (SNOMED CT)""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7520_DIAG_PROC3_OPCS1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr7520_diag_proc3_opcs2: Optional[str] = Field(default=None, description="""Record the diagnostic procedure(s) carried out using OPCS. This maybe recorded in addition to DIAGNOSTIC PROCEDURE (SNOMED CT)""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7520_DIAG_PROC3_OPCS2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr7520_diag_proc3_opcs3: Optional[str] = Field(default=None, description="""Record the diagnostic procedure(s) carried out using OPCS. This maybe recorded in addition to DIAGNOSTIC PROCEDURE (SNOMED CT)""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7520_DIAG_PROC3_OPCS3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr7520_diag_proc3_opcs4: Optional[str] = Field(default=None, description="""Record the diagnostic procedure(s) carried out using OPCS. This maybe recorded in addition to DIAGNOSTIC PROCEDURE (SNOMED CT)""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7520_DIAG_PROC3_OPCS4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr7520_diag_proc3_opcs5: Optional[str] = Field(default=None, description="""Record the diagnostic procedure(s) carried out using OPCS. This maybe recorded in addition to DIAGNOSTIC PROCEDURE (SNOMED CT)""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7520_DIAG_PROC3_OPCS5'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr7530_diag_proc3_snomedct1: Optional[str] = Field(default=None, description="""Record the diagnostic procedure(s) carried out using SNOMED CT. This maybe recorded in addition to DIAGNOSTIC PROCEDURE (OPCS).""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7530_DIAG_PROC3_SNOMEDCT1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr7530_diag_proc3_snomedct2: Optional[str] = Field(default=None, description="""Record the diagnostic procedure(s) carried out using SNOMED CT. This maybe recorded in addition to DIAGNOSTIC PROCEDURE (OPCS).""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7530_DIAG_PROC3_SNOMEDCT2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr7530_diag_proc3_snomedct3: Optional[str] = Field(default=None, description="""Record the diagnostic procedure(s) carried out using SNOMED CT. This maybe recorded in addition to DIAGNOSTIC PROCEDURE (OPCS).""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7530_DIAG_PROC3_SNOMEDCT3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr7530_diag_proc3_snomedct4: Optional[str] = Field(default=None, description="""Record the diagnostic procedure(s) carried out using SNOMED CT. This maybe recorded in addition to DIAGNOSTIC PROCEDURE (OPCS).""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7530_DIAG_PROC3_SNOMEDCT4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr7530_diag_proc3_snomedct5: Optional[str] = Field(default=None, description="""Record the diagnostic procedure(s) carried out using SNOMED CT. This maybe recorded in addition to DIAGNOSTIC PROCEDURE (OPCS).""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7530_DIAG_PROC3_SNOMEDCT5'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr7540_sentinel_node_biopsy_outcome3: Optional[SentinelNodeBiopsyOutcome] = Field(default=None, description="""Record the outcome of the Sentinel Node Biopsy""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7540_SENTINEL_NODE_BIOPSY_OUTCOME3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6230_org_site_id_of_diag: Optional[str] = Field(default=None, description="""The ORGANISATION IDENTIFIER of the Organisation site where the PATIENT DIAGNOSIS took place.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6230_ORG_SITE_ID_OF_DIAG'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(9)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr0390_basis_of_diag_cancer: Optional[BasisOfDiagnosisCancer] = Field(default=None, description="""This is the method used to confirm the cancer.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR0390_BASIS_OF_DIAG_CANCER'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(3)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr0180_morphology_icd_o_3: Optional[str] = Field(default=None, description="""The morphology code for the diagnosed cancer as defined by ICD-O-3. This can be recorded as well as or instead of MORPHOLOGY (SNOMED).""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR0180_MORPHOLOGY_ICD_O_3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(7)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6400_curr_morphology_snomed_diag: Optional[str] = Field(default=None, description="""This is the PATIENT DIAGNOSIS using the SNOMED International / SNOMED CT code for the cell type of the tumour recorded as part of a Cancer Care Spell. This can be recorded as well as or instead of MORPHOLOGY (ICD-O-3).""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6400_CURR_MORPHOLOGY_SNOMED_DIAG'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6490_curr_snomed_version_diag: Optional[SnomedVersionDiagnosis] = Field(default=None, description="""The version of SNOMED used to encode MORPHOLOGY (SNOMED) DIAGNOSIS""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6490_CURR_SNOMED_VERSION_DIAG'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr0480_topography_icd_o_3: Optional[str] = Field(default=None, description="""The topographical site code for the tumour as defined by ICD-O-3. This will normally be derived by Registries.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR0480_TOPOGRAPHY_ICD_O_3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(7)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr9010_ki67: Optional[str] = Field(default=None, description="""Record the Ki67 percentage
This is a pilot data item, required to support the accurate calculation of Grade.
This is a requirement for Neuroendocrine tumours (NET), optional for all other tumour types.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column', 'value': 'PP_CR9010_KI67'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(3)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr0410_grade_of_differentiationat_diag: Optional[GradeOfDifferentiationAtDiagnosis] = Field(default=None, description="""GRADE OF DIFFERENTIATION (AT DIAGNOSIS) is the definitive grade of the Tumour at the time of PATIENT DIAGNOSIS.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR0410_GRADE_OF_DIFFERENTIATIONAT_DIAG'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr0510_performance_status_adult: Optional[PerformanceStatusAdult] = Field(default=None, description="""A World Health Organisation classification indicating a PERSON's status relating to activity / disability.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR0510_PERFORMANCE_STATUS_ADULT'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6830_diagnosis_code_snomedct: Optional[str] = Field(default=None, description="""DIAGNOSIS CODE (SNOMED CT) is the SNOMED CT concept ID which is used to identify the clinical diagnosis given to the patient.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6830_DIAGNOSIS_CODE_SNOMEDCT'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6960_diag_metastatic_type_1: Optional[MetastaticType] = Field(default=None, description="""Indicate the type of metastatic disease diagnosed by the clinical team""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6960_DIAG_METASTATIC_TYPE_1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6970_diag_metastatic_site_1: Optional[MetastaticSite] = Field(default=None, description="""The site of the metastatic disease, if any, at diagnosis.
More than one site can be recorded""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6970_DIAG_METASTATIC_SITE_1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6960_diag_metastatic_type_2: Optional[MetastaticType] = Field(default=None, description="""Indicate the type of metastatic disease diagnosed by the clinical team""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6960_DIAG_METASTATIC_TYPE_2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6970_diag_metastatic_site_2: Optional[MetastaticSite] = Field(default=None, description="""The site of the metastatic disease, if any, at diagnosis.
More than one site can be recorded""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6970_DIAG_METASTATIC_SITE_2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6960_diag_metastatic_type_3: Optional[MetastaticType] = Field(default=None, description="""Indicate the type of metastatic disease diagnosed by the clinical team""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6960_DIAG_METASTATIC_TYPE_3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6970_diag_metastatic_site_3: Optional[MetastaticSite] = Field(default=None, description="""The site of the metastatic disease, if any, at diagnosis.
More than one site can be recorded""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6970_DIAG_METASTATIC_SITE_3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6960_diag_metastatic_type_4: Optional[MetastaticType] = Field(default=None, description="""Indicate the type of metastatic disease diagnosed by the clinical team""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6960_DIAG_METASTATIC_TYPE_4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6970_diag_metastatic_site_4: Optional[MetastaticSite] = Field(default=None, description="""The site of the metastatic disease, if any, at diagnosis.
More than one site can be recorded""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6970_DIAG_METASTATIC_SITE_4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr7600_primary_diag_subsidiary_comment: Optional[str] = Field(default=None, description="""Additional comments on diagnosis where coding is difficult or imprecise. (Examples of this would be: \"papillary glioneuronal tumour\" or \"angiocentric glioma\" to specify recently described diagnoses which do not have ICD10 or ICD-O-3 coding. \"anaplastic ependymoma\" or \"ependymoblastoma\" to distinguish between these two diagnoses which may have different treatment decisions or outcomes but which cannot be distinguished in ICD10 or ICD-O-3 coding.)""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR7600_PRIMARY_DIAG_SUBSIDIARY_COMMENT'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(50)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr7610_secondary_diag_icd1: Optional[str] = Field(default=None, description="""Types (ICD10 codes) of other significant conditions (e.g. Down Syndrome, NF1, Fanconi anaemia) which may predispose to cancer or influence treatment. Possible multiple entries.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR7610_SECONDARY_DIAG_ICD1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(6)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr7610_secondary_diag_icd2: Optional[str] = Field(default=None, description="""Types (ICD10 codes) of other significant conditions (e.g. Down Syndrome, NF1, Fanconi anaemia) which may predispose to cancer or influence treatment. Possible multiple entries.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR7610_SECONDARY_DIAG_ICD2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(6)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr7620_other_significant_diag_subsidiary_comment: Optional[str] = Field(default=None, description="""Additional comments on other significant conditions where coding is difficult or imprecise. (For example \"NF1\" or \"NF2\" to distinguish between these two distinct conditions which may have different treatment decisions or outcomes but cannot be coded separately.)""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR7620_OTHER_SIGNIFICANT_DIAG_SUBSIDIARY_COMMENT'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(50)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr7630_familial_cancer_syndrome: Optional[FamilialCancerSyndrome] = Field(default=None, description="""Indicate whether there is a possible or confirmed familial cancer syndrome""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR7630_FAMILIAL_CANCER_SYNDROME'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr7640_familial_cancer_syndrome_subsidiary_comment: Optional[str] = Field(default=None, description="""Specifies or describes familial cancer syndrome where Familial Cancer Syndrome is coded as \"Yes\" or \"Possible\". (For example \"Li-Fraumeni\", \"Rhabdoid tumour predisposition syndrome\" or \"Biallelic PMS2 mutation\" to identify distinct syndromes which may have different treatment decisions or outcomes but cannot be coded separately.)""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR7640_FAMILIAL_CANCER_SYNDROME_SUBSIDIARY_COMMENT'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(50)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr9020_functional_syndrome_class_indicator: Optional[FunctionalSyndromeClassificationIndicator] = Field(default=None, description="""Indicate whether there is a possible or confirmed Functional syndrome classification""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR9020_FUNCTIONAL_SYNDROME_CLASS_INDICATOR'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr9030_functional_syndrome_class_type1: Optional[FunctionalSyndromeClassificationType] = Field(default=None, description="""Specify the type of functional syndrome classification the patient is diagnosed with.
For Neuroendocrine tumours (NET) only.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR9030_FUNCTIONAL_SYNDROME_CLASS_TYPE1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr9030_functional_syndrome_class_type2: Optional[FunctionalSyndromeClassificationType] = Field(default=None, description="""Specify the type of functional syndrome classification the patient is diagnosed with.
For Neuroendocrine tumours (NET) only.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR9030_FUNCTIONAL_SYNDROME_CLASS_TYPE2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr9030_unknown_functional_syndrome_class_type1: Optional[FunctionalSyndromeClassificationType] = Field(default=None, description="""Specify the type of functional syndrome classification the patient is diagnosed with.
For Neuroendocrine tumours (NET) only.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR9030_UNKNOWN_FUNCTIONAL_SYNDROME_CLASS_TYPE1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr9040_unknown_other_functional_syndrome_class_type1: Optional[str] = Field(default=None, description="""Specify any other functional syndrome classification type""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR9040_UNKNOWN_OTHER_FUNCTIONAL_SYNDROME_CLASS_TYPE1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(50)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr9030_unknown_functional_syndrome_class_type2: Optional[FunctionalSyndromeClassificationType] = Field(default=None, description="""Specify the type of functional syndrome classification the patient is diagnosed with.
For Neuroendocrine tumours (NET) only.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR9030_UNKNOWN_FUNCTIONAL_SYNDROME_CLASS_TYPE2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr9040_unknown_other_functional_syndrome_class_type2: Optional[str] = Field(default=None, description="""Specify any other functional syndrome classification type""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR9040_UNKNOWN_OTHER_FUNCTIONAL_SYNDROME_CLASS_TYPE2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(50)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr9030_unknown_functional_syndrome_class_type3: Optional[FunctionalSyndromeClassificationType] = Field(default=None, description="""Specify the type of functional syndrome classification the patient is diagnosed with.
For Neuroendocrine tumours (NET) only.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR9030_UNKNOWN_FUNCTIONAL_SYNDROME_CLASS_TYPE3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr9040_unknown_other_functional_syndrome_class_type3: Optional[str] = Field(default=None, description="""Specify any other functional syndrome classification type""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR9040_UNKNOWN_OTHER_FUNCTIONAL_SYNDROME_CLASS_TYPE3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(50)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6960_prog1_metastatic_type1: Optional[MetastaticType] = Field(default=None, description="""Indicate the type of metastatic disease diagnosed by the clinical team""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6960_PROG1_METASTATIC_TYPE1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6970_prog1_metastatic_site1: Optional[MetastaticSite] = Field(default=None, description="""The site of the metastatic disease, if any, at diagnosis.
More than one site can be recorded""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6970_PROG1_METASTATIC_SITE1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6960_prog1_metastatic_type2: Optional[MetastaticType] = Field(default=None, description="""Indicate the type of metastatic disease diagnosed by the clinical team""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6960_PROG1_METASTATIC_TYPE2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6970_prog1_metastatic_site2: Optional[MetastaticSite] = Field(default=None, description="""The site of the metastatic disease, if any, at diagnosis.
More than one site can be recorded""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6970_PROG1_METASTATIC_SITE2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6960_prog1_metastatic_type3: Optional[MetastaticType] = Field(default=None, description="""Indicate the type of metastatic disease diagnosed by the clinical team""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6960_PROG1_METASTATIC_TYPE3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6970_prog1_metastatic_site3: Optional[MetastaticSite] = Field(default=None, description="""The site of the metastatic disease, if any, at diagnosis.
More than one site can be recorded""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6970_PROG1_METASTATIC_SITE3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6960_prog1_metastatic_type4: Optional[MetastaticType] = Field(default=None, description="""Indicate the type of metastatic disease diagnosed by the clinical team""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6960_PROG1_METASTATIC_TYPE4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6970_prog1_metastatic_site4: Optional[MetastaticSite] = Field(default=None, description="""The site of the metastatic disease, if any, at diagnosis.
More than one site can be recorded""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6970_PROG1_METASTATIC_SITE4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6960_prog2_metastatic_type1: Optional[MetastaticType] = Field(default=None, description="""Indicate the type of metastatic disease diagnosed by the clinical team""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6960_PROG2_METASTATIC_TYPE1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6970_prog2_metastatic_site1: Optional[MetastaticSite] = Field(default=None, description="""The site of the metastatic disease, if any, at diagnosis.
More than one site can be recorded""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6970_PROG2_METASTATIC_SITE1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6960_prog2_metastatic_type2: Optional[MetastaticType] = Field(default=None, description="""Indicate the type of metastatic disease diagnosed by the clinical team""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6960_PROG2_METASTATIC_TYPE2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6970_prog2_metastatic_site2: Optional[MetastaticSite] = Field(default=None, description="""The site of the metastatic disease, if any, at diagnosis.
More than one site can be recorded""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6970_PROG2_METASTATIC_SITE2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6960_prog2_metastatic_type3: Optional[MetastaticType] = Field(default=None, description="""Indicate the type of metastatic disease diagnosed by the clinical team""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6960_PROG2_METASTATIC_TYPE3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6970_prog2_metastatic_site3: Optional[MetastaticSite] = Field(default=None, description="""The site of the metastatic disease, if any, at diagnosis.
More than one site can be recorded""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6970_PROG2_METASTATIC_SITE3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6960_prog2_metastatic_type4: Optional[MetastaticType] = Field(default=None, description="""Indicate the type of metastatic disease diagnosed by the clinical team""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6960_PROG2_METASTATIC_TYPE4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6970_prog2_metastatic_site4: Optional[MetastaticSite] = Field(default=None, description="""The site of the metastatic disease, if any, at diagnosis.
More than one site can be recorded""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6970_PROG2_METASTATIC_SITE4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6910_progression1_date: Optional[date] = Field(default=None, description="""The DATE the progression was agreed by the clinical team.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6910_PROGRESSION1_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6910_progression2_date: Optional[date] = Field(default=None, description="""The DATE the progression was agreed by the clinical team.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6910_PROGRESSION2_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6910_progression3_date: Optional[date] = Field(default=None, description="""The DATE the progression was agreed by the clinical team.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6910_PROGRESSION3_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6910_progression4_date: Optional[date] = Field(default=None, description="""The DATE the progression was agreed by the clinical team.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6910_PROGRESSION4_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6910_progression5_date: Optional[date] = Field(default=None, description="""The DATE the progression was agreed by the clinical team.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6910_PROGRESSION5_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6910_progression6_date: Optional[date] = Field(default=None, description="""The DATE the progression was agreed by the clinical team.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6910_PROGRESSION6_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6910_progression7_date: Optional[date] = Field(default=None, description="""The DATE the progression was agreed by the clinical team.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6910_PROGRESSION7_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6910_progression8_date: Optional[date] = Field(default=None, description="""The DATE the progression was agreed by the clinical team.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6910_PROGRESSION8_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6910_progression9_date: Optional[date] = Field(default=None, description="""The DATE the progression was agreed by the clinical team.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6910_PROGRESSION9_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6910_progression10_date: Optional[date] = Field(default=None, description="""The DATE the progression was agreed by the clinical team.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6910_PROGRESSION10_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr7020_transformation_date1: Optional[date] = Field(default=None, description="""The DATE the transformation was agreed by the clinical team.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR7020_TRANSFORMATION_DATE1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr7010_morphology_icd_o_3_trans1: Optional[str] = Field(default=None, description="""The morphology code for the transformation of the cancer as defined by ICD-O-3. This can be recorded as well as or instead of MORPHOLOGY (SNOMED) TRANSFORMATION.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR7010_MORPHOLOGY_ICD_O_3_TRANS1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(7)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr7000_curr_morphology_snomed_trans1: Optional[str] = Field(default=None, description="""This is the TRANSFORMATION DIAGNOSIS using the SNOMED International / SNOMED CT code for the cell type of the tumour recorded as part of a Cancer Care Spell. This can be recorded as well as or instead of MORPHOLOGY (ICD-O-3) TRANSFORMATION.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR7000_CURR_MORPHOLOGY_SNOMED_TRANS1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr7030_curr_snomed_version_trans1: Optional[SnomedVersionTransformation] = Field(default=None, description="""The version of SNOMED used to encode MORPHOLOGY (SNOMED) TRANSFORMATION""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR7030_CURR_SNOMED_VERSION_TRANS1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr7020_transformation_date_2: Optional[date] = Field(default=None, description="""The DATE the transformation was agreed by the clinical team.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR7020_TRANSFORMATION_DATE_2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr7010_morphology_icd_o_3_trans2: Optional[str] = Field(default=None, description="""The morphology code for the transformation of the cancer as defined by ICD-O-3. This can be recorded as well as or instead of MORPHOLOGY (SNOMED) TRANSFORMATION.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR7010_MORPHOLOGY_ICD_O_3_TRANS2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(7)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr7000_curr_morphology_snomed_trans2: Optional[str] = Field(default=None, description="""This is the TRANSFORMATION DIAGNOSIS using the SNOMED International / SNOMED CT code for the cell type of the tumour recorded as part of a Cancer Care Spell. This can be recorded as well as or instead of MORPHOLOGY (ICD-O-3) TRANSFORMATION.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR7000_CURR_MORPHOLOGY_SNOMED_TRANS2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr7030_curr_snomed_version_trans2: Optional[SnomedVersionTransformation] = Field(default=None, description="""The version of SNOMED used to encode MORPHOLOGY (SNOMED) TRANSFORMATION""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR7030_CURR_SNOMED_VERSION_TRANS2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr6430_person_observation_height_in_metres1: Optional[str] = Field(default=None, description="""Height of the patient, in metres to 2 decimal""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6430_PERSON_OBSERVATION_HEIGHT_IN_METRES1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr6440_person_observation_weight1: Optional[str] = Field(default=None, description="""Weight of the patient, in kilograms with up to three decimal places (nnn.nnn).""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6440_PERSON_OBSERVATION_WEIGHT1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(7)'}},
         'domain_of': ['COSDResearchView']} })
    cr6450_body_mass_index1: Optional[str] = Field(default=None, description="""Estimate of a patient's Body Mass Index (BMI). If Height and Weight are provided, this can be automatically calculated.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6450_BODY_MASS_INDEX1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr6450_date_observation_measured1: Optional[date] = Field(default=None, description="""Estimate of a patient's Body Mass Index (BMI). If Height and Weight are provided, this can be automatically calculated.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6450_DATE_OBSERVATION_MEASURED1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr6430_person_observation_height_in_metres2: Optional[str] = Field(default=None, description="""Height of the patient, in metres to 2 decimal""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6430_PERSON_OBSERVATION_HEIGHT_IN_METRES2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr6440_person_observation_weight2: Optional[str] = Field(default=None, description="""Weight of the patient, in kilograms with up to three decimal places (nnn.nnn).""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6440_PERSON_OBSERVATION_WEIGHT2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(7)'}},
         'domain_of': ['COSDResearchView']} })
    cr6450_body_mass_index2: Optional[str] = Field(default=None, description="""Estimate of a patient's Body Mass Index (BMI). If Height and Weight are provided, this can be automatically calculated.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6450_BODY_MASS_INDEX2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr6450_date_observation_measured2: Optional[date] = Field(default=None, description="""Estimate of a patient's Body Mass Index (BMI). If Height and Weight are provided, this can be automatically calculated.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6450_DATE_OBSERVATION_MEASURED2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr2050_clinical_nurse_specialist_indication_code: Optional[ClinicalNurseSpecialistIndicationCode] = Field(default=None, description="""Record if and when the patient saw an appropriate site specific clinical nurse specialist.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR2050_CLINICAL_NURSE_SPECIALIST_INDICATION_CODE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr7800_tobacco_smoking_status: Optional[TobaccoSmokingStatus] = Field(default=None, description="""Specify the current tobacco smoking status of the patient.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7800_TOBACCO_SMOKING_STATUS'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr7810_tobacco_smoking_cessation: Optional[TobaccoSmokingCessation] = Field(default=None, description="""Was treatment for tobacco addiction/cessation given to the patient""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7810_TOBACCO_SMOKING_CESSATION'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr6760_history_of_alcohol_current: Optional[HistoryOfAlcoholCurrent] = Field(default=None, description="""Specify the current history of alcohol consumption for the patient (≤3 months) from date of diagnosis
These are based on the UK Chief Medical Officers' Alcohol Guideline Review (Jan 2016)""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6760_HISTORY_OF_ALCOHOL_CURRENT'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr6770_history_of_alcohol_past: Optional[HistoryOfAlcoholPast] = Field(default=None, description="""Specify the past history of alcohol consumption for the patient (>3 months) from date of diagnosis
These are based on the UK Chief Medical Officers' Alcohol Guideline Review (Jan 2016)""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6770_HISTORY_OF_ALCOHOL_PAST'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr9070_diabetes_mellitus_type1_and_type2_indicator: Optional[DiabetesMellitusType1AndType2Indicator] = Field(default=None, description="""Does the patient have a diagnosis of type 1 or type 2 diabetes mellitus?""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR9070_DIABETES_MELLITUS_TYPE1_AND_TYPE2_INDICATOR'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr7830_menopausal_status: Optional[MenopausalStatus] = Field(default=None, description="""Record the Menopausal Status (at the point of diagnosis) of female patients only""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7830_MENOPAUSAL_STATUS'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr7840_physical_activity_current: Optional[PhysicalActivityCurrent] = Field(default=None, description="""Specify the current physical activity level""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7840_PHYSICAL_ACTIVITY_CURRENT'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr7900_holistic_assessment_offered1: Optional[AssessmentOffered] = Field(default=None, description="""An indication of whether a PATIENT has been offered a Holistic Needs Assessment (HNA)""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7900_HOLISTIC_ASSESSMENT_OFFERED1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr7920_hol_assessment_care_plan_status1: Optional[AssessmentCarePlanStatus] = Field(default=None, description="""An indication of whether a PATIENT has completed a Holistic Needs Assessment (HNA) and /or Personalised Care and Support Plan (PCSP) was offered/completed""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7920_HOL_ASSESSMENT_CARE_PLAN_STATUS1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr7930_hol_assessment_care_plan_date1: Optional[date] = Field(default=None, description="""The date a Holistic Needs Assessment or Personalised Care and Support Plan is offered, declined, completed not required, or unable to be completed. In addition, a date should be provided where a decision was made not to offer an assessment 'Not Offered' for valid clinical reasons.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7930_HOL_ASSESSMENT_CARE_PLAN_DATE1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr7940_hol_assessment_care_plan_point_of_pathway1: Optional[AssessmentCarePlanPointOfPathway] = Field(default=None, description="""The point of the pathway where a Holistic Needs Assessment or Personalised Care and Support Plan is offered, declined, completed, not required, or unable to be completed""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7940_HOL_ASSESSMENT_CARE_PLAN_POINT_OF_PATHWAY1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr7950_hol_staff_role_offering_the_assessment1: Optional[StaffRoleOfferingTheAssessment] = Field(default=None, description="""Record the role of the individual offering the Holistic Needs Assessment (Secondary Care Only)""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7950_HOL_STAFF_ROLE_OFFERING_THE_ASSESSMENT1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr7960_hol_staff_role_offering_the_planning1: Optional[StaffRoleOfferingThePlanning] = Field(default=None, description="""Record the role of the individual offering the Personalised Care and Support Planning (Secondary Care Only)""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7960_HOL_STAFF_ROLE_OFFERING_THE_PLANNING1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr7900_holistic_assessment_offered2: Optional[AssessmentOffered] = Field(default=None, description="""An indication of whether a PATIENT has been offered a Holistic Needs Assessment (HNA)""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7900_HOLISTIC_ASSESSMENT_OFFERED2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr7920_hol_assessment_care_plan_status2: Optional[AssessmentCarePlanStatus] = Field(default=None, description="""An indication of whether a PATIENT has completed a Holistic Needs Assessment (HNA) and /or Personalised Care and Support Plan (PCSP) was offered/completed""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7920_HOL_ASSESSMENT_CARE_PLAN_STATUS2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr7930_hol_assessment_care_plan_date2: Optional[date] = Field(default=None, description="""The date a Holistic Needs Assessment or Personalised Care and Support Plan is offered, declined, completed not required, or unable to be completed. In addition, a date should be provided where a decision was made not to offer an assessment 'Not Offered' for valid clinical reasons.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7930_HOL_ASSESSMENT_CARE_PLAN_DATE2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr7940_hol_assessment_care_plan_point_of_pathway2: Optional[AssessmentCarePlanPointOfPathway] = Field(default=None, description="""The point of the pathway where a Holistic Needs Assessment or Personalised Care and Support Plan is offered, declined, completed, not required, or unable to be completed""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7940_HOL_ASSESSMENT_CARE_PLAN_POINT_OF_PATHWAY2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr7950_hol_staff_role_offering_the_assessment2: Optional[StaffRoleOfferingTheAssessment] = Field(default=None, description="""Record the role of the individual offering the Holistic Needs Assessment (Secondary Care Only)""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7950_HOL_STAFF_ROLE_OFFERING_THE_ASSESSMENT2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr7960_hol_staff_role_offering_the_planning2: Optional[StaffRoleOfferingThePlanning] = Field(default=None, description="""Record the role of the individual offering the Personalised Care and Support Planning (Secondary Care Only)""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7960_HOL_STAFF_ROLE_OFFERING_THE_PLANNING2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr0430_mdt_discussion_date_cancer: Optional[date] = Field(default=None, description="""The date on which the PATIENT's Cancer Care Plan was discussed at a Multidisciplinary Team Meeting and a treatment planning decision was made.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0430_MDT_DISCUSSION_DATE_CANCER'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr0460_cancer_care_plan_intent: Optional[CancerCarePlanIntent] = Field(default=None, description="""The intention of a Cancer Care Plan developed within a Cancer Care Spell.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0460_CANCER_CARE_PLAN_INTENT'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr0470_planned_cancer_treatment_type1: Optional[PlannedCancerTreatmentType] = Field(default=None, description="""This is the clinically proposed treatment, usually agreed at a Multi Disciplinary Team Meeting, and may not be the same as the treatment which is subsequently agreed with the patient. More than one planned treatment type may be recorded and these may either be alternative or sequential treatments.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0470_PLANNED_CANCER_TREATMENT_TYPE1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr0470_planned_cancer_treatment_type2: Optional[PlannedCancerTreatmentType] = Field(default=None, description="""This is the clinically proposed treatment, usually agreed at a Multi Disciplinary Team Meeting, and may not be the same as the treatment which is subsequently agreed with the patient. More than one planned treatment type may be recorded and these may either be alternative or sequential treatments.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0470_PLANNED_CANCER_TREATMENT_TYPE2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr0470_planned_cancer_treatment_type3: Optional[PlannedCancerTreatmentType] = Field(default=None, description="""This is the clinically proposed treatment, usually agreed at a Multi Disciplinary Team Meeting, and may not be the same as the treatment which is subsequently agreed with the patient. More than one planned treatment type may be recorded and these may either be alternative or sequential treatments.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0470_PLANNED_CANCER_TREATMENT_TYPE3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr0490_no_cancer_treatment_reason: Optional[NoCancerTreatmentReason] = Field(default=None, description="""The main reason why no active cancer treatment is specified within a Cancer Care Plan.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0490_NO_CANCER_TREATMENT_REASON'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr0520_t_category_final_pretreatment: Optional[str] = Field(default=None, description="""T CATEGORY (FINAL PRETREATMENT) is the code which classifies the size and extent of the primary tumour before treatment.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR0520_T_CATEGORY_FINAL_PRETREATMENT'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(15)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr0540_n_category_final_pretreatment: Optional[str] = Field(default=None, description="""N CATEGORY (FINAL PRETREATMENT) is the code which classifies the absence or presence and extent of regional lymph node metastases before treatment.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR0540_N_CATEGORY_FINAL_PRETREATMENT'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(15)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr0560_m_category_final_pretreatment: Optional[str] = Field(default=None, description="""M CATEGORY (FINAL PRETREATMENT) is the code which classifies the absence or presence of distant metastases pre treatment.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR0560_M_CATEGORY_FINAL_PRETREATMENT'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(15)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr0580_tnm_stage_grouping_final_pretreatment: Optional[str] = Field(default=None, description="""Record the overall clinical TNM stage grouping of the tumour, derived from each T, N and M component prior to treatment. This classification is based on all the evidence available to the clinician(s) with responsibility for assessing the patient and for the patient’s treatment plan. Such evidence arises from physical examination, imaging, endoscopy, biopsy, surgical exploration and other relevant examinations.
The overall pretreatment TNM stage grouping indicates the tumour stage at the time the treatment plan was devised.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR0580_TNM_STAGE_GROUPING_FINAL_PRETREATMENT'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(15)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6800_org_site_id_reported_pretreatment_tnm_stage: Optional[str] = Field(default=None, description="""This is the ORGANISATION IDENTIFIER of the ORGANISATION SITE where the diagnosing MDT agreed the Final PreTreatment TNM Stage""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6800_ORG_SITE_ID_REPORTED_PRETREATMENT_TNM_STAGE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(9)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr3120_stage_date_final_pretreatment_stage: Optional[date] = Field(default=None, description="""The date of the TNM STAGE GROUPING (FINAL PRE TREATMENT).""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR3120_STAGE_DATE_FINAL_PRETREATMENT_STAGE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr0620_t_category_integrated_stage: Optional[str] = Field(default=None, description="""T CATEGORY (INTEGRATED) is the code which classifies the size and extent of the primary tumour after treatment and/or after all available evidence has been collected.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR0620_T_CATEGORY_INTEGRATED_STAGE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(15)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr0630_n_category_integrated_stage: Optional[str] = Field(default=None, description="""N CATEGORY (INTEGRATED) is the code which classifies the absence or presence and extent of regional lymph node metastases after treatment and/or after all available evidence has been collected.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR0630_N_CATEGORY_INTEGRATED_STAGE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(15)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr0640_m_category_integrated_stage: Optional[str] = Field(default=None, description="""M CATEGORY (INTEGRATED) is the code classifies the absence or presence of distant metastases after treatment and/or after all available evidence has been collected.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR0640_M_CATEGORY_INTEGRATED_STAGE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(15)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr0610_tnm_stage_grouping_integrated: Optional[str] = Field(default=None, description="""Record the overall TNM stage grouping of the tumour, derived from each T, N and M component after treatment. This classification is based on all the evidence available to the clinician(s) with responsibility for assessing the patient. Such evidence arises from physical examination, imaging, endoscopy, biopsy, surgical exploration and other relevant examinations.
The overall integrated TNM stage grouping indicates the tumour stage after treatment and/or after all available evidence has been collected.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR0610_TNM_STAGE_GROUPING_INTEGRATED'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(15)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6810_org_site_id_reported_integrated_tnm_stage: Optional[str] = Field(default=None, description="""This is the ORGANISATION IDENTIFIER of the ORGANISATION SITE where the treating MDT post surgery (where surgery was the first treatment) agreed the Integrated TNM Stage""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6810_ORG_SITE_ID_REPORTED_INTEGRATED_TNM_STAGE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(9)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr3130_stage_date_integrated_stage: Optional[date] = Field(default=None, description="""The date of the TNM STAGE GROUPING (INTEGRATED)""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR3130_STAGE_DATE_INTEGRATED_STAGE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6980_tnm_coding_edition: Optional[TnmCodingEdition] = Field(default=None, description="""The TNM Coding edition in use""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6980_TNM_CODING_EDITION'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr2070_tnm_version_number_staging: Optional[str] = Field(default=None, description="""The AJCC, UICC or ENETS version number used for Tumour, Node and Metastasis (TNM) staging for cancer diagnosis.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR2070_TNM_VERSION_NUMBER_STAGING'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr8300_org_site_id_site_specific_stage1: Optional[str] = Field(default=None, description="""This is the ORGANISATION IDENTIFIER of the ORGANISATION SITE who carried out the site specific stage""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR8300_ORG_SITE_ID_SITE_SPECIFIC_STAGE1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(9)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr8310_stage_date_site_specific_stage1: Optional[date] = Field(default=None, description="""The date of the sample/MDT which provided a positive stage outcome""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR8310_STAGE_DATE_SITE_SPECIFIC_STAGE1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr8300_org_site_id_site_specific_stage2: Optional[str] = Field(default=None, description="""This is the ORGANISATION IDENTIFIER of the ORGANISATION SITE who carried out the site specific stage""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR8300_ORG_SITE_ID_SITE_SPECIFIC_STAGE2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(9)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr8310_stage_date_site_specific_stage2: Optional[date] = Field(default=None, description="""The date of the sample/MDT which provided a positive stage outcome""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR8310_STAGE_DATE_SITE_SPECIFIC_STAGE2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr6540_treat1_adjunctive_therapy: Optional[AdjunctiveTherapy] = Field(default=None, description="""Adjunctive therapy is therapy given in addition to the main therapy to maximize its effectiveness.
This field allows for the accurate recording of these to determine if Adjunctive therapy was Adjuvant (After the main therapy) or Neo-Adjuvant (Before the main therapy) or not applicable.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6540_TREAT1_ADJUNCTIVE_THERAPY'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr0680_treat1_cancer_treatment_intent: Optional[CancerTreatmentIntent] = Field(default=None, description="""The intention of the cancer treatment provided during a Cancer Care Spell.
* Disease Modification is Drug Specific ** Diagnostic and Staging are Surgery Specific""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0680_TREAT1_CANCER_TREATMENT_INTENT'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr1370_treat1_treatment_start_date_cancer: Optional[date] = Field(default=None, description="""This is the Start Date of the first, second or subsequent cancer treatment given to a PATIENT who is receiving care for a cancer condition.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR1370_TREAT1_TREATMENT_START_DATE_CANCER'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr2040_treat1_cancer_treatment_modality_registration: Optional[CancerTreatmentModalityRegistration] = Field(default=None, description="""The type of treatment or care which was delivered in a Cancer Treatment Period.
This is subset of Cancer Treatment Modality, which supports Cancer Registration in England""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR2040_TREAT1_CANCER_TREATMENT_MODALITY_REGISTRATION'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr1450_treat1_org_site_id_of_provider_cancer_treatment_start_date: Optional[str] = Field(default=None, description="""The ORGANISATION IDENTIFIER of the Organisation Site where the TREATMENT START DATE FOR CANCER is recorded.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR1450_TREAT1_ORG_SITE_ID_OF_PROVIDER_CANCER_TREATMENT_START_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(9)'}},
         'domain_of': ['COSDResearchView']} })
    cr8400_treat1_con_treat_prof_regissuer_code: Optional[ProfessionalRegistrationIssuerCodeConsultantTreatment] = Field(default=None, description="""A code which identifies the PROFESSIONAL REGISTRATION BODY for the Consultant or health care professional responsible for the treatment of the patient.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8400_TREAT1_CON_TREAT_PROF_REGISSUER_CODE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr8410_treat1_con_treat_prof_regentry_identifier: Optional[str] = Field(default=None, description="""The registration identifier allocated by a Professional Registration Body for the Consultant or health care professional responsible for the treatment of the patient.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8410_TREAT1_CON_TREAT_PROF_REGENTRY_IDENTIFIER'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(32)'}},
         'domain_of': ['COSDResearchView']} })
    cr8420_treat1_end_of_treatment_summary_date: Optional[date] = Field(default=None, description="""Record the date of completion of 'End of Treatment Summary' at the end of acute (secondary care) treatment(s) which was sent to the patient and/or the GP""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8420_TREAT1_END_OF_TREATMENT_SUMMARY_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr0740_treat1_discharge_date_hospital_provider_spell: Optional[date] = Field(default=None, description="""The date a PATIENT was discharged from a Hospital Provider Spell.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0740_TREAT1_DISCHARGE_DATE_HOSPITAL_PROVIDER_SPELL'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr9080_treat1_discharge_destination_hospital_provider_spell: Optional[DestinationOfDischargeHospitalProviderSpell] = Field(default=None, description="""This records the destination of a PATIENT on completion of the Hospital Provider Spell. It can also indicate that the PATIENT died.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR9080_TREAT1_DISCHARGE_DESTINATION_HOSPITAL_PROVIDER_SPELL'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr0710_treat1_procedure_date: Optional[date] = Field(default=None, description="""The date the procedure was carried out.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0710_TREAT1_PROCEDURE_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr8500_treat1_surgical_admission_type: Optional[SurgicalAdmissionType] = Field(default=None, description="""The type of Surgical Admission""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8500_TREAT1_SURGICAL_ADMISSION_TYPE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr8510_treat1_prof_reg_issuer_code_cons_surgeon1: Optional[ProfessionalRegistrationIssuerCodeConsultantSurgeon] = Field(default=None, description="""A code which identifies the PROFESSIONAL REGISTRATION BODY for the Consultant or health care professional who is responsible for the treatment of the patient. If he/she is part of a surgical team, add all consultant surgeons responsible for the procedure.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8510_TREAT1_PROF_REG_ISSUER_CODE_CONS_SURGEON1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr8520_treat1_prof_reg_entry_identifier_cons_surgeon1: Optional[str] = Field(default=None, description="""The registration identifier allocated by a Professional Registration Body for the Consultant surgeon responsible for the treatment of the patient. If he/she is part of a surgical team, add all consultant surgeons responsible for the procedure.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8520_TREAT1_PROF_REG_ENTRY_IDENTIFIER_CONS_SURGEON1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(32)'}},
         'domain_of': ['COSDResearchView']} })
    cr8510_treat1_prof_reg_issuer_code_cons_surgeon2: Optional[ProfessionalRegistrationIssuerCodeConsultantSurgeon] = Field(default=None, description="""A code which identifies the PROFESSIONAL REGISTRATION BODY for the Consultant or health care professional who is responsible for the treatment of the patient. If he/she is part of a surgical team, add all consultant surgeons responsible for the procedure.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8510_TREAT1_PROF_REG_ISSUER_CODE_CONS_SURGEON2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr8520_treat1_prof_reg_entry_identifier_cons_surgeon2: Optional[str] = Field(default=None, description="""The registration identifier allocated by a Professional Registration Body for the Consultant surgeon responsible for the treatment of the patient. If he/she is part of a surgical team, add all consultant surgeons responsible for the procedure.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8520_TREAT1_PROF_REG_ENTRY_IDENTIFIER_CONS_SURGEON2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(32)'}},
         'domain_of': ['COSDResearchView']} })
    cr8510_treat1_prof_reg_issuer_code_cons_surgeon3: Optional[ProfessionalRegistrationIssuerCodeConsultantSurgeon] = Field(default=None, description="""A code which identifies the PROFESSIONAL REGISTRATION BODY for the Consultant or health care professional who is responsible for the treatment of the patient. If he/she is part of a surgical team, add all consultant surgeons responsible for the procedure.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8510_TREAT1_PROF_REG_ISSUER_CODE_CONS_SURGEON3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr8520_treat1_prof_reg_entry_identifier_cons_surgeon3: Optional[str] = Field(default=None, description="""The registration identifier allocated by a Professional Registration Body for the Consultant surgeon responsible for the treatment of the patient. If he/she is part of a surgical team, add all consultant surgeons responsible for the procedure.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8520_TREAT1_PROF_REG_ENTRY_IDENTIFIER_CONS_SURGEON3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(32)'}},
         'domain_of': ['COSDResearchView']} })
    cr0720_treat1_primary_procedure_opcs: Optional[str] = Field(default=None, description="""PRIMARY PROCEDURE (OPCS) is the OPCS Classification of Interventions and Procedures code which is used to identify the primary Patient Procedure carried out.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0720_TREAT1_PRIMARY_PROCEDURE_OPCS'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr3040_treat1_primary_procedure_snomed_ct: Optional[str] = Field(default=None, description="""Primary procedure is the main procedure carried out using SNOMED CT. This maybe recorded in addition to PRIMARY PROCEDURE (OPCS).""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3040_TREAT1_PRIMARY_PROCEDURE_SNOMED_CT'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr0730_treat1_procedure_opcs2: Optional[str] = Field(default=None, description="""This is a procedure other than the PRIMARY PROCEDURE (OPCS), carried out and recorded for CDS or Hospital Episode Statistics purposes. (This may occur more than once).""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0730_TREAT1_PROCEDURE_OPCS2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr0730_treat1_procedure_opcs3: Optional[str] = Field(default=None, description="""This is a procedure other than the PRIMARY PROCEDURE (OPCS), carried out and recorded for CDS or Hospital Episode Statistics purposes. (This may occur more than once).""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0730_TREAT1_PROCEDURE_OPCS3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr0730_treat1_procedure_opcs4: Optional[str] = Field(default=None, description="""This is a procedure other than the PRIMARY PROCEDURE (OPCS), carried out and recorded for CDS or Hospital Episode Statistics purposes. (This may occur more than once).""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0730_TREAT1_PROCEDURE_OPCS4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr3050_treat1_procedure_snomed_ct2: Optional[str] = Field(default=None, description="""This is a procedure other than the PRIMARY PROCEDURE, carried out and recorded for CDS or Hospital Episode Statistics purposes. (This may occur more than once).This maybe recorded in addition to PROCEDURE (OPCS).""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3050_TREAT1_PROCEDURE_SNOMED_CT2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr3050_treat1_procedure_snomed_ct3: Optional[str] = Field(default=None, description="""This is a procedure other than the PRIMARY PROCEDURE, carried out and recorded for CDS or Hospital Episode Statistics purposes. (This may occur more than once).This maybe recorded in addition to PROCEDURE (OPCS).""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3050_TREAT1_PROCEDURE_SNOMED_CT3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr3050_treat1_procedure_snomed_ct4: Optional[str] = Field(default=None, description="""This is a procedure other than the PRIMARY PROCEDURE, carried out and recorded for CDS or Hospital Episode Statistics purposes. (This may occur more than once).This maybe recorded in addition to PROCEDURE (OPCS).""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3050_TREAT1_PROCEDURE_SNOMED_CT4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr6480_treat1_unplanned_return_to_theatre_indicator: Optional[UnplannedReturnToTheatreIndicator] = Field(default=None, description="""Whether or not the patient required a second (unplanned) operation during the same admission as the primary procedure""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6480_TREAT1_UNPLANNED_RETURN_TO_THEATRE_INDICATOR'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr6010_treat1_asa_score: Optional[AsaScore] = Field(default=None, description="""The ASA physical status classification system is a system for assessing the fitness of patients before surgery.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6010_TREAT1_ASA_SCORE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr6310_treat1_surgery_surgical_access_type: Optional[SurgicalAccessType] = Field(default=None, description="""The surgical access type used to perform the main procedure.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6310_TREAT1_SURGERY_SURGICAL_ACCESS_TYPE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr6540_treat2_adjunctive_therapy: Optional[AdjunctiveTherapy] = Field(default=None, description="""Adjunctive therapy is therapy given in addition to the main therapy to maximize its effectiveness.
This field allows for the accurate recording of these to determine if Adjunctive therapy was Adjuvant (After the main therapy) or Neo-Adjuvant (Before the main therapy) or not applicable.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6540_TREAT2_ADJUNCTIVE_THERAPY'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr0680_treat2_cancer_treatment_intent: Optional[CancerTreatmentIntent] = Field(default=None, description="""The intention of the cancer treatment provided during a Cancer Care Spell.
* Disease Modification is Drug Specific ** Diagnostic and Staging are Surgery Specific""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0680_TREAT2_CANCER_TREATMENT_INTENT'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr1370_treat2_treatment_start_date_cancer: Optional[date] = Field(default=None, description="""This is the Start Date of the first, second or subsequent cancer treatment given to a PATIENT who is receiving care for a cancer condition.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR1370_TREAT2_TREATMENT_START_DATE_CANCER'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr2040_treat2_cancer_treatment_modality_registration: Optional[CancerTreatmentModalityRegistration] = Field(default=None, description="""The type of treatment or care which was delivered in a Cancer Treatment Period.
This is subset of Cancer Treatment Modality, which supports Cancer Registration in England""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR2040_TREAT2_CANCER_TREATMENT_MODALITY_REGISTRATION'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr1450_treat2_org_site_id_of_provider_cancer_treatment_start_date: Optional[str] = Field(default=None, description="""The ORGANISATION IDENTIFIER of the Organisation Site where the TREATMENT START DATE FOR CANCER is recorded.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR1450_TREAT2_ORG_SITE_ID_OF_PROVIDER_CANCER_TREATMENT_START_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(9)'}},
         'domain_of': ['COSDResearchView']} })
    cr8400_treat2_con_treat_prof_regissuer_code: Optional[ProfessionalRegistrationIssuerCodeConsultantTreatment] = Field(default=None, description="""A code which identifies the PROFESSIONAL REGISTRATION BODY for the Consultant or health care professional responsible for the treatment of the patient.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8400_TREAT2_CON_TREAT_PROF_REGISSUER_CODE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr8410_treat2_con_treat_prof_regentry_identifier: Optional[str] = Field(default=None, description="""The registration identifier allocated by a Professional Registration Body for the Consultant or health care professional responsible for the treatment of the patient.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8410_TREAT2_CON_TREAT_PROF_REGENTRY_IDENTIFIER'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(32)'}},
         'domain_of': ['COSDResearchView']} })
    cr8420_treat2_end_of_treatment_summary_date: Optional[date] = Field(default=None, description="""Record the date of completion of 'End of Treatment Summary' at the end of acute (secondary care) treatment(s) which was sent to the patient and/or the GP""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8420_TREAT2_END_OF_TREATMENT_SUMMARY_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr0740_treat2_discharge_date_hospital_provider_spell: Optional[date] = Field(default=None, description="""The date a PATIENT was discharged from a Hospital Provider Spell.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0740_TREAT2_DISCHARGE_DATE_HOSPITAL_PROVIDER_SPELL'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr9080_treat2_discharge_destination_hospital_provider_spell: Optional[DestinationOfDischargeHospitalProviderSpell] = Field(default=None, description="""This records the destination of a PATIENT on completion of the Hospital Provider Spell. It can also indicate that the PATIENT died.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR9080_TREAT2_DISCHARGE_DESTINATION_HOSPITAL_PROVIDER_SPELL'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr0710_treat2_procedure_date: Optional[date] = Field(default=None, description="""The date the procedure was carried out.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0710_TREAT2_PROCEDURE_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr8500_treat2_surgical_admission_type: Optional[SurgicalAdmissionType] = Field(default=None, description="""The type of Surgical Admission""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8500_TREAT2_SURGICAL_ADMISSION_TYPE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr8510_treat2_prof_reg_issuer_code_cons_surgeon1: Optional[ProfessionalRegistrationIssuerCodeConsultantSurgeon] = Field(default=None, description="""A code which identifies the PROFESSIONAL REGISTRATION BODY for the Consultant or health care professional who is responsible for the treatment of the patient. If he/she is part of a surgical team, add all consultant surgeons responsible for the procedure.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8510_TREAT2_PROF_REG_ISSUER_CODE_CONS_SURGEON1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr8520_treat2_prof_reg_entry_identifier_cons_surgeon1: Optional[str] = Field(default=None, description="""The registration identifier allocated by a Professional Registration Body for the Consultant surgeon responsible for the treatment of the patient. If he/she is part of a surgical team, add all consultant surgeons responsible for the procedure.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8520_TREAT2_PROF_REG_ENTRY_IDENTIFIER_CONS_SURGEON1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(32)'}},
         'domain_of': ['COSDResearchView']} })
    cr8510_treat2_prof_reg_issuer_code_cons_surgeon2: Optional[ProfessionalRegistrationIssuerCodeConsultantSurgeon] = Field(default=None, description="""A code which identifies the PROFESSIONAL REGISTRATION BODY for the Consultant or health care professional who is responsible for the treatment of the patient. If he/she is part of a surgical team, add all consultant surgeons responsible for the procedure.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8510_TREAT2_PROF_REG_ISSUER_CODE_CONS_SURGEON2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr8520_treat2_prof_reg_entry_identifier_cons_surgeon2: Optional[str] = Field(default=None, description="""The registration identifier allocated by a Professional Registration Body for the Consultant surgeon responsible for the treatment of the patient. If he/she is part of a surgical team, add all consultant surgeons responsible for the procedure.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8520_TREAT2_PROF_REG_ENTRY_IDENTIFIER_CONS_SURGEON2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(32)'}},
         'domain_of': ['COSDResearchView']} })
    cr8510_treat2_prof_reg_issuer_code_cons_surgeon3: Optional[ProfessionalRegistrationIssuerCodeConsultantSurgeon] = Field(default=None, description="""A code which identifies the PROFESSIONAL REGISTRATION BODY for the Consultant or health care professional who is responsible for the treatment of the patient. If he/she is part of a surgical team, add all consultant surgeons responsible for the procedure.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8510_TREAT2_PROF_REG_ISSUER_CODE_CONS_SURGEON3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr8520_treat2_prof_reg_entry_identifier_cons_surgeon3: Optional[str] = Field(default=None, description="""The registration identifier allocated by a Professional Registration Body for the Consultant surgeon responsible for the treatment of the patient. If he/she is part of a surgical team, add all consultant surgeons responsible for the procedure.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8520_TREAT2_PROF_REG_ENTRY_IDENTIFIER_CONS_SURGEON3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(32)'}},
         'domain_of': ['COSDResearchView']} })
    cr0720_treat2_primary_procedure_opcs: Optional[str] = Field(default=None, description="""PRIMARY PROCEDURE (OPCS) is the OPCS Classification of Interventions and Procedures code which is used to identify the primary Patient Procedure carried out.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0720_TREAT2_PRIMARY_PROCEDURE_OPCS'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr3040_treat2_primary_procedure_snomed_ct: Optional[str] = Field(default=None, description="""Primary procedure is the main procedure carried out using SNOMED CT. This maybe recorded in addition to PRIMARY PROCEDURE (OPCS).""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3040_TREAT2_PRIMARY_PROCEDURE_SNOMED_CT'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr0730_treat2_procedure_opcs2: Optional[str] = Field(default=None, description="""This is a procedure other than the PRIMARY PROCEDURE (OPCS), carried out and recorded for CDS or Hospital Episode Statistics purposes. (This may occur more than once).""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0730_TREAT2_PROCEDURE_OPCS2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr0730_treat2_procedure_opcs3: Optional[str] = Field(default=None, description="""This is a procedure other than the PRIMARY PROCEDURE (OPCS), carried out and recorded for CDS or Hospital Episode Statistics purposes. (This may occur more than once).""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0730_TREAT2_PROCEDURE_OPCS3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr0730_treat2_procedure_opcs4: Optional[str] = Field(default=None, description="""This is a procedure other than the PRIMARY PROCEDURE (OPCS), carried out and recorded for CDS or Hospital Episode Statistics purposes. (This may occur more than once).""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0730_TREAT2_PROCEDURE_OPCS4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr3050_treat2_procedure_snomed_ct2: Optional[str] = Field(default=None, description="""This is a procedure other than the PRIMARY PROCEDURE, carried out and recorded for CDS or Hospital Episode Statistics purposes. (This may occur more than once).This maybe recorded in addition to PROCEDURE (OPCS).""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3050_TREAT2_PROCEDURE_SNOMED_CT2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr3050_treat2_procedure_snomed_ct3: Optional[str] = Field(default=None, description="""This is a procedure other than the PRIMARY PROCEDURE, carried out and recorded for CDS or Hospital Episode Statistics purposes. (This may occur more than once).This maybe recorded in addition to PROCEDURE (OPCS).""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3050_TREAT2_PROCEDURE_SNOMED_CT3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr3050_treat2_procedure_snomed_ct4: Optional[str] = Field(default=None, description="""This is a procedure other than the PRIMARY PROCEDURE, carried out and recorded for CDS or Hospital Episode Statistics purposes. (This may occur more than once).This maybe recorded in addition to PROCEDURE (OPCS).""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3050_TREAT2_PROCEDURE_SNOMED_CT4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr6480_treat2_unplanned_return_to_theatre_indicator: Optional[UnplannedReturnToTheatreIndicator] = Field(default=None, description="""Whether or not the patient required a second (unplanned) operation during the same admission as the primary procedure""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6480_TREAT2_UNPLANNED_RETURN_TO_THEATRE_INDICATOR'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr6010_treat2_asa_score: Optional[AsaScore] = Field(default=None, description="""The ASA physical status classification system is a system for assessing the fitness of patients before surgery.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6010_TREAT2_ASA_SCORE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr6310_treat2_surgery_surgical_access_type: Optional[SurgicalAccessType] = Field(default=None, description="""The surgical access type used to perform the main procedure.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6310_TREAT2_SURGERY_SURGICAL_ACCESS_TYPE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr6540_treat3_adjunctive_therapy: Optional[AdjunctiveTherapy] = Field(default=None, description="""Adjunctive therapy is therapy given in addition to the main therapy to maximize its effectiveness.
This field allows for the accurate recording of these to determine if Adjunctive therapy was Adjuvant (After the main therapy) or Neo-Adjuvant (Before the main therapy) or not applicable.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6540_TREAT3_ADJUNCTIVE_THERAPY'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr0680_treat3_cancer_treatment_intent: Optional[CancerTreatmentIntent] = Field(default=None, description="""The intention of the cancer treatment provided during a Cancer Care Spell.
* Disease Modification is Drug Specific ** Diagnostic and Staging are Surgery Specific""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0680_TREAT3_CANCER_TREATMENT_INTENT'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr1370_treat3_treatment_start_date_cancer: Optional[date] = Field(default=None, description="""This is the Start Date of the first, second or subsequent cancer treatment given to a PATIENT who is receiving care for a cancer condition.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR1370_TREAT3_TREATMENT_START_DATE_CANCER'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr2040_treat3_cancer_treatment_modality_registration: Optional[CancerTreatmentModalityRegistration] = Field(default=None, description="""The type of treatment or care which was delivered in a Cancer Treatment Period.
This is subset of Cancer Treatment Modality, which supports Cancer Registration in England""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR2040_TREAT3_CANCER_TREATMENT_MODALITY_REGISTRATION'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr1450_treat3_org_site_id_of_provider_cancer_treatment_start_date: Optional[str] = Field(default=None, description="""The ORGANISATION IDENTIFIER of the Organisation Site where the TREATMENT START DATE FOR CANCER is recorded.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR1450_TREAT3_ORG_SITE_ID_OF_PROVIDER_CANCER_TREATMENT_START_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(9)'}},
         'domain_of': ['COSDResearchView']} })
    cr8400_treat3_con_treat_prof_regissuer_code: Optional[ProfessionalRegistrationIssuerCodeConsultantTreatment] = Field(default=None, description="""A code which identifies the PROFESSIONAL REGISTRATION BODY for the Consultant or health care professional responsible for the treatment of the patient.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8400_TREAT3_CON_TREAT_PROF_REGISSUER_CODE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr8410_treat3_con_treat_prof_regentry_identifier: Optional[str] = Field(default=None, description="""The registration identifier allocated by a Professional Registration Body for the Consultant or health care professional responsible for the treatment of the patient.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8410_TREAT3_CON_TREAT_PROF_REGENTRY_IDENTIFIER'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(32)'}},
         'domain_of': ['COSDResearchView']} })
    cr8420_treat3_end_of_treatment_summary_date: Optional[date] = Field(default=None, description="""Record the date of completion of 'End of Treatment Summary' at the end of acute (secondary care) treatment(s) which was sent to the patient and/or the GP""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8420_TREAT3_END_OF_TREATMENT_SUMMARY_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr0740_treat3_discharge_date_hospital_provider_spell: Optional[date] = Field(default=None, description="""The date a PATIENT was discharged from a Hospital Provider Spell.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0740_TREAT3_DISCHARGE_DATE_HOSPITAL_PROVIDER_SPELL'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr9080_treat3_discharge_destination_hospital_provider_spell: Optional[DestinationOfDischargeHospitalProviderSpell] = Field(default=None, description="""This records the destination of a PATIENT on completion of the Hospital Provider Spell. It can also indicate that the PATIENT died.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR9080_TREAT3_DISCHARGE_DESTINATION_HOSPITAL_PROVIDER_SPELL'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr0710_treat3_procedure_date: Optional[date] = Field(default=None, description="""The date the procedure was carried out.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0710_TREAT3_PROCEDURE_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr8500_treat3_surgical_admission_type: Optional[SurgicalAdmissionType] = Field(default=None, description="""The type of Surgical Admission""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8500_TREAT3_SURGICAL_ADMISSION_TYPE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr8510_treat3_prof_reg_issuer_code_cons_surgeon1: Optional[ProfessionalRegistrationIssuerCodeConsultantSurgeon] = Field(default=None, description="""A code which identifies the PROFESSIONAL REGISTRATION BODY for the Consultant or health care professional who is responsible for the treatment of the patient. If he/she is part of a surgical team, add all consultant surgeons responsible for the procedure.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8510_TREAT3_PROF_REG_ISSUER_CODE_CONS_SURGEON1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr8520_treat3_prof_reg_entry_identifier_cons_surgeon1: Optional[str] = Field(default=None, description="""The registration identifier allocated by a Professional Registration Body for the Consultant surgeon responsible for the treatment of the patient. If he/she is part of a surgical team, add all consultant surgeons responsible for the procedure.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8520_TREAT3_PROF_REG_ENTRY_IDENTIFIER_CONS_SURGEON1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(32)'}},
         'domain_of': ['COSDResearchView']} })
    cr8510_treat3_prof_reg_issuer_code_cons_surgeon2: Optional[ProfessionalRegistrationIssuerCodeConsultantSurgeon] = Field(default=None, description="""A code which identifies the PROFESSIONAL REGISTRATION BODY for the Consultant or health care professional who is responsible for the treatment of the patient. If he/she is part of a surgical team, add all consultant surgeons responsible for the procedure.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8510_TREAT3_PROF_REG_ISSUER_CODE_CONS_SURGEON2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr8520_treat3_prof_reg_entry_identifier_cons_surgeon2: Optional[str] = Field(default=None, description="""The registration identifier allocated by a Professional Registration Body for the Consultant surgeon responsible for the treatment of the patient. If he/she is part of a surgical team, add all consultant surgeons responsible for the procedure.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8520_TREAT3_PROF_REG_ENTRY_IDENTIFIER_CONS_SURGEON2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(32)'}},
         'domain_of': ['COSDResearchView']} })
    cr8510_treat3_prof_reg_issuer_code_cons_surgeon3: Optional[ProfessionalRegistrationIssuerCodeConsultantSurgeon] = Field(default=None, description="""A code which identifies the PROFESSIONAL REGISTRATION BODY for the Consultant or health care professional who is responsible for the treatment of the patient. If he/she is part of a surgical team, add all consultant surgeons responsible for the procedure.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8510_TREAT3_PROF_REG_ISSUER_CODE_CONS_SURGEON3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr8520_treat3_prof_reg_entry_identifier_cons_surgeon3: Optional[str] = Field(default=None, description="""The registration identifier allocated by a Professional Registration Body for the Consultant surgeon responsible for the treatment of the patient. If he/she is part of a surgical team, add all consultant surgeons responsible for the procedure.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8520_TREAT3_PROF_REG_ENTRY_IDENTIFIER_CONS_SURGEON3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(32)'}},
         'domain_of': ['COSDResearchView']} })
    cr0720_treat3_primary_procedure_opcs: Optional[str] = Field(default=None, description="""PRIMARY PROCEDURE (OPCS) is the OPCS Classification of Interventions and Procedures code which is used to identify the primary Patient Procedure carried out.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0720_TREAT3_PRIMARY_PROCEDURE_OPCS'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr3040_treat3_primary_procedure_snomed_ct: Optional[str] = Field(default=None, description="""Primary procedure is the main procedure carried out using SNOMED CT. This maybe recorded in addition to PRIMARY PROCEDURE (OPCS).""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3040_TREAT3_PRIMARY_PROCEDURE_SNOMED_CT'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr0730_treat3_procedure_opcs2: Optional[str] = Field(default=None, description="""This is a procedure other than the PRIMARY PROCEDURE (OPCS), carried out and recorded for CDS or Hospital Episode Statistics purposes. (This may occur more than once).""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0730_TREAT3_PROCEDURE_OPCS2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr0730_treat3_procedure_opcs3: Optional[str] = Field(default=None, description="""This is a procedure other than the PRIMARY PROCEDURE (OPCS), carried out and recorded for CDS or Hospital Episode Statistics purposes. (This may occur more than once).""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0730_TREAT3_PROCEDURE_OPCS3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr0730_treat3_procedure_opcs4: Optional[str] = Field(default=None, description="""This is a procedure other than the PRIMARY PROCEDURE (OPCS), carried out and recorded for CDS or Hospital Episode Statistics purposes. (This may occur more than once).""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0730_TREAT3_PROCEDURE_OPCS4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr3050_treat3_procedure_snomed_ct2: Optional[str] = Field(default=None, description="""This is a procedure other than the PRIMARY PROCEDURE, carried out and recorded for CDS or Hospital Episode Statistics purposes. (This may occur more than once).This maybe recorded in addition to PROCEDURE (OPCS).""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3050_TREAT3_PROCEDURE_SNOMED_CT2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr3050_treat3_procedure_snomed_ct3: Optional[str] = Field(default=None, description="""This is a procedure other than the PRIMARY PROCEDURE, carried out and recorded for CDS or Hospital Episode Statistics purposes. (This may occur more than once).This maybe recorded in addition to PROCEDURE (OPCS).""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3050_TREAT3_PROCEDURE_SNOMED_CT3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr3050_treat3_procedure_snomed_ct4: Optional[str] = Field(default=None, description="""This is a procedure other than the PRIMARY PROCEDURE, carried out and recorded for CDS or Hospital Episode Statistics purposes. (This may occur more than once).This maybe recorded in addition to PROCEDURE (OPCS).""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3050_TREAT3_PROCEDURE_SNOMED_CT4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr6480_treat3_unplanned_return_to_theatre_indicator: Optional[UnplannedReturnToTheatreIndicator] = Field(default=None, description="""Whether or not the patient required a second (unplanned) operation during the same admission as the primary procedure""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6480_TREAT3_UNPLANNED_RETURN_TO_THEATRE_INDICATOR'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr6010_treat3_asa_score: Optional[AsaScore] = Field(default=None, description="""The ASA physical status classification system is a system for assessing the fitness of patients before surgery.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6010_TREAT3_ASA_SCORE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr6310_treat3_surgery_surgical_access_type: Optional[SurgicalAccessType] = Field(default=None, description="""The surgical access type used to perform the main procedure.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6310_TREAT3_SURGERY_SURGICAL_ACCESS_TYPE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr6540_treat4_adjunctive_therapy: Optional[AdjunctiveTherapy] = Field(default=None, description="""Adjunctive therapy is therapy given in addition to the main therapy to maximize its effectiveness.
This field allows for the accurate recording of these to determine if Adjunctive therapy was Adjuvant (After the main therapy) or Neo-Adjuvant (Before the main therapy) or not applicable.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6540_TREAT4_ADJUNCTIVE_THERAPY'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr0680_treat4_cancer_treatment_intent: Optional[CancerTreatmentIntent] = Field(default=None, description="""The intention of the cancer treatment provided during a Cancer Care Spell.
* Disease Modification is Drug Specific ** Diagnostic and Staging are Surgery Specific""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0680_TREAT4_CANCER_TREATMENT_INTENT'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr1370_treat4_treatment_start_date_cancer: Optional[date] = Field(default=None, description="""This is the Start Date of the first, second or subsequent cancer treatment given to a PATIENT who is receiving care for a cancer condition.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR1370_TREAT4_TREATMENT_START_DATE_CANCER'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr2040_treat4_cancer_treatment_modality_registration: Optional[CancerTreatmentModalityRegistration] = Field(default=None, description="""The type of treatment or care which was delivered in a Cancer Treatment Period.
This is subset of Cancer Treatment Modality, which supports Cancer Registration in England""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR2040_TREAT4_CANCER_TREATMENT_MODALITY_REGISTRATION'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr1450_treat4_org_site_id_of_provider_cancer_treatment_start_date: Optional[str] = Field(default=None, description="""The ORGANISATION IDENTIFIER of the Organisation Site where the TREATMENT START DATE FOR CANCER is recorded.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR1450_TREAT4_ORG_SITE_ID_OF_PROVIDER_CANCER_TREATMENT_START_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(9)'}},
         'domain_of': ['COSDResearchView']} })
    cr8400_treat4_con_treat_prof_regissuer_code: Optional[ProfessionalRegistrationIssuerCodeConsultantTreatment] = Field(default=None, description="""A code which identifies the PROFESSIONAL REGISTRATION BODY for the Consultant or health care professional responsible for the treatment of the patient.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8400_TREAT4_CON_TREAT_PROF_REGISSUER_CODE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr8410_treat4_con_treat_prof_regentry_identifier: Optional[str] = Field(default=None, description="""The registration identifier allocated by a Professional Registration Body for the Consultant or health care professional responsible for the treatment of the patient.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8410_TREAT4_CON_TREAT_PROF_REGENTRY_IDENTIFIER'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(32)'}},
         'domain_of': ['COSDResearchView']} })
    cr8420_treat4_end_of_treatment_summary_date: Optional[date] = Field(default=None, description="""Record the date of completion of 'End of Treatment Summary' at the end of acute (secondary care) treatment(s) which was sent to the patient and/or the GP""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8420_TREAT4_END_OF_TREATMENT_SUMMARY_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr0740_treat4_discharge_date_hospital_provider_spell: Optional[date] = Field(default=None, description="""The date a PATIENT was discharged from a Hospital Provider Spell.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0740_TREAT4_DISCHARGE_DATE_HOSPITAL_PROVIDER_SPELL'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr9080_treat4_discharge_destination_hospital_provider_spell: Optional[DestinationOfDischargeHospitalProviderSpell] = Field(default=None, description="""This records the destination of a PATIENT on completion of the Hospital Provider Spell. It can also indicate that the PATIENT died.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR9080_TREAT4_DISCHARGE_DESTINATION_HOSPITAL_PROVIDER_SPELL'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr0710_treat4_procedure_date: Optional[date] = Field(default=None, description="""The date the procedure was carried out.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0710_TREAT4_PROCEDURE_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr8500_treat4_surgical_admission_type: Optional[SurgicalAdmissionType] = Field(default=None, description="""The type of Surgical Admission""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8500_TREAT4_SURGICAL_ADMISSION_TYPE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr8510_treat4_prof_reg_issuer_code_cons_surgeon1: Optional[ProfessionalRegistrationIssuerCodeConsultantSurgeon] = Field(default=None, description="""A code which identifies the PROFESSIONAL REGISTRATION BODY for the Consultant or health care professional who is responsible for the treatment of the patient. If he/she is part of a surgical team, add all consultant surgeons responsible for the procedure.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8510_TREAT4_PROF_REG_ISSUER_CODE_CONS_SURGEON1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr8520_treat4_prof_reg_entry_identifier_cons_surgeon1: Optional[str] = Field(default=None, description="""The registration identifier allocated by a Professional Registration Body for the Consultant surgeon responsible for the treatment of the patient. If he/she is part of a surgical team, add all consultant surgeons responsible for the procedure.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8520_TREAT4_PROF_REG_ENTRY_IDENTIFIER_CONS_SURGEON1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(32)'}},
         'domain_of': ['COSDResearchView']} })
    cr8510_treat4_prof_reg_issuer_code_cons_surgeon2: Optional[ProfessionalRegistrationIssuerCodeConsultantSurgeon] = Field(default=None, description="""A code which identifies the PROFESSIONAL REGISTRATION BODY for the Consultant or health care professional who is responsible for the treatment of the patient. If he/she is part of a surgical team, add all consultant surgeons responsible for the procedure.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8510_TREAT4_PROF_REG_ISSUER_CODE_CONS_SURGEON2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr8520_treat4_prof_reg_entry_identifier_cons_surgeon2: Optional[str] = Field(default=None, description="""The registration identifier allocated by a Professional Registration Body for the Consultant surgeon responsible for the treatment of the patient. If he/she is part of a surgical team, add all consultant surgeons responsible for the procedure.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8520_TREAT4_PROF_REG_ENTRY_IDENTIFIER_CONS_SURGEON2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(32)'}},
         'domain_of': ['COSDResearchView']} })
    cr8510_treat4_prof_reg_issuer_code_cons_surgeon3: Optional[ProfessionalRegistrationIssuerCodeConsultantSurgeon] = Field(default=None, description="""A code which identifies the PROFESSIONAL REGISTRATION BODY for the Consultant or health care professional who is responsible for the treatment of the patient. If he/she is part of a surgical team, add all consultant surgeons responsible for the procedure.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8510_TREAT4_PROF_REG_ISSUER_CODE_CONS_SURGEON3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr8520_treat4_prof_reg_entry_identifier_cons_surgeon3: Optional[str] = Field(default=None, description="""The registration identifier allocated by a Professional Registration Body for the Consultant surgeon responsible for the treatment of the patient. If he/she is part of a surgical team, add all consultant surgeons responsible for the procedure.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8520_TREAT4_PROF_REG_ENTRY_IDENTIFIER_CONS_SURGEON3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(32)'}},
         'domain_of': ['COSDResearchView']} })
    cr0720_treat4_primary_procedure_opcs: Optional[str] = Field(default=None, description="""PRIMARY PROCEDURE (OPCS) is the OPCS Classification of Interventions and Procedures code which is used to identify the primary Patient Procedure carried out.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0720_TREAT4_PRIMARY_PROCEDURE_OPCS'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr3040_treat4_primary_procedure_snomed_ct: Optional[str] = Field(default=None, description="""Primary procedure is the main procedure carried out using SNOMED CT. This maybe recorded in addition to PRIMARY PROCEDURE (OPCS).""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3040_TREAT4_PRIMARY_PROCEDURE_SNOMED_CT'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr0730_treat4_procedure_opcs2: Optional[str] = Field(default=None, description="""This is a procedure other than the PRIMARY PROCEDURE (OPCS), carried out and recorded for CDS or Hospital Episode Statistics purposes. (This may occur more than once).""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0730_TREAT4_PROCEDURE_OPCS2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr0730_treat4_procedure_opcs3: Optional[str] = Field(default=None, description="""This is a procedure other than the PRIMARY PROCEDURE (OPCS), carried out and recorded for CDS or Hospital Episode Statistics purposes. (This may occur more than once).""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0730_TREAT4_PROCEDURE_OPCS3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr0730_treat4_procedure_opcs4: Optional[str] = Field(default=None, description="""This is a procedure other than the PRIMARY PROCEDURE (OPCS), carried out and recorded for CDS or Hospital Episode Statistics purposes. (This may occur more than once).""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0730_TREAT4_PROCEDURE_OPCS4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr3050_treat4_procedure_snomed_ct2: Optional[str] = Field(default=None, description="""This is a procedure other than the PRIMARY PROCEDURE, carried out and recorded for CDS or Hospital Episode Statistics purposes. (This may occur more than once).This maybe recorded in addition to PROCEDURE (OPCS).""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3050_TREAT4_PROCEDURE_SNOMED_CT2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr3050_treat4_procedure_snomed_ct3: Optional[str] = Field(default=None, description="""This is a procedure other than the PRIMARY PROCEDURE, carried out and recorded for CDS or Hospital Episode Statistics purposes. (This may occur more than once).This maybe recorded in addition to PROCEDURE (OPCS).""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3050_TREAT4_PROCEDURE_SNOMED_CT3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr3050_treat4_procedure_snomed_ct4: Optional[str] = Field(default=None, description="""This is a procedure other than the PRIMARY PROCEDURE, carried out and recorded for CDS or Hospital Episode Statistics purposes. (This may occur more than once).This maybe recorded in addition to PROCEDURE (OPCS).""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3050_TREAT4_PROCEDURE_SNOMED_CT4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr6480_treat4_unplanned_return_to_theatre_indicator: Optional[UnplannedReturnToTheatreIndicator] = Field(default=None, description="""Whether or not the patient required a second (unplanned) operation during the same admission as the primary procedure""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6480_TREAT4_UNPLANNED_RETURN_TO_THEATRE_INDICATOR'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr6010_treat4_asa_score: Optional[AsaScore] = Field(default=None, description="""The ASA physical status classification system is a system for assessing the fitness of patients before surgery.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6010_TREAT4_ASA_SCORE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr6310_treat4_surgery_surgical_access_type: Optional[SurgicalAccessType] = Field(default=None, description="""The surgical access type used to perform the main procedure.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6310_TREAT4_SURGERY_SURGICAL_ACCESS_TYPE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr8700_ac1_acute_oncology_assessment_date: Optional[date] = Field(default=None, description="""The date on which an Acute Oncology assessment was concluded""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8700_AC1_ACUTE_ONCOLOGY_ASSESSMENT_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr8710_ac1_organisation_site_identifier_acute_oncology: Optional[str] = Field(default=None, description="""The ORGANISATION SITE IDENTIFIER of the Organisation site acting as a Health Care Provider for the Acute Oncology assessment""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8710_AC1_ORGANISATION_SITE_IDENTIFIER_ACUTE_ONCOLOGY'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(5)'}},
         'domain_of': ['COSDResearchView']} })
    cr8720_ac1_assessment_location: Optional[AssessmentLocation] = Field(default=None, description="""The location where the Acute Oncology (AO) assessment was performed within the health care provider""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8720_AC1_ASSESSMENT_LOCATION'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr8730_ac1_patient_type1: Optional[PatientType] = Field(default=None, description="""Record the type each patient presentation is grouped within, as a result of the acute oncology assessment.
A table is available within the user guide to provide additional information.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8730_AC1_PATIENT_TYPE1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr8730_ac1_patient_type2: Optional[PatientType] = Field(default=None, description="""Record the type each patient presentation is grouped within, as a result of the acute oncology assessment.
A table is available within the user guide to provide additional information.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8730_AC1_PATIENT_TYPE2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr8740_ac1_outcome: Optional[Outcome] = Field(default=None, description="""Record the outcome of the acute oncology episode""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8740_AC1_OUTCOME'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr8700_ac2_acute_oncology_assessment_date: Optional[date] = Field(default=None, description="""The date on which an Acute Oncology assessment was concluded""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8700_AC2_ACUTE_ONCOLOGY_ASSESSMENT_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr8710_ac2_organisation_site_identifier_acute_oncology: Optional[str] = Field(default=None, description="""The ORGANISATION SITE IDENTIFIER of the Organisation site acting as a Health Care Provider for the Acute Oncology assessment""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8710_AC2_ORGANISATION_SITE_IDENTIFIER_ACUTE_ONCOLOGY'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(5)'}},
         'domain_of': ['COSDResearchView']} })
    cr8720_ac2_assessment_location: Optional[AssessmentLocation] = Field(default=None, description="""The location where the Acute Oncology (AO) assessment was performed within the health care provider""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8720_AC2_ASSESSMENT_LOCATION'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr8730_ac2_patient_type1: Optional[PatientType] = Field(default=None, description="""Record the type each patient presentation is grouped within, as a result of the acute oncology assessment.
A table is available within the user guide to provide additional information.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8730_AC2_PATIENT_TYPE1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr8730_ac2_patient_type2: Optional[PatientType] = Field(default=None, description="""Record the type each patient presentation is grouped within, as a result of the acute oncology assessment.
A table is available within the user guide to provide additional information.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8730_AC2_PATIENT_TYPE2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr8740_ac2_outcome: Optional[Outcome] = Field(default=None, description="""Record the outcome of the acute oncology episode""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8740_AC2_OUTCOME'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr8700_ac3_acute_oncology_assessment_date: Optional[date] = Field(default=None, description="""The date on which an Acute Oncology assessment was concluded""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8700_AC3_ACUTE_ONCOLOGY_ASSESSMENT_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr8710_ac3_organisation_site_identifier_acute_oncology: Optional[str] = Field(default=None, description="""The ORGANISATION SITE IDENTIFIER of the Organisation site acting as a Health Care Provider for the Acute Oncology assessment""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8710_AC3_ORGANISATION_SITE_IDENTIFIER_ACUTE_ONCOLOGY'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(5)'}},
         'domain_of': ['COSDResearchView']} })
    cr8720_ac3_assessment_location: Optional[AssessmentLocation] = Field(default=None, description="""The location where the Acute Oncology (AO) assessment was performed within the health care provider""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8720_AC3_ASSESSMENT_LOCATION'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr8730_ac3_patient_type1: Optional[PatientType] = Field(default=None, description="""Record the type each patient presentation is grouped within, as a result of the acute oncology assessment.
A table is available within the user guide to provide additional information.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8730_AC3_PATIENT_TYPE1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr8730_ac3_patient_type2: Optional[PatientType] = Field(default=None, description="""Record the type each patient presentation is grouped within, as a result of the acute oncology assessment.
A table is available within the user guide to provide additional information.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8730_AC3_PATIENT_TYPE2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr8740_ac3_outcome: Optional[Outcome] = Field(default=None, description="""Record the outcome of the acute oncology episode""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8740_AC3_OUTCOME'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr8800_laboratory_result_date1: Optional[date] = Field(default=None, description="""The date on which an investigation was concluded e.g. the date the result was authorised.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8800_LABORATORY_RESULT_DATE1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr8810_organisation_identifier_laboratory_result1: Optional[str] = Field(default=None, description="""The ORGANISATION IDENTIFIER of the Organisation site acting as a Health Care Provider, which processed the sample.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8810_ORGANISATION_IDENTIFIER_LABORATORY_RESULT1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(5)'}},
         'domain_of': ['COSDResearchView']} })
    cr8900_ldh_value1: Optional[str] = Field(default=None, description="""This is the peak LDH (Lactate Dehydrogenase Level) at diagnosis""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8900_LDH_VALUE1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(6)'}},
         'domain_of': ['COSDResearchView']} })
    cr8910_beta_human_chorionic_gonadotropin_serum1: Optional[str] = Field(default=None, description="""Maximum Serum level of HCG at diagnosis in IU/l (measured only for CNS germ cell tumours.)""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8910_BETA_HUMAN_CHORIONIC_GONADOTROPIN_SERUM1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(8)'}},
         'domain_of': ['COSDResearchView']} })
    cr8920_alpha_fetoprotein_serum1: Optional[str] = Field(default=None, description="""Maximum Serum level of alpha feto protein at diagnosis. AFP units recorded in kU/l (values > 100,000 are recorded)""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8920_ALPHA_FETOPROTEIN_SERUM1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(8)'}},
         'domain_of': ['COSDResearchView']} })
    cr8800_laboratory_result_date2: Optional[date] = Field(default=None, description="""The date on which an investigation was concluded e.g. the date the result was authorised.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8800_LABORATORY_RESULT_DATE2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr8810_organisation_identifier_laboratory_result2: Optional[str] = Field(default=None, description="""The ORGANISATION IDENTIFIER of the Organisation site acting as a Health Care Provider, which processed the sample.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8810_ORGANISATION_IDENTIFIER_LABORATORY_RESULT2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(5)'}},
         'domain_of': ['COSDResearchView']} })
    cr8900_ldh_value2: Optional[str] = Field(default=None, description="""This is the peak LDH (Lactate Dehydrogenase Level) at diagnosis""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8900_LDH_VALUE2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(6)'}},
         'domain_of': ['COSDResearchView']} })
    cr8910_beta_human_chorionic_gonadotropin_serum2: Optional[str] = Field(default=None, description="""Maximum Serum level of HCG at diagnosis in IU/l (measured only for CNS germ cell tumours.)""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8910_BETA_HUMAN_CHORIONIC_GONADOTROPIN_SERUM2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(8)'}},
         'domain_of': ['COSDResearchView']} })
    cr8920_alpha_fetoprotein_serum2: Optional[str] = Field(default=None, description="""Maximum Serum level of alpha feto protein at diagnosis. AFP units recorded in kU/l (values > 100,000 are recorded)""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8920_ALPHA_FETOPROTEIN_SERUM2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(8)'}},
         'domain_of': ['COSDResearchView']} })
    cr8800_laboratory_result_date3: Optional[date] = Field(default=None, description="""The date on which an investigation was concluded e.g. the date the result was authorised.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8800_LABORATORY_RESULT_DATE3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr8810_organisation_identifier_laboratory_result3: Optional[str] = Field(default=None, description="""The ORGANISATION IDENTIFIER of the Organisation site acting as a Health Care Provider, which processed the sample.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8810_ORGANISATION_IDENTIFIER_LABORATORY_RESULT3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(5)'}},
         'domain_of': ['COSDResearchView']} })
    cr8900_ldh_value3: Optional[str] = Field(default=None, description="""This is the peak LDH (Lactate Dehydrogenase Level) at diagnosis""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8900_LDH_VALUE3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(6)'}},
         'domain_of': ['COSDResearchView']} })
    cr8910_beta_human_chorionic_gonadotropin_serum3: Optional[str] = Field(default=None, description="""Maximum Serum level of HCG at diagnosis in IU/l (measured only for CNS germ cell tumours.)""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8910_BETA_HUMAN_CHORIONIC_GONADOTROPIN_SERUM3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(8)'}},
         'domain_of': ['COSDResearchView']} })
    cr8920_alpha_fetoprotein_serum3: Optional[str] = Field(default=None, description="""Maximum Serum level of alpha feto protein at diagnosis. AFP units recorded in kU/l (values > 100,000 are recorded)""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8920_ALPHA_FETOPROTEIN_SERUM3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(8)'}},
         'domain_of': ['COSDResearchView']} })
    cr0310_org_site_id_of_imaging1: Optional[str] = Field(default=None, description="""This is the ORGANISATION IDENTIFIER of the Organisation site where the imaging took place.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0310_ORG_SITE_ID_OF_IMAGING1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(9)'}},
         'domain_of': ['COSDResearchView']} })
    cr0320_procedure_date_cancer_imaging1: Optional[str] = Field(default=None, description="""The DATE the Cancer Imaging was carried out.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0320_PROCEDURE_DATE_CANCER_IMAGING1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(10)'}},
         'domain_of': ['COSDResearchView']} })
    cr6780_imaging_outcome1: Optional[ImagingOutcome] = Field(default=None, description="""Record the outcome for the imaging event as agreed with the radiologist or clinical team""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6780_IMAGING_OUTCOME1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr1610_imaging_code_nicip1: Optional[str] = Field(default=None, description="""IMAGING CODE (NICIP) is the National Interim Clinical Imaging Procedure Code Set code which is used to identify both the test modality and body site of the test.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR1610_IMAGING_CODE_NICIP1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(6)'}},
         'domain_of': ['COSDResearchView']} })
    cr3110_imaging_code_snowmed_ct1: Optional[str] = Field(default=None, description="""IMAGING CODE (SNOMED-CT) is the SNOMED CT concept ID which is used to identify both the test modality and body site of the test.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3110_IMAGING_CODE_SNOWMED_CT1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(19)'}},
         'domain_of': ['COSDResearchView']} })
    cr0330_cancer_imaging_modality1: Optional[CancerImagingModality] = Field(default=None, description="""The type of imaging procedure used during an Imaging or Radiodiagnostic Event for a Cancer Care Spell. NB: PET Scan also includes PET-CT Scan.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0330_CANCER_IMAGING_MODALITY1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr0340_imaging_anatomical_site1: Optional[str] = Field(default=None, description="""A classification of the part of the body that is the subject of an Imaging Or Radiodiagnostic Event.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0340_IMAGING_ANATOMICAL_SITE1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(5)'}},
         'domain_of': ['COSDResearchView']} })
    cr3000_anatomical_side_imaging1: Optional[AnatomicalSideImaging] = Field(default=None, description="""The side of the body that is the subject of an Imaging or Radiodiagnostic Event.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3000_ANATOMICAL_SIDE_IMAGING1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr0160_imaging_report_text1: Optional[str] = Field(default=None, description="""This is the full text provided in the imaging report and may be required by registries to derive final stage and diagnosis date for registration.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0160_IMAGING_REPORT_TEXT1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(MAX)'}},
         'domain_of': ['COSDResearchView']} })
    cr0310_org_site_id_of_imaging2: Optional[str] = Field(default=None, description="""This is the ORGANISATION IDENTIFIER of the Organisation site where the imaging took place.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0310_ORG_SITE_ID_OF_IMAGING2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(9)'}},
         'domain_of': ['COSDResearchView']} })
    cr0320_procedure_date_cancer_imaging2: Optional[str] = Field(default=None, description="""The DATE the Cancer Imaging was carried out.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0320_PROCEDURE_DATE_CANCER_IMAGING2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(10)'}},
         'domain_of': ['COSDResearchView']} })
    cr6780_imaging_outcome2: Optional[ImagingOutcome] = Field(default=None, description="""Record the outcome for the imaging event as agreed with the radiologist or clinical team""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6780_IMAGING_OUTCOME2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr1610_imaging_code_nicip2: Optional[str] = Field(default=None, description="""IMAGING CODE (NICIP) is the National Interim Clinical Imaging Procedure Code Set code which is used to identify both the test modality and body site of the test.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR1610_IMAGING_CODE_NICIP2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(6)'}},
         'domain_of': ['COSDResearchView']} })
    cr3110_imaging_code_snowmed_ct2: Optional[str] = Field(default=None, description="""IMAGING CODE (SNOMED-CT) is the SNOMED CT concept ID which is used to identify both the test modality and body site of the test.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3110_IMAGING_CODE_SNOWMED_CT2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(19)'}},
         'domain_of': ['COSDResearchView']} })
    cr0330_cancer_imaging_modality2: Optional[CancerImagingModality] = Field(default=None, description="""The type of imaging procedure used during an Imaging or Radiodiagnostic Event for a Cancer Care Spell. NB: PET Scan also includes PET-CT Scan.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0330_CANCER_IMAGING_MODALITY2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr0340_imaging_anatomical_site2: Optional[str] = Field(default=None, description="""A classification of the part of the body that is the subject of an Imaging Or Radiodiagnostic Event.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0340_IMAGING_ANATOMICAL_SITE2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(5)'}},
         'domain_of': ['COSDResearchView']} })
    cr3000_anatomical_side_imaging2: Optional[AnatomicalSideImaging] = Field(default=None, description="""The side of the body that is the subject of an Imaging or Radiodiagnostic Event.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3000_ANATOMICAL_SIDE_IMAGING2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr0160_imaging_report_text2: Optional[str] = Field(default=None, description="""This is the full text provided in the imaging report and may be required by registries to derive final stage and diagnosis date for registration.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0160_IMAGING_REPORT_TEXT2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(MAX)'}},
         'domain_of': ['COSDResearchView']} })
    cr0310_org_site_id_of_imaging3: Optional[str] = Field(default=None, description="""This is the ORGANISATION IDENTIFIER of the Organisation site where the imaging took place.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0310_ORG_SITE_ID_OF_IMAGING3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(9)'}},
         'domain_of': ['COSDResearchView']} })
    cr0320_procedure_date_cancer_imaging3: Optional[str] = Field(default=None, description="""The DATE the Cancer Imaging was carried out.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0320_PROCEDURE_DATE_CANCER_IMAGING3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(10)'}},
         'domain_of': ['COSDResearchView']} })
    cr6780_imaging_outcome3: Optional[ImagingOutcome] = Field(default=None, description="""Record the outcome for the imaging event as agreed with the radiologist or clinical team""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6780_IMAGING_OUTCOME3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr1610_imaging_code_nicip3: Optional[str] = Field(default=None, description="""IMAGING CODE (NICIP) is the National Interim Clinical Imaging Procedure Code Set code which is used to identify both the test modality and body site of the test.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR1610_IMAGING_CODE_NICIP3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(6)'}},
         'domain_of': ['COSDResearchView']} })
    cr3110_imaging_code_snowmed_ct3: Optional[str] = Field(default=None, description="""IMAGING CODE (SNOMED-CT) is the SNOMED CT concept ID which is used to identify both the test modality and body site of the test.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3110_IMAGING_CODE_SNOWMED_CT3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(19)'}},
         'domain_of': ['COSDResearchView']} })
    cr0330_cancer_imaging_modality3: Optional[CancerImagingModality] = Field(default=None, description="""The type of imaging procedure used during an Imaging or Radiodiagnostic Event for a Cancer Care Spell. NB: PET Scan also includes PET-CT Scan.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0330_CANCER_IMAGING_MODALITY3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr0340_imaging_anatomical_site3: Optional[str] = Field(default=None, description="""A classification of the part of the body that is the subject of an Imaging Or Radiodiagnostic Event.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0340_IMAGING_ANATOMICAL_SITE3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(5)'}},
         'domain_of': ['COSDResearchView']} })
    cr3000_anatomical_side_imaging3: Optional[AnatomicalSideImaging] = Field(default=None, description="""The side of the body that is the subject of an Imaging or Radiodiagnostic Event.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3000_ANATOMICAL_SIDE_IMAGING3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr0160_imaging_report_text3: Optional[str] = Field(default=None, description="""This is the full text provided in the imaging report and may be required by registries to derive final stage and diagnosis date for registration.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0160_IMAGING_REPORT_TEXT3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(MAX)'}},
         'domain_of': ['COSDResearchView']} })
    cr0310_org_site_id_of_imaging4: Optional[str] = Field(default=None, description="""This is the ORGANISATION IDENTIFIER of the Organisation site where the imaging took place.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0310_ORG_SITE_ID_OF_IMAGING4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(9)'}},
         'domain_of': ['COSDResearchView']} })
    cr0320_procedure_date_cancer_imaging4: Optional[str] = Field(default=None, description="""The DATE the Cancer Imaging was carried out.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0320_PROCEDURE_DATE_CANCER_IMAGING4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(10)'}},
         'domain_of': ['COSDResearchView']} })
    cr6780_imaging_outcome4: Optional[ImagingOutcome] = Field(default=None, description="""Record the outcome for the imaging event as agreed with the radiologist or clinical team""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6780_IMAGING_OUTCOME4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr1610_imaging_code_nicip4: Optional[str] = Field(default=None, description="""IMAGING CODE (NICIP) is the National Interim Clinical Imaging Procedure Code Set code which is used to identify both the test modality and body site of the test.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR1610_IMAGING_CODE_NICIP4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(6)'}},
         'domain_of': ['COSDResearchView']} })
    cr3110_imaging_code_snowmed_ct4: Optional[str] = Field(default=None, description="""IMAGING CODE (SNOMED-CT) is the SNOMED CT concept ID which is used to identify both the test modality and body site of the test.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3110_IMAGING_CODE_SNOWMED_CT4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(19)'}},
         'domain_of': ['COSDResearchView']} })
    cr0330_cancer_imaging_modality4: Optional[CancerImagingModality] = Field(default=None, description="""The type of imaging procedure used during an Imaging or Radiodiagnostic Event for a Cancer Care Spell. NB: PET Scan also includes PET-CT Scan.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0330_CANCER_IMAGING_MODALITY4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr0340_imaging_anatomical_site4: Optional[str] = Field(default=None, description="""A classification of the part of the body that is the subject of an Imaging Or Radiodiagnostic Event.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0340_IMAGING_ANATOMICAL_SITE4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(5)'}},
         'domain_of': ['COSDResearchView']} })
    cr3000_anatomical_side_imaging4: Optional[AnatomicalSideImaging] = Field(default=None, description="""The side of the body that is the subject of an Imaging or Radiodiagnostic Event.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3000_ANATOMICAL_SIDE_IMAGING4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr0160_imaging_report_text4: Optional[str] = Field(default=None, description="""This is the full text provided in the imaging report and may be required by registries to derive final stage and diagnosis date for registration.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0160_IMAGING_REPORT_TEXT4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(MAX)'}},
         'domain_of': ['COSDResearchView']} })
    cr0310_org_site_id_of_imaging5: Optional[str] = Field(default=None, description="""This is the ORGANISATION IDENTIFIER of the Organisation site where the imaging took place.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0310_ORG_SITE_ID_OF_IMAGING5'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(9)'}},
         'domain_of': ['COSDResearchView']} })
    cr0320_procedure_date_cancer_imaging5: Optional[str] = Field(default=None, description="""The DATE the Cancer Imaging was carried out.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0320_PROCEDURE_DATE_CANCER_IMAGING5'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(10)'}},
         'domain_of': ['COSDResearchView']} })
    cr6780_imaging_outcome5: Optional[ImagingOutcome] = Field(default=None, description="""Record the outcome for the imaging event as agreed with the radiologist or clinical team""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6780_IMAGING_OUTCOME5'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr1610_imaging_code_nicip5: Optional[str] = Field(default=None, description="""IMAGING CODE (NICIP) is the National Interim Clinical Imaging Procedure Code Set code which is used to identify both the test modality and body site of the test.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR1610_IMAGING_CODE_NICIP5'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(6)'}},
         'domain_of': ['COSDResearchView']} })
    cr3110_imaging_code_snowmed_ct5: Optional[str] = Field(default=None, description="""IMAGING CODE (SNOMED-CT) is the SNOMED CT concept ID which is used to identify both the test modality and body site of the test.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3110_IMAGING_CODE_SNOWMED_CT5'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(19)'}},
         'domain_of': ['COSDResearchView']} })
    cr0330_cancer_imaging_modality5: Optional[CancerImagingModality] = Field(default=None, description="""The type of imaging procedure used during an Imaging or Radiodiagnostic Event for a Cancer Care Spell. NB: PET Scan also includes PET-CT Scan.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0330_CANCER_IMAGING_MODALITY5'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr0340_imaging_anatomical_site5: Optional[str] = Field(default=None, description="""A classification of the part of the body that is the subject of an Imaging Or Radiodiagnostic Event.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0340_IMAGING_ANATOMICAL_SITE5'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(5)'}},
         'domain_of': ['COSDResearchView']} })
    cr3000_anatomical_side_imaging5: Optional[AnatomicalSideImaging] = Field(default=None, description="""The side of the body that is the subject of an Imaging or Radiodiagnostic Event.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3000_ANATOMICAL_SIDE_IMAGING5'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr0160_imaging_report_text5: Optional[str] = Field(default=None, description="""This is the full text provided in the imaging report and may be required by registries to derive final stage and diagnosis date for registration.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0160_IMAGING_REPORT_TEXT5'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(MAX)'}},
         'domain_of': ['COSDResearchView']} })
    cr0310_org_site_id_of_imaging6: Optional[str] = Field(default=None, description="""This is the ORGANISATION IDENTIFIER of the Organisation site where the imaging took place.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0310_ORG_SITE_ID_OF_IMAGING6'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(9)'}},
         'domain_of': ['COSDResearchView']} })
    cr0320_procedure_date_cancer_imaging6: Optional[str] = Field(default=None, description="""The DATE the Cancer Imaging was carried out.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0320_PROCEDURE_DATE_CANCER_IMAGING6'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(10)'}},
         'domain_of': ['COSDResearchView']} })
    cr6780_imaging_outcome6: Optional[ImagingOutcome] = Field(default=None, description="""Record the outcome for the imaging event as agreed with the radiologist or clinical team""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6780_IMAGING_OUTCOME6'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr1610_imaging_code_nicip6: Optional[str] = Field(default=None, description="""IMAGING CODE (NICIP) is the National Interim Clinical Imaging Procedure Code Set code which is used to identify both the test modality and body site of the test.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR1610_IMAGING_CODE_NICIP6'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(6)'}},
         'domain_of': ['COSDResearchView']} })
    cr3110_imaging_code_snowmed_ct6: Optional[str] = Field(default=None, description="""IMAGING CODE (SNOMED-CT) is the SNOMED CT concept ID which is used to identify both the test modality and body site of the test.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3110_IMAGING_CODE_SNOWMED_CT6'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(19)'}},
         'domain_of': ['COSDResearchView']} })
    cr0330_cancer_imaging_modality6: Optional[CancerImagingModality] = Field(default=None, description="""The type of imaging procedure used during an Imaging or Radiodiagnostic Event for a Cancer Care Spell. NB: PET Scan also includes PET-CT Scan.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0330_CANCER_IMAGING_MODALITY6'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr0340_imaging_anatomical_site6: Optional[str] = Field(default=None, description="""A classification of the part of the body that is the subject of an Imaging Or Radiodiagnostic Event.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0340_IMAGING_ANATOMICAL_SITE6'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(5)'}},
         'domain_of': ['COSDResearchView']} })
    cr3000_anatomical_side_imaging6: Optional[AnatomicalSideImaging] = Field(default=None, description="""The side of the body that is the subject of an Imaging or Radiodiagnostic Event.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3000_ANATOMICAL_SIDE_IMAGING6'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr0160_imaging_report_text6: Optional[str] = Field(default=None, description="""This is the full text provided in the imaging report and may be required by registries to derive final stage and diagnosis date for registration.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0160_IMAGING_REPORT_TEXT6'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(MAX)'}},
         'domain_of': ['COSDResearchView']} })
    cr0310_org_site_id_of_imaging7: Optional[str] = Field(default=None, description="""This is the ORGANISATION IDENTIFIER of the Organisation site where the imaging took place.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0310_ORG_SITE_ID_OF_IMAGING7'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(9)'}},
         'domain_of': ['COSDResearchView']} })
    cr0320_procedure_date_cancer_imaging7: Optional[str] = Field(default=None, description="""The DATE the Cancer Imaging was carried out.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0320_PROCEDURE_DATE_CANCER_IMAGING7'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(10)'}},
         'domain_of': ['COSDResearchView']} })
    cr6780_imaging_outcome7: Optional[ImagingOutcome] = Field(default=None, description="""Record the outcome for the imaging event as agreed with the radiologist or clinical team""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6780_IMAGING_OUTCOME7'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr1610_imaging_code_nicip7: Optional[str] = Field(default=None, description="""IMAGING CODE (NICIP) is the National Interim Clinical Imaging Procedure Code Set code which is used to identify both the test modality and body site of the test.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR1610_IMAGING_CODE_NICIP7'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(6)'}},
         'domain_of': ['COSDResearchView']} })
    cr3110_imaging_code_snowmed_ct7: Optional[str] = Field(default=None, description="""IMAGING CODE (SNOMED-CT) is the SNOMED CT concept ID which is used to identify both the test modality and body site of the test.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3110_IMAGING_CODE_SNOWMED_CT7'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(19)'}},
         'domain_of': ['COSDResearchView']} })
    cr0330_cancer_imaging_modality7: Optional[CancerImagingModality] = Field(default=None, description="""The type of imaging procedure used during an Imaging or Radiodiagnostic Event for a Cancer Care Spell. NB: PET Scan also includes PET-CT Scan.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0330_CANCER_IMAGING_MODALITY7'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr0340_imaging_anatomical_site7: Optional[str] = Field(default=None, description="""A classification of the part of the body that is the subject of an Imaging Or Radiodiagnostic Event.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0340_IMAGING_ANATOMICAL_SITE7'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(5)'}},
         'domain_of': ['COSDResearchView']} })
    cr3000_anatomical_side_imaging7: Optional[AnatomicalSideImaging] = Field(default=None, description="""The side of the body that is the subject of an Imaging or Radiodiagnostic Event.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3000_ANATOMICAL_SIDE_IMAGING7'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr0160_imaging_report_text7: Optional[str] = Field(default=None, description="""This is the full text provided in the imaging report and may be required by registries to derive final stage and diagnosis date for registration.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0160_IMAGING_REPORT_TEXT7'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(MAX)'}},
         'domain_of': ['COSDResearchView']} })
    cr0310_org_site_id_of_imaging8: Optional[str] = Field(default=None, description="""This is the ORGANISATION IDENTIFIER of the Organisation site where the imaging took place.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0310_ORG_SITE_ID_OF_IMAGING8'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(9)'}},
         'domain_of': ['COSDResearchView']} })
    cr0320_procedure_date_cancer_imaging8: Optional[str] = Field(default=None, description="""The DATE the Cancer Imaging was carried out.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0320_PROCEDURE_DATE_CANCER_IMAGING8'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(10)'}},
         'domain_of': ['COSDResearchView']} })
    cr6780_imaging_outcome8: Optional[ImagingOutcome] = Field(default=None, description="""Record the outcome for the imaging event as agreed with the radiologist or clinical team""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6780_IMAGING_OUTCOME8'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr1610_imaging_code_nicip8: Optional[str] = Field(default=None, description="""IMAGING CODE (NICIP) is the National Interim Clinical Imaging Procedure Code Set code which is used to identify both the test modality and body site of the test.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR1610_IMAGING_CODE_NICIP8'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(6)'}},
         'domain_of': ['COSDResearchView']} })
    cr3110_imaging_code_snowmed_ct8: Optional[str] = Field(default=None, description="""IMAGING CODE (SNOMED-CT) is the SNOMED CT concept ID which is used to identify both the test modality and body site of the test.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3110_IMAGING_CODE_SNOWMED_CT8'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(19)'}},
         'domain_of': ['COSDResearchView']} })
    cr0330_cancer_imaging_modality8: Optional[CancerImagingModality] = Field(default=None, description="""The type of imaging procedure used during an Imaging or Radiodiagnostic Event for a Cancer Care Spell. NB: PET Scan also includes PET-CT Scan.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0330_CANCER_IMAGING_MODALITY8'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr0340_imaging_anatomical_site8: Optional[str] = Field(default=None, description="""A classification of the part of the body that is the subject of an Imaging Or Radiodiagnostic Event.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0340_IMAGING_ANATOMICAL_SITE8'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(5)'}},
         'domain_of': ['COSDResearchView']} })
    cr3000_anatomical_side_imaging8: Optional[AnatomicalSideImaging] = Field(default=None, description="""The side of the body that is the subject of an Imaging or Radiodiagnostic Event.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3000_ANATOMICAL_SIDE_IMAGING8'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr0160_imaging_report_text8: Optional[str] = Field(default=None, description="""This is the full text provided in the imaging report and may be required by registries to derive final stage and diagnosis date for registration.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0160_IMAGING_REPORT_TEXT8'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(MAX)'}},
         'domain_of': ['COSDResearchView']} })
    cr0310_org_site_id_of_imaging9: Optional[str] = Field(default=None, description="""This is the ORGANISATION IDENTIFIER of the Organisation site where the imaging took place.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0310_ORG_SITE_ID_OF_IMAGING9'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(9)'}},
         'domain_of': ['COSDResearchView']} })
    cr0320_procedure_date_cancer_imaging9: Optional[str] = Field(default=None, description="""The DATE the Cancer Imaging was carried out.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0320_PROCEDURE_DATE_CANCER_IMAGING9'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(10)'}},
         'domain_of': ['COSDResearchView']} })
    cr6780_imaging_outcome9: Optional[ImagingOutcome] = Field(default=None, description="""Record the outcome for the imaging event as agreed with the radiologist or clinical team""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6780_IMAGING_OUTCOME9'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr1610_imaging_code_nicip9: Optional[str] = Field(default=None, description="""IMAGING CODE (NICIP) is the National Interim Clinical Imaging Procedure Code Set code which is used to identify both the test modality and body site of the test.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR1610_IMAGING_CODE_NICIP9'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(6)'}},
         'domain_of': ['COSDResearchView']} })
    cr3110_imaging_code_snowmed_ct9: Optional[str] = Field(default=None, description="""IMAGING CODE (SNOMED-CT) is the SNOMED CT concept ID which is used to identify both the test modality and body site of the test.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3110_IMAGING_CODE_SNOWMED_CT9'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(19)'}},
         'domain_of': ['COSDResearchView']} })
    cr0330_cancer_imaging_modality9: Optional[CancerImagingModality] = Field(default=None, description="""The type of imaging procedure used during an Imaging or Radiodiagnostic Event for a Cancer Care Spell. NB: PET Scan also includes PET-CT Scan.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0330_CANCER_IMAGING_MODALITY9'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr0340_imaging_anatomical_site9: Optional[str] = Field(default=None, description="""A classification of the part of the body that is the subject of an Imaging Or Radiodiagnostic Event.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0340_IMAGING_ANATOMICAL_SITE9'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(5)'}},
         'domain_of': ['COSDResearchView']} })
    cr3000_anatomical_side_imaging9: Optional[AnatomicalSideImaging] = Field(default=None, description="""The side of the body that is the subject of an Imaging or Radiodiagnostic Event.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3000_ANATOMICAL_SIDE_IMAGING9'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr0160_imaging_report_text9: Optional[str] = Field(default=None, description="""This is the full text provided in the imaging report and may be required by registries to derive final stage and diagnosis date for registration.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0160_IMAGING_REPORT_TEXT9'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(MAX)'}},
         'domain_of': ['COSDResearchView']} })
    cr0310_org_site_id_of_imaging10: Optional[str] = Field(default=None, description="""This is the ORGANISATION IDENTIFIER of the Organisation site where the imaging took place.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0310_ORG_SITE_ID_OF_IMAGING10'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(9)'}},
         'domain_of': ['COSDResearchView']} })
    cr0320_procedure_date_cancer_imaging10: Optional[str] = Field(default=None, description="""The DATE the Cancer Imaging was carried out.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0320_PROCEDURE_DATE_CANCER_IMAGING10'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(10)'}},
         'domain_of': ['COSDResearchView']} })
    cr6780_imaging_outcome10: Optional[ImagingOutcome] = Field(default=None, description="""Record the outcome for the imaging event as agreed with the radiologist or clinical team""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6780_IMAGING_OUTCOME10'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr1610_imaging_code_nicip10: Optional[str] = Field(default=None, description="""IMAGING CODE (NICIP) is the National Interim Clinical Imaging Procedure Code Set code which is used to identify both the test modality and body site of the test.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR1610_IMAGING_CODE_NICIP10'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(6)'}},
         'domain_of': ['COSDResearchView']} })
    cr3110_imaging_code_snowmed_ct10: Optional[str] = Field(default=None, description="""IMAGING CODE (SNOMED-CT) is the SNOMED CT concept ID which is used to identify both the test modality and body site of the test.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3110_IMAGING_CODE_SNOWMED_CT10'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(19)'}},
         'domain_of': ['COSDResearchView']} })
    cr0330_cancer_imaging_modality10: Optional[CancerImagingModality] = Field(default=None, description="""The type of imaging procedure used during an Imaging or Radiodiagnostic Event for a Cancer Care Spell. NB: PET Scan also includes PET-CT Scan.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0330_CANCER_IMAGING_MODALITY10'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr0340_imaging_anatomical_site10: Optional[str] = Field(default=None, description="""A classification of the part of the body that is the subject of an Imaging Or Radiodiagnostic Event.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0340_IMAGING_ANATOMICAL_SITE10'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(5)'}},
         'domain_of': ['COSDResearchView']} })
    cr3000_anatomical_side_imaging10: Optional[AnatomicalSideImaging] = Field(default=None, description="""The side of the body that is the subject of an Imaging or Radiodiagnostic Event.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3000_ANATOMICAL_SIDE_IMAGING10'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr0160_imaging_report_text10: Optional[str] = Field(default=None, description="""This is the full text provided in the imaging report and may be required by registries to derive final stage and diagnosis date for registration.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0160_IMAGING_REPORT_TEXT10'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(MAX)'}},
         'domain_of': ['COSDResearchView']} })
    cr8100_mdt_discussion1: Optional[MultidisciplinaryTeamMeetingDiscussion] = Field(default=None, description="""Record if the patient was not discussed within a MDT Meeting""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8100_MDT_DISCUSSION1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr8110_mdt_discussion_type1: Optional[MultidisciplinaryTeamMeetingDiscussionType] = Field(default=None, description="""Record if the patient was discussed within a Multidisciplinary Team Meeting (MDTM)""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8110_MDT_DISCUSSION_TYPE1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3080_mdt_date1: Optional[str] = Field(default=None, description="""Record the date of each Multidisciplinary Team meeting where the patient was discussed.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3080_MDT_DATE1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3090_mdt_organisation_site_id1: Optional[str] = Field(default=None, description="""The ORGANISATION IDENTIFIER of the Organisation Site where the Multidisciplinary Team Meeting took place. (For joint MDT meetings a new MDT section must be recorded for each meeting)""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3090_MDT_ORGANISATION_SITE_ID1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3190_mdt_type1: Optional[MultidisciplinaryTeamMeetingType] = Field(default=None, description="""Record the type of MDT meeting at which the patient was discussed. Please provide the most detailed level of information that is possible.
Note: the codes at the high level (shown in bold) are Tumour groups and the items below each high-level code are Multidisciplinary Teams. ORGANISATIONS should only use the high-level code if the Multidisciplinary Team is not listed.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3190_MDT_TYPE1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3160_mdt_type_comment1: Optional[str] = Field(default=None, description="""To provide additional information on the MDT Meeting type where not covered in the list provided""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3160_MDT_TYPE_COMMENT1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(60)'}},
         'domain_of': ['COSDResearchView']} })
    cr8100_mdt_discussion2: Optional[MultidisciplinaryTeamMeetingDiscussion] = Field(default=None, description="""Record if the patient was not discussed within a MDT Meeting""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8100_MDT_DISCUSSION2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr8110_mdt_discussion_type2: Optional[MultidisciplinaryTeamMeetingDiscussionType] = Field(default=None, description="""Record if the patient was discussed within a Multidisciplinary Team Meeting (MDTM)""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8110_MDT_DISCUSSION_TYPE2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3080_mdt_date2: Optional[str] = Field(default=None, description="""Record the date of each Multidisciplinary Team meeting where the patient was discussed.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3080_MDT_DATE2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3090_mdt_organisation_site_id2: Optional[str] = Field(default=None, description="""The ORGANISATION IDENTIFIER of the Organisation Site where the Multidisciplinary Team Meeting took place. (For joint MDT meetings a new MDT section must be recorded for each meeting)""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3090_MDT_ORGANISATION_SITE_ID2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3190_mdt_type2: Optional[MultidisciplinaryTeamMeetingType] = Field(default=None, description="""Record the type of MDT meeting at which the patient was discussed. Please provide the most detailed level of information that is possible.
Note: the codes at the high level (shown in bold) are Tumour groups and the items below each high-level code are Multidisciplinary Teams. ORGANISATIONS should only use the high-level code if the Multidisciplinary Team is not listed.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3190_MDT_TYPE2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3160_mdt_type_comment2: Optional[str] = Field(default=None, description="""To provide additional information on the MDT Meeting type where not covered in the list provided""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3160_MDT_TYPE_COMMENT2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(60)'}},
         'domain_of': ['COSDResearchView']} })
    cr8100_mdt_discussion3: Optional[MultidisciplinaryTeamMeetingDiscussion] = Field(default=None, description="""Record if the patient was not discussed within a MDT Meeting""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8100_MDT_DISCUSSION3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr8110_mdt_discussion_type3: Optional[MultidisciplinaryTeamMeetingDiscussionType] = Field(default=None, description="""Record if the patient was discussed within a Multidisciplinary Team Meeting (MDTM)""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8110_MDT_DISCUSSION_TYPE3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3080_mdt_date3: Optional[str] = Field(default=None, description="""Record the date of each Multidisciplinary Team meeting where the patient was discussed.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3080_MDT_DATE3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3090_mdt_organisation_site_id3: Optional[str] = Field(default=None, description="""The ORGANISATION IDENTIFIER of the Organisation Site where the Multidisciplinary Team Meeting took place. (For joint MDT meetings a new MDT section must be recorded for each meeting)""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3090_MDT_ORGANISATION_SITE_ID3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3190_mdt_type3: Optional[MultidisciplinaryTeamMeetingType] = Field(default=None, description="""Record the type of MDT meeting at which the patient was discussed. Please provide the most detailed level of information that is possible.
Note: the codes at the high level (shown in bold) are Tumour groups and the items below each high-level code are Multidisciplinary Teams. ORGANISATIONS should only use the high-level code if the Multidisciplinary Team is not listed.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3190_MDT_TYPE3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3160_mdt_type_comment3: Optional[str] = Field(default=None, description="""To provide additional information on the MDT Meeting type where not covered in the list provided""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3160_MDT_TYPE_COMMENT3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(60)'}},
         'domain_of': ['COSDResearchView']} })
    cr8100_mdt_discussion4: Optional[MultidisciplinaryTeamMeetingDiscussion] = Field(default=None, description="""Record if the patient was not discussed within a MDT Meeting""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8100_MDT_DISCUSSION4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr8110_mdt_discussion_type4: Optional[MultidisciplinaryTeamMeetingDiscussionType] = Field(default=None, description="""Record if the patient was discussed within a Multidisciplinary Team Meeting (MDTM)""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8110_MDT_DISCUSSION_TYPE4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3080_mdt_date4: Optional[str] = Field(default=None, description="""Record the date of each Multidisciplinary Team meeting where the patient was discussed.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3080_MDT_DATE4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3090_mdt_organisation_site_id4: Optional[str] = Field(default=None, description="""The ORGANISATION IDENTIFIER of the Organisation Site where the Multidisciplinary Team Meeting took place. (For joint MDT meetings a new MDT section must be recorded for each meeting)""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3090_MDT_ORGANISATION_SITE_ID4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3190_mdt_type4: Optional[MultidisciplinaryTeamMeetingType] = Field(default=None, description="""Record the type of MDT meeting at which the patient was discussed. Please provide the most detailed level of information that is possible.
Note: the codes at the high level (shown in bold) are Tumour groups and the items below each high-level code are Multidisciplinary Teams. ORGANISATIONS should only use the high-level code if the Multidisciplinary Team is not listed.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3190_MDT_TYPE4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3160_mdt_type_comment4: Optional[str] = Field(default=None, description="""To provide additional information on the MDT Meeting type where not covered in the list provided""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3160_MDT_TYPE_COMMENT4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(60)'}},
         'domain_of': ['COSDResearchView']} })
    cr8100_mdt_discussion5: Optional[MultidisciplinaryTeamMeetingDiscussion] = Field(default=None, description="""Record if the patient was not discussed within a MDT Meeting""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8100_MDT_DISCUSSION5'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr8110_mdt_discussion_type5: Optional[MultidisciplinaryTeamMeetingDiscussionType] = Field(default=None, description="""Record if the patient was discussed within a Multidisciplinary Team Meeting (MDTM)""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8110_MDT_DISCUSSION_TYPE5'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3080_mdt_date5: Optional[str] = Field(default=None, description="""Record the date of each Multidisciplinary Team meeting where the patient was discussed.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3080_MDT_DATE5'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3090_mdt_organisation_site_id5: Optional[str] = Field(default=None, description="""The ORGANISATION IDENTIFIER of the Organisation Site where the Multidisciplinary Team Meeting took place. (For joint MDT meetings a new MDT section must be recorded for each meeting)""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3090_MDT_ORGANISATION_SITE_ID5'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3190_mdt_type5: Optional[MultidisciplinaryTeamMeetingType] = Field(default=None, description="""Record the type of MDT meeting at which the patient was discussed. Please provide the most detailed level of information that is possible.
Note: the codes at the high level (shown in bold) are Tumour groups and the items below each high-level code are Multidisciplinary Teams. ORGANISATIONS should only use the high-level code if the Multidisciplinary Team is not listed.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3190_MDT_TYPE5'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3160_mdt_type_comment5: Optional[str] = Field(default=None, description="""To provide additional information on the MDT Meeting type where not covered in the list provided""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3160_MDT_TYPE_COMMENT5'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(60)'}},
         'domain_of': ['COSDResearchView']} })
    cr8100_mdt_discussion6: Optional[MultidisciplinaryTeamMeetingDiscussion] = Field(default=None, description="""Record if the patient was not discussed within a MDT Meeting""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8100_MDT_DISCUSSION6'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr8110_mdt_discussion_type6: Optional[MultidisciplinaryTeamMeetingDiscussionType] = Field(default=None, description="""Record if the patient was discussed within a Multidisciplinary Team Meeting (MDTM)""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8110_MDT_DISCUSSION_TYPE6'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3080_mdt_date6: Optional[str] = Field(default=None, description="""Record the date of each Multidisciplinary Team meeting where the patient was discussed.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3080_MDT_DATE6'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3090_mdt_organisation_site_id6: Optional[str] = Field(default=None, description="""The ORGANISATION IDENTIFIER of the Organisation Site where the Multidisciplinary Team Meeting took place. (For joint MDT meetings a new MDT section must be recorded for each meeting)""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3090_MDT_ORGANISATION_SITE_ID6'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3190_mdt_type6: Optional[MultidisciplinaryTeamMeetingType] = Field(default=None, description="""Record the type of MDT meeting at which the patient was discussed. Please provide the most detailed level of information that is possible.
Note: the codes at the high level (shown in bold) are Tumour groups and the items below each high-level code are Multidisciplinary Teams. ORGANISATIONS should only use the high-level code if the Multidisciplinary Team is not listed.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3190_MDT_TYPE6'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3160_mdt_type_comment6: Optional[str] = Field(default=None, description="""To provide additional information on the MDT Meeting type where not covered in the list provided""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3160_MDT_TYPE_COMMENT6'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(60)'}},
         'domain_of': ['COSDResearchView']} })
    cr8100_mdt_discussion7: Optional[MultidisciplinaryTeamMeetingDiscussion] = Field(default=None, description="""Record if the patient was not discussed within a MDT Meeting""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8100_MDT_DISCUSSION7'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr8110_mdt_discussion_type7: Optional[MultidisciplinaryTeamMeetingDiscussionType] = Field(default=None, description="""Record if the patient was discussed within a Multidisciplinary Team Meeting (MDTM)""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8110_MDT_DISCUSSION_TYPE7'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3080_mdt_date7: Optional[str] = Field(default=None, description="""Record the date of each Multidisciplinary Team meeting where the patient was discussed.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3080_MDT_DATE7'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3090_mdt_organisation_site_id7: Optional[str] = Field(default=None, description="""The ORGANISATION IDENTIFIER of the Organisation Site where the Multidisciplinary Team Meeting took place. (For joint MDT meetings a new MDT section must be recorded for each meeting)""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3090_MDT_ORGANISATION_SITE_ID7'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3190_mdt_type7: Optional[MultidisciplinaryTeamMeetingType] = Field(default=None, description="""Record the type of MDT meeting at which the patient was discussed. Please provide the most detailed level of information that is possible.
Note: the codes at the high level (shown in bold) are Tumour groups and the items below each high-level code are Multidisciplinary Teams. ORGANISATIONS should only use the high-level code if the Multidisciplinary Team is not listed.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3190_MDT_TYPE7'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3160_mdt_type_comment7: Optional[str] = Field(default=None, description="""To provide additional information on the MDT Meeting type where not covered in the list provided""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3160_MDT_TYPE_COMMENT7'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(60)'}},
         'domain_of': ['COSDResearchView']} })
    cr8100_mdt_discussion8: Optional[MultidisciplinaryTeamMeetingDiscussion] = Field(default=None, description="""Record if the patient was not discussed within a MDT Meeting""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8100_MDT_DISCUSSION8'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr8110_mdt_discussion_type8: Optional[MultidisciplinaryTeamMeetingDiscussionType] = Field(default=None, description="""Record if the patient was discussed within a Multidisciplinary Team Meeting (MDTM)""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8110_MDT_DISCUSSION_TYPE8'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3080_mdt_date8: Optional[str] = Field(default=None, description="""Record the date of each Multidisciplinary Team meeting where the patient was discussed.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3080_MDT_DATE8'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3090_mdt_organisation_site_id8: Optional[str] = Field(default=None, description="""The ORGANISATION IDENTIFIER of the Organisation Site where the Multidisciplinary Team Meeting took place. (For joint MDT meetings a new MDT section must be recorded for each meeting)""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3090_MDT_ORGANISATION_SITE_ID8'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3190_mdt_type8: Optional[MultidisciplinaryTeamMeetingType] = Field(default=None, description="""Record the type of MDT meeting at which the patient was discussed. Please provide the most detailed level of information that is possible.
Note: the codes at the high level (shown in bold) are Tumour groups and the items below each high-level code are Multidisciplinary Teams. ORGANISATIONS should only use the high-level code if the Multidisciplinary Team is not listed.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3190_MDT_TYPE8'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3160_mdt_type_comment8: Optional[str] = Field(default=None, description="""To provide additional information on the MDT Meeting type where not covered in the list provided""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3160_MDT_TYPE_COMMENT8'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(60)'}},
         'domain_of': ['COSDResearchView']} })
    cr8100_mdt_discussion9: Optional[MultidisciplinaryTeamMeetingDiscussion] = Field(default=None, description="""Record if the patient was not discussed within a MDT Meeting""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8100_MDT_DISCUSSION9'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr8110_mdt_discussion_type9: Optional[MultidisciplinaryTeamMeetingDiscussionType] = Field(default=None, description="""Record if the patient was discussed within a Multidisciplinary Team Meeting (MDTM)""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8110_MDT_DISCUSSION_TYPE9'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3080_mdt_date9: Optional[str] = Field(default=None, description="""Record the date of each Multidisciplinary Team meeting where the patient was discussed.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3080_MDT_DATE9'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3090_mdt_organisation_site_id9: Optional[str] = Field(default=None, description="""The ORGANISATION IDENTIFIER of the Organisation Site where the Multidisciplinary Team Meeting took place. (For joint MDT meetings a new MDT section must be recorded for each meeting)""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3090_MDT_ORGANISATION_SITE_ID9'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3190_mdt_type9: Optional[MultidisciplinaryTeamMeetingType] = Field(default=None, description="""Record the type of MDT meeting at which the patient was discussed. Please provide the most detailed level of information that is possible.
Note: the codes at the high level (shown in bold) are Tumour groups and the items below each high-level code are Multidisciplinary Teams. ORGANISATIONS should only use the high-level code if the Multidisciplinary Team is not listed.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3190_MDT_TYPE9'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3160_mdt_type_comment9: Optional[str] = Field(default=None, description="""To provide additional information on the MDT Meeting type where not covered in the list provided""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3160_MDT_TYPE_COMMENT9'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(60)'}},
         'domain_of': ['COSDResearchView']} })
    cr8100_mdt_discussion10: Optional[MultidisciplinaryTeamMeetingDiscussion] = Field(default=None, description="""Record if the patient was not discussed within a MDT Meeting""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8100_MDT_DISCUSSION10'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr8110_mdt_discussion_type10: Optional[MultidisciplinaryTeamMeetingDiscussionType] = Field(default=None, description="""Record if the patient was discussed within a Multidisciplinary Team Meeting (MDTM)""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8110_MDT_DISCUSSION_TYPE10'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3080_mdt_date10: Optional[str] = Field(default=None, description="""Record the date of each Multidisciplinary Team meeting where the patient was discussed.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3080_MDT_DATE10'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3090_mdt_organisation_site_id10: Optional[str] = Field(default=None, description="""The ORGANISATION IDENTIFIER of the Organisation Site where the Multidisciplinary Team Meeting took place. (For joint MDT meetings a new MDT section must be recorded for each meeting)""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3090_MDT_ORGANISATION_SITE_ID10'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3190_mdt_type10: Optional[MultidisciplinaryTeamMeetingType] = Field(default=None, description="""Record the type of MDT meeting at which the patient was discussed. Please provide the most detailed level of information that is possible.
Note: the codes at the high level (shown in bold) are Tumour groups and the items below each high-level code are Multidisciplinary Teams. ORGANISATIONS should only use the high-level code if the Multidisciplinary Team is not listed.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3190_MDT_TYPE10'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3160_mdt_type_comment10: Optional[str] = Field(default=None, description="""To provide additional information on the MDT Meeting type where not covered in the list provided""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3160_MDT_TYPE_COMMENT10'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(60)'}},
         'domain_of': ['COSDResearchView']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
COSDResearchView.model_rebuild()
