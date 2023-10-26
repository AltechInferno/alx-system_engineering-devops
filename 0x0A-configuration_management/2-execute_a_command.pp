# this script kills a process named killmenow

exec { 'pkill killmenow':
  provider => 'shell',
  command  => 'pkill killmenow'
}
