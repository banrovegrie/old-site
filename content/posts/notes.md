---
title: "Git"
date: 2021-06-29T21:43:59+05:30
tags: ["dev", "git"]
---

# Getting Started

- For `Github-CLI`, refer to it's beautiful documentation.

## Setting up the Git environment

### Git Configuration

```bash
git config <options> <values>
```

1. `--system`: [`/etc/gitconfig`]
   - Contains values applied to every user on the system and all their repos.
2. `--global`: [`~/.gitconfig` /`~/.config/git/config` ]
   - Values specific to the user.
3. `--local`: [`<path-to-repo>/.git/config`]
   - Values specific to the repo.

**NOTE:** Use the following to view the settings and where they come from.

```bash
git config --list --show-origin
```

- To set <branch-name> as the default branch name,

  ```bash
  git config --global init.defaultBranch <branch-name>
  ```

<hr>

# Git Basics

## Structure and status of files

- `git add <filename>` :- Track and stage the file.

- `git status -s` :- Short status.

  ### Gitignore

  - Rules for using `.gitignore`:-

    1. `#` :: Comments for gitignore file

    2. `Glob` Patterns work and will be applied recursively throughout the entire working tree.

    3. `/` :: Start patterns to avoid recursivity

       ​     :: End pattersn to specify directory

    4. `!` :: Negate a pattern.

  - **Glob Patterns**: Simplified `regex` used by sheels.

:notebook: Find out `.gitignore` files for projects of a specific language.

- `git diff` :- Exact changes from last commit, which have not yet been staged.
- `git diff --staged` :- Self-explanatory
- `git commit` :- Commit your changes.

### Removing Files

- If you want to delete the file (from including `git` database), do the following:

  ```bash
  rm <file>
  git status # The file should be shown deleted and not staged
  git rm <file>
  git status # Stages the file removal
  ```

- Use `-f` option to forcefully delete if the file was staged previously.

- To keep the file in working directory but remove it from the staging area, use

  ```bash
  git rm --cached <file/directory/file-glob>
  ```

  :notebook: Use `\*` , otherwise git does its own filename explansion in-addition to shell's filename expansion.

## Commit History

- `git log <options>`$\star$ `-- [<path/to/file>]` 

  Shows the commit history with the hashes. The following options are popular:

  - `-p / --patch [-<no-of-logs>]` :: Show difference introduced in each commit.
  - `--stat`
  - `--pretty=<options> (!)[--graph]`
    - `oneline` :: supports graph
    - `short`
    - `full`
    - `fuller`
    - `format:<git-print-format>` :: use it without the `:` for the available specifiers. Supports graph
  - `--grep` :: Search for keywords in the commit message
  - `[--since/before=<time.format>]` :: Ex= `2.months`, `2 years ago` etc.
  - `-S <string>` :: Shows only those commits that  changed the number of occurrences of `<string>`.
  - `--no-merges` :: Are not merge commits
  - `--all` :: Shows log for all the branches.
  - `--graph` 

- `git shortlog`



## Undoing Things

- To redo a commit, stage the respective files to be `re-commited` and run the following:

  ```bash
  git commit --amend
  ```


### Un-staging a file :warning:

Dangerous Way:

```bash
git reset HEAD <file>
```

### Un-modifying a modified file :warning:

```bash
git checkout -- <file>
```

### Restore (safe and secure) 

```bash
git restore --staged <file>
```

### Un-modifying a modified file

```bash
git restore <file>
```

## Working with remotes

- `git remote -v` :: Shows URLs that git has stored for the short-name used.

- `git remote add <shortname> <url>` :: Add new remotes.

- ### Fetching

  ```bash
  git fetch <remote>
  ```

  to download data from your remote repo. 

What `git pull` does is it automatically fetches the data and merges it into the current (working/ same short-name(?))branch.

- `git push <remote> <branch>`  :: If there's a push conflict, we need to fetch their work first.
- `git remote show [<remote>]` :: Info about the remote.

- `git remote rename <remote> <new-shortname>`
- `git remote remove <shortname>`



## Tagging

Used for tagging release points for the software (`v1.0`, `v2.0` etc.).

```bash
git tag [-l/--list <glob-pattern>]
```

### Creating Tags

- **Lightweight Tag** :- Pointer to a specific commit.

  > ```bash
  > git tag <version-tag>
  > ```

- **Annotated Tags**:- Full objects in the git database.

  > ```bash
  > git tag -a <version-tag> -m "message"
  > ```

You can also tag commits later after you've moved past them.

### Sharing Tags

- `git push` doesn't transfer tags to remote servers.

  ```bash
  git push <remote> [--tags/<tags>+] 
  ```

  :notebook: Use option `--follow-tags` to just push annotated tags.

### Deleting Tags

- Just from local repo, use  `git tag -d <tagname>`
- For remote servers,
  1. `git push <remote> :refs/tags/<tagname>`
  2. `git push <remote> --delete <tagname>`

### Checkout Tags

To view versions of files that a tag points to,

```bash
git checkout <tagname>
```

which puts us in `detached HEAD` state. Therefore, if we make changes now and create a commit, tag stays the same but the new commit will be unreachable from any branch. So, just use make another branch for the same: 

```bash
git checkout -b <branch-name> <tagname>
```

### Switching b/w branches 

```bash
git switch [<option> [<value>]* <branch> 
```

- `-c` :: Create a new branch and switch to it.
- `-` :: Move to the last checkout branch.

## Git Aliases

```bash
git config <access-specifier> alias.<name> <to-be-substituted-command>
```

Ex:

1. `git config --global alias.last 'log -1 HEAD'` :: `git last` would now give the last commit info. 
2. `git config --global alias.visual '!<command>'` :: Command to open a visually aesthetic `gitlog`.

<hr>


# Git Branching

## GIT Structure

- Refer to the guide. Neat explanations.

### Git Branching

- `git checkout -b <name>` :: Make a branch and checkout.
- `git merge <branchname>` :: Merge the branch into the current one.

### Git Merge Conflicts

Check using `git status`. 

1. Make respective changes, given by `git merge` for the conflicting files.
2. `git mergetool` :: Use to merge conflicting branches.



## Branch Management

```bash
git branch [<options> [<values>]] [<branch>]
```

- `-v` :: Show branches with last commits.

- `--[no-]merged` 

  - Show branches already merged into the provided/ current one.
  - Helps to keep track of branches safe for deletion.

-  `--move <prev-name> <branchname>` 

  - Renames the branch.

  - To keep it synced online on Github/ Gitlab, run 

    ```bash
    git push --set-upstream origin <branchname>
    ```

    Still, the branch would persist on remote, so delete using

    ```bash
    git push origin --delete <prev-name>
    ```



## Branching Workflows & Remote Branches

- Refer to the guide.

- `git ls-remote <remote>` :: Shows remote references.

- `git fetch <remote>` :: Synchronise your work with a given remote.

- After fetching from remote, if we want to work on the branch, just run:

  ```bash
  git checkout -b <new-name> <branch>
  ```

- `git config --global credential.helper cache` :: If you don’t want to type it every single time you push, you can set up a “credential cache”.

- A 'tracking branch' in Git is a local branch that is connected to a remote branch. When you push and pull on that branch, it automatically pushes and pulls to the remote branch that it is connected with. The command 

  ```bash
  git checkout --track <remote>/<branch>
  # There's even a shortcut for the same
  git checkout <branch>
  ```

  To setup a local branch with different name, use:

  ```bash
  git checkout -b <new-name> <remote>/<branch>
  ```

  If there's already a branch, setup upstream by:

  ```bash
  git branch [-u/ --set-upstream-to] <remote>/<branch>
  
  # @{upstream}/ @{u} now refers to this upstream setup
  # so 
  git merge origin/master
  # is the same as
  git merge @{u}
  ```

- `git branch -vv` :: List  all the tracking branches setup

- `git push <remote> --delete <branch>` :: Delete the branch in the remote server.

## Rebasing

- Refer to the [guide](https://git-scm.com/book/en/v2/Git-Branching-Rebasing) for understanding.

