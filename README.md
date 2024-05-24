# Bookworms and Bestsellers (B&B)
### [B&B](https://bookwormsandbestsellers.in) is a book recommendation and exchange platform for everyone.
#### It is being developed as a Minor Project be me, [Antriksh Narang](https://github.com/AntrikshNarang) and [Arjun Nambiar](https://github.com/ShadowSlayer03)

## Install Miniconda
(Skip this step if you are not working on the ML part of the project)
### For Ubuntu (Debian-based)
1. Download Miniconda for Python 3.9 bash script [here](https://repo.anaconda.com/miniconda/Miniconda3-py39_23.5.2-0-Linux-x86_64.sh)
2. Grant execution permissions using:
    `sudo chmod u+x Miniconda3-py39_23.5.2-0-Linux-x86_64.sh`
3. Install Miniconda 3 using:
    `./Miniconda3-py39_23.5.2-0-Linux-x86_64.sh`
4. Continue the default installation process until "Thank you for installing Miniconda3!" message is obtained.
5. Once the installation completes, the following commands register conda as a new command to the default bash script (bashrc file)
```
source ~/.bashrc
conda config --set auto_activate_base false
source ~/.bashrc
```

### For Windows
1. Download Miniconda for Python 3.9 .exe file from [here](https://repo.anaconda.com/miniconda/Miniconda3-py39_23.5.2-0-Windows-x86_64.exe)
2. Follow standard installation procedure

### Initial virtual-environment and Notebook server setup using conda
1. Create a new environment installing the dependencies from the yml file:
```
conda env create -f requirements.yml --prefix /path/to/venv
```

2. List all environments - some with names, some with only path:
```
conda env list    
```

3. Activates the said environment:
```
conda activate /path/to/venv
```

4. (OPTIONAL) Enable to open directories using the jupyter-notebook or jupyter-lab server:
```
python -m ipykernel install --user [--name=<ENV_NAME>] [--prefix=/path/to/venv]
```

### Using the virtual environment:
1. `conda env list` - Lists available environments
2. `conda activate /path/to/venv` - Activates the environment env_name
3. Run project related commands/scripts.
4. `conda deactivate` - Deactivates the environment

## Project Set-up (ML)
1. Requirements are installed while creating the environment `conda env create -f requirements_conda.yml --prefix ./.venv`
2. Activate the conda environment.
2. conda should have installed pip requirements from _requirements_conda_pip.txt_ file. But sometimes torch fails to install during the enviroment set up. In that case run `pip install -r requirements_conda_pip.txt`
3. Run any suitable commands/scripts.
4. Deactivate the conda environment.

## Project Set-up (Backend)

1. Run this **outside any environments** to download _pipenv_: `pip install pipenv`. This shall be the dependency manager for all python projects. Here we are using it to manage flask and its dependencies.
2. Navigate to the backend's root directory from the project's root directory: `cd ./backend`
3. Run the following to install all production and development dependencies from the Pipfile [Pipenv reference](https://realpython.com/pipenv-guide/):
```
pipenv install
pipenv install --dev
```
4. Run the shell in the environment created by pipenv using `pipenv shell`
5. Run all Flask related commands here.
6. Exit the shell (ie. the environment) using the command `exit`

### Initialize the app and the DB
1. Navigate to the root directory of the backend: `cd ./backend`
2. Add a .env file as per the .env.example file in this directory.
3. Run the app using 
```
flask run                       # if FLASK_ENV="bnb" is listed in .env file
flask --app bnb run [--debug]   # Otherwise
```
4. Run `flask db init` for initialization of the `migrations/` directory **(only once)**
5. Use the following two commands to make migrations and upgrade the database to those changes **(every time the schema changes)**:
```
flask db migrate    # for creating a migration in ./migrations/versions
flask db upgrade    # to actually upgrade the database
```