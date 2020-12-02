# minimal-jupyterhub-docker-config


Dies funktioniert nur unter Linux.

1. Es muss die benötigte Software installiert sein.

    * docker
    * Python 3
    * Einige zusätzliche Module. Diese sind alle in der `requirements.txt` aufgelistet, also mit einem
`python3 -m pip install -r ./requirements.txt` sind alle wichtigen Pakete installiert.

2. Benenne .env.sample in .env um und vergebe den Admin-Username und Admin-Passwort.

3. Führe das Skript start.sh aus.

Nun sollte die Umgebung starten:
- Auf dem Port 8000 ist der JupyterHub erreichbar
- Auf dem Port 5984 ist die CouchDB erreichbar

Unter http://**<IP-Adresse/Hostname>**:5984/_utils/ ist Fauxton erreichbar, die GUI für die Datenbank.

