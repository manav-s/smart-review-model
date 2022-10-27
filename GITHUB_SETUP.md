# Github Setup
Github is a website that allows us to host a git project. Essentially, it allows us to share information between each other more easily in a way that changes can be done incrementally and in a way that lets us record them and go back if any mistakes are made. Git is the system that allows us to track this and github essentially hosts a git project we all access.

## SSH Keys
In order to communicate with Github, we need something called an ssh key. This key or rather key pair allows us to communicate with servers over something called ssh or secure shell. This is something you can investigate in your own time, but for now it is important to note that 2 keys are made from this process, a private key and a public key. You do not need to touch the private key, but the public key is what you will need.  

In order for you to generate a new key pair, open up a command prompt (windows) or terminal (mac) and type `ssh-keygen`. It will then ask a series of questions. Use the default location for your file and set a password. This will generate the pair of keys in your `.ssh` folder which is usually under your personal root directory.

In order to add this to Github, go to your github settings, ssh keys, and then copy the contents from the public key file to the place for your public key and give it a good descriptive name. Click save and it will link the ssh key properly. Now you have ssh linked to Github.

## Git
Git is a command line tool, so in other words, it is controlled through your command line or terminal. In order to install it, go to [this download link](https://git-scm.com/downloads) and download the appropriate version of git for your computer. Install it and restart your terminal or command line interface by fulling closing all instances.

## Cloning
In order to get access to our repository on your computer, you need to clone it down. On the home page, click the Code button, make sure it is on ssh (second option) and copy what is there. That is the link to the github repository. Finally, open up a terminal or command line window and cd to the place you would like your file to be and do `git clone [link]`. This will clone a copy to your computer. To learn how to do things within this copy, see `GITHUB_USAGE.md`.