# Theory
1. What does it mean when Git commits are described as immutable? How is that reconciled with the ability to amend or delete commits?
```
Git commits have a SHA-1 hash associated with them that is guaranteed to be unique. Therefore any changes made to an existing commit will also change the associated SHA-1, making an individual commit immutable.
Amending a commit changes the SHA. Deleting it removes it from the branch, but it remains in history
```

2. What does it mean to merge branches A into branch B?
```
It means the changes made in branch A will be added on top of branch B whenever possible after conflicts have been resolved.
```

3. What does it mean to rebase branch A on top of branch B?
```
It means the changes made in branch A will be added on top of branch B in a linear fashion as if all the changes happened in one branch.
```

4. What is a “fast-forward merge”?
```
A merge where only the pointer to the head of the branch moves.
```

5. How does a tag differ from a branch?
```
A tag is for a specific commit.
```

6. What are the most common use cases for tags?
```
Release tag.
Bugfix tag.
```

7. What is a “commit-ish”?
```
```

8. What is the difference between HEAD and a “head”?
```
"HEAD" is a special reference that points to the commit you're on in the currently checked-out branch.
```

9. What is the origin?
```
A default name that git assigns to a remote repository.
```

10. What is the different between git fetch and git pull?
```
git fetch: fetches remote repo's data, doesn't change anything in the working tree.
git pull: git fetch + git merge/rebase
```

11. What is a merge conflict? How do you resolve a merge conflict?
```
Merge conflict: Branch B's changes overlap/conflict with changes in Branch A.
Remove/modify changes so that they no longer overlap.
```

12. How would you find the commit where a bug was introduced?
```
git bisect start
git bisect bad
git bisect good [commit]
```

13. How do you check out the code for a previous commit so that you can debug it?
```
git checkout SHA
```

14. What is “Detached HEAD mode”? How do you get into detached HEAD mode? How do you get out of detached HEAD mode?
```
"Detached HEAD mode" is a state in Git where you're no longer on a specific branch, but rather directly at a specific commit. In this mode, you're not on a named branch, and any new commits you make will not be part of any branch until you create a new branch. This state is useful for examining the code at a specific commit, experimenting, or creating temporary changes.

git checkout SHA
```

15. What does rewriting history mean? When might you do it? When should you not rewrite history? What can go wrong when you modify history?
```

```

16. When should you delete a commit vs revert it?
```
```

17. What is the difference between git reset 29f5e54 and git checkout  31f5e54?
```
reset: --hard not working dir safe, move branch that HEAD points to
checkout: working dir safe, moves HEAD itself
```

18. What is the difference between a soft, hard, and mixed reset?
```
soft: moves what HEAD points to
mixed: moves what HEAD points to, changes staging area to match HEAD
hard: moves what HEAD points to, changes staging area to match HEAD, changes working tree to match HEAD
```

19. When would you use git reset?
```
When you want to undo a recent commit, move the head back, or reset the current branch to a previous state.
```

20. Is it possible to lose a commit? Or to lose your changes? Under what circumstances?
```
Commits are very hard to lose because it will be stored in history. Changes can be lost if you use git reset --hard 
```

21. What is the reflog? When would you use it?
```
reflog is short for "reference log", it is git's way of keep HEAD's history, much like shell history.
```


# Practical
Please clone https://github.com/imc-trading/devschool-git-exam.

1. Check out the branch resume. Change the commit message from “Add Wok Experience” to “Add Work Experience”. What commands did you run?
```
git status
git branch --all
git checkout resume
git commit --amend
```

2. Add this “Work Experience” item in “Resume.md”:
```
### The Normal Brand
- Web Developer -- 2019-2021
  - Implemented OAuth login process to support Social Login.
  - Added web analytics
 ```
Commit it on the branch resume with the message “Add Normal Brand item”. What command(s) did you run?
```
git add Resume.md
git commit -m "Add Normal Brand item"

OR

git commit -a -m "Add Normal Brand item"
```

3. The commit on the branch resume with the message “fill edu” has some issues. Fix it like this: 1. Change the message to “Add content for Education section”. 2. The commit has introduced some whitespaces at the end of two lines. Remove those. What command(s) did you run? Explain your actions.
```
git log --pretty=oneline -> get commit history
git rebase -i HEAD~3 -> interactive rebase of the last 3 commits leading up to "HEAD(current branch)"

Edit file to remove empty lines.
git add Resume.md
git commit --amend -> change commit message
git rebase --continue

resolve and confirm changes for the next commits
git add Resume.md
git rebase --continue
```

4. The commit with the message “Add empty lines” is not useful. Remove it from the history. What command(s) did you run?
```
git rebase -i HEAD~4
delete the commit from the text editor
```

5. There is a branch called skills. How can you show the content of the Resume.md file on that branch without switching to the branch?
```
git show origin/skills:Resume.md
```

6. On the branch skills there is a commit called “Add skills”. Add that commit on top of the branch resume without switching branches away from resume. That should create a conflict. Fix it by incorporating both the previous and the new changes. What commands and actions did you do?
```
git log origin/skills --pretty=oneline --abbrev-commit -> get commit logs for the skills branch
git cherry-pick #sha -> cherry pick the commit you'd like to merge in
resolve conflicts
git add Resume.md
git cherry-pick --continue
```

7. In Resume.md there is a line ### Illinois State University. How can you find out what is the last commit that changed/introduced that line? What is the message of that commit? What commands did you run?
```
git log -S '### Illinois State University' -- Resume.md
```

8. Create a branch called letter_of_intent forking off from the branch job_applications. Create a file there called letter.txt with the content I need this job, please!. Commit this file on the letter_of_intent branch with the commit message Add letter of intent. Add another commit that adds this line to letter.txt: Sincerely yours, Norman. Commit it with the message Sign letter. What commands did you run?
```
git checkout job_applications
git checkout -b letter_of_intent
touch letter.txt
git add letter.txt
git commit -a -m "Add letter of intent"
git commit -a -m "Sign letter"
```

9. Rebase the letter_of_intent onto the resume branch without including the commits on the job_applications branch. Basically add the commits Add letter of intent and Sign letter on top of resume without changing resume and point letter_of_intent to the last commit. Do not use cherry-pick. What command did you run?
```
git rebase -i resume -> interactive rebase, choose which commits to keep
```

10. Merge the branch letter_of_intent into the branch resume. What commands did you run? Explain the merge strategy taken.
```
git merge --no-ff letter_of_intent
```


11. Merge the job_applications branch into the branch resume. What commands did you run? What merge strategy was taken? What happened to the git history of the resume branch?
```
```