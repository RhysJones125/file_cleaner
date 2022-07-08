# File cleaner
Just a quick thing to obfuscate potential personal information from a file.

## How to run
Install dependencies via conda using 
```bash
conda env create -f environment.yml
```

or install using pip
```bash
pip install pandas
```

---

Add the files to the solution and populate the ```files``` list in main.py.

Add the columns needed to be obfuscated to the ```column_to_change``` list.

Run main.py

```bash
python main.py
```
