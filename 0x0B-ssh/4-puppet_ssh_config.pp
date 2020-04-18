#make changes to our configuration file
file_line { 'no password':
ensure => present,
path   => '/etc/ssh/ssh_config',
line   => 'PasswordAuthentication no',
}

file_line { 'ssh':
ensure => present,
path   => '/etc/ssh/ssh_config',
line   => 'IdentityFile ~/.ssh/holberton',
}

