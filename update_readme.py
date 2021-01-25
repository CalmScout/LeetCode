"""
Script updates `README.md` with respect to files at ./easy and ./medium folders.
"""
import os

curr_dir = os.path.dirname(__file__)
with open(os.path.join(curr_dir, "README.md"), 'w') as readme:
    readme.write("# LeetCode\nDeliberate practice in coding.\n")
    langs = [l for l in os.listdir(curr_dir) if os.path.isdir(os.path.join(curr_dir, l)) and l[0] != '.']
    for lang in langs:
        readme.write("## {}\n".format(lang))
        readme.write("### Easy\n")
        easy = sorted(os.listdir(f"{curr_dir}/{lang}/easy"))
        easy = [x.split("_")[0] for x in easy]
        easy_solved = ""
        for el in easy:
            easy_solved += "{}, ".format(el)
        readme.write(easy_solved[:-2] + "\n")
        readme.write("### Medium\n")
        medium = sorted(os.listdir(f"{curr_dir}/{lang}/medium"))
        medium = [x.split("_")[0] for x in medium]
        medium_solved = ""
        for el in medium:
            medium_solved += "{}, ".format(el)
        readme.write(medium_solved[:-2] + '\n')
