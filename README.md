# NUH Research Metadata

[![MIT License][license-badge]][carrot-mapper-repo]
[![Repo][github-badge]][carrot-mapper-repo]
[![Releases][releases-badge]][releases]
![Python][python-badge]
[![Docs][docs-badge]][docs]

Data dictionaries, schema definitions, and metadata for research datasets from **Nottingham University Hospitals NHS Trust (NUH)**, one of the largest acute NHS trusts in England, serving a population of approximately 2.5 million across Nottinghamshire and surrounding counties.

This repository describes the **structure and content** of each dataset — field names, types, permitted values, and coding standards. All datasets are pseudonymised research views; access to the data requires a formal data access request.

Full documentation is at **[health-informatics-uon.github.io/nuh-data](https://health-informatics-uon.github.io/nuh-data)**.

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


[repo]: https://github.com/Health-Informatics-UoN/nuh-data
[docs]: https://health-informatics-uon.github.io/nuh-data/
[releases]: https://github.com/Health-Informatics-UoN/nuh-data/releases
[releases-badge]: https://img.shields.io/github/v/release/health-informatics-uon/nuh-data?include_prereleases&style=flat-square
