# Unix 101
**Executive Summary:** This Document is the lesson plan for unix. We will teach using 'Bash' (Bourne Again Shell). We will explore how to get access to a Bash terminal regardless of operating system. And then the first commands a user commonly encounters.

## Main takeaway: It is worth it to become proficient with Unix

## Definitions
1. **Operating System** - software to manage computer hardware
1. **Unix** - a family of operating systems
2. **Linux** - a family of unix-like operating systems
4. **Shell** - software to facilitate giving instructions to the operating system - the user talks to the shell and the shell passes on to the operating system
8. **Shell**
   * ![](https://github.com/UVADS/orientation-technical/blob/d8bb11a4090297eb117eaa8b836a8dbb8379d8cc/images/image6.png)
   * Source: http://galileo.phys.virginia.edu/compfac/courses/ credit Bryan Wright 
5. **Bash** - Bourne Again SHell - a particular shell and one we will use for this lesson
6. **GUI** - Graphical User Interface - eg: clicking on icons with a mouse cursor or tapping icons
7. **CLI** - Command Line Interface - eg: the user types commands and uses specific syntax



## History of Unix
![](https://github.com/UVADS/orientation-technical/blob/e89f6cb5c7eb9882cfeac30a1417fe29279c700e/images/image5.png)

Source: http://galileo.phys.virginia.edu/compfac/courses/geek-hours/shell.html credit Bryan Wright

**NB**: MacOS is off the Unix family tree

## Getting Started BASH
Now that you have the background, it is time to get your machine set up with BASH. The first step is the software. Here are instructions depending on your platform:

* Mac: Open a terminal. (Use the spotlight search to find the app named “terminal.”) (NB: depending on the age of your computer you may be running a different but similar shell)
* Linux: Open a terminal. (You will need to look it up because it depends on your flavor.)
* Windows: Unfortunately, BASH is not necessarily native on a Windows machine. Install VSCode (see item 3 on checklist). Open a terminal (Ctrl+Shift+`) 

## First Commands
Bash is a CLI. To do anything you must input a command and often some additional parameters. The challenge is how to learn those commands in the first place. Here is the workflow to start with.

1. type a command
2. press the enter key
3. read the output the computer prints back to you

Let's dig in ....

### pwd
This command stands for 'print working directory'. A working directory is the location in the operating systems file structure where commands will operate from. By analogy if you asked someone where they are they may say something like "1600 Pennsylvania Ave". In that way when you say to the computer 'pwd' it will say it's location.

Example

![](https://github.com/UVADS/orientation-technical/blob/a91aca54ec7a63e4775d8c5c62e52a4dcc4e69a0/images/pwd.png)

### ls
The next thing you may want to know is what files are in the working directory. The 'ls' command stands for 'list'. By analogy if you asked someone what do you see in front of you they may say "The White House". In that way when you say to the computer 'ls' it will list 'what it sees' at that location.

Example

![](https://github.com/UVADS/orientation-technical/blob/c51f30d1f43aa5bb043a2ed9b02edd006b6bf581/images/ls.png)

### cd
The 'cd' command stands for 'change directory'. This is where we start moving around. Continuing our analogy you could tell someone to go home and they would move. In this case when you tell the computer to 'cd <location>' it will change the location. For this example we will combine it with pwd.
  
Example

![](https://github.com/UVADS/orientation-technical/blob/ca4124aacd9cfacc0437b28899cc0fc45031ed09/images/cd.png)

This one is a stretch so let's break it down.
1. use pwd to ask the computer what the working directory is
2. use cd to change directory. Also new is that we add an argument to the command (/c/Users/petea_000) which in this case is the directory we want to change to
3. we repeat pwd but see the output has changed because we used cd

**Extend:** You may be wondering, "can I use cd but instead of saying 'goto this address', could I say the equivalent of 'go one block north'?" The answer is Yes you can. Read [this page](https://www.geeksforgeeks.org/absolute-relative-pathnames-unix/) and ask questions.

### history
This is a fun little bonus command. No example here you can try it for yourself. If you type 'history' command your computer will print all of the commands it has run (recently)

## Editing a File
The next step is to create a file and edit the contents. We will just be looking to do a text file and use it for our 'hello world' program.

There are many programs you can choose to edit a file. In this case type the following

`nano hello-world.sh`

You are now in a text editor. Go ahead a write your 'hello world' program. In this environment it is a single line

`echo 'hello world'`

Then save your file (Ctrl+O)
Then exit (Ctrl+X)

**NB** You actually don't need to use the mouse. Experience the joy of not wasting time as you move back and forth between the mouse and the keyboard.

## Running 'hello world'
Now we run the program.

Example

![](https://github.com/UVADS/orientation-technical/blob/4f59236eafba19f08bdb10ba10ed4470e4fe3d2e/images/run.png)

You will note in  my example we have stumbled into our first error. When we typed the name of the program the computer did not recognize it as a command, but by adding './' the computer did recognize it. To untangle that little puzzle we need to dig into the concept that causes the greatest number of errors for students in the MSDS program.

## The PATH forward
The next step in the Unix journey is to understand the PATH variable. However we have already gone further in this lesson. We will leave it here for you to rest. When you are ready to untangle the './' take a swing at researching it yourself and use the keywords: unix, and path environment varible to guide you. Then come to Pete with questions.



# Conclusions, Homework, and Takeaways
* This was the most involved and challenging lesson in the orientation. It actually goes beyond orientation and gets into teaching because Pete cannot help himself.
* Many students coming into our program come from the GUI world not the CLI world. As a result for many this approach is disorienting and that is challenging. The way forward is to find a few hooks to grab to orient.
* The homework is to explore the path variable. Put in a good faith effort and see how far you can go. Then bring questions you have to Pete.
* Getting the skills from this lesson takes time and consistent use. Working through any material on these topics won't be beneficial without sustained practice.


## Main takeaway: It is worth it to become proficient with Unix
## Backup takeaway: If you are using a mouse, you are usually slowing yourself down

## Reading List
This list is initially populated with wikipedia articles. The goal of the exercise for the students is to improve this list. When you find something better make a pull request and improve the list.
* http://galileo.phys.virginia.edu/compfac/courses/sysadmin1/
    * http://galileo.phys.virginia.edu/compfac/courses/geek-hours/shell.html
* https://www.gnu.org/software/bash/
* https://en.wikipedia.org/wiki/GNU
