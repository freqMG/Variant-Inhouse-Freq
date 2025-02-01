# Variant Inhouse Frequency Pipeline

## Overview
This repository provides a pipeline to process NGS (WES & CES) VCF files and compute in-house variant frequencies.

## Features
- Merges multiple VCF files into a single dataset
- Filters and reformats variant data
- Calculates variant frequency and produces a final dataset

## Installation
### Requirements
Ensure you have the following dependencies installed:
- Python 3.x
- pandas

Install dependencies using pip:
```bash
pip install pandas
```

## Usage
Run the pipeline with:
```bash
python ngs_pipeline.py
```

## Output Files
- `frequency_data.txt`: Processed variant data
- `filtered_data.txt`: Filtered frequency results

## License
This project is licensed under the MIT License.
