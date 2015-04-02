class { 'postgresql::server':
    ip_mask_deny_postgres_user => '0.0.0.0/32',
    ip_mask_allow_all_users => '0.0.0.0/0',
    listen_addresses => '*',
    postgres_password          => 'a',
}

# Shamelessly stolen from the system of record because online examples are...
# inconsistent in results.
postgresql::server::pg_hba_rule { 'trust local access to all':
  type        => 'local',
  user        => 'all',
  auth_method => 'trust',
  order       => '001',
  database    => 'all',
}

postgresql::server::pg_hba_rule { 'trust host access to all':
  type        => 'host',
  user        => 'all',
  auth_method => 'trust',
  order       => '002',
  database    => 'all',
  address     => '0.0.0.0/0'
}

postgresql::server::pg_hba_rule { 'trust host access to 1/128':
  type        => 'host',
  user        => 'all',
  auth_method => 'trust',
  order       => '003',
  database    => 'all',
  address     => '::1/128'
}

postgresql::server::db { 'discotype':
  user     => 'discotype',
  password => 'discotype',
}

postgresql::server::role { 'vagrant':
  password_hash => postgresql_password('vagrant', 'vagrant'),
  superuser => true,
}

postgresql::server::role { 'root':
  password_hash => postgresql_password('root', 'root'),
  superuser => true,
}

postgresql::server::database_grant { 'grant vagrant access to discovery prototype':
  privilege => 'ALL',
  db        => 'discotype',
  role      => 'vagrant',
}

postgresql::server::database_grant { 'grant root access to discovery prototype':
  privilege => 'ALL',
  db        => 'discotype',
  role      => 'root',
}
