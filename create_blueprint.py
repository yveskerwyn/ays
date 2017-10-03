import os
import requests
from jinja2 import Environment, FileSystemLoader

exec(open("variables.py").read())

TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
    trim_blocks=False)

def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)

def create_blueprint(BASE_URL, jwt_token, vm_location, vm_vdc, account_name, vm_name, vm_port, vm_disksize, vm_osimage, vm_memory):

    fname = "create_vm_" +  vm_name + ".yaml"
    var_nginx = ""
    if "NGINX" in vm_name:
        var_nginx = 'yes'

    context = {
    '__BASE_URL__': BASE_URL,
    '__JWT_TOKEN__': jwt_token,
    '__VM_LOCATION__': vm_location,
    '__VM_VDC__': vm_vdc,
    '__ACCOUNT_NAME__': account_name,
    '__VM_NAME__': vm_name,
    '__VM_PORT__': vm_port,
    '__BOOT_DISK_SIZE__': vm_disksize,
    '__VM_MEMORY__': vm_memory,
    '__OS_IMAGE__': vm_osimage,
    'var_nginx': var_nginx
    }
    #
    with open(fname, 'w') as f:
        yaml_file = render_template('create_vm.yaml.j2', context)
        f.write(yaml_file)
        f.close()

def main():

    # Create jwt for OpenvCloud
    
    params = {
        'grant_type': 'client_credentials',
        'client_id': os.environ['CLIENT_ID'],
        'client_secret': os.environ['SECRET'],
        'response_type': 'id_token',
        'scope': 'offline_access'
    }

    url = 'https://itsyou.online/v1/oauth/access_token'
    resp = requests.post(url, params=params)
    resp.raise_for_status()
    jwt_token = resp.content.decode('utf8')

    for vm_name in vm_names:
        print("Creating Blueprint for " + vm_name)
        create_blueprint(BASE_URL, jwt_token, vm_location, vm_vdc, account_name, vm_name, vm_port, vm_disksize, vm_osimage, vm_memory)

if __name__ == "__main__":
    main()