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
1. `conda env create -f requirements.yml` - Creates a new environment installing the dependencies from the .yml file
2. `conda env list` - Should list all environments
3. `conda activate <ENV_NAME>` - Activates the said environment
4. `python -m ipykernel install --user --name=<ENV_NAME>` - (OPTIONAL) enables to open directories using the `jupyter-notebook` or `jupyter-lab` server.

# Using the virtual environment:
1. `conda env list` - Lists available environments
2. `conda activate <ENV_NAME>` - Activates the environment env_name
3. Run project related commands.
4. `conda deactivate` - Deactivates the environment

# Dependency installation
1. Requirements are installed while creating the environment `conda env create -f requirements.yml`
2. If not so, they can be installed _**after activating the environment**_, using `pip install -r requirements4pip.txt`

# Run the flask app
1. Navigate to the project's root directory
2. Run `flask --app bnb run [--debug]`

# Initialize the app with the DB
1. Navigate to the project's root directory
2. Run `flask --app bnb init-db`



