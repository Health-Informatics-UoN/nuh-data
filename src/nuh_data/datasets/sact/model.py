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
                     'controlled_vocabulary': {'tag': 'controlled_vocabulary',
                                               'value': 'OTHER'},
                     'created_by_name': {'tag': 'created_by_name',
                                         'value': 'Nottingham University Hospitals '
                                                  'NHS Trust'},
                     'data_custodian': {'tag': 'data_custodian',
                                        'value': 'Nottingham University Hospitals '
                                                 'NHS Trust'},
                     'data_standards': {'tag': 'data_standards',
                                        'value': 'OMOP, OTHER'},
                     'geographic_coverage': {'tag': 'geographic_coverage',
                                             'value': 'Nottinghamshire, England'},
                     'population_size': {'tag': 'population_size',
                                         'value': '33156'},
                     'publishing_frequency': {'tag': 'publishing_frequency',
                                              'value': 'Quarterly'},
                     'temporal_coverage_end': {'tag': 'temporal_coverage_end',
                                               'value': '2026-03-01'},
                     'temporal_coverage_start': {'tag': 'temporal_coverage_start',
                                                 'value': '2009-01-01'}},
     'created_by': 'https://github.com/Health-Informatics-UoN',
     'default_prefix': 'sact',
     'default_range': 'string',
     'description': 'Clinical dataset documenting systemic anti-cancer treatment '
                    'records from Nottingham University Hospitals NHS Trust. '
                    'Covers patients receiving systemic anti-cancer therapies '
                    '(chemotherapy and other systemic treatments) from 2009 '
                    'onwards, capturing patient demographics, regimen details, '
                    'cycle data, and individual drug administrations.',
     'id': 'https://health-informatics-uon.github.io/nuh-data/datasets/sact',
     'imports': ['linkml:types'],
     'keywords': ['systemic anti-cancer therapy',
                  'SACT',
                  'oncology',
                  'chemotherapy',
                  'NHS',
                  'Nottingham',
                  'cancer treatment',
                  'clinical'],
     'license': 'https://opensource.org/license/mit',
     'name': 'sact',
     'prefixes': {'ICD': {'prefix_prefix': 'ICD',
                          'prefix_reference': 'http://id.who.int/icd/entity/'},
                  'SNOMED': {'prefix_prefix': 'SNOMED',
                             'prefix_reference': 'http://snomed.info/id/'},
                  'dmd': {'prefix_prefix': 'dmd',
                          'prefix_reference': 'https://dmd.nhs.uk/concept/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'sact': {'prefix_prefix': 'sact',
                           'prefix_reference': 'https://health-informatics-uon.github.io/nuh-data/datasets/sact/'}},
     'source_file': 'schemas/datasets/sact/sact.yaml',
     'title': 'NUH Systemic Anti-Cancer Therapy Dataset (SACT)'} )

class NHSNumberStatusCode(str, Enum):
    """
    Verification status of the NHS number provided.
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
    Trace needs to be resolved - NHS Number or patient detail conflict
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


class PersonStatedGenderCode(str, Enum):
    """
    Person's gender as self-declared.
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


class AdjunctiveTherapyType(str, Enum):
    """
    Whether therapy was given in addition to the main therapy, and if so, whether before or after.
    """
    number_1 = "1"
    """
    Adjuvant (after main therapy)
    """
    number_2 = "2"
    """
    Neoadjuvant (before main therapy)
    """
    number_3 = "3"
    """
    Not Applicable (Primary Treatment)
    """
    number_9 = "9"
    """
    Not Known
    """


class IntentOfTreatment(str, Enum):
    """
    Intent of the SACT regimen.
    """
    A = "A"
    """
    Adjuvant
    """
    N = "N"
    """
    Neo-Adjuvant
    """
    C = "C"
    """
    Curative
    """
    P = "P"
    """
    Palliative
    """
    D = "D"
    """
    Disease Modification
    """
    number_01 = "01"
    """
    Curative - aiming to permanently eradicate disease
    """
    number_02 = "02"
    """
    Palliative - aiming to extend life expectancy
    """
    number_03 = "03"
    """
    Palliative - aiming to relieve and/or control malignancy related symptoms
    """
    number_04 = "04"
    """
    Palliative - aiming to achieve remission
    """
    number_05 = "05"
    """
    Palliative - aiming to delay tumour progression
    """
    number_98 = "98"
    """
    Other
    """
    number_99 = "99"
    """
    Not Known
    """


class PerformanceStatusAdult(str, Enum):
    """
    WHO performance status classification for patients aged 19 years and above, indicating activity level and disability.
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
    Ambulatory and capable of all self-care but unable to carry out any work; up and about more than 50% of waking hours
    """
    number_3 = "3"
    """
    Symptomatic and in a chair or in bed for greater than 50% of the day but not bedridden
    """
    number_4 = "4"
    """
    Completely disabled; cannot carry out any self-care; totally confined to bed or chair
    """


class YesNoIndicator(str, Enum):
    """
    Simple yes/no indicator.
    """
    Y = "Y"
    """
    Yes
    """
    N = "N"
    """
    No
    """


class ClinicalTrialIndicator(str, Enum):
    """
    Whether the patient is currently in an active SACT clinical trial.
    """
    number_01 = "01"
    """
    Patient is taking part in a clinical trial
    """
    number_02 = "02"
    """
    Patient is not taking part in a clinical trial
    """
    number_99 = "99"
    """
    Not Known
    """


class AdministrationMeasurementCode(str, Enum):
    """
    Units of measurement used for each drug administration in a SACT cycle.
    """
    number_01 = "01"
    """
    mg
    """
    number_02 = "02"
    """
    Mcg
    """
    number_03 = "03"
    """
    g
    """
    number_04 = "04"
    """
    Units
    """
    number_05 = "05"
    """
    Cells
    """
    number_06 = "06"
    """
    x10^6 PFU
    """
    number_07 = "07"
    """
    x10^8 PFU
    """
    number_98 = "98"
    """
    Other
    """
    number_99 = "99"
    """
    Not Known
    """


class SACTAdministrationRouteCode(str, Enum):
    """
    Prescribed method of delivery for each administration in a SACT cycle.
    """
    number_01 = "01"
    """
    Intravenous
    """
    number_02 = "02"
    """
    Oral
    """
    number_03 = "03"
    """
    Intrathecal
    """
    number_04 = "04"
    """
    Intramuscular
    """
    number_05 = "05"
    """
    Subcutaneous
    """
    number_06 = "06"
    """
    Intraarterial
    """
    number_07 = "07"
    """
    Intraperitoneal
    """
    number_08 = "08"
    """
    Other intracavity / Intracavernous
    """
    number_09 = "09"
    """
    Intravesical (Intra-Vesicular)
    """
    number_10 = "10"
    """
    Intratumour / Intralesional
    """
    number_11 = "11"
    """
    Cutaneous (Topical)
    """
    number_12 = "12"
    """
    Intradermal
    """
    number_13 = "13"
    """
    Intratumour
    """
    number_14 = "14"
    """
    Intralesional
    """
    number_98 = "98"
    """
    Other
    """



class SACTResearchView(ConfiguredBaseModel):
    """
    Flat research view combining patient, regimen, cycle, and drug administration data. Corresponds to RVW.SACT_RESEARCH_VIEW in the source database. Each row represents a single drug administration event, with regimen and patient context repeated per row.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://health-informatics-uon.github.io/nuh-data/datasets/sact',
         'tree_root': True})

    etl_id: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column', 'value': 'ETL_ID'},
                         'sql_type': {'tag': 'sql_type', 'value': 'INT'}},
         'domain_of': ['SACTResearchView']} })
    etl_date: Optional[datetime ] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column', 'value': 'ETL_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATETIME'}},
         'domain_of': ['SACTResearchView']} })
    direct_care_published_runid: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'DIRECT_CARE_PUBLISHED_RUNID'},
                         'sql_type': {'tag': 'sql_type', 'value': 'INT'}},
         'domain_of': ['SACTResearchView']} })
    dataset_name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column', 'value': 'DATASET_NAME'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(300)'}},
         'domain_of': ['SACTResearchView']} })
    ndo_run_date: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column', 'value': 'NDO_RUN_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['SACTResearchView']} })
    file_name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column', 'value': 'FILE_NAME'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(150)'}},
         'domain_of': ['SACTResearchView']} })
    file_period_start: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'FILE_PERIOD_START'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(20)'}},
         'domain_of': ['SACTResearchView']} })
    file_period_end: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'FILE_PERIOD_END'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(20)'}},
         'domain_of': ['SACTResearchView']} })
    pseudo_nhs_number: Optional[str] = Field(default=None, description="""The NHS NUMBER, the primary identifier of a PERSON, is a unique identifier for a PATIENT within the NHS in England and Wales. Pseudonymised for research use.""", json_schema_extra = { "linkml_meta": {'annotations': {'sensitivity': {'tag': 'sensitivity',
                                         'value': 'pseudonymised'},
                         'sql_column': {'tag': 'sql_column',
                                        'value': 'PSEUDO_NHS_NUMBER'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARBINARY(100)'}},
         'domain_of': ['SACTResearchView']} })
    nhs_number_status: Optional[NHSNumberStatusCode] = Field(default=None, description="""The NHS NUMBER STATUS INDICATOR CODE indicates the verification status of the NHS number provided.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'NHS_NUMBER_STATUS'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(4)'}},
         'domain_of': ['SACTResearchView']} })
    date_of_birth_year: Optional[str] = Field(default=None, description="""Year component of the patient's date of birth, extracted from DATE OF BIRTH for privacy preservation.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'DATE_OF_BIRTH_YEAR'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(8)'}},
         'domain_of': ['SACTResearchView']} })
    date_of_birth_month: Optional[str] = Field(default=None, description="""Month component of the patient's date of birth, extracted from DATE OF BIRTH for privacy preservation.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'DATE_OF_BIRTH_MONTH'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(4)'}},
         'domain_of': ['SACTResearchView']} })
    date_of_birth_mid_month: Optional[date] = Field(default=None, description="""Approximate date of birth using the 15th of the birth month, for use in age calculations while preserving patient privacy.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'DATE_OF_BIRTH_MID_MONTH'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['SACTResearchView']} })
    person_stated_gender_code: Optional[PersonStatedGenderCode] = Field(default=None, description="""Person's gender as self-declared (or inferred by observation for those unable to declare their PERSON STATED GENDER).""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PERSON_STATED_GENDER_CODE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(2)'}},
         'domain_of': ['SACTResearchView']} })
    llsoa: Optional[str] = Field(default=None, description="""Lower Layer Super Output Area, derived from PATIENT POSTCODE for geographic analysis while preserving patient privacy.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column', 'value': 'LLSOA'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(18)'}},
         'domain_of': ['SACTResearchView']} })
    consultant_gmc_code: Optional[str] = Field(default=None, description="""Code of the consultant who initiated the SACT treatment. Derived from the GENERAL MEDICAL COUNCIL REFERENCE NUMBER.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CONSULTANT_GMC_CODE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(16)'}},
         'domain_of': ['SACTResearchView']} })
    consultant_spec_code: Optional[str] = Field(default=None, description="""Specialty code of the consultant who initiated the SACT treatment.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CONSULTANT_SPEC_CODE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(16)'}},
         'domain_of': ['SACTResearchView']} })
    org_id_code_provider: Optional[str] = Field(default=None, description="""The ORGANISATION IDENTIFIER of the Organisation acting as a Health Care Provider. Complies with ANANA standard DCB0090.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'ORG_ID_CODE_PROVIDER'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(10)'}},
         'domain_of': ['SACTResearchView']} })
    primary_diagnosis: Optional[str] = Field(default=None, description="""Primary diagnosis at time of decision to treat, coded using ICD. This is the PRIMARY DIAGNOSIS (ICD) at the start of the Systemic Anti-Cancer Therapy.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PRIMARY_DIAGNOSIS'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(12)'}},
         'domain_of': ['SACTResearchView']} })
    morphology_icd_o: Optional[str] = Field(default=None, description="""Morphology coded using ICD-O at time of decision to treat. This is the Morphology ICD-O at the start of the Systemic Anti-Cancer Therapy. Required for Haematology cases.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'MORPHOLOGY_ICD_O'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(14)'}},
         'domain_of': ['SACTResearchView']} })
    diagnosis_code_snomed: Optional[str] = Field(default=None, description="""SNOMED CT concept ID identifying the clinical diagnosis given to the patient.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'DIAGNOSIS_CODE_SNOMED'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(36)'},
                         'vocabulary': {'tag': 'vocabulary', 'value': 'SNOMED CT'}},
         'domain_of': ['SACTResearchView']} })
    adjunctive_therapy: Optional[AdjunctiveTherapyType] = Field(default=None, description="""Adjunctive therapy is therapy given in addition to the main therapy to maximise its effectiveness. Records whether the therapy was Adjuvant (after the main therapy), Neo-Adjuvant (before the main therapy), or not applicable.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'ADJUNCTIVE_THERAPY'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(2)'}},
         'domain_of': ['SACTResearchView']} })
    intent_of_treatment: Optional[IntentOfTreatment] = Field(default=None, description="""Intent of the SACT regimen.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'INTENT_OF_TREATMENT'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(4)'}},
         'domain_of': ['SACTResearchView']} })
    regimen: Optional[str] = Field(default=None, description="""The acronym derived from the drugs used in the Anti-Cancer Drug Regimen, used to identify the drugs used in the regimen.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column', 'value': 'REGIMEN'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(300)'}},
         'domain_of': ['SACTResearchView']} })
    height_start_reg: Optional[float] = Field(default=None, description="""Height in metres at start of SACT regimen.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'HEIGHT_START_REG'},
                         'sql_type': {'tag': 'sql_type', 'value': 'FLOAT'}},
         'domain_of': ['SACTResearchView'],
         'unit': {'ucum_code': 'm'}} })
    weight_start_of_reg: Optional[float] = Field(default=None, description="""Weight in kilogrammes at start of SACT regimen.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'WEIGHT_START_OF_REG'},
                         'sql_type': {'tag': 'sql_type', 'value': 'FLOAT'}},
         'domain_of': ['SACTResearchView'],
         'unit': {'ucum_code': 'kg'}} })
    perf_status_start_reg_ad: Optional[PerformanceStatusAdult] = Field(default=None, description="""WHO performance status at start of the regimen, for patients aged 19 years and above.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PERF_STATUS_START_REG_AD'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(2)'}},
         'domain_of': ['SACTResearchView']} })
    co_morbidity_adjustment: Optional[YesNoIndicator] = Field(default=None, description="""Whether the patient's overall physical state (other diseases and conditions) was a significant factor in deciding on the regimen, or in varying the dose or treatment interval.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CO_MORBIDITY_ADJUSTMENT'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(2)'}},
         'domain_of': ['SACTResearchView']} })
    date_decision_to_treat: Optional[date] = Field(default=None, description="""The date on which the consultation between the PATIENT and the clinician took place and a Planned Cancer Treatment was agreed.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'DATE_DECISION_TO_TREAT'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['SACTResearchView']} })
    start_date_regimen: Optional[date] = Field(default=None, description="""The first administration date of the first cycle of a regimen.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'START_DATE_REGIMEN'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['SACTResearchView']} })
    clinical_trial: Optional[ClinicalTrialIndicator] = Field(default=None, description="""Records whether the patient is currently in an active Systemic Anti-Cancer Therapy trial.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column', 'value': 'CLINICAL_TRIAL'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(4)'}},
         'domain_of': ['SACTResearchView']} })
    cycle_number: Optional[int] = Field(default=None, description="""Cycle number, numbered sequentially within each regimen.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column', 'value': 'CYCLE_NUMBER'},
                         'sql_type': {'tag': 'sql_type', 'value': 'INT'}},
         'domain_of': ['SACTResearchView']} })
    start_date_cycle: Optional[date] = Field(default=None, description="""Date of first drug administration in each cycle.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'START_DATE_CYCLE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['SACTResearchView']} })
    weight_start_cycle: Optional[float] = Field(default=None, description="""Weight in kilogrammes at start of the cycle.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'WEIGHT_START_CYCLE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'FLOAT'}},
         'domain_of': ['SACTResearchView'],
         'unit': {'ucum_code': 'kg'}} })
    perf_stat_start_cycle_ad: Optional[PerformanceStatusAdult] = Field(default=None, description="""WHO performance status at start of the cycle, for patients aged 19 years and above.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PERF_STAT_START_CYCLE_AD'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(2)'}},
         'domain_of': ['SACTResearchView']} })
    drug_name: Optional[str] = Field(default=None, description="""The name of the anti-cancer drug, taken from the British National Formulary.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column', 'value': 'DRUG_NAME'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(110)'}},
         'domain_of': ['SACTResearchView']} })
    dm_d: Optional[str] = Field(default=None, description="""The unique ID from the dm+d (Dictionary of Medicines and Devices) database, based around the drug name and manufacturer. Pilot item for v3.0, required only for official Pilot sites.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column', 'value': 'DM_D'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(36)'},
                         'vocabulary': {'tag': 'vocabulary',
                                        'value': 'NHS Dictionary of Medicines and '
                                                 'Devices (dm+d)'}},
         'domain_of': ['SACTResearchView']} })
    actual_dose_per_admin: Optional[str] = Field(default=None, description="""Dose in mg or other applicable unit for each administration in a SACT cycle.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'ACTUAL_DOSE_PER_ADMIN'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(100)'}},
         'domain_of': ['SACTResearchView']} })
    admin_meas_per_actual_dose: Optional[AdministrationMeasurementCode] = Field(default=None, description="""Units of measurement used for each administration in a SACT cycle.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'ADMIN_MEAS_PER_ACTUAL_DOSE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(16)'}},
         'domain_of': ['SACTResearchView']} })
    ot_admin_meas_per_actual_dose: Optional[str] = Field(default=None, description="""Free-text description of a unit of measurement not available within the coded [admin_meas_per_actual_dose] field. Only populated when code 98 (Other) is selected.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'OT_ADMIN_MEAS_PER_ACTUAL_DOSE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(30)'}},
         'domain_of': ['SACTResearchView']} })
    unit_meas_snomed_ct_dm_d: Optional[str] = Field(default=None, description="""The SNOMED CT concept ID from the NHS Dictionary of Medicines and Devices identifying the unit of measurement.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'UNIT_MEAS_SNOMED_CT_DM_D'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(36)'},
                         'vocabulary': {'tag': 'vocabulary',
                                        'value': 'SNOMED CT / dm+d'}},
         'domain_of': ['SACTResearchView']} })
    sact_administration_route: Optional[SACTAdministrationRouteCode] = Field(default=None, description="""The prescribed method of delivery for each administration in a SACT cycle.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'SACT_ADMINISTRATION_ROUTE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(4)'}},
         'domain_of': ['SACTResearchView']} })
    route_admin_snomed_ct_dm_d: Optional[str] = Field(default=None, description="""The SNOMED CT concept ID from the NHS Dictionary of Medicines and Devices identifying the route of administration.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'ROUTE_ADMIN_SNOMED_CT_DM_D'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(36)'},
                         'vocabulary': {'tag': 'vocabulary',
                                        'value': 'SNOMED CT / dm+d'}},
         'domain_of': ['SACTResearchView']} })
    administration_date: Optional[date] = Field(default=None, description="""The date on which the anti-cancer drug was administered to a patient, an infusion commenced, or an oral drug initially dispensed to the patient.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'ADMINISTRATION_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['SACTResearchView']} })
    org_identifier_sact_admin: Optional[str] = Field(default=None, description="""Organisation Identifier of the organisation responsible for each administration in a SACT cycle. Complies with ANANA standard DCB0090.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'ORG_IDENTIFIER_SACT_ADMIN'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(10)'}},
         'domain_of': ['SACTResearchView']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
SACTResearchView.model_rebuild()
