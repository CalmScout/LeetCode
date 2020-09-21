"""
Script updates `README.md` with respect to files at ./easy and ./medium folders.
"""
import os


with open("README.md", 'w') as readme:
    readme.write("# LeetCode\nDeliberate practice in coding.\n")
    langs = [l for l in os.listdir() if os.path.isdir(l) and l[0] != '.']
    for lang in langs:
        readme.write("## {}\n".format(lang))
        readme.write("### Easy\n")
        easy = sorted(os.listdir("./{}/easy".format(lang)))
        easy = [x.split("_")[0] for x in easy]
        easy_solved = ""
        for el in easy:
            easy_solved += "{}, ".format(el)
        readme.write(easy_solved[:-2] + "\n")
        readme.write("### Medium\n")
        medium = sorted(os.listdir("./{}/medium".format(lang)))
        medium = [x.split("_")[0] for x in medium]
        medium_solved = ""
        for el in medium:
            medium_solved += "{}, ".format(el)
        readme.write(medium_solved[:-2] + '\n')
