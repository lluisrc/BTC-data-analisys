Realizar una buena documentacion para ayudarme en un futuro o que otra persona le pueda ayudar

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
