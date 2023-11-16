# increases file limit for holberton user

# increase hard file limit
exec { 'increase-hard-file-limit-for-holberton-user':
  command => 'sed -i "/holberton hard/s/5/70000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

# increase soft file limit
exec { 'increase-soft-file-limit-for-holberton-user':
  command => 'sed -i "/holberton soft/s/4/70000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}