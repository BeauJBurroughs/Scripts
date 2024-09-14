import sys

FILE =sys.argv[1]

# Open the id_rsa file, read its contents, clean it, and overwrite the file
with open(FILE, 'rb') as f:
    lines = f.readlines()
# Remove carriage returns or whatever is causing issue from each line
cleaned_lines = [line.replace(b'\x0d\x0a', b'\x0a') for line in lines]
# if missing at end of append another new line
cleaned_lines.append(b'\x0a')
# Write the cleaned lines back to the file (or another file)
with open(FILE, 'wb') as f:
    f.writelines(cleaned_lines)
