# Fix 500 error 

exec {'replace':
  path     => '/usr/local/bin/:/bin/',
  provider => shell,
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
