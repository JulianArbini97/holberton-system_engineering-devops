# Comment line
exec { 'func':
  command => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/' /var/www/html/wp-settings.php",
  provider =>  'shell',
}