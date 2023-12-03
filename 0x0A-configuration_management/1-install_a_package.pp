# install a specific version of flask (2.1.0)

exec { 'flask':
  command => 'pip3 install flash==2.1.0',
}
