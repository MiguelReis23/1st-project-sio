## Description

[Add a brief description of your project here]

## Authors

- GABRIEL JANICAS DA SILVA **108689**<br>
- MARTIM HENRIQUES CARVALHO **108749**<br>
- MIGUEL ROSA REIS **108545**<br>
- RAFAEL ANDRE VALENTE LEITE **108257**<br>
- RODRIGO MIGUEL BARROS MOÇO **108939**<br>


## Vulnerabilities

[Add any known vulnerabilities or security concerns here]



## RUN

1. Create the virtual environment:
```bash
python3 -m venv venv
```
2. Activate the virtual environment (Every time you open a new terminal you need to do this to make the virtual environment the default Python interpreter of this shell):
```bash
source venv/bin/activate
```
or (Windows):
```bash
.\venv\Scripts\activate.ps1
```

3. Install the requirements:
```bash
pip install -r requirements.txt
```

4. Run the application:


```bash
./run.sh app <PORT>
```
or:
```bash
./run.sh app_sec <PORT>
```

&emsp;&emsp;In Windows use instead:

```bash
.\run.bat app <PORT>
```
or:
```bash
.\run.bat app_sec <PORT>
```
5. Access the website:

```bash
http://127.0.0.1:<PORT>
```