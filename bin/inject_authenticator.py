#!/usr/bin/env python

import glob
import os.path
import pdb
import argparse #parsing arguments
import numpy as np
import toml
import bs4
import shutil

#########################  MAIN   ######################################################

def main():
    parser = argparse.ArgumentParser(description='inject Keycloak authenticator js in html')
    parser.add_argument('-t', '--toml', type=str, default='inject.toml',
        help='Configuration TOML file')
  
    arg = parser.parse_args()

    # read config file
    cfg = toml.load(arg.toml)
    root_dir = cfg['html']['root_dir']
    build_dir = cfg['html']['build_dir']
        
    # create list of png files
    all_files = []
    for (roots,dirs,file) in os.walk(root_dir+'/'+build_dir):
        for f in file: 
            if f.endswith('.html'): 
                all_files.append(os.path.join(roots, f))
                
    for file in all_files:
        # load the file
        with open(file) as inf:
            txt = inf.read()
            soup = bs4.BeautifulSoup(txt, 'html.parser')
        # inject unlock and logout buttons
        # load the file
        unlock_logout = cfg['html']['unlock_logout_inject']
        with open(unlock_logout) as inf:
            txt = inf.read()
            soup2 = bs4.BeautifulSoup(txt, 'html.parser')
        find_left_header = len(soup.find_all('div', class_='header-article__left'))
        if find_left_header>0:
            soup.find_all('div', class_='header-article__left')[-1].append(soup2)
            # save the file again
            with open(file, "w") as outf: outf.write(str(soup))
            print("Injecting unlock and logout button in all:", file)
        else:
            print('Warning: Did not inject a header for - ', file)

#######################################################################################    
    # loop through list of restricted criterion
    restricted = cfg['restricted']
    files_inject = {} #initialize
    for rtyp in restricted:
        
        resource_roles = restricted[rtyp]['resource_roles']
        authenticator = restricted[rtyp]['authenticator']
        files_add = restricted[rtyp]['files_add']
        files_drop = restricted[rtyp]['files_drop']
        print('Restriction type:', resource_roles)
        print('Authenticator:', authenticator)
        files_regex = restricted[rtyp]['files_regex']
        files = glob.glob(root_dir+'/'+build_dir+'/'+files_regex)
        # now drop certain files from restriction
        for dropped in files_drop:
            for file in files:
                if dropped in file: files.remove(file) #if string is present
        # now add certain files to restriction
        for file in all_files:
            for added in files_add:
                if added in file: 
                    files.append(file)
                    files_add.remove(added)
        if len(files_add)>0: #if there is a lingering file that should have been added
            print("Warning: Following files have not been found in your path:")
            for file in files_add:
                print(file)
          
        # update the list
        if len(files) > 0:
            files_inject[rtyp] = {}
            files_inject[rtyp]['resource_roles'] = resource_roles
            files_inject[rtyp]['authenticator'] = authenticator
            files_inject[rtyp]['files'] = files
                  
        # now remove files from all_list to know what will be public
        for file in files: 
            if file in all_files: all_files.remove(file)
    
    #Print list of files
    print("Public files:")
    for file in all_files: print(file)
    
#######################################################################################
    
    #Copy the keycloak file
    js_dir = cfg['html']['js_dir']
    body_tag_inject = cfg['html']['body_tag_inject']
    body_tag_inject=body_tag_inject.split('=')
    
    
    # Copy file example.txt into a new file called example_copy.txt
    keycloak_js = cfg['html']['keycloak_js']
    keycloak_js_site = js_dir+'/'+os.path.basename(keycloak_js)
    shutil.copy(keycloak_js, keycloak_js_site)
    keycloak_token = cfg['html']['keycloak_web_token']
    keycloak_token_site = js_dir+'/'+os.path.basename(keycloak_token)
    shutil.copy(keycloak_token, keycloak_token_site)

                    
    for rtyp in files_inject:
        for file in files_inject[rtyp]['files']:
            print("Injecting JS:", file)
            
            authfile = os.path.dirname(file)+'/'+os.path.basename(files_inject[rtyp]['authenticator'])
            # Read in authenticator file and place relative paths to homepage
            homepage = os.path.relpath(build_dir,os.path.dirname(file))
            with open(files_inject[rtyp]['authenticator'], 'r') as file_in : filedata = file_in.read()
            # Replace the target string
            filedata = filedata.replace('homepage', "'"+homepage+"'")
            # Write the file out again
            with open(authfile, 'w') as output: output.write(filedata)
            
            # load the file
            with open(file) as inf:
                txt = inf.read()
                soup = bs4.BeautifulSoup(txt, 'html.parser')
                
            # add keycloak to body
            soup.body[body_tag_inject[0]] = body_tag_inject[1]
            
            # create a new script in head
            comment = bs4.Comment('Keycloak PHP/HTML Authenticator')
            soup.head.insert(0,"\n")
            soup.head.insert(1, comment)    
            # relative paths does not work for keycloak.js unless you put at the top of head
            src_path = os.path.relpath(keycloak_js_site,os.path.dirname(file))
            new_script = soup.new_tag("script",src=src_path)
            soup.head.insert(2,"\n")
            soup.head.insert(3, new_script)    
            src_path = os.path.relpath(authfile,os.path.dirname(file))
            new_script = soup.new_tag("script",src=src_path)
            soup.head.insert(4,"\n")
            soup.head.insert(5,new_script)
            soup.head.insert(6,"\n")
            soup.head.insert(7,"\n")
            soup.body.wrap(soup.new_tag("div", **{"id": "hideDiv", "style": "display:none"}))
                        
            # save the file again
            with open(file, "w") as outf: outf.write(str(soup))
    
    return


if __name__ == "__main__":
    main()
#######################################################################################

