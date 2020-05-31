#User limit
exec { 'setup user limits':
  command  => 'echo "holberton - nofile 25000" > /etc/security/limits.conf',
  provider => shell,
}
