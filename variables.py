# AYS Variables
repo_name = "yvestesting"
vm_location = "be-gen-1"
vm_vdc = "ydc"
account_name = "myaccount"
ays_client = "http://localhost:5000"
vm_osimage = "Ubuntu 16.04 x64"
vm_memory = "1" #Memory in Gigs

# VM Related Variables
user_name = "cloudscalers" #Base name for the Account in the VM
publicIp = "<PUBLIC_IP>" #Public IP Associated to the VDC or Cloud Space
publicPort = "80"
vm_localPort = "80"
protocol = "tcp"
vm_name_db = "GIG_WP_DB" #The Name has to be Unique
vm_sizeId = "2" #You need to Check the Catalogue in the GIG.
#vm_imageId= "4" #You need to Check the Catalogue in the GIG. RedHat
vm_imageId= "1" #You need to Check the Catalogue in the GIG. Ubuntu
vm_cloudspaceId = "659" #This is the target Cloud Space from your Account

# Common Variables
vm_disksize = "20" #These are GBs.
# This Token has to be generated using your itsyou.online credentials
jwt_token = "<TOKEN>"
# URL for the GIG Server.
BASE_URL = "be-gen-1.demo.greenitglobe.com"
#vm_names = ['GIG_WP_DB','GIG_WP','GIG_WP_NGINX']
vm_names = ['yves_vm_1']

# These are the WordPress database settings
wp_db_name = "wordpress"
wp_db_user = "wordpress"
wp_db_password = "secret"
