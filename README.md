# RSA2048

RSA2048 private key hacking (educational project)

## Requirements

- Python 3
- [Dask](https://docs.dask.org/en/stable/) runtime

## Install

```shell
$ source ./env/bin/activate
$ pip install -r ./requirements.txt
```

## Prepare

On a separate highly available node:

```shell
$ dask scheduler
```

And several workers as follows:

```shell
$ dask worker scheduler-host:8786 --memory-limit 1GB --death-timeout 120 --name worker-name --local-directory /tmp/
```

## Run

Configure by editing `config.py` and run on scheduler node:

```shell
$ python3 ./app.py
```
