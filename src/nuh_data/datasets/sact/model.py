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
version = "0.0.1"


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
    pseudo_nhs_number: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sensitivity': {'tag': 'sensitivity',
                                         'value': 'pseudonymised'},
                         'sql_column': {'tag': 'sql_column',
                                        'value': 'PSEUDO_NHS_NUMBER'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARBINARY(100)'}},
         'domain_of': ['SACTResearchView']} })
    nhs_number_status: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'NHS_NUMBER_STATUS'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(4)'}},
         'domain_of': ['SACTResearchView']} })
    date_of_birth_year: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'DATE_OF_BIRTH_YEAR'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(8)'}},
         'domain_of': ['SACTResearchView']} })
    date_of_birth_month: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'DATE_OF_BIRTH_MONTH'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(4)'}},
         'domain_of': ['SACTResearchView']} })
    date_of_birth_mid_month: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'DATE_OF_BIRTH_MID_MONTH'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['SACTResearchView']} })
    person_stated_gender_code: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PERSON_STATED_GENDER_CODE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(2)'}},
         'domain_of': ['SACTResearchView']} })
    llsoa: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column', 'value': 'LLSOA'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(18)'}},
         'domain_of': ['SACTResearchView']} })
    consultant_gmc_code: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CONSULTANT_GMC_CODE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(16)'}},
         'domain_of': ['SACTResearchView']} })
    consultant_spec_code: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CONSULTANT_SPEC_CODE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(16)'}},
         'domain_of': ['SACTResearchView']} })
    org_id_code_provider: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'ORG_ID_CODE_PROVIDER'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(10)'}},
         'domain_of': ['SACTResearchView']} })
    primary_diagnosis: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PRIMARY_DIAGNOSIS'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(12)'}},
         'domain_of': ['SACTResearchView']} })
    morphology_icd_o: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'MORPHOLOGY_ICD_O'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(14)'}},
         'domain_of': ['SACTResearchView']} })
    diagnosis_code_snomed: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'DIAGNOSIS_CODE_SNOMED'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(36)'}},
         'domain_of': ['SACTResearchView']} })
    adjunctive_therapy: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'ADJUNCTIVE_THERAPY'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(2)'}},
         'domain_of': ['SACTResearchView']} })
    intent_of_treatment: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'INTENT_OF_TREATMENT'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(4)'}},
         'domain_of': ['SACTResearchView']} })
    regimen: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column', 'value': 'REGIMEN'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(300)'}},
         'domain_of': ['SACTResearchView']} })
    height_start_reg: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'HEIGHT_START_REG'},
                         'sql_type': {'tag': 'sql_type', 'value': 'FLOAT'}},
         'domain_of': ['SACTResearchView'],
         'unit': {'ucum_code': 'cm'}} })
    weight_start_of_reg: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'WEIGHT_START_OF_REG'},
                         'sql_type': {'tag': 'sql_type', 'value': 'FLOAT'}},
         'domain_of': ['SACTResearchView'],
         'unit': {'ucum_code': 'kg'}} })
    perf_status_start_reg_ad: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PERF_STATUS_START_REG_AD'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(2)'}},
         'domain_of': ['SACTResearchView']} })
    co_morbidity_adjustment: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CO_MORBIDITY_ADJUSTMENT'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(2)'}},
         'domain_of': ['SACTResearchView']} })
    date_decision_to_treat: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'DATE_DECISION_TO_TREAT'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['SACTResearchView']} })
    start_date_regimen: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'START_DATE_REGIMEN'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['SACTResearchView']} })
    clinical_trial: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column', 'value': 'CLINICAL_TRIAL'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(4)'}},
         'domain_of': ['SACTResearchView']} })
    cycle_number: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column', 'value': 'CYCLE_NUMBER'},
                         'sql_type': {'tag': 'sql_type', 'value': 'INT'}},
         'domain_of': ['SACTResearchView']} })
    start_date_cycle: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'START_DATE_CYCLE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['SACTResearchView']} })
    weight_start_cycle: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'WEIGHT_START_CYCLE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'FLOAT'}},
         'domain_of': ['SACTResearchView'],
         'unit': {'ucum_code': 'kg'}} })
    perf_stat_start_cycle_ad: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'PERF_STAT_START_CYCLE_AD'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(2)'}},
         'domain_of': ['SACTResearchView']} })
    drug_name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column', 'value': 'DRUG_NAME'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(110)'}},
         'domain_of': ['SACTResearchView']} })
    dm_d: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column', 'value': 'DM_D'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(36)'},
                         'vocabulary': {'tag': 'vocabulary',
                                        'value': 'NHS Dictionary of Medicines and '
                                                 'Devices (dm+d)'}},
         'domain_of': ['SACTResearchView']} })
    actual_dose_per_admin: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'ACTUAL_DOSE_PER_ADMIN'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(100)'}},
         'domain_of': ['SACTResearchView']} })
    admin_meas_per_actual_dose: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'ADMIN_MEAS_PER_ACTUAL_DOSE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(16)'}},
         'domain_of': ['SACTResearchView']} })
    ot_admin_meas_per_actual_dose: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'OT_ADMIN_MEAS_PER_ACTUAL_DOSE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(30)'}},
         'domain_of': ['SACTResearchView']} })
    unit_meas_snomed_ct_dm_d: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'UNIT_MEAS_SNOMED_CT_DM_D'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(36)'},
                         'vocabulary': {'tag': 'vocabulary',
                                        'value': 'SNOMED CT / dm+d'}},
         'domain_of': ['SACTResearchView']} })
    sact_administration_route: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'SACT_ADMINISTRATION_ROUTE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(4)'}},
         'domain_of': ['SACTResearchView']} })
    route_admin_snomed_ct_dm_d: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'ROUTE_ADMIN_SNOMED_CT_DM_D'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(36)'},
                         'vocabulary': {'tag': 'vocabulary',
                                        'value': 'SNOMED CT / dm+d'}},
         'domain_of': ['SACTResearchView']} })
    administration_date: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'ADMINISTRATION_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['SACTResearchView']} })
    org_identifier_sact_admin: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'ORG_IDENTIFIER_SACT_ADMIN'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(10)'}},
         'domain_of': ['SACTResearchView']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
SACTResearchView.model_rebuild()
