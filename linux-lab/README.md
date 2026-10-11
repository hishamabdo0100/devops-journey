# Linux Basics Lab

This lab is part of my DevOps learning journey.

## Topics Practiced

* Linux filesystem navigation
* Working with directories
* Creating files
* Copying files
* Moving and renaming files
* Removing files

## Commands Practiced

```bash
pwd
ls
cd
cd ..
cd -
mkdir
touch
cp
mv
rm
```

## Lab Structure

```text
linux-lab/
├── docs/
│   ├── notes-copy.txt
│   └── readme.txt
└── notes.txt
```

## What I Learned

* `/` is the root directory in Linux.
* `/home` contains users' home directories.
* `/etc` contains configuration files.
* `/var` contains variable data such as logs.
* `pwd` shows the current working directory.
* `ls` lists files and directories.
* `cd` changes the current directory.
* `mkdir` creates directories.
* `touch` creates files.
* `cp` copies files.
* `mv` moves or renames files.
* `rm` removes files.

## Practical Challenge

Created a `docs` directory, created `readme.txt` inside it, copied `notes.txt`, and moved the copy into the `docs` directory.

## Status

Completed

---

## Linux Lab #2 — Reading and Inspecting Logs

### Topics Practiced

* Reading files with `cat`
* Inspecting files with `head`
* Inspecting files with `tail`
* Monitoring logs with `tail -f`
* Searching logs with `grep`
* Appending data with `>>`

### Commands Practiced

```bash
cat app.log
head -n 3 app.log
tail -n 3 app.log
tail -f app.log
grep "ERROR" app.log
grep "WARNING" app.log
grep "INFO" app.log
```

### Log Monitoring

Used `tail -f` to monitor `app.log` in real time.

New log entries were appended using:

```bash
echo "ERROR Database connection lost" >> app.log
echo "INFO Database reconnecting" >> app.log
```

The new entries appeared automatically in the terminal running `tail -f`.

### Troubleshooting Example

Used `grep` to find error messages:

```bash
grep "ERROR" app.log
```

This returned all log entries containing `ERROR`.

### Status

Completed

---

## Linux Permissions Lab

### Objective

Practice Linux file permissions using `chmod` on Ubuntu Server.

### Permission Values

| Permission    | Value |
| ------------- | ----: |
| `r` (read)    |     4 |
| `w` (write)   |     2 |
| `x` (execute) |     1 |

### Permission Categories

* **Owner:** The user who owns the file.
* **Group:** Users belonging to the file's group.
* **Others:** All other users.

### Practical Experiments

Created a test file and inspected its permissions:

```bash
touch permission-test.txt
ls -l permission-test.txt
```

Changed the permissions to `600`:

```bash
chmod 600 permission-test.txt
ls -l permission-test.txt
```

Expected permissions:

```text
-rw-------
```

Changed the permissions to `755`:

```bash
chmod 755 permission-test.txt
ls -l permission-test.txt
```

Expected permissions:

```text
-rwxr-xr-x
```

Changed the permissions to `644`:

```bash
chmod 644 permission-test.txt
ls -l permission-test.txt
```

Expected permissions:

```text
-rw-r--r--
```

### Understanding Numeric Permissions

Each digit represents the combined permission values for one category.

* `600`: Owner can read and write; group and others have no permissions.
* `755`: Owner can read, write, and execute; group and others can read and execute.
* `644`: Owner can read and write; group and others can read only.

### Environment

Ubuntu Server running inside VirtualBox. Commands were executed through an SSH connection from Git Bash on Windows.

### Key Takeaway

`chmod` changes file permissions. The `ls -l` command displays the resulting permissions, allowing them to be verified.

### Status

Completed

