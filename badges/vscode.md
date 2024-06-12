![](https://github.com/UVADS/orientation-technical/blob/main/content/images/vscode-badge.png)

# VS Code

Visual Studio Code or VS Code is a powerful tool for getting data science work done. In your career you will have many choices about which tool to use, but for now, trust us, we will start with VS Code for teaching the core skills. As you develop you can explore other tools and decide what you like the most.
Why VS Code? Well as of 2022 according to Stack Overflow VS Code is the most popular coding environment with about three quarters of the market share!

In this badge we will get VS Code up and running and you will work through the fundamentals of **getting a coding environment up and running on your laptop**. This is an **essential skill for every data scientist** to develop, but, beware, it is not easy. This requires good mental preparation and fortitude. Expect to stumble and get frustrated.


## Requirements

1. **read** about:
   1. the difference between: text editors, word processors, and integrated development environments.
   2. the specific history and differences between Visual Studio and Visual Studio Code (n.b. we will use VS Code)
   3. Shells, focus on the difference between a Graphical user interface (GUI) and a Command line interface (CLI)
   4. the specific history of Bash (Bourne Again Shell), its syntax, and environment variables (especially PATH)
   5. package management and specifically the package manager conda and "conda environments"

   * **Tell** a friend about what you learned and how they can use the tools in their everyday life even if they are not a programmer. **Explain** to them why people would configure their environmetn before programming. **Explain** the difference between: text editors, word processors, and integrated development environments.

2. **install** VS Code and use the *Source Control* panel to clone a GitHub repository.
   * *hint/help*: If you're like me and prefer not to use the mouse, Ctrl+Shift+G is the shortcut key to open the panel.
   * You **may need to install** git during this process. Go for it! You can do it!

3. **configure** the default terminal in VS Code to be "Git Bash"
   * *hint/help*: If you're like me and prefer not to use the mouse, Ctrl+Shift+P and then enter "Terminal: Select Default Profile"
   * *hint/help*:This can be a very tricky step. Sometimes VS Code will have trouble finding something you installed and you have to do extra work to find it. But rest assured, this will be effort well spent, because issues such as this arise **CONSTANTLY** in Data Science work.

4. **connect** VS Code to GitHub.
   * **Work** on your cloned repo, commit a change, and push that change back up to GitHub.
      * hint: use `git clone`
      * This step is tricky. You will edit files "locally" on your machine. But you won't see the changes reflected on GitHub "remote" until you do `git push`
   
   * In this process you **may have to configure** your profile with a terminal command like 
    
        `$ git config --global user.name "John Doe"`
   
        `$ git config --global user.email johndoe@example.com`
   * In this process you **may also have to sign into GitHub** from VS Code to give permission to modify the repo on GitHub.


5. **explore** your computer file system using three Bash commands `pwd`, `ls`, `cd`. **Compare** what you find with the exploration with the documentation for Windows/MacOS/Linux as appropriate to your machine. **Find** another member of your cohort with a different operating system and discuss the differnences between your file systems.
   * *hint/help*:The `history` command is helpful for recalling earlier commands you entered.
   * **use** of command switches to enable additional functionality. (try `ls` and `ls -a` and `ls -l` and `ls -lhrta`)


6. **install** miniconda, make the 'conda' command available in your PATH in Git BASH terminal in VS Code. Celebrate your victory with another member of your cohort and swap stories about what was tricky and what you learned.
    * *hint/help*: "Phew". That was a lot of jargon. Break it down, understand each piece and then execute.
    * This is a rather tricky step, the way you know it works is at the end you can **run** the `conda` command.

     `$ conda --version`
     
     You will then get one of two responses
     * `bash: conda: command not found` --> not yet done
     * `conda 22.11.1` --> done (n.b. your conda version may vary) 

    * *hint/help*: Along the way you will deepend your understanding of environment variables and in particular the PATH variable.

7. **read** about conda environments and **use** `conda` to create an environment for code development. **Brainstorm** several reasons why you would use a conda environment.
     * *hint/help*: documentation here --> https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html


8. **read** about more features of VS Code. Choose TWO from the list below and then share what you learned with another member of your cohort.
   * Extensions
   * Debuggers
   * Something you find interesting



