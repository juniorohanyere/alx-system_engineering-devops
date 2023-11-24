# install flask package

exec { 'flask':
  command => '/usr/bin/pip3 install flask=2.1.0',
}
