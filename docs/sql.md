# SQLの構成とか

## Tables
* users: 利用者情報  
```sql
CREATE TABLE users (
  id serial NOT NULL,
  userName varchar NOT NULL,
  password_hash varchar NOT NULL,
  tags varchar,
  birthdate date NOT NULL,
  address varchar NOT NULL,
  telephone_number varchar NOT NULL,
  email varchar,
  card_number integer NOT NULL,
  created_at timestamp NOT NULL DEFAULT clock_timestamp(),
  updated_at timestamp
);
```

* bibs: 書誌情報参照のためのレコード  
```sql
CREATE TABLE bibs (
  id serial NOT NULL,
  bib_id integer NOT NULL,
  isbn integer NOT NULL,
  ndl_code integer NOT NULL,
  is_not_on_ndl boolean NOT NULL DEFAULT FALSE,
  reference varchar NOT NULL DEFAULT 'ndl',
  original_data_code integer,
  created_at timestamp NOT NULL DEFAULT clock_timestamp()
);
```

* ptbl: 書誌情報  
```sql
CREATE TABLE ptbl (
  id serial NOT NULL,
  name varchar NOT NULL,
  issuer varchar NOT NULL
);
```