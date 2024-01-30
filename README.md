In this project you will see com tu use python scripts to import massive data to mysql database.

First at all we have to create a mysql database with the next tables:
- BTC_price.
```sql
CREATE TABLE `BTC_price` (
  `day` DATE,
  `price` FLOAT,
  `open` FLOAT,
  `high` FLOAT,
  `low` FLOAT,
  `vol` BIGINT,
  `change` FLOAT,
  PRIMARY KEY (`day`)
)
```
- BTC_blocks.
```sql
CREATE TABLE BTC_blocks (
  id INT,
  hash VARCHAR(64),
  time DATETIME,
  size INT,
  stripped_size INT,
  weight INT,
  version INT,
  nonce BIGINT,
  difficulty BIGINT,
  transaction_count INT,
  witness_count INT,
  input_count INT,
  output_count INT,
  input_total DOUBLE,
  input_total_usd DOUBLE,
  output_total DOUBLE,
  output_total_usd DOUBLE,
  cdd_total DOUBLE,
  generation DOUBLE,
  guessed_miner VARCHAR(64),
  PRIMARY KEY (id)
  );
```

Now we can use python scripts for download, unzip and import data to mysql database.
> [!NOTE]
> You have to modify the script to write the corrects parameters to connect to your mysql.
