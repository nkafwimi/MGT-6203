# Team-94
 Team 94's group project GitHub repository for MGT 6203 (Canvas) Summer of 2022 semester.


## Env Setup: 

### Prerequisites

* Python 3.9 
* Miniconda (https://docs.conda.io/en/latest/miniconda.html)


### Create Python Virtual Environment  

```
$ conda create -n py39 python=3.9
$ conda activate py39
```

### Install Python Requirements

```
$ cd salary_pridiction_for_software_developer
$ pip install -r requirements.txt
```

### Download the Stackoverflow Data

There is a python script written to download the data from source location and saves it in ./Data/source/<year>.csv . Use the below command to download the files. DO NOT PUSH THE SOURCE CSV TO GIT

```
$ python Scripts/download_survey_data.py --all
```

### Launch Jupyter Notebook 

```
$ jupyter notebook
```


## Git Commit Signature:

```
$ git commit -m "[name of the auther]| <commit message>"
```