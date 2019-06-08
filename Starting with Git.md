Starting with Git

In this article we will learn how to setup a Git repository ,add files to the repository,make commits and finally make this repository public by putting it on Github.

You must have heard of Git repository.But what makes a repository a Git repository?

It is as similar to a folder which you have on your computer,the only thing which makes it a git repository is it stores the metadata of the history of the folder in a .git directory  which is present in the directory but hidden.

Without further ado lets make a git repository but before that make sure you install git on your computer.

Download git from this link: https://git-scm.com/downloads

There are two ways to do it.

1.Either you have a folder where you have bunch of files and you want that folder to become a Git repository.

Go to that folder on git and type git init.

It adds a .git file to the folder and Voila !! it is now a git repository.

2.You are starting afresh and want to initialize a repository where you will start putting up your work.

As we are starting afresh,we shall go with the 2^nd^ approach 

Steps which I followed are the following:

1.Open git bash.

1.Create a new folder named **git_example** using mkdir 

2.Changed my director to **git_example** through cd(change directory)

3.Make sure we don't have any file inside this folder through command **ls -a**(shows normal as well as hidden files)

4.Initialized this folder as a git repository by **git init**

5.Doing **ls -a** to make sure it is now a git repository ( .git file(hidden file) appeared inside the folder).

![1537886716983](C:\Users\u6yuv\AppData\Roaming\Typora\typora-user-images\1537886716983.png)

Anytime we can check the status of our repository by typing **git status**:

![1537887522094](C:\Users\u6yuv\AppData\Roaming\Typora\typora-user-images\1537887522094.png)

It provides a bunch of information:

1.We are in the master branch

2.We have not done any commit yet



Now lets add our first .txt file file in this directory

![1537888132957](C:\Users\u6yuv\AppData\Roaming\Typora\typora-user-images\1537888132957.png)

It opens a notepad with a new text file.

![1537888216618](C:\Users\u6yuv\AppData\Roaming\Typora\typora-user-images\1537888216618.png)

Add the text in the file and close it.

Now if you do **ls** we will see ex1.txt file created.

We can also check the repository status here by typing **git status**

![1537888348050](C:\Users\u6yuv\AppData\Roaming\Typora\typora-user-images\1537888348050.png)We can see   that now  **ex1.txt** file is listed as untracked files.

Now I would like to encourage you to create one more file using the same steps we followed above.

## Once you are done , do **git status** ,you will now find two files under untracked file.

![1537890251774](C:\Users\u6yuv\AppData\Roaming\Typora\typora-user-images\1537890251774.png)

# **Staging Area**

![1537889917662](C:\Users\u6yuv\AppData\Roaming\Typora\typora-user-images\1537889917662.png)

Consider a scenario where you are writing code to build a new features on a product.These two files which we added earlier contains the codes for the new feature.You finished up  coding for 1st file and would like to commit.

Git provides an intermediate directory called staging directory which is Git way of saying "Hey here is the cache where you can put all your  files which are finely prepared to commit. "

So lets go ahead and add ex1.txt file to staging directory

![1537890929401](C:\Users\u6yuv\AppData\Roaming\Typora\typora-user-images\1537890929401.png)

W can see our ex1.txt file is in the staging area which is why it is marked as **Changes to be commited**

and our **ex2.txt** file is still untracked.



*Note-If you accidentally added file to staging area,you can remove it using **git reset**.*

Now we are about to make our first commit .When we do this we need to write a message describing our changes.

We can add commit message in two ways:

1.Use **git commit**.It will open the editor where you can add your commit message.

2.Using command line via  **git commit -m "commit message"**.

Lets go ahead and make our first commit.

![1537891502458](C:\Users\u6yuv\AppData\Roaming\Typora\typora-user-images\1537891502458.png)

*Refer this [this style guide](http://udacity.github.io/git-styleguide/) describes some common best practices when writing commit messages.*

We can use **git log** to see the commit has been created.Here it is..

![1537892268507](C:\Users\u6yuv\AppData\Roaming\Typora\typora-user-images\1537892268507.png)



Do git status and see the changes

![1537892434954](C:\Users\u6yuv\AppData\Roaming\Typora\typora-user-images\1537892434954.png)

The initial commit note has gone away and the only remaining untracked file is ex2.txt.

You can go ahead and commit ex2.txt in the same way we did for ex1.txt.

Once you done with commit,the result of git status will be we having nothing else to commit.

![1537892596162](C:\Users\u6yuv\AppData\Roaming\Typora\typora-user-images\1537892596162.png)

We have nothing to commit.



Now lets make some changes in our ex1.txt and ex2.txt.

I am adding a new line of text in each file. 

![1537893539391](C:\Users\u6yuv\AppData\Roaming\Typora\typora-user-images\1537893539391.png)

Now lets do **git status**

![1537893617731](C:\Users\u6yuv\AppData\Roaming\Typora\typora-user-images\1537893617731.png)

As we modified these two files,we can see them tagged as modified.



Lets take a step back and think about what  working directory,staging directory and Repository looks like right now:

Repository generally consist of several commits and each commits consist of several files.As till now we just did commit once so it contains 1 commit which has ex1.txt and ex2.txt .

Staging area is the copy of most recent commit untill we add changes to it.So right now it has the same files as in repository.

Finally working directory also has the same files as we have in staging directory and repository but we have made changes in the ex1.txt and ex2.txt .

![1537894490956](C:\Users\u6yuv\AppData\Roaming\Typora\typora-user-images\1537894490956.png)

Denoting changed file through *



Now to compare between working directory and staging directory,we will use **git diff**

![1537894590131](C:\Users\u6yuv\AppData\Roaming\Typora\typora-user-images\1537894590131.png)

text in green shows the changes that I did.

Now we will go ahead and commit these changes to the repository 

![1537895049584](C:\Users\u6yuv\AppData\Roaming\Typora\typora-user-images\1537895049584.png)

Doing **git log** will give the following details:

![1537895111948](C:\Users\u6yuv\AppData\Roaming\Typora\typora-user-images\1537895111948.png)

We can see the list of commits that we did till now.

To compare two commits in repository  use **git diff commit_id1 commit_id2**

![1537895559370](C:\Users\u6yuv\AppData\Roaming\Typora\typora-user-images\1537895559370.png)

To compare between  staging area and most recent commit do **git diff --staged**.



Github 

Now how can we share this work of ours with someone else?

Here enters the Github

It is a website that allows us to share entire git repository to people.

Go ahead and create a Github account using  this link https://github.com/



Once you are in your account use **+** sign to create a new repository

![1537984525463](C:\Users\u6yuv\AppData\Roaming\Typora\typora-user-images\1537984525463.png)



If I were making a repository on Github before I had created any content then I would check this README box because that way my repository will start out with 1 commit in it.

*Note-You cannot clone a repository with 0 commit.*

But since I already had commits in my repository that I want to share I won't check this box.

Once you create your repository it will take you to this page:

![1537984852827](C:\Users\u6yuv\AppData\Roaming\Typora\typora-user-images\1537984852827.png)

W ewill be using the https link to add this repository as a remote to our local repository on our computer.

Lets get back to Git

Run **git remote**

It will show all the configured remotes till now.As we have not configured yet it will show none.

Run **git remote add origin** **<paste the https link here>**

As we have just one remote for this repository ,I am naming it as origin

![1537985068763](C:\Users\u6yuv\AppData\Roaming\Typora\typora-user-images\1537985068763.png)

We can see now origin remote has been created.

To check you entered the right https link we can do

**git remote -v**

![1537985143593](C:\Users\u6yuv\AppData\Roaming\Typora\typora-user-images\1537985143593.png)

The output shows both the url from where we will fetch the data from and push the data to.

Now lets push the local repository to Github using the command

**git push origin master**

By default all our files are under master branch.We can create multiple branches and push accordingly.

You can refer this link to understanding What a Branch is

https://git-scm.com/book/en/v1/Git-Branching-What-a-Branch-Is

![1537985390074](C:\Users\u6yuv\AppData\Roaming\Typora\typora-user-images\1537985390074.png) 

Voila!!! We successfully sent our repository on Github.

Refresh the Github page and you will find all your files under the Git tutorial Repository.

![1537985509308](C:\Users\u6yuv\AppData\Roaming\Typora\typora-user-images\1537985509308.png)

You can notice there are 3 commits in this repository which is inline with the commits that we did in our local repository.

That is all for now.