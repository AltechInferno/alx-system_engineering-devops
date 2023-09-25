# Setting up my client config file
include stdlib

file_line { 'Turn off passwd auth':
  line    => '    PasswordAuthentication no',
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  replace => true,
}

file_line { 'Delare identity file':
  path    => '/etc/ssh/ssh_config',
  line    => '     IdentityFile ~/.ssh/school',
  ensure  => present,
  replace => true,
}
