import os
print("Welecome to Stegano by Sam Sepiol aka Naimish")
print("Visit my Github page to get more information https://www.github.com/NaimishPandey")
print("Checking Requirements")
print("steghide Package should be installed")
print("Installing steghide")
install = os.system("sudo apt install steghide")
print(install)
while True:
	print("Enter 0 to encode")
	print("Enter 1 to decode")
	print("Enter any shit to exit \n")
	choice = input("Enter your choice:")
	encode = "0"
	decode = "1"
	if choice is encode:
		print("Doing Your Encoding Job Sir\n")
		image_name = input("Enter The Name of image:")
		print("You should have a file you wanted to Embed")
		file = input("Enter the name of file:")
		password = input("Enter the password you want to use to encode the file:")
		print("Encoding file")
		e = os.system(f"steghide embed -cf {image_name} -ef {file} -p {password}")
		print(e)
		print("Encoding Successful")
	elif choice is decode:
		print("Doing Your Decoding Job Sir\n")
		image_name = input("Enter The Name of image:")
		password = input("Enter the password to decode the file:")
		print("Decoding File")
		d = os.system(f"steghide extract -sf {image_name} -p {password} ")
		print(d)
		print("Decoding Successful")
		with open("embed.txt") as f:
			content = f.read()
			print(f"The message is :{content}\n")
			print("Your Message has been saved")
	else:
		print("Thank You For Using this tool")
		break
