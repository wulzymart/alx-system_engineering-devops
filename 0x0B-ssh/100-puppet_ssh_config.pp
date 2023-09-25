# updates ssh config file
file { '/etc/ssh/ssh_config':
    ensure  => 'present',
}->

file_line { 'identity file':
    ensure => 'present',
    path   => '/etc/ssh/ssh_config',
    line   => '     IdentityFile ~/.ssh/school',
}

file_line { 'no password':
    ensure => 'present',
    path   => '/etc/ssh/ssh_config',
    line   => '     PasswordAuthentication no',
}
