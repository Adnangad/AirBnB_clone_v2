# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Create necessary directories
file { ['/data', '/data/web_static', '/data/web_static/releases', '/data/web_static/shared', '/data/web_static/releases/test']:
  ensure => directory,
}

# Create a fake HTML file
file { '/data/web_static/releases/test/index.html':
  ensure  => file,
  content => '<html><head><title>Test Page</title></head><body><h1>This is a test page</h1></body></html>',
}

# Set ownership of /data/ folder recursively
file { '/data':
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}

# Create symbolic link /data/web_static/current
file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test',
}

# Update Nginx configuration
file_line { 'nginx_alias':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => '    location /hbnb_static { alias /data/web_static/current/; }',
}
