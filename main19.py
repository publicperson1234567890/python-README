import os

print "Windows\nLinux\nBsd\nMacOS\n"

value = raw_input("Enter Your OS: ")

if value == "Linux" or value == "linux":
	cmd = "uname -a"
elif value == "bsd" or value == "BSD" or value == "Bsd":
	cmd = "uname -a"
elif value == "Windows" or value == "windows":
	cmd = "Get-CimInstance Win32_OperatingSystem | Format-List *"
elif value == "MacOS" or value == "macos":
	cmd = "uname -a"
else: 
	print "You write wrong command!"

clear = "clear"
returned_value = os.system(clear)
returned_value = os.system(cmd)
