import os
import time
# 1. The files and directories to be backed up are specified in a list.
# Example on Windows:
source = ['E:\Gurov_SSD_256\IT\Testing\Automation_08_09_2019"']
# Example on Mac OS X and Linux:
# source = ['/Users/swa/notes']
# Notice we had to use double quotes inside the string for names with spaces in it.
# 2. The backup must be stored in a main backup directory
# Example on Windows:
target_dir_E = 'E:\Gurov_SSD_256\IT\Testing\Automation_08_09_2019_backup'
# target_dir_D = 'D:\IT\Testing\Automation_08_09_2019_backup'
# Example on Mac OS X and Linux:
# target_dir = '/Users/swa/backup'
# Remember to change this to which folder you will be using
# Create target directory if it is not present
if not os.path.exists(target_dir_E):
    os.mkdir(target_dir_E) # make directory
###
# if not os.path.exists(target_dir_D):
    # os.mkdir(target_dir_D) # make directory
# 3. The files are backed up into a zip file.
# 4. The current day is the name of the subdirectory in the main directory.
today_e = target_dir_E + os.sep + time.strftime(f'%Y_%m_%d')
###
# today_d = target_dir_D + os.sep + time.strftime(f'%Y_%m_%d')
# The current time is the name of the zip archive.
now = time.strftime(f'%H_%M_%S')
# Take a comment from the user to create the name of the zip file
comment = str(input('Enter a comment: '))
# Check if a comment was entered
if len(comment) == 0:
    target_e = today_e + os.sep + now + '.zip'
else:
    target_e = today_e + os.sep + now + '_' + \
        comment.replace(' ', '_') + '.zip'
###
# if len(comment) == 0:
#     target_d = today_d + os.sep + now + '.zip'
# else:
#     target_d = today_d + os.sep + now + '_' + \
#         comment.replace(' ', '_') + '.zip'
# Create the subdirectory if it isn't already there
if not os.path.exists(today_e):
    os.mkdir(today_e)
    print('Successfully created directory', today_e)
###
# if not os.path.exists(today_d):
#     os.mkdir(today_d)
#     print('Successfully created directory', today_d)
# 5. We use the zip command to put the files in a zip archive
zip_command_e = "zip -r {0} {1}".format(target_e, ' '.join(source))
###
# zip_command_d = "zip -r {0} {1}".format(target_d, ' '.join(source))
# Run the backup
print("Zip command is: " + zip_command_e)
print("Running:")
if os.system(zip_command_e) == 0:
    print('Successful backup to', target_e)
else:
    print('Backup FAILED')
###
# print("Zip command is: " + zip_command_d)
# print("Running:")
# if os.system(zip_command_d) == 0:
#     print('Successful backup to', target_d)
# else:
#     print('Backup FAILED')