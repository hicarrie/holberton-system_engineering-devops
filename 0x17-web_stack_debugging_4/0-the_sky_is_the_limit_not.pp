# Changes limits in /etc/default/nginx and /etc/nginx/nginx.conf
exec { 'nginx':
  command => 'sed -i "s/15/15000/" /etc/default/nginx; service nginx restart',
  path    => '/usr/bin:/usr/sbin:/bin',
}
