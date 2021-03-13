import os
import subprocess as sb

print("\n\n\t\tWELCOME TO LVM PARTITION CONSOLE")
print("""
        Press 1 : Create physical volume from available Hard-Disk
        Press 2 : Create Volume group from Physical Volume
        Press 3 : Create Logical Volume
        Press 4 : Show the logical volumes
        Press 5 : Extend the Logical Volume
        Press 6 : Reduce the size of LV
        Press 7 : Exit
\n""")

while True:
	
	ch=input("Enter your choice : ")
	#print(ch)
	if int(ch)==1:
	   hd=input("\nEnter your hard disk name: ")
	   output=sb.getstatusoutput("pvcreate {}".format(hd))
	   print(output[1])

	elif int(ch)==2:
	   pv=input("\nEnter your physical Volume name: ")
	   gn=input("Enter your Volume Group name: ")
	   output=sb.getstatusoutput("vgcreate {} {}".format(gn,pv))
	   print(output[1])

	elif int(ch)==3:
	   lv=input("\nEnter logical volume  name: ")
	   vg=input("Enter volume group name: ")
	   size=input("\nEnter the size of lv : ")
	   output=sb.getstatusoutput("lvcreate --size {} --name {} {}".format(size,lv,vg))
	   print(output[1])
	   fol=input("Give folder name where you want to mount: ")
	   out=sb.getstatusoutput("mkdir {}".format(fol))
	   out1=os.system("mkfs.ext4 /dev/{}/{}".format(vg,lv))
	   out2=sb.getstatusoutput("mount /dev/{}/{} {}".format(vg,lv,fol))
	   #sb.getstatusoutput("echo `mount /dev/{}/{} {}".format(vg,lv,fol)` > /etc/rc.d/rc.local")
	   #sb.getstatusoutput("chmod +x /etc/rc.d/rc.local")
	    

	elif int(ch)==4:
	   lv=input("\nTell me your lv  name: ")
	   output=sb.getstatusoutput("lvdisplay | grep {}".format(lv))
	   print(output[1])
	elif int(ch)==5:


	    size=input("\n Tell me the size: ")
	    lv=input("Enter your logical volume: ")
	    output=sb.getstatusoutput("lvextend --size +{} /dev/firstvg/{} ".format(size,lv))
	    out=sb.getstatusoutput("resize2fs /dev/firstvg/{}".format(lv))

	elif int(ch)==7:
	    exit()
	else:
	    print("Option not supported")


