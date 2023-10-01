# /usr/bin/python3
from pick import pick
def boldcolos(text):
    bold_start = '\033[1;36m'
    bold_end = '\033[0m'
    return bold_start + text + bold_end

def info(field):
    return input(field + " ")
answers = {}

answers['Name'] = info("[*] " + boldcolos("The name of the contest "))
answers['Chall'] = info("[*] " + boldcolos("The name of the challenge "))
title = "The category of the challenge: "
options = ['Web', 'Forensics', 'Cryptography', 'Steganography', 'Networking', 'MISC', 'Warm-up', 'Binary Exploitation', 'Reverse Engineering', 'OSINT', 'Pwn']
option, index = pick(options, title, indicator=str('->'))
print("[*] " + boldcolos("The category of the challenge ") + "[" + option + "]")

answers['Points'] = info("[*] " + boldcolos("Points received after solving:"))
answers['Solves'] = info("[*] " + boldcolos("The number of solves "))
answers['Blood'] = info("[*] " + boldcolos("Were you the first to solve it?") + " (y/n) ")
answers['Attach'] = info("[*] " + boldcolos("Were files attached?") + " (y/n) ")
answers['Flag'] = info("[*] " + boldcolos("The flag"))

ctfn = f"{answers['Name']}"
chn = f"{answers['Chall']}"
filename = ctfn.replace(" ", "_")+ '_' + chn.replace(" ", "_")+ ".md"

with open(filename, 'w') as file:
    file.write(f"## {answers['Name']}: {answers['Chall']} \n")
    file.write(f"#### Category: {option}\n#### Score: {answers['Points']}\n#### Number of Solves: {answers['Solves']} ")
    if (answers['Blood'] == 'y') or (answers['Blood'] =='Y'):
        file.write("[First Blood 🩸] \n")
    file.write('\n### Description\n\n> Description here \n')
    if (answers['Attach'] == 'y') or (answers['Attach'] == 'Y'):
        file.write("\n**Files Attached:**\n")
    file.write("\n### Summary \n\n")
    constant = """\
    
### Solution Steps

![Illustration](https://i.imgur.com/F7WSZKo.jpg)

"""
    file.write(constant)
    file.write(f"\nFlag: `{answers['Flag']}`\n")
    constant2 = """\

### Conclusion


### References

1. [link1](-)
2. [link2](-)
3. [link3](-)
"""
    file.write(constant2)

print("\n[+] The write-up file " + boldcolos(filename) + " was generated!")
