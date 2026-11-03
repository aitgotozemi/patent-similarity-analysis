"""研究室 DB への接続（読み取り専用）。接続情報はリポジトリ直下の .env（INI 形式）から読む。"""
import configparser
from pathlib import Path

import psycopg

ENV_PATH = Path(__file__).resolve().parents[1] / ".env"


def connect(section: str = "DEFAULT") -> psycopg.Connection:
    cfg = configparser.ConfigParser()
    cfg.read(ENV_PATH, encoding="utf-8")
    s = cfg[section]
    conn = psycopg.connect(
        host=s["HOST"], port=s["PORT"], dbname=s["DBNAME"],
        user=s["USER"], password=s["PASSWORD"], connect_timeout=10,
    )
    conn.read_only = True
    return conn
