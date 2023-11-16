# increase upper limit and restart nginx

exec { 'increase upper limit':
  ensure => present,
  provider => shell,
  command  => 'sed -i s/15/1000000/ /etc/default/nginx'
}
exec { 'restart nginx':
  provider => shell,
  command  => 'sudo service nginx restart'
}
