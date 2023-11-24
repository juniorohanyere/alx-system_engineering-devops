# use exec to kill a particular process

exec {'kill-killmenow':
  command => 'pkill killmenow',
  path    => '/usr/bin';
}
