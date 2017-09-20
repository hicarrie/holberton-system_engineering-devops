# Changes limits in /etc/default/nginx and /etc/nginx/nginx.conf
exec { 'nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/bin/:/usr/sbin:/bin',
}

exec { 'workerlimit':
  command => 'sed -i "s/worker_processes 4;/worker_processes 4;\nworker_rlimit_nofile 16384;/" /etc/nginx/nginx.conf',
  path    => '/usr/bin/:/usr/sbin:/bin',
}

exec { 'restart':
  command => 'service nginx restart',
  path    => '/usr/bin/:/usr/sbin:/bin',
}
