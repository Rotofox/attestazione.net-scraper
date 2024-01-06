## Simple web scraper for attestazione.net

### Developed with Python 3.9

### Installation steps:
1. Install Python 3.9
2. Open a terminal (cmd, bash, powershell, etc)
3. Navigate to the project folder
4. Setup your Python environment `python3 -m venv this-project-environment`
    - You can call it anything, I went with `this-project-environment`
5. Install dependencies by running this command: ` pip install -r requirements.txt`
6. Run the scraper by running one of these commands: 
    - Powershell `python .\attestazione-net-scaper.py`
    - CMD `python attestazione-net-scaper.py`
    - bash `python attestazione-net-scaper.py`

### BONUS:

Not doing anything? Program not working? 

Try going into the `attestazione-net-scaper.py` file and write this at the end under all the code `get_data_from_n_pages(1, 10)`. This will scrape page 1,2,3,...10 of the table on the website. It might take a while so go do something else for 5 minutes.