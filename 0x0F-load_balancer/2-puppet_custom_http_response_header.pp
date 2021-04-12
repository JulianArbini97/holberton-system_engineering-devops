# Comment

exec {'OneCommandInstallation':
  command => 'sudo apt-get update -y; sudo apt-get install nginx -y; 
  	      sudo sed -i "46i\add_header X-Served_By \$HOSTNAME;" /etc/nginx/sites-available/default; sudo service nginx restart',
  provider => 'shell',
}
