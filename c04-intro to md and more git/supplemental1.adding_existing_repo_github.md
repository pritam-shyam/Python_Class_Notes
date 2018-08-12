# Pushing an existing local repo up to GitHub.

When starting a new project, it's best to create your GitHub repo first, and then clone this to your local drive (you then add files to this cloned repo and then push it back to the GitHub server).

But, despite this "best practice", there are times when you may not want to move/disturb your existing work and rather push it to GitHub from the existing directory. In this case, you will want to create an empty repo on GitHub and "push" your existing content into this new repo.

## 1. Create a new local repo

Let's begin by creating a new local repo.
```
git init
echo "Hello world!" >> test.txt
git add .
git commit -m "First Commit"
```

## 2. Create a new (empty) GitHub repo

Now, create an empty repository on GitHub.

NOTE: This process is much easier your new GitHub repo is empty, therefore DO NOT INITIALIZE YOUR NEW REPOS WITH A README.md FILE.

## 3. Add remote GitHub repo as "origin"

Once you've created your new repo, copy the remote repository URL (this is displayed in your new repo page on GitHub -- look for the button "Clone or download")

Now, we set the origin in our local repo to that of the GitHub URL.

```
git remote add origin <remote repository URL>
git remote -v
```

## 4. Push local repo content to GitHub repo.

You can now push your local repo up to GitHub

```
git push origin master
```

Go look at your GitHub page, and you should find your test.txt file is now loaded into your GitHub repo.

### Appendix:

For more information on this process, look [here](https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/)
