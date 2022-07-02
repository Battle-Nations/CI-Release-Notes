import sys

print("Hey <@&{0}>, we've got a new release!".format(sys.argv[3]))
print("**Release Notes v{0}**".format(sys.argv[2]))
print("**What's New**")
with open(sys.argv[1], "r") as f:
    for line in f:
        if len(line.strip()) > 0:
            print("- {0}".format(line.strip()))
