

create a remote branch from a local branch or vice versa, so I've outlined both scenarios as well as provided information on merging the remote and local branches.

#####Creating a remote called "github":#####
git remote add github git://github.com/jdoe/coolapp.git
git fetch github

#####List all remote branches:#####
git branch -r
  github/gh-pages
  github/master
  github/next
  github/pu
  
#####Create a new local branch (test) from a github's remote branch (pu):#####
git branch test github/pu
git checkout test

#####Merge changes from github's remote branch (pu) with local branch (test):#####
git fetch github
git checkout test
git merge github/pu

#####Update github's remote branch (pu) from a local branch (test):#####
git push github test:pu

#####Creating a new branch on a remote uses the same syntax as updating a remote branch. 
For example, create new remote branch (beta) on github from local branch (test):#####
git push github test:beta

#####Delete remote branch (pu) from github:#####
git push github :pu

refresh the remote branches:
git remote update origin --prune
