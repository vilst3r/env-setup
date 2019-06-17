# env-setup

Python scripts to replicate personal development environment across any machine with proper packaging and editor profiles and settings. Linux machine environment only.

# Requirements
- Python 3 system binary installed to run the script
- Run 'pip3 install -r requirements' to fetch all script dependencies
- Configure 'git-credentials.txt' with username, email & oath token properties delimited by a colon

# Process
1. Configure git ssh key (requires passcode)
2. Installs homebrew (requires passcode)
3. Installs brew packages from './config/brew.txt'
4. Installs brew cask software from './config/brew-cask.txt'
5. Install & Configure vim
6. Install & Configure bash
7. Install & Configure powerline

# Todo
- Finish configuring that powerline config (currently doing)
- Add regex to file processing for more efficient code style
- Configure iterm2 profile somehow...
- Automate generation of git-credential file if not found in project
- All done after that
