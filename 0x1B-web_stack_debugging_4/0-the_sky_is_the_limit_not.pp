# Free nginx 

# Increase the limit
exec {
  command => 'sed -i "s/15/7000/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

# restart nginx
-> exec { 'restart nginx':
  command => 'sudo service nginx restart',
  path    => '/etc/init.d/'
}