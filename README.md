# Getting Started

This is a sample script to show how to set up the virtual environment, read a csv and plot a graph. A set of python libraries are installed in the virtual environment using a requirements.txt.

1. Create a virtual environment in new terminal

```
sd@drs-macbook-air APAN5400 % python3 -m venv venv
sd@drs-macbook-air APAN5400 % source venv/bin/activate
```

2. Create requirements.txt

```
pandas
numpy
matplotlib
```
In Terminal run: ```pip install -r requirements.txt```

# Commit your work to Git

Do not commit the `data/` folder or the `venv/` virtual environment. Both are listed in `.gitignore`.

1. Check which files changed

```
git status
```

2. Stage the files you want to save (scripts, README, requirements). Do not add `data/`.

```
git add Module1/ README.md requirements.txt
```

3. Confirm only the right files are staged

```
git status
```

4. Commit with a short message that describes the change

```
git commit -m "Add Module 1 analysis script"
```

5. Push your commit to GitHub

```
git push -u origin main
```

If this is the first time you are connecting this folder to GitHub, create a repository on GitHub, then run:

```
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/APAN5400.git
git push -u origin main
```

Replace `YOUR_GITHUB_USERNAME` with your GitHub username. If GitHub asks for a password over HTTPS, use a personal access token, not your GitHub account password.

# Commit any additional changes 

1. See what changed

```git status```

2. Add the files you want to commit

```git add ../README.md```

3. Commit with message

```git commit -m "Add Git instructions for students to the README"```

4. Upload to GitHub

```git push```

5. For later work, repeat the same four steps. Stage only the files you mean to keep (for example git add Module1/test_mod.py). data/ and venv/ stay out because they are in .gitignore.