#!/usr/bin/env python

import glob
import os.path
import argparse #parsing arguments
import numpy as np
import bs4
import urllib.parse

#########################  MAIN   ######################################################

def main():
    parser = argparse.ArgumentParser(description='inject Keycloak authenticator js in html')
    parser.add_argument('-r', '--root', type=str, default='.',
        help='Root direcory for searcing')
    parser.add_argument('-b', '--build', type=str, default='_build/html',
        help='Directory where HTML are built')
    arg = parser.parse_args()

    # read config file
    root_dir = arg.root
    build_dir = arg.build
        
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
        # inject jupyter
        find_jupyter = len(soup.find_all('a', class_='headerbtn',title="Launch on JupyterHub"))
        
        if find_jupyter>0:
            select = soup.find('a', class_='headerbtn',title="Launch on JupyterHub")
            sub1 = "lab/tree/avni-courses.solid-earth-fundamentals/bin/"
            sub2 = "&branch=main"
            test_str = select['href']
            test_str=test_str.replace(sub1,"*")
            test_str=test_str.replace(sub2,"*")
            re=test_str.split("*")
            res=re[1]
            
            # create links for Problem sets anf Field Trips
            if res.startswith('PS_') or res.startswith('Field_Trip_'):
                select['href'] = 'https://geodynamics.org/tools/solidearth/invoke?params='+urllib.parse.quote('file(notebook):/apps/solidearth/'+res,safe='')
            else:
                select['href'] = 'https://geodynamics.org/tools/solidearth/invoke?params='+urllib.parse.quote('file(notebook):/apps/solidearth/welcome.ipynb',safe='')                
            
            # save the file again
            with open(file, "w") as outf: outf.write(str(soup))
            print("Modified the JupyterLab link:", file)
        else:
            print('Warning: Did not modify the JupyterLab link - ', file)
            
            

#######################################################################################    

if __name__ == "__main__":
    main()
#######################################################################################