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
                     'data_standards': {'tag': 'data_standards', 'value': 'OTHER'},
                     'geographic_coverage': {'tag': 'geographic_coverage',
                                             'value': 'Nottinghamshire, England'}},
     'created_by': 'https://github.com/Health-Informatics-UoN',
     'default_prefix': 'demographics',
     'default_range': 'string',
     'description': 'demographics',
     'id': 'https://health-informatics-uon.github.io/nuh-data/datasets/demographics',
     'imports': ['linkml:types'],
     'keywords': ['NHS', 'Nottingham', 'clinical'],
     'license': 'demographics',
     'name': 'demographics',
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
                  'dmd': {'prefix_prefix': 'dmd',
                          'prefix_reference': 'https://dmd.nhs.uk/concept/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'}},
     'source_file': 'schemas/datasets/demographics/demographics.yaml',
     'title': 'demographics'} )


class Demographics(ConfiguredBaseModel):
    """
    demographics
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://health-informatics-uon.github.io/nuh-data/datasets/demographics',
         'tree_root': True})

    etl_id: Optional[int] = Field(default=None, description="""Internal identifier for the ETL batch run that loaded this record.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column', 'value': 'ETL_ID'},
                         'sql_type': {'tag': 'sql_type', 'value': 'INT'}},
         'domain_of': ['Demographics']} })
    etl_date: Optional[datetime ] = Field(default=None, description="""Date and time the ETL process ran.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column', 'value': 'ETL_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATETIME'}},
         'domain_of': ['Demographics']} })
    core_pid_published_runid: Optional[int] = Field(default=None, description="""TBA""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'CORE_PID_PUBLISHED_RUNID'},
                         'sql_type': {'tag': 'sql_type', 'value': 'INT'}},
         'domain_of': ['Demographics']} })
    ndo_run_date: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column', 'value': 'NDO_RUN_DATE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['Demographics']} })
    pseudo_nhs_number: Optional[str] = Field(default=None, description="""The NHS NUMBER, the primary identifier of a PERSON, is a unique identifier for a PATIENT within the NHS in England and Wales. Pseudonymised for research use.""", json_schema_extra = { "linkml_meta": {'annotations': {'sensitivity': {'tag': 'sensitivity',
                                         'value': 'pseudonymised'},
                         'sql_column': {'tag': 'sql_column',
                                        'value': 'PSEUDO_NHS_NUMBER'},
                         'sql_type': {'tag': 'sql_type', 'value': 'VARBINARY(100)'}},
         'domain_of': ['Demographics']} })
    dob_mid_month: Optional[date] = Field(default=None, description="""Mid-month proxy date of birth, derived as the 15th of the patient's birth month.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column', 'value': 'DOB_MID_MONTH'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['Demographics']} })
    deceased: Optional[int] = Field(default=None, description="""TBA""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column', 'value': 'DECEASED'},
                         'sql_type': {'tag': 'sql_type', 'value': 'INT'}},
         'domain_of': ['Demographics']} })
    date_of_death: Optional[date] = Field(default=None, description="""(TBA) The date of the participant's death""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column', 'value': 'DATE_OF_DEATH'},
                         'sql_type': {'tag': 'sql_type', 'value': 'DATE'}},
         'domain_of': ['Demographics']} })
    sex_code: Optional[str] = Field(default=None, description="""TBA""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column', 'value': 'SEX_CODE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(12)'}},
         'domain_of': ['Demographics']} })
    sex: Optional[str] = Field(default=None, description="""TBA""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column', 'value': 'SEX'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(128)'}},
         'domain_of': ['Demographics']} })
    gender_identity_code: Optional[str] = Field(default=None, description="""TBA""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'GENDER_IDENTITY_CODE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(12)'}},
         'domain_of': ['Demographics']} })
    gender_identity: Optional[str] = Field(default=None, description="""TBA""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'GENDER_IDENTITY'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(128)'}},
         'domain_of': ['Demographics']} })
    admin_gender: Optional[str] = Field(default=None, description="""TBA""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column', 'value': 'ADMIN_GENDER'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(128)'}},
         'domain_of': ['Demographics']} })
    ethnicity_code: Optional[str] = Field(default=None, description="""TBA""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column', 'value': 'ETHNICITY_CODE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(12)'}},
         'domain_of': ['Demographics']} })
    ethnicity: Optional[str] = Field(default=None, description="""TBA""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column', 'value': 'ETHNICITY'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(128)'}},
         'domain_of': ['Demographics']} })
    marital_status_code: Optional[str] = Field(default=None, description="""TBA""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column',
                                        'value': 'MARITAL_STATUS_CODE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(12)'}},
         'domain_of': ['Demographics']} })
    marital_status: Optional[str] = Field(default=None, description="""TBA""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column', 'value': 'MARITAL_STATUS'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(128)'}},
         'domain_of': ['Demographics']} })
    religion_code: Optional[str] = Field(default=None, description="""TBA""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column', 'value': 'RELIGION_CODE'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(12)'}},
         'domain_of': ['Demographics']} })
    religion: Optional[str] = Field(default=None, description="""TBA""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column', 'value': 'RELIGION'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(128)'}},
         'domain_of': ['Demographics']} })
    nationality: Optional[str] = Field(default=None, description="""TBA""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column', 'value': 'NATIONALITY'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(100)'}},
         'domain_of': ['Demographics']} })
    llsoa: Optional[str] = Field(default=None, description="""Lower Layer Super Output Area, derived from PATIENT POSTCODE for geographic analysis while preserving patient privacy.""", json_schema_extra = { "linkml_meta": {'annotations': {'sql_column': {'tag': 'sql_column', 'value': 'LLSOA'},
                         'sql_type': {'tag': 'sql_type', 'value': 'NVARCHAR(200)'}},
         'domain_of': ['Demographics']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Demographics.model_rebuild()
