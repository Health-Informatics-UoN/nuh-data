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
    pseudo_c000070_unique_record_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sensitivity': {'tag': 'sensitivity',
                                         'value': 'pseudonymised'},
                         'sql_column': {'tag': 'sql_column',
                                        'value': 'PSEUDO_C000070_UNIQUE_RECORD_ID'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARBINARY(100)'}},
         'domain_of': ['COSDResearchView']} })
    pseudo_cr0010_nhs_number: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sensitivity': {'tag': 'sensitivity',
                                         'value': 'pseudonymised'},
                         'sql_column': {'tag': 'sql_column',
                                        'value': 'PSEUDO_CR0010_NHS_NUMBER'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARBINARY(100)'}},
         'domain_of': ['COSDResearchView']} })
    cr1350_nhs_num_stat_code: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
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
    cr0030_provider_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0030_PROVIDER_ID'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(5)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr0370_diag_primary_diag_icd: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR0370_DIAG_PRIMARY_DIAG_ICD'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(6)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr0380_diag_tumour_laterality: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR0380_DIAG_TUMOUR_LATERALITY'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr2030_diag_date_of_primary_diag_clin_agreed: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR2030_DIAG_DATE_OF_PRIMARY_DIAG_CLIN_AGREED'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    npp_cr6500_date_diagnosis_clinically_agreed: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'NPP_CR6500_DATE_DIAGNOSIS_CLINICALLY_AGREED'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    npp_cr7100_diag_original_primary_diagnosis_icd: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'NPP_CR7100_DIAG_ORIGINAL_PRIMARY_DIAGNOSIS_ICD'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(6)'}},
         'domain_of': ['COSDResearchView']} })
    npp_cr6520_rec1_metastatic_type1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'NPP_CR6520_REC1_METASTATIC_TYPE1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    npp_cr1590_rec1_metastatic_site1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'NPP_CR1590_REC1_METASTATIC_SITE1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    npp_cr6520_rec1_metastatic_type2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'NPP_CR6520_REC1_METASTATIC_TYPE2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    npp_cr1590_rec1_metastatic_site2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'NPP_CR1590_REC1_METASTATIC_SITE2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    npp_cr1550_diag_palliative_care_specialist_seen_indicator_cancer_recurrence: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'NPP_CR1550_DIAG_PALLIATIVE_CARE_SPECIALIST_SEEN_INDICATOR_CANCER_RECURRENCE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    npp_cr9000_diag_relapse_method_of_detection_1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'NPP_CR9000_DIAG_RELAPSE_METHOD_OF_DETECTION_1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    npp_cr9000_diag_relapse_method_of_detection_2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'NPP_CR9000_DIAG_RELAPSE_METHOD_OF_DETECTION_2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    npp_cr6900_progression_icd: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'NPP_CR6900_PROGRESSION_ICD'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(6)'}},
         'domain_of': ['COSDResearchView']} })
    npp_cr6520_prog_metastatic_type_progression1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'NPP_CR6520_PROG_METASTATIC_TYPE_PROGRESSION1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    npp_cr1590_prog_metastatic_site_progression1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'NPP_CR1590_PROG_METASTATIC_SITE_PROGRESSION1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    npp_cr6520_prog_metastatic_type_progression2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'NPP_CR6520_PROG_METASTATIC_TYPE_PROGRESSION2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    npp_cr1590_prog_metastatic_site_progression2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'NPP_CR1590_PROG_METASTATIC_SITE_PROGRESSION2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    npp_cr7200_trans_original_morphologyicd_o_3: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'NPP_CR7200_TRANS_ORIGINAL_MORPHOLOGYICD_O_3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(7)'}},
         'domain_of': ['COSDResearchView']} })
    npp_cr7210_trans_original_morphology_snomed: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'NPP_CR7210_TRANS_ORIGINAL_MORPHOLOGY_SNOMED'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    npp_cr7010_trans_morphology_icd_o_3_trans: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'NPP_CR7010_TRANS_MORPHOLOGY_ICD_O_3_TRANS'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(7)'}},
         'domain_of': ['COSDResearchView']} })
    npp_cr7000_trans_morphology_snomed_trans: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'NPP_CR7000_TRANS_MORPHOLOGY_SNOMED_TRANS'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    npp_cr7030_trans_snomed_version_current_trans: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'NPP_CR7030_TRANS_SNOMED_VERSION_CURRENT_TRANS'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    llsoa: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column', 'value': 'LLSOA'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(9)'}},
         'domain_of': ['COSDResearchView']} })
    cr3170_person_stated_gender_code: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3170_PERSON_STATED_GENDER_CODE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr6840_person_sexual_orientation_code_at_diagnosis: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6840_PERSON_SEXUAL_ORIENTATION_CODE_AT_DIAGNOSIS'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr0110_general_medical_practitioner_specified: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0110_GENERAL_MEDICAL_PRACTITIONER_SPECIFIED'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(8)'}},
         'domain_of': ['COSDResearchView']} })
    cr0120_general_medical_practice_code_patient_registration: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0120_GENERAL_MEDICAL_PRACTICE_CODE_PATIENT_REGISTRATION'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(8)'}},
         'domain_of': ['COSDResearchView']} })
    cr0150_ethnic_category: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0150_ETHNIC_CATEGORY'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr9060_ethnic_category_2021: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR9060_ETHNIC_CATEGORY_2021'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr1600_source_of_referral_op: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR1600_SOURCE_OF_REFERRAL_OP'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr0230_date_first_seen: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR0230_DATE_FIRST_SEEN'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr7300_prof_reg_issuer_code_cons_first_seen: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR7300_PROF_REG_ISSUER_CODE_CONS_FIRST_SEEN'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr7310_prof_reg_entry_id_cons_first_seen: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR7310_PROF_REG_ENTRY_ID_CONS_FIRST_SEEN'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(32)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr1410_org_site_prov_first_seen: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR1410_ORG_SITE_PROV_FIRST_SEEN'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(9)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr1360_date_first_seen_cancer_specialist: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR1360_DATE_FIRST_SEEN_CANCER_SPECIALIST'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr1400_org_site_id_prov_first_cancer_specialist: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR1400_ORG_SITE_ID_PROV_FIRST_CANCER_SPECIALIST'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(9)'}},
         'domain_of': ['COSDResearchView']} })
    npp_cr0300_source_of_referral: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'NPP_CR0300_SOURCE_OF_REFERRAL'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    npp_cr7400_date_first_seen: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'NPP_CR7400_DATE_FIRST_SEEN'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    npp_cr7410_org_site_id_prov_first_seen: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'NPP_CR7410_ORG_SITE_ID_PROV_FIRST_SEEN'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(9)'}},
         'domain_of': ['COSDResearchView']} })
    cr7500_diag_proc1_org_site_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7500_DIAG_PROC1_ORG_SITE_ID'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(9)'}},
         'domain_of': ['COSDResearchView']} })
    cr7510_diag_proc1_procedure_date: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7510_DIAG_PROC1_PROCEDURE_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr7520_diag_proc1_opcs1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7520_DIAG_PROC1_OPCS1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr7520_diag_proc1_opcs2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7520_DIAG_PROC1_OPCS2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr7520_diag_proc1_opcs3: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7520_DIAG_PROC1_OPCS3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr7520_diag_proc1_opcs4: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7520_DIAG_PROC1_OPCS4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr7520_diag_proc1_opcs5: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7520_DIAG_PROC1_OPCS5'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr7530_diag_proc1_snomedct1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7530_DIAG_PROC1_SNOMEDCT1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr7530_diag_proc1_snomedct2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7530_DIAG_PROC1_SNOMEDCT2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr7530_diag_proc1_snomedct3: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7530_DIAG_PROC1_SNOMEDCT3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr7530_diag_proc1_snomedct4: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7530_DIAG_PROC1_SNOMEDCT4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr7530_diag_proc1_snomedct5: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7530_DIAG_PROC1_SNOMEDCT5'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr7540_sentinel_node_biopsy_outcome1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7540_SENTINEL_NODE_BIOPSY_OUTCOME1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr7500_diag_proc2_org_site_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7500_DIAG_PROC2_ORG_SITE_ID'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(9)'}},
         'domain_of': ['COSDResearchView']} })
    cr7510_diag_proc2_procedure_date: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7510_DIAG_PROC2_PROCEDURE_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr7520_diag_proc2_opcs1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7520_DIAG_PROC2_OPCS1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr7520_diag_proc2_opcs2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7520_DIAG_PROC2_OPCS2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr7520_diag_proc2_opcs3: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7520_DIAG_PROC2_OPCS3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr7520_diag_proc2_opcs4: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7520_DIAG_PROC2_OPCS4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr7520_diag_proc2_opcs5: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7520_DIAG_PROC2_OPCS5'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr7530_diag_proc2_snomedct1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7530_DIAG_PROC2_SNOMEDCT1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr7530_diag_proc2_snomedct2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7530_DIAG_PROC2_SNOMEDCT2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr7530_diag_proc2_snomedct3: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7530_DIAG_PROC2_SNOMEDCT3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr7530_diag_proc2_snomedct4: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7530_DIAG_PROC2_SNOMEDCT4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr7530_diag_proc2_snomedct5: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7530_DIAG_PROC2_SNOMEDCT5'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr7540_sentinel_node_biopsy_outcome2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7540_SENTINEL_NODE_BIOPSY_OUTCOME2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr7500_diag_proc3_org_site_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7500_DIAG_PROC3_ORG_SITE_ID'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(9)'}},
         'domain_of': ['COSDResearchView']} })
    cr7510_diag_proc3_procedure_date: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7510_DIAG_PROC3_PROCEDURE_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr7520_diag_proc3_opcs1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7520_DIAG_PROC3_OPCS1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr7520_diag_proc3_opcs2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7520_DIAG_PROC3_OPCS2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr7520_diag_proc3_opcs3: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7520_DIAG_PROC3_OPCS3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr7520_diag_proc3_opcs4: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7520_DIAG_PROC3_OPCS4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr7520_diag_proc3_opcs5: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7520_DIAG_PROC3_OPCS5'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr7530_diag_proc3_snomedct1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7530_DIAG_PROC3_SNOMEDCT1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr7530_diag_proc3_snomedct2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7530_DIAG_PROC3_SNOMEDCT2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr7530_diag_proc3_snomedct3: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7530_DIAG_PROC3_SNOMEDCT3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr7530_diag_proc3_snomedct4: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7530_DIAG_PROC3_SNOMEDCT4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr7530_diag_proc3_snomedct5: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7530_DIAG_PROC3_SNOMEDCT5'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr7540_sentinel_node_biopsy_outcome3: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7540_SENTINEL_NODE_BIOPSY_OUTCOME3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6230_org_site_id_of_diag: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6230_ORG_SITE_ID_OF_DIAG'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(9)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr0390_basis_of_diag_cancer: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR0390_BASIS_OF_DIAG_CANCER'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(3)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr0180_morphology_icd_o_3: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR0180_MORPHOLOGY_ICD_O_3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(7)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6400_curr_morphology_snomed_diag: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6400_CURR_MORPHOLOGY_SNOMED_DIAG'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6490_curr_snomed_version_diag: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6490_CURR_SNOMED_VERSION_DIAG'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr0480_topography_icd_o_3: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR0480_TOPOGRAPHY_ICD_O_3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(7)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr9010_ki67: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column', 'value': 'PP_CR9010_KI67'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(3)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr0410_grade_of_differentiationat_diag: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR0410_GRADE_OF_DIFFERENTIATIONAT_DIAG'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr0510_performance_status_adult: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR0510_PERFORMANCE_STATUS_ADULT'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6830_diagnosis_code_snomedct: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6830_DIAGNOSIS_CODE_SNOMEDCT'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6960_diag_metastatic_type_1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6960_DIAG_METASTATIC_TYPE_1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6970_diag_metastatic_site_1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6970_DIAG_METASTATIC_SITE_1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6960_diag_metastatic_type_2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6960_DIAG_METASTATIC_TYPE_2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6970_diag_metastatic_site_2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6970_DIAG_METASTATIC_SITE_2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6960_diag_metastatic_type_3: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6960_DIAG_METASTATIC_TYPE_3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6970_diag_metastatic_site_3: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6970_DIAG_METASTATIC_SITE_3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6960_diag_metastatic_type_4: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6960_DIAG_METASTATIC_TYPE_4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6970_diag_metastatic_site_4: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6970_DIAG_METASTATIC_SITE_4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr7600_primary_diag_subsidiary_comment: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR7600_PRIMARY_DIAG_SUBSIDIARY_COMMENT'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(50)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr7610_secondary_diag_icd1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR7610_SECONDARY_DIAG_ICD1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(6)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr7610_secondary_diag_icd2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR7610_SECONDARY_DIAG_ICD2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(6)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr7620_other_significant_diag_subsidiary_comment: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR7620_OTHER_SIGNIFICANT_DIAG_SUBSIDIARY_COMMENT'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(50)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr7630_familial_cancer_syndrome: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR7630_FAMILIAL_CANCER_SYNDROME'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr7640_familial_cancer_syndrome_subsidiary_comment: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR7640_FAMILIAL_CANCER_SYNDROME_SUBSIDIARY_COMMENT'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(50)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr9020_functional_syndrome_class_indicator: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR9020_FUNCTIONAL_SYNDROME_CLASS_INDICATOR'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr9030_functional_syndrome_class_type1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR9030_FUNCTIONAL_SYNDROME_CLASS_TYPE1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr9030_functional_syndrome_class_type2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR9030_FUNCTIONAL_SYNDROME_CLASS_TYPE2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr9030_unknown_functional_syndrome_class_type1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR9030_UNKNOWN_FUNCTIONAL_SYNDROME_CLASS_TYPE1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr9040_unknown_other_functional_syndrome_class_type1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR9040_UNKNOWN_OTHER_FUNCTIONAL_SYNDROME_CLASS_TYPE1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(50)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr9030_unknown_functional_syndrome_class_type2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR9030_UNKNOWN_FUNCTIONAL_SYNDROME_CLASS_TYPE2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr9040_unknown_other_functional_syndrome_class_type2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR9040_UNKNOWN_OTHER_FUNCTIONAL_SYNDROME_CLASS_TYPE2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(50)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr9030_unknown_functional_syndrome_class_type3: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR9030_UNKNOWN_FUNCTIONAL_SYNDROME_CLASS_TYPE3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr9040_unknown_other_functional_syndrome_class_type3: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR9040_UNKNOWN_OTHER_FUNCTIONAL_SYNDROME_CLASS_TYPE3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(50)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6960_prog1_metastatic_type1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6960_PROG1_METASTATIC_TYPE1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6970_prog1_metastatic_site1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6970_PROG1_METASTATIC_SITE1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6960_prog1_metastatic_type2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6960_PROG1_METASTATIC_TYPE2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6970_prog1_metastatic_site2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6970_PROG1_METASTATIC_SITE2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6960_prog1_metastatic_type3: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6960_PROG1_METASTATIC_TYPE3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6970_prog1_metastatic_site3: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6970_PROG1_METASTATIC_SITE3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6960_prog1_metastatic_type4: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6960_PROG1_METASTATIC_TYPE4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6970_prog1_metastatic_site4: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6970_PROG1_METASTATIC_SITE4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6960_prog2_metastatic_type1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6960_PROG2_METASTATIC_TYPE1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6970_prog2_metastatic_site1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6970_PROG2_METASTATIC_SITE1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6960_prog2_metastatic_type2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6960_PROG2_METASTATIC_TYPE2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6970_prog2_metastatic_site2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6970_PROG2_METASTATIC_SITE2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6960_prog2_metastatic_type3: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6960_PROG2_METASTATIC_TYPE3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6970_prog2_metastatic_site3: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6970_PROG2_METASTATIC_SITE3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6960_prog2_metastatic_type4: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6960_PROG2_METASTATIC_TYPE4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6970_prog2_metastatic_site4: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6970_PROG2_METASTATIC_SITE4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6910_progression1_date: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6910_PROGRESSION1_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6910_progression2_date: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6910_PROGRESSION2_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6910_progression3_date: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6910_PROGRESSION3_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6910_progression4_date: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6910_PROGRESSION4_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6910_progression5_date: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6910_PROGRESSION5_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6910_progression6_date: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6910_PROGRESSION6_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6910_progression7_date: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6910_PROGRESSION7_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6910_progression8_date: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6910_PROGRESSION8_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6910_progression9_date: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6910_PROGRESSION9_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6910_progression10_date: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6910_PROGRESSION10_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr7020_transformation_date1: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR7020_TRANSFORMATION_DATE1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr7010_morphology_icd_o_3_trans1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR7010_MORPHOLOGY_ICD_O_3_TRANS1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(7)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr7000_curr_morphology_snomed_trans1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR7000_CURR_MORPHOLOGY_SNOMED_TRANS1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr7030_curr_snomed_version_trans1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR7030_CURR_SNOMED_VERSION_TRANS1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr7020_transformation_date_2: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR7020_TRANSFORMATION_DATE_2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr7010_morphology_icd_o_3_trans2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR7010_MORPHOLOGY_ICD_O_3_TRANS2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(7)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr7000_curr_morphology_snomed_trans2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR7000_CURR_MORPHOLOGY_SNOMED_TRANS2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr7030_curr_snomed_version_trans2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR7030_CURR_SNOMED_VERSION_TRANS2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr6430_person_observation_height_in_metres1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6430_PERSON_OBSERVATION_HEIGHT_IN_METRES1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr6440_person_observation_weight1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6440_PERSON_OBSERVATION_WEIGHT1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(7)'}},
         'domain_of': ['COSDResearchView']} })
    cr6450_body_mass_index1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6450_BODY_MASS_INDEX1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr6450_date_observation_measured1: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6450_DATE_OBSERVATION_MEASURED1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr6430_person_observation_height_in_metres2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6430_PERSON_OBSERVATION_HEIGHT_IN_METRES2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr6440_person_observation_weight2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6440_PERSON_OBSERVATION_WEIGHT2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(7)'}},
         'domain_of': ['COSDResearchView']} })
    cr6450_body_mass_index2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6450_BODY_MASS_INDEX2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr6450_date_observation_measured2: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6450_DATE_OBSERVATION_MEASURED2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr2050_clinical_nurse_specialist_indication_code: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR2050_CLINICAL_NURSE_SPECIALIST_INDICATION_CODE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr7800_tobacco_smoking_status: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7800_TOBACCO_SMOKING_STATUS'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr7810_tobacco_smoking_cessation: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7810_TOBACCO_SMOKING_CESSATION'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr6760_history_of_alcohol_current: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6760_HISTORY_OF_ALCOHOL_CURRENT'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr6770_history_of_alcohol_past: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6770_HISTORY_OF_ALCOHOL_PAST'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr9070_diabetes_mellitus_type1_and_type2_indicator: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR9070_DIABETES_MELLITUS_TYPE1_AND_TYPE2_INDICATOR'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr7830_menopausal_status: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7830_MENOPAUSAL_STATUS'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr7840_physical_activity_current: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7840_PHYSICAL_ACTIVITY_CURRENT'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr7900_holistic_assessment_offered1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7900_HOLISTIC_ASSESSMENT_OFFERED1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr7920_hol_assessment_care_plan_status1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7920_HOL_ASSESSMENT_CARE_PLAN_STATUS1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr7930_hol_assessment_care_plan_date1: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7930_HOL_ASSESSMENT_CARE_PLAN_DATE1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr7940_hol_assessment_care_plan_point_of_pathway1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7940_HOL_ASSESSMENT_CARE_PLAN_POINT_OF_PATHWAY1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr7950_hol_staff_role_offering_the_assessment1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7950_HOL_STAFF_ROLE_OFFERING_THE_ASSESSMENT1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr7960_hol_staff_role_offering_the_planning1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7960_HOL_STAFF_ROLE_OFFERING_THE_PLANNING1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr7900_holistic_assessment_offered2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7900_HOLISTIC_ASSESSMENT_OFFERED2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr7920_hol_assessment_care_plan_status2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7920_HOL_ASSESSMENT_CARE_PLAN_STATUS2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr7930_hol_assessment_care_plan_date2: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7930_HOL_ASSESSMENT_CARE_PLAN_DATE2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr7940_hol_assessment_care_plan_point_of_pathway2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7940_HOL_ASSESSMENT_CARE_PLAN_POINT_OF_PATHWAY2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr7950_hol_staff_role_offering_the_assessment2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7950_HOL_STAFF_ROLE_OFFERING_THE_ASSESSMENT2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr7960_hol_staff_role_offering_the_planning2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR7960_HOL_STAFF_ROLE_OFFERING_THE_PLANNING2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr0430_mdt_discussion_date_cancer: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0430_MDT_DISCUSSION_DATE_CANCER'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr0460_cancer_care_plan_intent: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0460_CANCER_CARE_PLAN_INTENT'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr0470_planned_cancer_treatment_type1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0470_PLANNED_CANCER_TREATMENT_TYPE1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr0470_planned_cancer_treatment_type2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0470_PLANNED_CANCER_TREATMENT_TYPE2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr0470_planned_cancer_treatment_type3: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0470_PLANNED_CANCER_TREATMENT_TYPE3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr0490_no_cancer_treatment_reason: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0490_NO_CANCER_TREATMENT_REASON'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr0520_t_category_final_pretreatment: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR0520_T_CATEGORY_FINAL_PRETREATMENT'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(15)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr0540_n_category_final_pretreatment: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR0540_N_CATEGORY_FINAL_PRETREATMENT'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(15)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr0560_m_category_final_pretreatment: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR0560_M_CATEGORY_FINAL_PRETREATMENT'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(15)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr0580_tnm_stage_grouping_final_pretreatment: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR0580_TNM_STAGE_GROUPING_FINAL_PRETREATMENT'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(15)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6800_org_site_id_reported_pretreatment_tnm_stage: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6800_ORG_SITE_ID_REPORTED_PRETREATMENT_TNM_STAGE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(9)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr3120_stage_date_final_pretreatment_stage: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR3120_STAGE_DATE_FINAL_PRETREATMENT_STAGE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr0620_t_category_integrated_stage: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR0620_T_CATEGORY_INTEGRATED_STAGE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(15)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr0630_n_category_integrated_stage: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR0630_N_CATEGORY_INTEGRATED_STAGE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(15)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr0640_m_category_integrated_stage: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR0640_M_CATEGORY_INTEGRATED_STAGE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(15)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr0610_tnm_stage_grouping_integrated: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR0610_TNM_STAGE_GROUPING_INTEGRATED'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(15)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6810_org_site_id_reported_integrated_tnm_stage: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6810_ORG_SITE_ID_REPORTED_INTEGRATED_TNM_STAGE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(9)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr3130_stage_date_integrated_stage: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR3130_STAGE_DATE_INTEGRATED_STAGE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr6980_tnm_coding_edition: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR6980_TNM_CODING_EDITION'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr2070_tnm_version_number_staging: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR2070_TNM_VERSION_NUMBER_STAGING'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr8300_org_site_id_site_specific_stage1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR8300_ORG_SITE_ID_SITE_SPECIFIC_STAGE1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(9)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr8310_stage_date_site_specific_stage1: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR8310_STAGE_DATE_SITE_SPECIFIC_STAGE1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr8300_org_site_id_site_specific_stage2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR8300_ORG_SITE_ID_SITE_SPECIFIC_STAGE2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(9)'}},
         'domain_of': ['COSDResearchView']} })
    pp_cr8310_stage_date_site_specific_stage2: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PP_CR8310_STAGE_DATE_SITE_SPECIFIC_STAGE2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr6540_treat1_adjunctive_therapy: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6540_TREAT1_ADJUNCTIVE_THERAPY'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr0680_treat1_cancer_treatment_intent: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0680_TREAT1_CANCER_TREATMENT_INTENT'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr1370_treat1_treatment_start_date_cancer: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR1370_TREAT1_TREATMENT_START_DATE_CANCER'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr2040_treat1_cancer_treatment_modality_registration: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR2040_TREAT1_CANCER_TREATMENT_MODALITY_REGISTRATION'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr1450_treat1_org_site_id_of_provider_cancer_treatment_start_date: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR1450_TREAT1_ORG_SITE_ID_OF_PROVIDER_CANCER_TREATMENT_START_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(9)'}},
         'domain_of': ['COSDResearchView']} })
    cr8400_treat1_con_treat_prof_regissuer_code: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8400_TREAT1_CON_TREAT_PROF_REGISSUER_CODE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr8410_treat1_con_treat_prof_regentry_identifier: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8410_TREAT1_CON_TREAT_PROF_REGENTRY_IDENTIFIER'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(32)'}},
         'domain_of': ['COSDResearchView']} })
    cr8420_treat1_end_of_treatment_summary_date: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8420_TREAT1_END_OF_TREATMENT_SUMMARY_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr0740_treat1_discharge_date_hospital_provider_spell: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0740_TREAT1_DISCHARGE_DATE_HOSPITAL_PROVIDER_SPELL'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr9080_treat1_discharge_destination_hospital_provider_spell: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR9080_TREAT1_DISCHARGE_DESTINATION_HOSPITAL_PROVIDER_SPELL'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr0710_treat1_procedure_date: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0710_TREAT1_PROCEDURE_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr8500_treat1_surgical_admission_type: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8500_TREAT1_SURGICAL_ADMISSION_TYPE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr8510_treat1_prof_reg_issuer_code_cons_surgeon1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8510_TREAT1_PROF_REG_ISSUER_CODE_CONS_SURGEON1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr8520_treat1_prof_reg_entry_identifier_cons_surgeon1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8520_TREAT1_PROF_REG_ENTRY_IDENTIFIER_CONS_SURGEON1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(32)'}},
         'domain_of': ['COSDResearchView']} })
    cr8510_treat1_prof_reg_issuer_code_cons_surgeon2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8510_TREAT1_PROF_REG_ISSUER_CODE_CONS_SURGEON2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr8520_treat1_prof_reg_entry_identifier_cons_surgeon2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8520_TREAT1_PROF_REG_ENTRY_IDENTIFIER_CONS_SURGEON2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(32)'}},
         'domain_of': ['COSDResearchView']} })
    cr8510_treat1_prof_reg_issuer_code_cons_surgeon3: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8510_TREAT1_PROF_REG_ISSUER_CODE_CONS_SURGEON3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr8520_treat1_prof_reg_entry_identifier_cons_surgeon3: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8520_TREAT1_PROF_REG_ENTRY_IDENTIFIER_CONS_SURGEON3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(32)'}},
         'domain_of': ['COSDResearchView']} })
    cr0720_treat1_primary_procedure_opcs: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0720_TREAT1_PRIMARY_PROCEDURE_OPCS'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr3040_treat1_primary_procedure_snomed_ct: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3040_TREAT1_PRIMARY_PROCEDURE_SNOMED_CT'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr0730_treat1_procedure_opcs2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0730_TREAT1_PROCEDURE_OPCS2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr0730_treat1_procedure_opcs3: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0730_TREAT1_PROCEDURE_OPCS3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr0730_treat1_procedure_opcs4: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0730_TREAT1_PROCEDURE_OPCS4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr3050_treat1_procedure_snomed_ct2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3050_TREAT1_PROCEDURE_SNOMED_CT2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr3050_treat1_procedure_snomed_ct3: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3050_TREAT1_PROCEDURE_SNOMED_CT3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr3050_treat1_procedure_snomed_ct4: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3050_TREAT1_PROCEDURE_SNOMED_CT4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr6480_treat1_unplanned_return_to_theatre_indicator: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6480_TREAT1_UNPLANNED_RETURN_TO_THEATRE_INDICATOR'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr6010_treat1_asa_score: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6010_TREAT1_ASA_SCORE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr6310_treat1_surgery_surgical_access_type: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6310_TREAT1_SURGERY_SURGICAL_ACCESS_TYPE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr6540_treat2_adjunctive_therapy: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6540_TREAT2_ADJUNCTIVE_THERAPY'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr0680_treat2_cancer_treatment_intent: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0680_TREAT2_CANCER_TREATMENT_INTENT'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr1370_treat2_treatment_start_date_cancer: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR1370_TREAT2_TREATMENT_START_DATE_CANCER'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr2040_treat2_cancer_treatment_modality_registration: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR2040_TREAT2_CANCER_TREATMENT_MODALITY_REGISTRATION'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr1450_treat2_org_site_id_of_provider_cancer_treatment_start_date: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR1450_TREAT2_ORG_SITE_ID_OF_PROVIDER_CANCER_TREATMENT_START_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(9)'}},
         'domain_of': ['COSDResearchView']} })
    cr8400_treat2_con_treat_prof_regissuer_code: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8400_TREAT2_CON_TREAT_PROF_REGISSUER_CODE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr8410_treat2_con_treat_prof_regentry_identifier: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8410_TREAT2_CON_TREAT_PROF_REGENTRY_IDENTIFIER'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(32)'}},
         'domain_of': ['COSDResearchView']} })
    cr8420_treat2_end_of_treatment_summary_date: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8420_TREAT2_END_OF_TREATMENT_SUMMARY_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr0740_treat2_discharge_date_hospital_provider_spell: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0740_TREAT2_DISCHARGE_DATE_HOSPITAL_PROVIDER_SPELL'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr9080_treat2_discharge_destination_hospital_provider_spell: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR9080_TREAT2_DISCHARGE_DESTINATION_HOSPITAL_PROVIDER_SPELL'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr0710_treat2_procedure_date: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0710_TREAT2_PROCEDURE_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr8500_treat2_surgical_admission_type: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8500_TREAT2_SURGICAL_ADMISSION_TYPE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr8510_treat2_prof_reg_issuer_code_cons_surgeon1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8510_TREAT2_PROF_REG_ISSUER_CODE_CONS_SURGEON1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr8520_treat2_prof_reg_entry_identifier_cons_surgeon1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8520_TREAT2_PROF_REG_ENTRY_IDENTIFIER_CONS_SURGEON1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(32)'}},
         'domain_of': ['COSDResearchView']} })
    cr8510_treat2_prof_reg_issuer_code_cons_surgeon2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8510_TREAT2_PROF_REG_ISSUER_CODE_CONS_SURGEON2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr8520_treat2_prof_reg_entry_identifier_cons_surgeon2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8520_TREAT2_PROF_REG_ENTRY_IDENTIFIER_CONS_SURGEON2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(32)'}},
         'domain_of': ['COSDResearchView']} })
    cr8510_treat2_prof_reg_issuer_code_cons_surgeon3: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8510_TREAT2_PROF_REG_ISSUER_CODE_CONS_SURGEON3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr8520_treat2_prof_reg_entry_identifier_cons_surgeon3: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8520_TREAT2_PROF_REG_ENTRY_IDENTIFIER_CONS_SURGEON3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(32)'}},
         'domain_of': ['COSDResearchView']} })
    cr0720_treat2_primary_procedure_opcs: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0720_TREAT2_PRIMARY_PROCEDURE_OPCS'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr3040_treat2_primary_procedure_snomed_ct: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3040_TREAT2_PRIMARY_PROCEDURE_SNOMED_CT'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr0730_treat2_procedure_opcs2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0730_TREAT2_PROCEDURE_OPCS2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr0730_treat2_procedure_opcs3: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0730_TREAT2_PROCEDURE_OPCS3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr0730_treat2_procedure_opcs4: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0730_TREAT2_PROCEDURE_OPCS4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr3050_treat2_procedure_snomed_ct2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3050_TREAT2_PROCEDURE_SNOMED_CT2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr3050_treat2_procedure_snomed_ct3: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3050_TREAT2_PROCEDURE_SNOMED_CT3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr3050_treat2_procedure_snomed_ct4: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3050_TREAT2_PROCEDURE_SNOMED_CT4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr6480_treat2_unplanned_return_to_theatre_indicator: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6480_TREAT2_UNPLANNED_RETURN_TO_THEATRE_INDICATOR'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr6010_treat2_asa_score: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6010_TREAT2_ASA_SCORE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr6310_treat2_surgery_surgical_access_type: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6310_TREAT2_SURGERY_SURGICAL_ACCESS_TYPE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr6540_treat3_adjunctive_therapy: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6540_TREAT3_ADJUNCTIVE_THERAPY'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr0680_treat3_cancer_treatment_intent: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0680_TREAT3_CANCER_TREATMENT_INTENT'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr1370_treat3_treatment_start_date_cancer: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR1370_TREAT3_TREATMENT_START_DATE_CANCER'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr2040_treat3_cancer_treatment_modality_registration: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR2040_TREAT3_CANCER_TREATMENT_MODALITY_REGISTRATION'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr1450_treat3_org_site_id_of_provider_cancer_treatment_start_date: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR1450_TREAT3_ORG_SITE_ID_OF_PROVIDER_CANCER_TREATMENT_START_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(9)'}},
         'domain_of': ['COSDResearchView']} })
    cr8400_treat3_con_treat_prof_regissuer_code: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8400_TREAT3_CON_TREAT_PROF_REGISSUER_CODE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr8410_treat3_con_treat_prof_regentry_identifier: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8410_TREAT3_CON_TREAT_PROF_REGENTRY_IDENTIFIER'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(32)'}},
         'domain_of': ['COSDResearchView']} })
    cr8420_treat3_end_of_treatment_summary_date: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8420_TREAT3_END_OF_TREATMENT_SUMMARY_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr0740_treat3_discharge_date_hospital_provider_spell: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0740_TREAT3_DISCHARGE_DATE_HOSPITAL_PROVIDER_SPELL'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr9080_treat3_discharge_destination_hospital_provider_spell: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR9080_TREAT3_DISCHARGE_DESTINATION_HOSPITAL_PROVIDER_SPELL'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr0710_treat3_procedure_date: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0710_TREAT3_PROCEDURE_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr8500_treat3_surgical_admission_type: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8500_TREAT3_SURGICAL_ADMISSION_TYPE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr8510_treat3_prof_reg_issuer_code_cons_surgeon1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8510_TREAT3_PROF_REG_ISSUER_CODE_CONS_SURGEON1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr8520_treat3_prof_reg_entry_identifier_cons_surgeon1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8520_TREAT3_PROF_REG_ENTRY_IDENTIFIER_CONS_SURGEON1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(32)'}},
         'domain_of': ['COSDResearchView']} })
    cr8510_treat3_prof_reg_issuer_code_cons_surgeon2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8510_TREAT3_PROF_REG_ISSUER_CODE_CONS_SURGEON2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr8520_treat3_prof_reg_entry_identifier_cons_surgeon2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8520_TREAT3_PROF_REG_ENTRY_IDENTIFIER_CONS_SURGEON2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(32)'}},
         'domain_of': ['COSDResearchView']} })
    cr8510_treat3_prof_reg_issuer_code_cons_surgeon3: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8510_TREAT3_PROF_REG_ISSUER_CODE_CONS_SURGEON3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr8520_treat3_prof_reg_entry_identifier_cons_surgeon3: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8520_TREAT3_PROF_REG_ENTRY_IDENTIFIER_CONS_SURGEON3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(32)'}},
         'domain_of': ['COSDResearchView']} })
    cr0720_treat3_primary_procedure_opcs: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0720_TREAT3_PRIMARY_PROCEDURE_OPCS'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr3040_treat3_primary_procedure_snomed_ct: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3040_TREAT3_PRIMARY_PROCEDURE_SNOMED_CT'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr0730_treat3_procedure_opcs2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0730_TREAT3_PROCEDURE_OPCS2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr0730_treat3_procedure_opcs3: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0730_TREAT3_PROCEDURE_OPCS3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr0730_treat3_procedure_opcs4: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0730_TREAT3_PROCEDURE_OPCS4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr3050_treat3_procedure_snomed_ct2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3050_TREAT3_PROCEDURE_SNOMED_CT2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr3050_treat3_procedure_snomed_ct3: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3050_TREAT3_PROCEDURE_SNOMED_CT3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr3050_treat3_procedure_snomed_ct4: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3050_TREAT3_PROCEDURE_SNOMED_CT4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr6480_treat3_unplanned_return_to_theatre_indicator: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6480_TREAT3_UNPLANNED_RETURN_TO_THEATRE_INDICATOR'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr6010_treat3_asa_score: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6010_TREAT3_ASA_SCORE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr6310_treat3_surgery_surgical_access_type: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6310_TREAT3_SURGERY_SURGICAL_ACCESS_TYPE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr6540_treat4_adjunctive_therapy: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6540_TREAT4_ADJUNCTIVE_THERAPY'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr0680_treat4_cancer_treatment_intent: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0680_TREAT4_CANCER_TREATMENT_INTENT'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr1370_treat4_treatment_start_date_cancer: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR1370_TREAT4_TREATMENT_START_DATE_CANCER'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr2040_treat4_cancer_treatment_modality_registration: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR2040_TREAT4_CANCER_TREATMENT_MODALITY_REGISTRATION'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr1450_treat4_org_site_id_of_provider_cancer_treatment_start_date: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR1450_TREAT4_ORG_SITE_ID_OF_PROVIDER_CANCER_TREATMENT_START_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(9)'}},
         'domain_of': ['COSDResearchView']} })
    cr8400_treat4_con_treat_prof_regissuer_code: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8400_TREAT4_CON_TREAT_PROF_REGISSUER_CODE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr8410_treat4_con_treat_prof_regentry_identifier: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8410_TREAT4_CON_TREAT_PROF_REGENTRY_IDENTIFIER'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(32)'}},
         'domain_of': ['COSDResearchView']} })
    cr8420_treat4_end_of_treatment_summary_date: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8420_TREAT4_END_OF_TREATMENT_SUMMARY_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr0740_treat4_discharge_date_hospital_provider_spell: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0740_TREAT4_DISCHARGE_DATE_HOSPITAL_PROVIDER_SPELL'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr9080_treat4_discharge_destination_hospital_provider_spell: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR9080_TREAT4_DISCHARGE_DESTINATION_HOSPITAL_PROVIDER_SPELL'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr0710_treat4_procedure_date: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0710_TREAT4_PROCEDURE_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr8500_treat4_surgical_admission_type: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8500_TREAT4_SURGICAL_ADMISSION_TYPE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr8510_treat4_prof_reg_issuer_code_cons_surgeon1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8510_TREAT4_PROF_REG_ISSUER_CODE_CONS_SURGEON1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr8520_treat4_prof_reg_entry_identifier_cons_surgeon1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8520_TREAT4_PROF_REG_ENTRY_IDENTIFIER_CONS_SURGEON1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(32)'}},
         'domain_of': ['COSDResearchView']} })
    cr8510_treat4_prof_reg_issuer_code_cons_surgeon2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8510_TREAT4_PROF_REG_ISSUER_CODE_CONS_SURGEON2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr8520_treat4_prof_reg_entry_identifier_cons_surgeon2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8520_TREAT4_PROF_REG_ENTRY_IDENTIFIER_CONS_SURGEON2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(32)'}},
         'domain_of': ['COSDResearchView']} })
    cr8510_treat4_prof_reg_issuer_code_cons_surgeon3: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8510_TREAT4_PROF_REG_ISSUER_CODE_CONS_SURGEON3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr8520_treat4_prof_reg_entry_identifier_cons_surgeon3: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8520_TREAT4_PROF_REG_ENTRY_IDENTIFIER_CONS_SURGEON3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(32)'}},
         'domain_of': ['COSDResearchView']} })
    cr0720_treat4_primary_procedure_opcs: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0720_TREAT4_PRIMARY_PROCEDURE_OPCS'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr3040_treat4_primary_procedure_snomed_ct: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3040_TREAT4_PRIMARY_PROCEDURE_SNOMED_CT'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr0730_treat4_procedure_opcs2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0730_TREAT4_PROCEDURE_OPCS2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr0730_treat4_procedure_opcs3: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0730_TREAT4_PROCEDURE_OPCS3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr0730_treat4_procedure_opcs4: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0730_TREAT4_PROCEDURE_OPCS4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr3050_treat4_procedure_snomed_ct2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3050_TREAT4_PROCEDURE_SNOMED_CT2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr3050_treat4_procedure_snomed_ct3: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3050_TREAT4_PROCEDURE_SNOMED_CT3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr3050_treat4_procedure_snomed_ct4: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3050_TREAT4_PROCEDURE_SNOMED_CT4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(18)'}},
         'domain_of': ['COSDResearchView']} })
    cr6480_treat4_unplanned_return_to_theatre_indicator: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6480_TREAT4_UNPLANNED_RETURN_TO_THEATRE_INDICATOR'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr6010_treat4_asa_score: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6010_TREAT4_ASA_SCORE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr6310_treat4_surgery_surgical_access_type: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6310_TREAT4_SURGERY_SURGICAL_ACCESS_TYPE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr8700_ac1_acute_oncology_assessment_date: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8700_AC1_ACUTE_ONCOLOGY_ASSESSMENT_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr8710_ac1_organisation_site_identifier_acute_oncology: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8710_AC1_ORGANISATION_SITE_IDENTIFIER_ACUTE_ONCOLOGY'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(5)'}},
         'domain_of': ['COSDResearchView']} })
    cr8720_ac1_assessment_location: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8720_AC1_ASSESSMENT_LOCATION'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr8730_ac1_patient_type1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8730_AC1_PATIENT_TYPE1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr8730_ac1_patient_type2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8730_AC1_PATIENT_TYPE2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr8740_ac1_outcome: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8740_AC1_OUTCOME'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr8700_ac2_acute_oncology_assessment_date: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8700_AC2_ACUTE_ONCOLOGY_ASSESSMENT_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr8710_ac2_organisation_site_identifier_acute_oncology: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8710_AC2_ORGANISATION_SITE_IDENTIFIER_ACUTE_ONCOLOGY'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(5)'}},
         'domain_of': ['COSDResearchView']} })
    cr8720_ac2_assessment_location: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8720_AC2_ASSESSMENT_LOCATION'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr8730_ac2_patient_type1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8730_AC2_PATIENT_TYPE1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr8730_ac2_patient_type2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8730_AC2_PATIENT_TYPE2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr8740_ac2_outcome: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8740_AC2_OUTCOME'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr8700_ac3_acute_oncology_assessment_date: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8700_AC3_ACUTE_ONCOLOGY_ASSESSMENT_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr8710_ac3_organisation_site_identifier_acute_oncology: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8710_AC3_ORGANISATION_SITE_IDENTIFIER_ACUTE_ONCOLOGY'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(5)'}},
         'domain_of': ['COSDResearchView']} })
    cr8720_ac3_assessment_location: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8720_AC3_ASSESSMENT_LOCATION'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr8730_ac3_patient_type1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8730_AC3_PATIENT_TYPE1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr8730_ac3_patient_type2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8730_AC3_PATIENT_TYPE2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr8740_ac3_outcome: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8740_AC3_OUTCOME'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr8800_laboratory_result_date1: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8800_LABORATORY_RESULT_DATE1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr8810_organisation_identifier_laboratory_result1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8810_ORGANISATION_IDENTIFIER_LABORATORY_RESULT1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(5)'}},
         'domain_of': ['COSDResearchView']} })
    cr8900_ldh_value1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8900_LDH_VALUE1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(6)'}},
         'domain_of': ['COSDResearchView']} })
    cr8910_beta_human_chorionic_gonadotropin_serum1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8910_BETA_HUMAN_CHORIONIC_GONADOTROPIN_SERUM1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(8)'}},
         'domain_of': ['COSDResearchView']} })
    cr8920_alpha_fetoprotein_serum1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8920_ALPHA_FETOPROTEIN_SERUM1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(8)'}},
         'domain_of': ['COSDResearchView']} })
    cr8800_laboratory_result_date2: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8800_LABORATORY_RESULT_DATE2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr8810_organisation_identifier_laboratory_result2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8810_ORGANISATION_IDENTIFIER_LABORATORY_RESULT2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(5)'}},
         'domain_of': ['COSDResearchView']} })
    cr8900_ldh_value2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8900_LDH_VALUE2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(6)'}},
         'domain_of': ['COSDResearchView']} })
    cr8910_beta_human_chorionic_gonadotropin_serum2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8910_BETA_HUMAN_CHORIONIC_GONADOTROPIN_SERUM2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(8)'}},
         'domain_of': ['COSDResearchView']} })
    cr8920_alpha_fetoprotein_serum2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8920_ALPHA_FETOPROTEIN_SERUM2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(8)'}},
         'domain_of': ['COSDResearchView']} })
    cr8800_laboratory_result_date3: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8800_LABORATORY_RESULT_DATE3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['COSDResearchView']} })
    cr8810_organisation_identifier_laboratory_result3: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8810_ORGANISATION_IDENTIFIER_LABORATORY_RESULT3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(5)'}},
         'domain_of': ['COSDResearchView']} })
    cr8900_ldh_value3: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8900_LDH_VALUE3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(6)'}},
         'domain_of': ['COSDResearchView']} })
    cr8910_beta_human_chorionic_gonadotropin_serum3: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8910_BETA_HUMAN_CHORIONIC_GONADOTROPIN_SERUM3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(8)'}},
         'domain_of': ['COSDResearchView']} })
    cr8920_alpha_fetoprotein_serum3: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8920_ALPHA_FETOPROTEIN_SERUM3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(8)'}},
         'domain_of': ['COSDResearchView']} })
    cr0310_org_site_id_of_imaging1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0310_ORG_SITE_ID_OF_IMAGING1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(9)'}},
         'domain_of': ['COSDResearchView']} })
    cr0320_procedure_date_cancer_imaging1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0320_PROCEDURE_DATE_CANCER_IMAGING1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(10)'}},
         'domain_of': ['COSDResearchView']} })
    cr6780_imaging_outcome1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6780_IMAGING_OUTCOME1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr1610_imaging_code_nicip1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR1610_IMAGING_CODE_NICIP1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(6)'}},
         'domain_of': ['COSDResearchView']} })
    cr3110_imaging_code_snowmed_ct1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3110_IMAGING_CODE_SNOWMED_CT1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(19)'}},
         'domain_of': ['COSDResearchView']} })
    cr0330_cancer_imaging_modality1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0330_CANCER_IMAGING_MODALITY1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr0340_imaging_anatomical_site1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0340_IMAGING_ANATOMICAL_SITE1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(5)'}},
         'domain_of': ['COSDResearchView']} })
    cr3000_anatomical_side_imaging1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3000_ANATOMICAL_SIDE_IMAGING1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr0160_imaging_report_text1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0160_IMAGING_REPORT_TEXT1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(MAX)'}},
         'domain_of': ['COSDResearchView']} })
    cr0310_org_site_id_of_imaging2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0310_ORG_SITE_ID_OF_IMAGING2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(9)'}},
         'domain_of': ['COSDResearchView']} })
    cr0320_procedure_date_cancer_imaging2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0320_PROCEDURE_DATE_CANCER_IMAGING2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(10)'}},
         'domain_of': ['COSDResearchView']} })
    cr6780_imaging_outcome2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6780_IMAGING_OUTCOME2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr1610_imaging_code_nicip2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR1610_IMAGING_CODE_NICIP2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(6)'}},
         'domain_of': ['COSDResearchView']} })
    cr3110_imaging_code_snowmed_ct2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3110_IMAGING_CODE_SNOWMED_CT2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(19)'}},
         'domain_of': ['COSDResearchView']} })
    cr0330_cancer_imaging_modality2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0330_CANCER_IMAGING_MODALITY2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr0340_imaging_anatomical_site2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0340_IMAGING_ANATOMICAL_SITE2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(5)'}},
         'domain_of': ['COSDResearchView']} })
    cr3000_anatomical_side_imaging2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3000_ANATOMICAL_SIDE_IMAGING2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr0160_imaging_report_text2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0160_IMAGING_REPORT_TEXT2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(MAX)'}},
         'domain_of': ['COSDResearchView']} })
    cr0310_org_site_id_of_imaging3: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0310_ORG_SITE_ID_OF_IMAGING3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(9)'}},
         'domain_of': ['COSDResearchView']} })
    cr0320_procedure_date_cancer_imaging3: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0320_PROCEDURE_DATE_CANCER_IMAGING3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(10)'}},
         'domain_of': ['COSDResearchView']} })
    cr6780_imaging_outcome3: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6780_IMAGING_OUTCOME3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr1610_imaging_code_nicip3: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR1610_IMAGING_CODE_NICIP3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(6)'}},
         'domain_of': ['COSDResearchView']} })
    cr3110_imaging_code_snowmed_ct3: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3110_IMAGING_CODE_SNOWMED_CT3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(19)'}},
         'domain_of': ['COSDResearchView']} })
    cr0330_cancer_imaging_modality3: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0330_CANCER_IMAGING_MODALITY3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr0340_imaging_anatomical_site3: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0340_IMAGING_ANATOMICAL_SITE3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(5)'}},
         'domain_of': ['COSDResearchView']} })
    cr3000_anatomical_side_imaging3: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3000_ANATOMICAL_SIDE_IMAGING3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr0160_imaging_report_text3: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0160_IMAGING_REPORT_TEXT3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(MAX)'}},
         'domain_of': ['COSDResearchView']} })
    cr0310_org_site_id_of_imaging4: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0310_ORG_SITE_ID_OF_IMAGING4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(9)'}},
         'domain_of': ['COSDResearchView']} })
    cr0320_procedure_date_cancer_imaging4: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0320_PROCEDURE_DATE_CANCER_IMAGING4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(10)'}},
         'domain_of': ['COSDResearchView']} })
    cr6780_imaging_outcome4: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6780_IMAGING_OUTCOME4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr1610_imaging_code_nicip4: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR1610_IMAGING_CODE_NICIP4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(6)'}},
         'domain_of': ['COSDResearchView']} })
    cr3110_imaging_code_snowmed_ct4: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3110_IMAGING_CODE_SNOWMED_CT4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(19)'}},
         'domain_of': ['COSDResearchView']} })
    cr0330_cancer_imaging_modality4: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0330_CANCER_IMAGING_MODALITY4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr0340_imaging_anatomical_site4: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0340_IMAGING_ANATOMICAL_SITE4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(5)'}},
         'domain_of': ['COSDResearchView']} })
    cr3000_anatomical_side_imaging4: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3000_ANATOMICAL_SIDE_IMAGING4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr0160_imaging_report_text4: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0160_IMAGING_REPORT_TEXT4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(MAX)'}},
         'domain_of': ['COSDResearchView']} })
    cr0310_org_site_id_of_imaging5: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0310_ORG_SITE_ID_OF_IMAGING5'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(9)'}},
         'domain_of': ['COSDResearchView']} })
    cr0320_procedure_date_cancer_imaging5: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0320_PROCEDURE_DATE_CANCER_IMAGING5'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(10)'}},
         'domain_of': ['COSDResearchView']} })
    cr6780_imaging_outcome5: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6780_IMAGING_OUTCOME5'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr1610_imaging_code_nicip5: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR1610_IMAGING_CODE_NICIP5'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(6)'}},
         'domain_of': ['COSDResearchView']} })
    cr3110_imaging_code_snowmed_ct5: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3110_IMAGING_CODE_SNOWMED_CT5'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(19)'}},
         'domain_of': ['COSDResearchView']} })
    cr0330_cancer_imaging_modality5: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0330_CANCER_IMAGING_MODALITY5'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr0340_imaging_anatomical_site5: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0340_IMAGING_ANATOMICAL_SITE5'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(5)'}},
         'domain_of': ['COSDResearchView']} })
    cr3000_anatomical_side_imaging5: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3000_ANATOMICAL_SIDE_IMAGING5'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr0160_imaging_report_text5: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0160_IMAGING_REPORT_TEXT5'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(MAX)'}},
         'domain_of': ['COSDResearchView']} })
    cr0310_org_site_id_of_imaging6: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0310_ORG_SITE_ID_OF_IMAGING6'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(9)'}},
         'domain_of': ['COSDResearchView']} })
    cr0320_procedure_date_cancer_imaging6: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0320_PROCEDURE_DATE_CANCER_IMAGING6'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(10)'}},
         'domain_of': ['COSDResearchView']} })
    cr6780_imaging_outcome6: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6780_IMAGING_OUTCOME6'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr1610_imaging_code_nicip6: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR1610_IMAGING_CODE_NICIP6'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(6)'}},
         'domain_of': ['COSDResearchView']} })
    cr3110_imaging_code_snowmed_ct6: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3110_IMAGING_CODE_SNOWMED_CT6'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(19)'}},
         'domain_of': ['COSDResearchView']} })
    cr0330_cancer_imaging_modality6: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0330_CANCER_IMAGING_MODALITY6'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr0340_imaging_anatomical_site6: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0340_IMAGING_ANATOMICAL_SITE6'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(5)'}},
         'domain_of': ['COSDResearchView']} })
    cr3000_anatomical_side_imaging6: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3000_ANATOMICAL_SIDE_IMAGING6'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr0160_imaging_report_text6: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0160_IMAGING_REPORT_TEXT6'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(MAX)'}},
         'domain_of': ['COSDResearchView']} })
    cr0310_org_site_id_of_imaging7: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0310_ORG_SITE_ID_OF_IMAGING7'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(9)'}},
         'domain_of': ['COSDResearchView']} })
    cr0320_procedure_date_cancer_imaging7: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0320_PROCEDURE_DATE_CANCER_IMAGING7'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(10)'}},
         'domain_of': ['COSDResearchView']} })
    cr6780_imaging_outcome7: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6780_IMAGING_OUTCOME7'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr1610_imaging_code_nicip7: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR1610_IMAGING_CODE_NICIP7'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(6)'}},
         'domain_of': ['COSDResearchView']} })
    cr3110_imaging_code_snowmed_ct7: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3110_IMAGING_CODE_SNOWMED_CT7'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(19)'}},
         'domain_of': ['COSDResearchView']} })
    cr0330_cancer_imaging_modality7: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0330_CANCER_IMAGING_MODALITY7'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr0340_imaging_anatomical_site7: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0340_IMAGING_ANATOMICAL_SITE7'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(5)'}},
         'domain_of': ['COSDResearchView']} })
    cr3000_anatomical_side_imaging7: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3000_ANATOMICAL_SIDE_IMAGING7'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr0160_imaging_report_text7: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0160_IMAGING_REPORT_TEXT7'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(MAX)'}},
         'domain_of': ['COSDResearchView']} })
    cr0310_org_site_id_of_imaging8: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0310_ORG_SITE_ID_OF_IMAGING8'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(9)'}},
         'domain_of': ['COSDResearchView']} })
    cr0320_procedure_date_cancer_imaging8: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0320_PROCEDURE_DATE_CANCER_IMAGING8'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(10)'}},
         'domain_of': ['COSDResearchView']} })
    cr6780_imaging_outcome8: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6780_IMAGING_OUTCOME8'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr1610_imaging_code_nicip8: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR1610_IMAGING_CODE_NICIP8'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(6)'}},
         'domain_of': ['COSDResearchView']} })
    cr3110_imaging_code_snowmed_ct8: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3110_IMAGING_CODE_SNOWMED_CT8'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(19)'}},
         'domain_of': ['COSDResearchView']} })
    cr0330_cancer_imaging_modality8: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0330_CANCER_IMAGING_MODALITY8'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr0340_imaging_anatomical_site8: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0340_IMAGING_ANATOMICAL_SITE8'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(5)'}},
         'domain_of': ['COSDResearchView']} })
    cr3000_anatomical_side_imaging8: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3000_ANATOMICAL_SIDE_IMAGING8'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr0160_imaging_report_text8: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0160_IMAGING_REPORT_TEXT8'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(MAX)'}},
         'domain_of': ['COSDResearchView']} })
    cr0310_org_site_id_of_imaging9: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0310_ORG_SITE_ID_OF_IMAGING9'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(9)'}},
         'domain_of': ['COSDResearchView']} })
    cr0320_procedure_date_cancer_imaging9: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0320_PROCEDURE_DATE_CANCER_IMAGING9'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(10)'}},
         'domain_of': ['COSDResearchView']} })
    cr6780_imaging_outcome9: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6780_IMAGING_OUTCOME9'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr1610_imaging_code_nicip9: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR1610_IMAGING_CODE_NICIP9'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(6)'}},
         'domain_of': ['COSDResearchView']} })
    cr3110_imaging_code_snowmed_ct9: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3110_IMAGING_CODE_SNOWMED_CT9'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(19)'}},
         'domain_of': ['COSDResearchView']} })
    cr0330_cancer_imaging_modality9: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0330_CANCER_IMAGING_MODALITY9'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr0340_imaging_anatomical_site9: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0340_IMAGING_ANATOMICAL_SITE9'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(5)'}},
         'domain_of': ['COSDResearchView']} })
    cr3000_anatomical_side_imaging9: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3000_ANATOMICAL_SIDE_IMAGING9'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr0160_imaging_report_text9: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0160_IMAGING_REPORT_TEXT9'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(MAX)'}},
         'domain_of': ['COSDResearchView']} })
    cr0310_org_site_id_of_imaging10: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0310_ORG_SITE_ID_OF_IMAGING10'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(9)'}},
         'domain_of': ['COSDResearchView']} })
    cr0320_procedure_date_cancer_imaging10: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0320_PROCEDURE_DATE_CANCER_IMAGING10'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(10)'}},
         'domain_of': ['COSDResearchView']} })
    cr6780_imaging_outcome10: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR6780_IMAGING_OUTCOME10'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(2)'}},
         'domain_of': ['COSDResearchView']} })
    cr1610_imaging_code_nicip10: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR1610_IMAGING_CODE_NICIP10'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(6)'}},
         'domain_of': ['COSDResearchView']} })
    cr3110_imaging_code_snowmed_ct10: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3110_IMAGING_CODE_SNOWMED_CT10'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(19)'}},
         'domain_of': ['COSDResearchView']} })
    cr0330_cancer_imaging_modality10: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0330_CANCER_IMAGING_MODALITY10'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(4)'}},
         'domain_of': ['COSDResearchView']} })
    cr0340_imaging_anatomical_site10: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0340_IMAGING_ANATOMICAL_SITE10'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(5)'}},
         'domain_of': ['COSDResearchView']} })
    cr3000_anatomical_side_imaging10: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3000_ANATOMICAL_SIDE_IMAGING10'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(1)'}},
         'domain_of': ['COSDResearchView']} })
    cr0160_imaging_report_text10: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR0160_IMAGING_REPORT_TEXT10'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(MAX)'}},
         'domain_of': ['COSDResearchView']} })
    cr8100_mdt_discussion1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8100_MDT_DISCUSSION1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr8110_mdt_discussion_type1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8110_MDT_DISCUSSION_TYPE1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3080_mdt_date1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3080_MDT_DATE1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3090_mdt_organisation_site_id1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3090_MDT_ORGANISATION_SITE_ID1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3190_mdt_type1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3190_MDT_TYPE1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3160_mdt_type_comment1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3160_MDT_TYPE_COMMENT1'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(60)'}},
         'domain_of': ['COSDResearchView']} })
    cr8100_mdt_discussion2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8100_MDT_DISCUSSION2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr8110_mdt_discussion_type2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8110_MDT_DISCUSSION_TYPE2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3080_mdt_date2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3080_MDT_DATE2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3090_mdt_organisation_site_id2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3090_MDT_ORGANISATION_SITE_ID2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3190_mdt_type2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3190_MDT_TYPE2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3160_mdt_type_comment2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3160_MDT_TYPE_COMMENT2'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(60)'}},
         'domain_of': ['COSDResearchView']} })
    cr8100_mdt_discussion3: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8100_MDT_DISCUSSION3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr8110_mdt_discussion_type3: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8110_MDT_DISCUSSION_TYPE3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3080_mdt_date3: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3080_MDT_DATE3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3090_mdt_organisation_site_id3: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3090_MDT_ORGANISATION_SITE_ID3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3190_mdt_type3: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3190_MDT_TYPE3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3160_mdt_type_comment3: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3160_MDT_TYPE_COMMENT3'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(60)'}},
         'domain_of': ['COSDResearchView']} })
    cr8100_mdt_discussion4: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8100_MDT_DISCUSSION4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr8110_mdt_discussion_type4: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8110_MDT_DISCUSSION_TYPE4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3080_mdt_date4: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3080_MDT_DATE4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3090_mdt_organisation_site_id4: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3090_MDT_ORGANISATION_SITE_ID4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3190_mdt_type4: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3190_MDT_TYPE4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3160_mdt_type_comment4: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3160_MDT_TYPE_COMMENT4'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(60)'}},
         'domain_of': ['COSDResearchView']} })
    cr8100_mdt_discussion5: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8100_MDT_DISCUSSION5'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr8110_mdt_discussion_type5: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8110_MDT_DISCUSSION_TYPE5'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3080_mdt_date5: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3080_MDT_DATE5'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3090_mdt_organisation_site_id5: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3090_MDT_ORGANISATION_SITE_ID5'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3190_mdt_type5: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3190_MDT_TYPE5'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3160_mdt_type_comment5: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3160_MDT_TYPE_COMMENT5'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(60)'}},
         'domain_of': ['COSDResearchView']} })
    cr8100_mdt_discussion6: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8100_MDT_DISCUSSION6'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr8110_mdt_discussion_type6: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8110_MDT_DISCUSSION_TYPE6'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3080_mdt_date6: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3080_MDT_DATE6'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3090_mdt_organisation_site_id6: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3090_MDT_ORGANISATION_SITE_ID6'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3190_mdt_type6: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3190_MDT_TYPE6'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3160_mdt_type_comment6: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3160_MDT_TYPE_COMMENT6'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(60)'}},
         'domain_of': ['COSDResearchView']} })
    cr8100_mdt_discussion7: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8100_MDT_DISCUSSION7'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr8110_mdt_discussion_type7: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8110_MDT_DISCUSSION_TYPE7'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3080_mdt_date7: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3080_MDT_DATE7'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3090_mdt_organisation_site_id7: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3090_MDT_ORGANISATION_SITE_ID7'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3190_mdt_type7: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3190_MDT_TYPE7'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3160_mdt_type_comment7: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3160_MDT_TYPE_COMMENT7'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(60)'}},
         'domain_of': ['COSDResearchView']} })
    cr8100_mdt_discussion8: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8100_MDT_DISCUSSION8'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr8110_mdt_discussion_type8: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8110_MDT_DISCUSSION_TYPE8'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3080_mdt_date8: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3080_MDT_DATE8'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3090_mdt_organisation_site_id8: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3090_MDT_ORGANISATION_SITE_ID8'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3190_mdt_type8: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3190_MDT_TYPE8'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3160_mdt_type_comment8: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3160_MDT_TYPE_COMMENT8'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(60)'}},
         'domain_of': ['COSDResearchView']} })
    cr8100_mdt_discussion9: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8100_MDT_DISCUSSION9'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr8110_mdt_discussion_type9: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8110_MDT_DISCUSSION_TYPE9'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3080_mdt_date9: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3080_MDT_DATE9'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3090_mdt_organisation_site_id9: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3090_MDT_ORGANISATION_SITE_ID9'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3190_mdt_type9: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3190_MDT_TYPE9'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3160_mdt_type_comment9: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3160_MDT_TYPE_COMMENT9'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(60)'}},
         'domain_of': ['COSDResearchView']} })
    cr8100_mdt_discussion10: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8100_MDT_DISCUSSION10'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr8110_mdt_discussion_type10: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR8110_MDT_DISCUSSION_TYPE10'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3080_mdt_date10: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3080_MDT_DATE10'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3090_mdt_organisation_site_id10: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3090_MDT_ORGANISATION_SITE_ID10'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3190_mdt_type10: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3190_MDT_TYPE10'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(20)'}},
         'domain_of': ['COSDResearchView']} })
    cr3160_mdt_type_comment10: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CR3160_MDT_TYPE_COMMENT10'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARCHAR(60)'}},
         'domain_of': ['COSDResearchView']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
COSDResearchView.model_rebuild()
