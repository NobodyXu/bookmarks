 1. `sudo apt install software-properties-common gnupg`
 2. `wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | sudo apt-key add -`, add to `source.list`: `deb https://pkg.jenkins.io/debian binary/`
 3. `sudo apt update && sudo apt install tmux htop neovim nginx jenkins git default-jre-headless default-jdk-headless rsync certbot python-certbot-nginx`
