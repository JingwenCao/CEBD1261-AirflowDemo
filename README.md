# CEBD1261-AirflowDemo
 
## Install Airflow according to: https://github.com/puckel/docker-airflow

## Copy dags and docker-entrypoint-initdb.d folders to your docker-airflow folder

## Replace the docker-compose-LocalExecutor.yml file in docker-airflow folder with this one

## To run:

### Setup
1) Start Docker

2) Navigate to the directory where your docker-airflow is

3) Run command "docker-compose -f docker-compose-LocalExecutor.yml up -d"

4) Run command "docker ps" (Note, if you don't see postgresql, run the command from #3 again)

### Create database
5) Copy the postgresql container ID and run the command "docker exec -it [your postgres container ID here] bash"

6) Inside the container, navigate into the docker-entrypoint-initdb.d folder with the command "cd docker-entrypoint-initdb.d"

7) Inside the folder, run the file with the command "bash init-user-db.sh"

8) If you want to check if the table was created, you can enter the database with the command "psql -v --username "$POSTGRES_USER" --dbname "$POSTGRES_DB", and once you're in the database (the command window command should say "airflow >>"), you can run the command "\d weather_table". Exit the database with the command "\q", and from the postgres container with "exit".

### Configure Airflow
9) Go into your localhost:8080 and you should see Airflow running. Go to Admin -> Connections and above the table, click the tab "Create". Enter the following fields: Conn id = weather_id, conn type = Postgres, Host = postgres, Schema = airflow, login = airflow, password = airflow. Save.

### Run your dag
10) Click on DAGs in airflow, and you should see the weatherdag. On the far left, there's a switch. Toggle it on to run the DAG. Click on it to view the status (go to the far left tab to view the progress). Both tasks should run successfully.

### Check your table to validate its success
11) Enter the database again with the command "psql -v --username "$POSTGRES_USER" --dbname "$POSTGRES_DB", and once you're in the database (the command window command should say "airflow >>"), you can run the command "SELECT * FROM weather_table", and it should print out all of the loaded values from the weather API.


I hope this was comprehensive! If you run into any bugs, feel free to message me on Slack, or on my personal email (racheljcao@gmail.com).
