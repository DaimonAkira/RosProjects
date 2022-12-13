from ftplib import FTP 
import os
import fileinput
 
ftp = FTP()
ftp.set_debuglevel(2)
ftp.connect('ftp.cankocum.com', 21) 
ftp.login('marslogin@cankocum.com','Kruxel299t.')
 
localdir = "C:\\Users\\makaj\\Desktop\\Ros Projects\\RosProjects\\ftpuploader\\images"

ftp.cwd('/images/')
 
def ftp_upload(localfile, remotefile):
  fp = open(localfile, 'rb')
  ftp.storbinary('STOR %s' % os.path.basename(localfile), fp, 1024)
  fp.close()
  print("after upload " + localfile + " to " + remotefile)  

def upload_img(file):
  ftp_upload(localdir + "\\" + file, file)

lastlist = []
 
for line in fileinput.input(localdir + "\\list.txt"):
    lastlist.append(line.rstrip("\n"))
 
currentlist = os.listdir(localdir)
 
newfiles = list(set(currentlist) - set(lastlist))
 
if len(newfiles) == 0:
  print("No files need to upload")
else:
  for needupload in newfiles:
    print("uploading " + localdir + "\\" + needupload)
    upload_img(needupload)
    with open(localdir + "\\list.txt", "a") as myfile:
      myfile.write(needupload + "\n")
 
ftp.quit()

ftp = FTP()
ftp.set_debuglevel(2)
ftp.connect('ftp.cankocum.com', 21) 
ftp.login('marslogin@cankocum.com','Kruxel299t.')

ftp.cwd('/images/thumbnail/')
 
def ftp_upload(localfile, remotefile):
  fp = open(localfile, 'rb')
  ftp.storbinary('STOR %s' % os.path.basename(localfile), fp, 1024)
  fp.close()
  print("after upload " + localfile + " to " + remotefile)
 
 
def upload_img(file):
  ftp_upload(localdir + "\\" + file, file)
 
lastlist = []
 
for line in fileinput.input(localdir + "\\listthumb.txt"):
    lastlist.append(line.rstrip("\n"))
 
currentlist = os.listdir(localdir)
 
newfiles = list(set(currentlist) - set(lastlist))
 
if len(newfiles) == 0:
  print("No files need to upload")
else:
  for needupload in newfiles:
    print("uploading " + localdir + "\\" + needupload)
    upload_img(needupload)
    with open(localdir + "\\listthumb.txt", "a") as myfile:
      myfile.write(needupload + "\n")