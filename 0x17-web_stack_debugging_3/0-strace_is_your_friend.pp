#Replace phpp by php
exec { 'fix using strace':
  command => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/g' 
  /var/www/html/wp-settings.php",
  path    => ['/bin'],
}
