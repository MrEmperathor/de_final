#!/bin/bash

url=$1
user_mega="xohemom858@fironia.com"
pass_mega="Pelish242019"

# https://amb.milastores.com/wp-content/ai1wm-backups/amb.milastores.com-20210312-160533-t6122x.wpress'
name_file=$(echo "${url}" | cut -d"/" -f6)
wget "${url}"; \
megaput "${name_file}" -u "${user_mega}" -p "${pass_mega}"

link_mega=$(megals -e /Root/"${name_file}" -u "${user_mega}" -p "${pass_mega}" | cut -d' ' -f4)


echo "${link_mega}"
echo "${name_file}"
echo "--------------" >> backup_sites
echo "${name_file}" >> backup_sites.txt
echo "${link_mega}" >> backup_sites.txt
echo "--------------" >> backup_sites

rm "${name_file}"