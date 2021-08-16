def mysql_config():
    

    db_config = {
        'host': 'ovaas2.mysql.database.azure.com',
        'port': 3306,
        'user': 'techc@ovaas2',
        'password': 'Ovaas.369',
        'database': 'ovaas',
        'ssl': {'ssl':
                    {'ca': '../DBHelper/BaltimoreCyberTrustRoot.crt.pem'}
                }
    }

    return db_config

def mysql_config_localhost():
    db_config = {
        'host': 'localhost',
        'port': 3306,
        'user': 'li',
        'password': '123123',
        'database': 'ovaas',
    }
    return db_config
