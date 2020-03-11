"""
Script updates `README.md` with respect to files at ./easy and ./medium folders.
"""
import os

easy = sorted(os.listdir("./easy"))
easy = [x.split("_")[0] for x in easy]

medium = sorted(os.listdir("./medium"))
medium = [x.split("_")[0] for x in medium]

with open("README.md", 'w') as readme:
    readme.write("# LeetCode\n")
    readme.write("### Easy\n")
    easy_solved = ""
    for el in easy:
        easy_solved += "{}, ".format(el)
    readme.write(easy_solved[:-2] + "\n")
    readme.write("### Medium\n")
    medium_solved = ""
    for el in medium:
        medium_solved += "{}, ".format(el)
    readme.write(medium_solved[:-2] + '\n')
