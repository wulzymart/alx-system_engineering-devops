# create a manifest that kills a process named killmenow.
exec { 'pkill -9 killmenow':
    command => 'pkill -f killmenow',
    path    => '/usr/bin:/usr/sbin:/bin'
}
