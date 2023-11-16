# remove limit
exec { 'remove upper limit':
  ensure => present,
  provider => shell,
  command  => 'sed -i s/holberton/"# holberton"/ /etc/security/limits.conf'
}
