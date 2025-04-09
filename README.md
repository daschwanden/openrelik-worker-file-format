
# OpenRelik worker Mach-O and ELF file format parsing
## Description
This repository contains the code for an [OpenRelik](https://openrelik.org/) Worker that provides workflow tasks to parse [Mach-O](https://en.wikipedia.org/wiki/Mach-O) and [ELF](https://en.wikipedia.org/wiki/Executable_and_Linkable_Format) files.

You can add the Worker to your OpenRelik [Getting started](https://openrelik.org/docs/getting-started/) setup by adding the following section to the [```docker-compose.yml```](https://github.com/openrelik/openrelik-deploy/blob/main/docker/docker-compose.yml) file.


## Deploy
Add the below configuration to the OpenRelik docker-compose.yml file.

```
openrelik-worker-file-format:
    container_name: openrelik-worker-file-format
    image: ghcr.io/daschwanden/openrelik-worker-file-format:latest
    restart: always
    environment:
      - REDIS_URL=redis://openrelik-redis:6379
      - OPENRELIK_PYDEBUG=0
    volumes:
      - ./data:/usr/share/openrelik/data
    command: "celery --app=src.app worker --task-events --concurrency=4 --loglevel=INFO -Q openrelik-worker-file-format"
    # ports:
      # - 5678:5678 # For debugging purposes.
```

## Test
```
pip install poetry
poetry install --with test --no-root
poetry run pytest --cov=. -v
```