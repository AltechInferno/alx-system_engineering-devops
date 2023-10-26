# stable version
exec { 'add nginx stable repo':
  command => 'sudo add-apt-repository ppa:nginx/stable',
  path    => ['/usr/local/sbin', '/usr/local/bin', '/usr/sbin', '/usr/bin', '/sbin', '/bin'],
  require => Exec['update packages'],
}

exec { 'update packages':
  command => 'apt-get update',
  path    => ['/usr/local/sbin', '/usr/local/bin', '/usr/sbin', '/usr/bin', '/sbin', '/bin'],
}

package { 'nginx':
  ensure => 'installed',
  require => Exec['add nginx stable repo'],
}

exec { 'allow HTTP':
  command => "ufw allow 'Nginx HTTP'",
  path    => ['/usr/local/sbin', '/usr/local/bin', '/usr/sbin', '/usr/bin', '/sbin', '/bin'],
  onlyif  => '! dpkg -l nginx | egrep \'îi.*nginx\' > /dev/null 2>&1',
}

exec { 'chmod www folder':
  command => 'chmod -R 755 /var/www',
  path    => ['/usr/local/sbin', '/usr/local/bin', '/usr/sbin', '/usr/bin', '/sbin', '/bin'],
}

file { '/var/www/html/index.html':
  ensure  => 'file',
  content => "Hello World!\n",
}

file { '/var/www/html/404.html':
  ensure  => 'file',
  content => "Ceci n'est pas une page\n",
}

file { 'Nginx default config file':
  path    => '/etc/nginx/sites-enabled/default',
  ensure  => 'file',
  content => "
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;
    server_name _;
    location / {
        try_files \$uri \$uri/ =404;
    }
    error_page 404 /404.html;
    location  /404.html {
        internal;
    }
    if (\$request_filename ~ redirect_me){
        rewrite ^ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
    }
}
",
  require => [Package['nginx'], File['/var/www/html/404.html']],
}

exec { 'restart service':
  command => 'service nginx restart',
  path    => ['/usr/bin', '/usr/sbin', '/bin'],
  require => File['Nginx default config file'],
}

service { 'nginx':
  ensure => 'running',
  require => Package['nginx'],
}

