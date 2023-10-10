from datetime import datetime
from uuid import uuid4

date = datetime.now().isoformat()
id = uuid4()

print("Todays date is {} and id is {}".format(date, id))
