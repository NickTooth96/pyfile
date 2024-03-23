# Pyfile

A small tool to sort image files by year and month.

Written by Nick Toothaker

July 2023

Last Update: 7/31/2023

## Getting Started

To use this tool simply clone it to your machine. This will create a directory called pyfile. This directory contains the program files for pyfile.

Pyfile runs as a CLI so you can use it from the terminal. To use pyfile type the following into the terminal you used to clone the repository:

```python3 ./pyfile/pyfile.py --Help```

or you could `cd` into `pyfile/` and run this command:

```python3 ./pyfile.py --Help```

This will display the help page for pyfile. The help page should explain the tool well enough but if you are impatient, you can follow the steps in next section.

## Quick Start

### List Files in Directory

To list all the files in a directory type the following:

```python3 main.py -l --src "<source_directory>"```

To list everything in the current working directory use:

```python3 main.py -l```


lists everything in the root directory.

### Sort Images by Year/Month

To sort images into directories by year/month type the following:

```python3 pyfile.py -s --source=source --destination=destination```

### Unsort Images

To unsort images that are in directories sorted by year/month type the following:

```python3 pyfile.py -u --source=source```
