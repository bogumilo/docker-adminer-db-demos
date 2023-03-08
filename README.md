# Overview
These docker demos combines [Adminer](https://www.adminer.org/) with the most popular SQL databases
in multicontainer environement.
## Clone this repo
```bash
git clone https://github.com/bogumilo/docker-adminer-db-demos.git
```
## Run multi-container of selected demo in its directory
Available demos:
- [demo-postgres](https://github.com/bogumilo/docker-adminer-db-demos/demo-postgres)
- [demo-mysql](https://github.com/bogumilo/docker-adminer-db-demos/demo-mysql)
- demo-mssql
```bash
docker compose up
```
## Ways to ingest data
1. Adminer GUI
2. Run the script `python ingest_data.py` (prefilled with dummy data)
## Quick reference
- Check third party documentation for license information
- [Troubleshooting MySQL connection](https://stackoverflow.com/questions/44543842/how-to-connect-locally-hosted-mysql-database-with-the-docker-container)
