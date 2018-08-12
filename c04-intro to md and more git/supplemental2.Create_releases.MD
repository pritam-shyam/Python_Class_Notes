# Create Releases of you Repo

A handy feature in Git is tagging certain commits. This is commonly done to signify releases of your work.

## Listing tags

Move into private MIS407-cid00xx repo directory.

To find a list of existing releases:
```
git tag
```
At this stage, there are none.

## Tagging a staged release (uncommitted)

Let's add an additional file to our repo, and stage the changes.

```
echo "Alpha release" >> release.txt
git add .
```

Now, before committing the staged changes, let's tag this release.

```
git tag -a v0.0.1 -m "initial alpha release "
```

Now, we can commit and push these changes to GitHub

```
git commit -m "initial alpha release"
git push origin master
```
## Tagging a previously committed set of changes

You can also tag a previous release. To do this, you must find the haskey forthe previous release by using the git log command, and then tagging that specific release
```
git log --pretty=oneline
git tag -a v0.0.2 9fceb02xxxxxxxx
```

Now, we can push our tagged release to GitHub
```
git push origin v0.0.2
```


## Appendix:
For more detail on tagging releases, see https://git-scm.com/book/en/v2/Git-Basics-Tagging
