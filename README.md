# Codeleap Challenge

This is a Django app made as a challenge for the Jr Backend position @ Codeleap.

This applications is deployed at https://codeleap-challenge.fly.dev/careers/

## How to run

1. Clone this repository

```
git clone https://github.com/matheusnovaisz/codeleap-challenge.git
```

2. Copy the .env.example and set the DATABASE_URL variable

 ```
 cp .env.example .env
 ```
  You don't need to change as we're using a docker database container.

3. Build the docker containers

  ```
  docker compose up -d
  ```

4. Run the migrations

```
docker-compose run web usr/local/bin/python managapy.migrate
```

5. Open your Django application on http://localhost:8000