# fixes wordpress setting error of mispelt php extension

exec { 'phpp fix':
    command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
    path    => ['/bin','/usr/bin']
}
