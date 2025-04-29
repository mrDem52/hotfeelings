import asyncio
import os
import sys
from orm import create_tables, insert_data

sys.path.insert(1, os.path.join(sys.path[0], '..'))

create_tables()

asyncio.run(insert_data())
