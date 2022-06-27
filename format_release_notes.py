import sys

print("**Release Notes v{0}**".format(sys.argv[1]))
print("**What's New**")
with open("releasenotes.txt", "r") as f:
    for line in f:
        print("- {0}".format(line.strip()))
