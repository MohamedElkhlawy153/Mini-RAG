# mini-rag

This is a minimal implementation of the RAG model for question answering.

## Requirements

- Python 3.9 or later


#### Install Python using MiniConda


1. Download and install MiniConda from [here](https://docs.anaconda.com/free/miniconda/#quick-command-line-install)
2. Create a new environment using the following command:


```
$ conda create -n mini-rag-app python=3.9
```


3. Activate the environment:

```

$ conda activate mini-rag-app
```


### (Optional) Setup you command line interface for better readability


```
export PS1="\[\033[01;32m\]\u@\h:\w\n\[\033[00m\]\$ "
```


## Installation


### Install the required packages


```
$ pip install -r requirements.txt
```


### Setup the environment variables


```
$ cp .env.example .env
```

Set your environment variables in the `.env` file. Like `OPENAI_API_KEY` value.
