## Config
### crawl_data:
- output_folder: path to output folder

### convert_to_jsonl:
- pdf_path: output folder from crawl_data
- text_rule_file: rule for fix pdf can use from this path (.\src\data\scripts\merge_pdf\pdf_correction_rules_new.txt)

## Run scrape Admincourt
- For documents in each sub-section: a, b, c, d 
```bash
python src\data\scripts\crawl_admincourt\scrape_admincourt.py --config-name crawl-admincourt_doc-a.yaml
```
- For documents in only sub-section: e
```bash
python src\data\scripts\crawl_admincourt\scrape_admincourt_doc-e.py --config-name crawl-admincourt_doc-e.yaml
```

## Run convert to jsonl
```bash
python src\data\scripts\crawl_admincourt\convert_to_jsonl.py
```