# Bookworms and Bestsellers (B&B)
### [B&B](https://bookwormsandbestsellers.in) is a book recommendation and exchange platform for everyone.
#### It is being developed as a Minor Project be me, [Antriksh Narang](https://github.com/AntrikshNarang) and [Arjun Nambiar](https://github.com/ShadowSlayer03)

# Install Miniconda
### For Ubuntu (Debian-based)
1. Download Miniconda for Python 3.9 bash script [here](https://repo.anaconda.com/miniconda/Miniconda3-py39_23.5.2-0-Linux-x86_64.sh)
2. Grant execution permissions using:
    `sudo chmod u+x Miniconda3-py39_23.5.2-0-Linux-x86_64.sh`
3. Install Miniconda 3 using:
    `./Miniconda3-py39_23.5.2-0-Linux-x86_64.sh`
4. Continue the default installation process until "Thank you for installing Miniconda3!" message is obtained.
5. Once the installation completes, the following commands register conda as a new command to the default bash script (bashrc file):
    1. `source ~/.bashrc`
    2. `conda config --set auto_activate_base false`
    3. `source ~/.bashrc`

### For Windows
1. Download Miniconda for Python 3.9 .exe file from [here](https://repo.anaconda.com/miniconda/Miniconda3-py39_23.5.2-0-Windows-x86_64.exe)
2. Follow standard installation procedure

# Initial virtual-environment and Notebook server setup
1. `conda env create -f requirements.yml --prefix /path/to/venv` - Creates a new environment installing the dependencies from the .yml file
2. `conda env list` - Should list all environments - some with names, some with only path
3. `conda activate /path/to/venv` - Activates the said environment
4. `python -m ipykernel install --user [--name=<ENV_NAME>] [--prefix=/path/to/venv]` - (OPTIONAL) enables to open directories using the `jupyter-notebook` or `jupyter-lab` server.

# Using the virtual environment:
1. `conda env list` - Lists available environments
2. `conda activate /path/to/venv` - Activates the environment env_name
3. Run project related commands.
4. `conda deactivate` - Deactivates the environment

# Dependency installation
1. Requirements are installed while creating the environment `conda env create -f requirements_conda.yml --prefix ./.venv`
2. If not so, they can be installed _**after activating the environment**_, using `pip install -r requirements_conda_pip.txt`

# Run the flask app

1. Run this outside all environments to download **pipenv**: `pip install pipenv`. This shall be the dependency manager for Flask.
2. Navigate to the backend's root directory from the project's root directory: **`cd ./bnb`**
3. Run the following: `pipenv install` - installs all dependencies [Pipenv reference](https://realpython.com/pipenv-guide/)
4. Navigate to the project's root directory: `cd ..`
5. Prepend each of the following flask commands with: `pipenv run`
6. For example, to run the app: `pipenv run flask --app bnb run [--debug]`

# Initialize the app with the DB
1. Navigate to the bnb folder
2. Add a .env file as per the .env.example file in /bnb/bnb.
3. Run `flask db init` for initialization of migration files
4. Run `flask db migrate` for creating migration files
5. Run `flask db upgrade` to make tables (make sure your database server is up and running)