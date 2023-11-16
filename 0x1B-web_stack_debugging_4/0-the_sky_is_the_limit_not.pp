# Free nginx 

# Increase the limit
exec { 'fix--for-nginx':
  command => 'sed -i "s/15/7000/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

# eestart nginx
-> exec { 'nginx-restart':
  command => 'service nginx restart',
  path    => '/etc/init.d/'
}